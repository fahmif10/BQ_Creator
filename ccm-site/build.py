#!/usr/bin/env python3
"""Static site generator for CCM Secretarial (English + Bahasa Melayu).

Usage:  python3 build.py            -> writes the finished site into ./dist
Change SITE below to the live domain before deploying: it feeds canonical
URLs, Open Graph tags, JSON-LD, hreflang and sitemap.xml.
"""
import html, json, os, shutil, datetime
import content as EN
import content_ms as MS
from content import TRUST, QUOTES, BUSINESS
from i18n import UI, JS, LANGS

SITE = "https://www.ccmsecretarial.com"
TODAY = datetime.date.today().isoformat()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "dist")
B = BUSINESS
esc = html.escape

WA_SVG = ('<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3Z"/></svg>')
WA_SM = WA_SVG.replace('width="22" height="22"', 'width="18" height="18"')

# Language-specific data bundles. Paths inside are language-relative (no "ms/" prefix).
DATA = {
    "en": dict(SERVICES=EN.SERVICES, PERSONAS=EN.PERSONAS, QUIZ=EN.QUIZ, FAQS=EN.HOME_FAQS, PAGES=EN.PAGES, GUIDES=EN.GUIDES,
               PRIVACY=EN.PRIVACY_HTML, PRIVACY_UPDATED=EN.PRIVACY_UPDATED, PRIVACY_PATH="privacy-policy/", GUIDES_PATH="guides/"),
    "ms": dict(SERVICES=MS.SERVICES, PERSONAS=MS.PERSONAS, QUIZ=MS.QUIZ, FAQS=MS.HOME_FAQS, PAGES=MS.PAGES, GUIDES=MS.GUIDES,
               PRIVACY=MS.PRIVACY_HTML, PRIVACY_UPDATED=MS.PRIVACY_UPDATED, PRIVACY_PATH=MS.PRIVACY_PATH, GUIDES_PATH="panduan/"),
}

# EN real path <-> MS real path, for hreflang and the language switcher
PAIRS = {"": "ms/", "guides/": "ms/panduan/", "privacy-policy/": "ms/" + MS.PRIVACY_PATH}
for _s in MS.SERVICES:
    PAIRS[_s["en_path"]] = "ms/" + _s["path"]
for _p in MS.PAGES:
    PAIRS[_p["en_path"]] = "ms/" + _p["path"]
for _g in MS.GUIDES:
    PAIRS[_g["en_path"]] = "ms/" + _g["path"]
REV = {v: k for k, v in PAIRS.items()}


def wa(text=""):
    from urllib.parse import quote
    return "https://wa.me/%s%s" % (B["wa"], ("?text=" + quote(text)) if text else "")


def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def org_ref():
    return {"@id": SITE + "/#business"}


class Ctx:
    """Per-page helper. Relative URLs keep the site working at a domain root or a sub-path."""
    def __init__(self, path, lang="en", absolute=False):
        self.path = path  # real path, e.g. "ms/perkhidmatan/audit/"
        self.lang = lang
        self.T = UI[lang]
        self.D = DATA[lang]
        self.prefix = LANGS[lang]["prefix"]
        self.depth = len([p for p in path.split("/") if p])
        self.absolute = absolute
        en = path if lang == "en" else REV.get(path)
        ms = path if lang == "ms" else PAIRS.get(path)
        self.alts = {"en": en, "ms": ms}

    def u(self, target):  # assets and real paths
        if self.absolute:
            return SITE + "/" + target
        if target == "#contact":
            return "#contact"
        pre = "../" * self.depth
        return (pre + target) if (pre + target) else "./"

    def p(self, rel):  # language-relative page path
        if rel == "#contact":
            return "#contact"
        return self.u(self.prefix + rel)

    def other(self):
        o = "ms" if self.lang == "en" else "en"
        return self.alts[o] if self.alts[o] is not None else ("ms/" if o == "ms" else "")


def business_ld(c):
    T = c.T
    D = c.D
    return {
        "@context": "https://schema.org",
        "@type": ["AccountingService", "ProfessionalService"],
        "@id": SITE + "/#business",
        "name": B["name"], "alternateName": B["legal"], "url": SITE + "/",
        "logo": SITE + "/assets/logo.png", "image": SITE + "/assets/og-image.png",
        "description": B["description"], "telephone": B["tel"], "email": B["email"],
        "priceRange": "Fixed-fee quotes",
        "address": {"@type": "PostalAddress", "streetAddress": B["street"], "addressLocality": "Shah Alam",
                    "addressRegion": "Selangor", "addressCountry": "MY"},
        "areaServed": [{"@type": "Country", "name": "Malaysia"}, {"@type": "AdministrativeArea", "name": "Klang Valley"},
                       {"@type": "City", "name": "Shah Alam"}],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "09:00", "closes": "18:00"}],
        "contactPoint": [{"@type": "ContactPoint", "contactType": "customer service", "telephone": B["tel"],
                          "email": B["email"], "areaServed": "MY", "availableLanguage": ["en", "ms"]}],
        **({"memberOf": [{"@type": "Organization", "name": m} for m in TRUST["memberships"]]} if TRUST["memberships"] else {}),
        **({"hasCredential": [{"@type": "EducationalOccupationalCredential", "name": n, "credentialCategory": "license",
                               "identifier": v} for n, v in TRUST["credentials"]]} if TRUST["credentials"] else {}),
        "knowsAbout": ["Company secretarial services Malaysia", "SSM company registration", "Sdn Bhd annual return",
                       "Bookkeeping and accounting for SMEs", "Statutory audit Malaysia", "LHDN Form C tax filing"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Compliance services for Malaysian SMEs",
                            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["title"],
                                                 "url": SITE + "/" + c.prefix + s["path"]}} for s in D["SERVICES"]]},
    }


def faq_ld(faqs, lang="en"):
    return {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": LANGS[lang]["html"],
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + p}
                                for i, (n, p) in enumerate(trail)]}


def header(c):
    T = c.T
    cur = c.path
    dd = "".join('<a href="%s"%s>%s</a>' % (c.p(p), ' aria-current="page"' if c.prefix + p == cur else "", esc(n)) for n, p in T["nav"])
    sw = c.other()
    return f'''<a class="skip" href="#main">{T["skip"]}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{c.p("")}" aria-label="{esc(B["name"])} {T["home_label"]}"><img src="{c.u("assets/logo.png")}" alt="" width="40" height="40"><b>{esc(B["name"])}<small>{esc(B["legal"])}</small></b></a>
<button class="menu-btn" type="button" aria-label="{T["menu"]}" aria-expanded="false" aria-controls="site-nav">☰</button>
<nav class="nav" id="site-nav" aria-label="Main">
<details class="dd"><summary>{T["nav_services"]}</summary><div class="dd-menu">{dd}</div></details>
<a href="{c.p("#health")}">{T["nav_health"]}</a>
<a href="{c.p(c.D["GUIDES_PATH"])}"{' aria-current="page"' if cur == c.prefix + c.D["GUIDES_PATH"] else ""}>{T["nav_guides"]}</a>
<a href="{c.p("#faq")}">{T["nav_faq"]}</a>
<a href="{c.u(sw)}" class="lang-sw" hreflang="{"ms" if c.lang == "en" else "en"}" lang="{"ms" if c.lang == "en" else "en"}" aria-label="{T["switch_aria"]}">{T["switch_label"]}</a>
<a href="{c.u("#contact")}" class="nav-cta">{T["nav_talk"]}</a>
</nav>
<a class="btn btn-ghost header-cta" href="{wa()}" rel="noopener">{WA_SM} {T["whatsapp"]}</a>
<a class="btn header-cta" href="{c.u("#contact")}">{T["cta_consult"]}</a>
</div></header>'''


def footer(c):
    T = c.T
    svc = "".join('<li><a href="%s">%s</a></li>' % (c.p(p), esc(n)) for n, p in T["nav"])
    gd = "".join('<li><a href="%s">%s</a></li>' % (c.p(g["path"]), esc(g["short"])) for g in c.D["GUIDES"][:4])
    sw = c.other()
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{c.p("")}"><img src="{c.u("assets/logo.png")}" alt="" width="36" height="36" loading="lazy"><b>{esc(B["name"])}<small>{esc(B["legal"])}</small></b></a>
<address style="margin-top:16px">{esc(B["street"])}<br>{esc(B["locality"])}<br><a href="tel:{B["tel"]}">{esc(B["tel_display"])}</a><br><a href="mailto:{B["email"]}">{esc(B["email"])}</a></address></div>
<div><h2>{T["foot_services"]}</h2><ul>{svc}</ul></div>
<div><h2>{T["foot_guides"]}</h2><ul>{gd}<li><a href="{c.p(c.D["GUIDES_PATH"])}">{T["foot_all_guides"]}</a></li></ul></div>
<div><h2>{T["foot_company"]}</h2><ul><li><a href="{c.u("#contact")}">{T["cta_consult"]}</a></li><li><a href="{c.p("#faq")}">{T["foot_faq"]}</a></li><li><a href="{wa()}" rel="noopener">WhatsApp</a></li><li><a href="{c.p(c.D["PRIVACY_PATH"])}">{T["foot_privacy"]}</a></li><li><a href="{c.u(sw)}" hreflang="{"ms" if c.lang == "en" else "en"}">{T["switch_label"]}</a></li></ul></div>
</div>
<p class="legal">© {datetime.date.today().year} {esc(B["name"])} ({esc(B["legal"])}), Shah Alam, Selangor, Malaysia. {T["legal"]}</p>
</div></footer>
<a class="fab" href="{wa()}" rel="noopener" aria-label="{T["fab_aria"]}">{WA_SVG}<span>{T["fab_text"]}</span></a>
<script type="application/json" id="i18n">{json.dumps(JS[c.lang], ensure_ascii=False)}</script>
<script src="{c.u("assets/app.js")}" defer></script>'''


def head(c, title, desc, extra_ld=(), og_type="website", canonical_path=None, noindex=False):
    T = c.T
    cp = c.path if canonical_path is None else canonical_path
    url = SITE + "/" + cp
    ldj = "\n".join(ld(x) for x in extra_ld)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">'
    alt = ""
    if canonical_path is None:
        a = c.alts
        if a["en"] is not None:
            alt += f'<link rel="alternate" hreflang="en-MY" href="{SITE}/{a["en"]}">\n'
            alt += f'<link rel="alternate" hreflang="x-default" href="{SITE}/{a["en"]}">\n'
        if a["ms"] is not None:
            alt += f'<link rel="alternate" hreflang="ms-MY" href="{SITE}/{a["ms"]}">\n'
    L = LANGS[c.lang]
    return f'''<!DOCTYPE html>
<html lang="{L["html"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{url}">
{alt}<meta name="theme-color" content="#955857">
<meta name="geo.region" content="MY-10">
<meta name="geo.placename" content="Shah Alam">
<meta property="og:site_name" content="{esc(B["name"])}">
<meta property="og:locale" content="{L["og"]}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(B["name"])} {esc(T["og_alt"])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/og-image.png">
<link rel="icon" href="{c.u("assets/favicon.png")}" type="image/png">
<link rel="apple-touch-icon" href="{c.u("assets/apple-touch-icon.png")}">
<link rel="preload" href="{c.u("assets/fonts/inter.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{c.u("assets/fonts/fraunces.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{c.u("assets/style.css")}">
{ldj}
</head>'''


def breadcrumbs(c, trail):
    items = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            items.append('<li aria-current="page">%s</li>' % esc(n))
        else:
            items.append('<li><a href="%s">%s</a></li>' % (c.p(p), esc(n)))
    return '<nav class="crumbs" aria-label="%s"><div class="wrap"><ol>%s</ol></div></nav>' % (c.T["breadcrumb"], "".join(items))


def crumb_trail_ld(c, trail):
    return crumbs_ld([(n, c.prefix + p) for n, p in trail])


def faq_block(faqs, heading_tag="h3"):
    return "".join('<details><summary><%s class="faq-q">%s</%s></summary><p>%s</p></details>' %
                   (heading_tag, esc(q), heading_tag, esc(a)) for q, a in faqs)


def contact_section(c, heading=None):
    T = c.T
    heading = heading or T["c_heading"]
    nopts = "".join('<label><input type="checkbox" name="need" value="%s"><span>%s</span></label>' % (n, n) for n in T["needs"])
    sopts = "".join('<label><input type="radio" name="stage" value="%s"><span>%s</span></label>' % (s, s) for s in T["stages"])
    return f'''<section id="contact" class="alt-bg"><div class="wrap contact-grid">
<div>
<p class="eyebrow">{T["c_eyebrow"]}</p>
<h2 class="h2">{esc(heading)}</h2>
<p class="muted" style="margin-top:14px;font-size:1.05rem">{T["c_intro"]}</p>
<dl class="details">
<div><dt>{T["d_phone"]}</dt><dd><a href="tel:{B["tel"]}">{esc(B["tel_display"])}</a></dd></div>
<div><dt>{T["d_wa"]}</dt><dd><a href="{wa()}" rel="noopener">{esc(B["tel_display"])}</a></dd></div>
<div><dt>{T["d_office"]}</dt><dd>{esc(B["street"])}<br>{esc(B["locality"])}</dd></div>
<div><dt>{T["d_email"]}</dt><dd><a href="mailto:{B["email"]}">{esc(B["email"])}</a></dd></div>
<div><dt>{T["d_hours"]}</dt><dd>{esc(T["hours"])}</dd></div>
</dl>
</div>
<div>
<form class="form" id="enquiry" action="mailto:{B["email"]}" method="post" enctype="text/plain">
<div class="pbars" aria-hidden="true"><i class="on"></i><i></i><i></i></div>
<p class="step-n" aria-live="polite">{T["step_of"].format(n=1)}</p>
<fieldset data-step="0"><legend>{T["q_need"]}</legend><div class="opts">{nopts}</div></fieldset>
<fieldset data-step="1"><legend>{T["q_stage"]}</legend><div class="radios">{sopts}</div></fieldset>
<fieldset data-step="2"><legend>{T["q_reach"]}</legend><div class="f">
<div class="two"><label>{T["f_name"]}<input name="name" autocomplete="name" required></label>
<label>{T["f_phone"]}<input name="phone" type="tel" autocomplete="tel" inputmode="tel" required></label></div>
<label>{T["f_company"]} <span class="opt">{T["optional"]}</span><input name="company" autocomplete="organization"></label>
<label>{T["f_msg"]} <span class="opt">{T["optional"]}</span><textarea name="msg" rows="3"></textarea></label>
</div></fieldset>
<p class="err" role="alert"></p>
<div class="form-nav"><button type="button" class="btn btn-ghost" id="f-back" hidden>{T["back"]}</button>
<button type="button" class="btn" id="f-next">{T["next"]}</button></div>
<noscript><div class="form-nav"><button type="submit" class="btn">{T["submit"]}</button></div></noscript>
<p class="form-foot">{T["prefer_chat"]} <a href="{wa()}" rel="noopener">{T["wa_direct"]}</a>.</p>
<p class="form-foot" style="margin-top:6px">{T["privacy_note"]} <a href="{c.p(c.D["PRIVACY_PATH"])}">{T["foot_privacy"].lower()}</a>.</p>
</form>
<div class="form thanks" id="thanks" hidden>
<div class="tick"><b>✓</b></div>
<h3>{T["thanks_h"]}<span id="thanks-name"></span>.</h3>
<p>{T["thanks_p1"]}<span id="thanks-phone"></span>{T["thanks_p2"]}<span id="thanks-need"></span>{T["thanks_p3"]}</p>
<a class="btn" id="thanks-wa" href="{wa()}" rel="noopener">{T["send_wa"]}</a>
<a class="btn btn-ghost" id="thanks-mail" style="margin-top:10px;width:100%" href="mailto:{B["email"]}">{T["send_mail"]}</a>
<button type="button" class="form-foot" id="f-new" style="border:0;background:none;cursor:pointer;margin-top:16px;min-height:44px">{T["new_enq"]}</button>
</div>
</div></div></section>'''


def page(c, title, desc, body, extra_ld=(), og_type="website", noindex=False, canonical_path=None):
    return (head(c, title, desc, extra_ld, og_type, canonical_path, noindex) + "\n<body>\n" + header(c) +
            '\n<main id="main">\n' + body + "\n</main>\n" + footer(c) + "\n</body>\n</html>\n")


def write(path, content):
    full = os.path.join(OUT, path, "index.html") if not path.endswith(".html") else os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def trust_block(c):
    """Credentials, memberships, stats and client logos. Renders nothing until real data is supplied."""
    t = TRUST
    T = c.T
    if not any(t.values()):
        return ""
    out = ['<section class="trust" aria-labelledby="trust-h" style="padding:clamp(40px,5vw,64px) 0"><div class="wrap">',
           '<h2 id="trust-h" class="eyebrow" style="margin-bottom:20px">%s</h2>' % T["trust_h"]]
    if t["stats"]:
        out.append('<ul class="stats">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (esc(n), esc(l)) for n, l in t["stats"]))
    badges = ["<li><strong>%s</strong><span>%s</span></li>" % (esc(n), esc(v)) for n, v in t["credentials"]]
    badges += ["<li><strong>%s</strong><span>%s</span></li>" % (esc(m), T["member"]) for m in t["memberships"]]
    if badges:
        out.append('<ul class="creds">%s</ul>' % "".join(badges))
    if t["clients"]:
        out.append('<p class="muted" style="margin-top:28px;font-size:.9rem">%s</p><ul class="logos">%s</ul>' % (T["trust_clients"],
                   "".join('<li><img src="%s" alt="%s" height="36" loading="lazy"></li>' % (c.u(p), esc(n)) for n, p in t["clients"])))
    out.append("</div></section>")
    return "".join(out)


# ---------------------------------------------------------------- home
def build_home(lang):
    c = Ctx(LANGS[lang]["prefix"], lang)
    T, D = c.T, c.D
    months = "".join('<option value="%d"%s>%s</option>' % (i + 1, " selected" if i == 11 else "", m) for i, m in enumerate(T["months"]))
    fb = "".join('<li><span class="d"><b>%s</b><span>%s</span></span><span><strong>%s</strong><small>%s</small></span><span class="chip">—</span></li>' % f
                 for f in T["pl_fallback"])
    planner = f'''<aside class="card planner" id="planner" aria-labelledby="planner-h">
<div class="planner-top"><p class="k">{T["pl_k"]}</p>
<h2 id="planner-h">{T["pl_h1"]}<span id="p-days">{T["pl_default_days"]}</span>.</h2>
<div class="fields"><label>{T["pl_inc"]}<input type="date" id="p-inc" value="2024-03-15"></label>
<label>{T["pl_fye"]}<select id="p-fye">{months}</select></label></div></div>
<ol class="dl" id="p-list">{fb}</ol>
<div class="planner-foot"><a class="btn btn-dark" id="p-remind" href="{wa(T["pl_remind_wa"])}" rel="noopener">{WA_SM} {T["pl_remind"]}</a>
<p class="note">{T["pl_note"]}</p></div></aside>'''

    ticks = "".join("<li>%s</li>" % t for t in T["h_ticks"])
    strip = "".join("<li><strong>%s</strong><span>%s</span></li>" % s for s in T["h_strip"])
    hero = f'''<section class="hero"><div class="wrap">
<div>
<p class="pill"><i></i>{T["h_pill"]}</p>
<h1 class="h1">{T["h_h1a"]}<em class="accent">{T["h_h1b"]}</em>{T["h_h1c"]}</h1>
<p class="lead">{T["h_lead"]}</p>
<div class="cta-row"><a class="btn btn-lg" href="#contact">{T["h_cta1"]}</a><a class="btn btn-lg btn-ghost" href="{wa(T["wa_default"])}" rel="noopener">{WA_SM} {T["h_cta2"]}</a></div>
<p class="hint">{T["h_hint"]} <a href="#health">{T["h_hint_link"]}</a></p>
<ul class="ticks">{ticks}</ul>
</div>
{planner}
</div></section>
<div class="strip"><ul>{strip}</ul></div>'''

    tabs = "".join(f'<button type="button" class="tab" role="tab" data-persona-tab="{p["id"]}" aria-selected="{"true" if p["id"]=="run" else "false"}"><span class="n">0{i+1}</span><span class="t">{esc(p["label"])}</span><span class="s">{esc(p["sub"])}</span></button>'
                   for i, p in enumerate(D["PERSONAS"]))
    panels = ""
    for p in D["PERSONAS"]:
        lab = p.get("label_l") or p["label"].lower()
        panels += f'''<div class="persona" data-persona-panel="{p["id"]}" role="tabpanel">
<div class="card"><h3>{esc(p["headline"])}</h3><p class="muted">{esc(p["intro"])}</p><ul class="checks">{"".join("<li>%s</li>" % esc(n) for n in p["needs"])}</ul></div>
<div class="plan"><div class="top"><p>{T["p_rec"]}</p><span>{T["p_fixed"]}</span></div><h3>{esc(p["plan"])}</h3><p class="pd">{esc(p["planDesc"])}</p>
<ul>{"".join("<li>%s</li>" % esc(i) for i in p["includes"])}</ul>
<div class="acts"><a class="btn btn-light btn-lg" href="#contact" data-quote-persona="{esc(p["plan"])}" data-needs="{esc("|".join(p["need"]))}" data-stage="{esc(p["stage"])}">{T["p_quote"]}</a>
<a class="btn btn-outline-d" href="{wa(T["p_wa_msg"].format(label=lab, plan=p["plan"]))}" rel="noopener">{T["p_wa_btn"]}</a>
<p class="alt">{esc(p["alt"])}</p></div></div></div>'''
    paths = f'''<section id="paths"><div class="wrap"><div class="sec-head"><p class="eyebrow">{T["p_eyebrow"]}</p><h2 class="h2">{T["p_h2"]}</h2>
<p class="muted">{T["p_sub"]}</p></div>
<div class="tabs" role="tablist" aria-label="{T["p_aria"]}">{tabs}</div>{panels}</div></section>'''

    cards = "".join(f'''<a class="svc" href="{c.p(s["path"])}"><span class="n">0{i+1}</span><h3>{esc(s["title"])}</h3><p>{esc(s["desc"])}</p>
<ul>{"".join("<li>%s</li>" % esc(x) for x in s["items"])}</ul><span class="more">{esc(s["cta"])}</span></a>''' for i, s in enumerate(D["SERVICES"]))
    services = f'''<section id="services" style="padding-top:0"><div class="wrap"><div style="padding-top:40px;border-top:1px solid var(--line);margin-bottom:28px;max-width:760px">
<h2 class="h2" style="font-size:clamp(1.6rem,2.8vw,2.1rem)">{T["s_h2"]}</h2>
<p class="muted" style="margin-top:12px">{T["s_sub"]}</p></div>
<div class="grid">{cards}</div></div></section>'''

    quiz_items = "".join("<li>%s</li>" % esc(q["q"]) for q in D["QUIZ"])
    badges = "".join("<li>%s</li>" % b for b in T["hc_badges"])
    health = f'''<section id="health" class="dark"><div class="wrap split">
<div><p class="eyebrow">{T["hc_eyebrow"]}</p><h2 class="h2">{T["hc_h2"]}</h2>
<p class="muted" style="margin-top:16px;font-size:1.05rem;max-width:30em">{T["hc_p1"]}<em>{T["hc_and"]}</em>{T["hc_p2"]}</p>
<ul class="badges">{badges}</ul></div>
<div class="quiz" id="quiz">
<div id="quiz-static"><p class="muted">{T["hc_static"]}</p><ol class="noscript-list">{quiz_items}</ol><p class="muted" style="margin-top:16px">{T["hc_static_cta"]} <a href="{wa(T["hc_wa"])}" style="color:var(--brand-on-dark)">{T["hc_static_link"]}</a>.</p></div>
<div id="quiz-run" hidden><div class="quiz-meta"><span id="quiz-n">{T["hc_q"].format(n=1, t=len(D["QUIZ"]))}</span><button type="button" id="quiz-back" hidden>{T["hc_back"]}</button></div>
<div class="bar"><i id="quiz-bar" style="width:0"></i></div>
<p class="q" id="quiz-q" aria-live="polite"></p>
<div class="ans"><button type="button" data-ans="yes">{T["hc_yes"]}</button><button type="button" data-ans="no">{T["hc_no"]}</button><button type="button" data-ans="unsure">{T["hc_unsure"]}</button></div></div>
<div id="quiz-done" hidden><div class="score"><div class="ring" id="quiz-ring"><b id="quiz-score">0/5</b></div><div><h3 id="quiz-title"></h3><p id="quiz-msg"></p></div></div>
<div class="gaps" id="quiz-gaps" hidden><h4>{T["hc_gaps"]}</h4><ul></ul></div>
<div class="quiz-end"><a class="btn btn-light" id="quiz-wa" href="{wa()}" rel="noopener">{T["hc_send"]}</a><button type="button" class="btn btn-outline-d" id="quiz-reset">{T["hc_retake"]}</button></div></div>
<script type="application/json" id="quiz-data">{json.dumps(D["QUIZ"], ensure_ascii=False)}</script>
</div></div></section>'''

    process = f'''<section id="process"><div class="wrap"><div class="sec-head"><p class="eyebrow">{T["pr_eyebrow"]}</p><h2 class="h2">{T["pr_h2"]}</h2></div>
<ol class="steps">{"".join(f'<li class="{cl}"><span class="top"><span class="num">{n}</span><span class="who">{w}</span></span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for n, w, t, d, cl in T["pr_steps"])}</ol></div></section>'''

    quotes = "".join(f'''<figure class="quote"><blockquote><p class="lead-q">“{esc(q["lead"])}”</p><p class="body-q">{esc(q["body"])}</p></blockquote>
<figcaption><strong>{esc(q["name"])}</strong><span>{esc(q["role"])}</span><em>{esc(q["uses"])}</em></figcaption></figure>''' for q in QUOTES)
    note = '<p class="muted" style="margin:-20px 0 28px;font-size:.9rem" lang="en">%s</p>' % T["cl_note"] if T["cl_note"] else ""
    clients = f'''<section id="clients" class="alt-bg"><div class="wrap"><div class="sec-head"><p class="eyebrow">{T["cl_eyebrow"]}</p><h2 class="h2">{T["cl_h2"]}</h2></div>{note}
<div class="quotes" lang="en">{quotes}</div></div></section>'''

    guides = "".join(f'''<a class="post" href="{c.p(g["path"])}"><span class="tag">{esc(g["tag"])}</span><h3>{esc(g["h1"])}</h3><p>{esc(g["excerpt"])}</p><span class="more">{T["read_guide"]}</span></a>''' for g in D["GUIDES"][:3])
    guide_sec = f'''<section><div class="wrap"><div class="sec-head"><p class="eyebrow">{T["g_eyebrow"]}</p><h2 class="h2">{T["g_h2"]}</h2></div><div class="cards-3">{guides}</div><p style="margin-top:24px"><a href="{D["GUIDES_PATH"]}">{T["g_all"].format(n=len(D["GUIDES"]))}</a></p></div></section>'''

    faq = f'''<section id="faq"><div class="wrap faq-wrap"><div><p class="eyebrow">{T["faq_eyebrow"]}</p><h2 class="h2">{T["faq_h2"]}</h2>
<p class="muted" style="margin-top:14px;font-size:1.05rem">{T["faq_cant"]} <a href="{wa(T["faq_wa"])}" rel="noopener">{T["faq_ask"]}</a></p></div>
<div class="faq">{faq_block(D["FAQS"])}</div></div></section>'''

    areas = f'''<section style="padding-top:0"><div class="wrap"><div style="border-top:1px solid var(--line);padding-top:40px;max-width:760px"><h2 class="h2" style="font-size:clamp(1.5rem,2.6vw,2rem)">{T["ar_h2"]}</h2>
<p class="muted" style="margin-top:12px">{T["ar_p"]}</p>
<ul class="areas">{"".join("<li>%s</li>" % a for a in T["ar_list"])}</ul></div></div></section>'''

    body = hero + trust_block(c) + paths + services + health + process + clients + guide_sec + faq + areas + contact_section(c)
    lds = [business_ld(c),
           {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": B["name"],
            "inLanguage": ["en-MY", "ms-MY"], "publisher": org_ref()},
           {"@context": "https://schema.org", "@type": "WebPage", "url": SITE + "/" + c.path, "name": T["home_title"],
            "description": T["home_desc"], "isPartOf": {"@id": SITE + "/#website"}, "about": org_ref(), "inLanguage": LANGS[lang]["html"]},
           faq_ld(D["FAQS"], lang)]
    write(c.path, page(c, T["home_title"], T["home_desc"], body, lds))


# ---------------------------------------------------------------- service pages
def build_service(pg, lang):
    c = Ctx(LANGS[lang]["prefix"] + pg["path"], lang)
    T, D = c.T, c.D
    trail = [(T["home"], ""), (pg["crumb"], pg["path"])]
    hero = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">{esc(pg["eyebrow"])}</p><h1 class="h1" style="font-size:clamp(2.1rem,4.4vw,3.2rem)">{esc(pg["h1"])}</h1><p class="lead">{esc(pg["lead"])}</p>
<div class="cta-row"><a class="btn btn-lg" href="#contact">{T["svc_quote"]}</a><a class="btn btn-lg btn-ghost" href="{wa(pg["crumb"])}" rel="noopener">{T["svc_ask_wa"]}</a></div></div>
<div class="card"><h2 style="font-size:1.3rem">{esc(pg["box_title"])}</h2><ul class="checks">{"".join("<li>%s</li>" % esc(x) for x in pg["box"])}</ul></div>
</div></section>'''
    related = "".join('<li><a href="%s">%s</a></li>' % (c.p(p), esc(n)) for n, p in T["nav"] if p != pg["path"])
    main = f'''<section style="padding-top:0"><div class="wrap two-col"><article class="prose">{pg["body"]}</article>
<aside class="aside-card"><h2>{T["svc_aside_h"]}</h2><p>{T["svc_aside_p"]}</p>
<a class="btn" href="#contact">{T["get_consult"]}</a><a class="btn btn-ghost" href="{wa()}" rel="noopener">WhatsApp {esc(B["tel_display"])}</a>
<ul>{related}</ul></aside></div></section>'''
    faqs = pg["faqs"]
    faq = f'''<section class="alt-bg"><div class="wrap faq-wrap"><div><p class="eyebrow">{T["faq_eyebrow"]}</p><h2 class="h2">{esc(pg["faq_h"])}</h2></div><div class="faq">{faq_block(faqs)}</div></div></section>'''
    body = breadcrumbs(c, trail) + hero + main + faq + contact_section(c)
    svc = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + "/" + c.path + "#service", "name": pg["crumb"],
           "serviceType": pg["crumb"], "description": pg["desc"], "url": SITE + "/" + c.path, "provider": org_ref(),
           "inLanguage": LANGS[lang]["html"], "areaServed": {"@type": "Country", "name": "Malaysia"},
           "audience": {"@type": "BusinessAudience", "name": "Small and medium enterprises in Malaysia"}}
    lds = [business_ld(c), svc, crumb_trail_ld(c, trail), faq_ld(faqs, lang)]
    if pg.get("howto"):
        lds.append({"@context": "https://schema.org", "@type": "HowTo", "name": pg["howto"]["name"], "inLanguage": LANGS[lang]["html"],
                    "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(pg["howto"]["steps"])]})
    write(c.path, page(c, pg["title"], pg["desc"], body, lds))


# ---------------------------------------------------------------- guides
def build_guide(g, lang):
    c = Ctx(LANGS[lang]["prefix"] + g["path"], lang)
    T, D = c.T, c.D
    others = [x for x in D["GUIDES"] if x["path"] != g["path"]][:4]
    rel = "".join('<li><a href="%s">%s</a></li>' % (c.p(x["path"]), esc(x["h1"])) for x in others)
    svc = "".join('<li><a href="%s">%s</a></li>' % (c.p(s["path"]), esc(s["title"])) for s in D["SERVICES"])
    trail = [(T["home"], ""), (T["guides"], D["GUIDES_PATH"]), (g["short"], g["path"])]
    callout = (f'<strong>{T["guide_callout_h"]}</strong> {T["guide_callout_a"]} <a href="{c.p("#health")}">{T["guide_callout_b"]}</a> '
               f'{T["guide_callout_c"]} <a href="#contact">{T["guide_callout_d"]}</a> {T["guide_callout_e"]}')
    body = breadcrumbs(c, trail) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">{esc(g["tag"])}</p><h1 class="h1" style="font-size:clamp(2rem,4.2vw,3rem);max-width:20em">{esc(g["h1"])}</h1>
<p class="lead">{esc(g["lead"])}</p><p class="meta">{T["guide_by"]} {esc(B["name"])} · {T["guide_updated"]} {g["updated_human"]}</p></div></section>
<section style="padding-top:0"><div class="wrap two-col"><article class="prose">{g["body"]}
<div class="callout">{callout}</div></article>
<aside class="aside-card"><h2>{T["related_services"]}</h2><ul>{svc}</ul><a class="btn" href="#contact">{T["get_consult"]}</a>
<h3 style="margin-top:24px">{T["more_guides"]}</h3><ul>{rel}</ul></aside></div></section>''' + (
        f'<section class="alt-bg"><div class="wrap faq-wrap"><div><p class="eyebrow">{T["faq_eyebrow"]}</p><h2 class="h2">{T["quick_answers"]}</h2></div><div class="faq">{faq_block(g["faqs"])}</div></div></section>' if g.get("faqs") else "") + contact_section(c)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
           "datePublished": g["published"], "dateModified": g["published"], "inLanguage": LANGS[lang]["html"],
           "mainEntityOfPage": SITE + "/" + c.path, "image": SITE + "/assets/og-image.png",
           "author": {"@type": "Organization", "name": B["name"], "url": SITE + "/"}, "publisher": org_ref()}
    lds = [business_ld(c), art, crumb_trail_ld(c, trail)]
    if g.get("faqs"):
        lds.append(faq_ld(g["faqs"], lang))
    write(c.path, page(c, g["title"], g["desc"], body, lds, og_type="article"))


def build_guides_index(lang):
    c = Ctx(LANGS[lang]["prefix"] + DATA[lang]["GUIDES_PATH"], lang)
    T, D = c.T, c.D
    cards = "".join(f'''<a class="post" href="{c.p(g["path"])}"><span class="tag">{esc(g["tag"])}</span><h2 style="font-size:1.3rem;line-height:1.25;margin-top:10px">{esc(g["h1"])}</h2><p>{esc(g["excerpt"])}</p><span class="more">{T["read_guide"]}</span></a>''' for g in D["GUIDES"])
    trail = [(T["home"], ""), (T["guides"], D["GUIDES_PATH"])]
    body = breadcrumbs(c, trail) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">{T["guides"]}</p><h1 class="h1" style="font-size:clamp(2.1rem,4.4vw,3.2rem)">{T["guides_index_h1"]}</h1>
<p class="lead">{T["guides_index_lead"]}</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="cards-3">{cards}</div></div></section>''' + contact_section(c)
    lds = [business_ld(c), {"@context": "https://schema.org", "@type": "CollectionPage", "name": T["guides_index_title"], "url": SITE + "/" + c.path,
                            "description": T["guides_index_desc"], "inLanguage": LANGS[lang]["html"], "isPartOf": {"@id": SITE + "/#website"}},
           crumb_trail_ld(c, trail)]
    write(c.path, page(c, T["guides_index_title"], T["guides_index_desc"], body, lds))


def build_privacy(lang):
    c = Ctx(LANGS[lang]["prefix"] + DATA[lang]["PRIVACY_PATH"], lang)
    T, D = c.T, c.D
    trail = [(T["home"], ""), (T["privacy"], D["PRIVACY_PATH"])]
    body = breadcrumbs(c, trail) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">{T["legal_eyebrow"]}</p><h1 class="h1" style="font-size:clamp(2rem,4vw,3rem)">{T["privacy"]}</h1>
<p class="meta">{T["last_updated"]} {D["PRIVACY_UPDATED"]}</p></div></section>
<section style="padding-top:0"><div class="wrap"><article class="prose">{D["PRIVACY"]}</article></div></section>'''
    write(c.path, page(c, T["privacy_title"], T["privacy_desc"], body, [crumb_trail_ld(c, trail)]))


def build_404():
    c = Ctx("", "en", absolute=True)
    T = c.T
    body = f'''<section class="page-hero"><div class="wrap" style="max-width:720px"><p class="eyebrow">404</p><h1 class="h1" style="font-size:clamp(2rem,4vw,3rem)">{T["nf_h1"]}</h1>
<p class="lead">{T["nf_lead"]}</p><ul class="checks">{"".join('<li><a href="%s">%s</a></li>' % (c.p(p), esc(n)) for n, p in T["nav"])}<li><a href="{c.p("guides/")}">{T["guides"]}</a></li></ul>
<div class="cta-row"><a class="btn" href="{c.p("")}">{T["nf_home"]}</a></div></div></section>'''
    write("404.html", page(c, T["nf_title"], T["nf_title"], body, [], noindex=True, canonical_path="404.html"))


def build_static():
    urls = [("", "1.0", "weekly")] + [(s["path"], "0.9", "monthly") for s in EN.PAGES] + [("guides/", "0.7", "weekly")] + \
           [(g["path"], "0.7", "monthly") for g in EN.GUIDES] + [("privacy-policy/", "0.2", "yearly")]
    ms_urls = [("ms/", "0.9", "weekly")] + [("ms/" + s["path"], "0.8", "monthly") for s in MS.PAGES] + [("ms/panduan/", "0.6", "weekly")] + \
              [("ms/" + g["path"], "0.6", "monthly") for g in MS.GUIDES] + [("ms/" + MS.PRIVACY_PATH, "0.2", "yearly")]

    def alt_links(p):
        en = p if p in PAIRS else REV.get(p)
        ms = PAIRS.get(p) if p in PAIRS else p
        out = ""
        if en is not None:
            out += f'<xhtml:link rel="alternate" hreflang="en-MY" href="{SITE}/{en}"/><xhtml:link rel="alternate" hreflang="x-default" href="{SITE}/{en}"/>'
        if ms is not None:
            out += f'<xhtml:link rel="alternate" hreflang="ms-MY" href="{SITE}/{ms}"/>'
        return out
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' +
          "".join(f"  <url><loc>{SITE}/{p}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority>{alt_links(p)}</url>\n"
                  for p, pr, cf in urls + ms_urls) + "</urlset>\n")
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: {SITE}/sitemap.xml\n")
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)


def make_images():
    from PIL import Image, ImageDraw, ImageFont
    a = os.path.join(OUT, "assets")
    logo = Image.open(os.path.join(HERE, "assets", "logo.png")).convert("RGBA")
    logo.resize((64, 64), Image.LANCZOS).save(os.path.join(a, "favicon.png"))
    ap = Image.new("RGBA", (180, 180), (255, 255, 255, 255))
    ap.paste(logo.resize((140, 140), Image.LANCZOS), (20, 20), logo.resize((140, 140), Image.LANCZOS))
    ap.convert("RGB").save(os.path.join(a, "apple-touch-icon.png"))
    og = Image.new("RGB", (1200, 630), (149, 88, 87))
    d = ImageDraw.Draw(og)

    def font(names, size):
        for n in names:
            try:
                return ImageFont.truetype(n, size)
            except OSError:
                pass
        return ImageFont.load_default()
    serif = ["/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf", "DejaVuSerif.ttf"]
    sans = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVuSans.ttf"]
    card = Image.new("RGBA", (150, 150), (255, 255, 255, 255))
    card.paste(logo.resize((120, 120), Image.LANCZOS), (15, 15), logo.resize((120, 120), Image.LANCZOS))
    og.paste(card.convert("RGB"), (80, 80))
    d.text((80, 270), "CCM Secretarial", font=font(serif, 84), fill="white")
    d.text((80, 385), "Company secretary, accounting, audit & tax", font=font(sans, 38), fill=(244, 231, 230))
    d.text((80, 440), "for Malaysian SMEs", font=font(sans, 38), fill=(244, 231, 230))
    d.text((80, 540), "Shah Alam, Selangor  ·  ccmsecretarial.com", font=font(sans, 28), fill=(226, 179, 178))
    og.save(os.path.join(a, "og-image.png"), optimize=True)


if __name__ == "__main__":
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_static()
    make_images()
    for lang in ("en", "ms"):
        build_home(lang)
        for p in DATA[lang]["PAGES"]:
            build_service(p, lang)
        for g in DATA[lang]["GUIDES"]:
            build_guide(g, lang)
        build_guides_index(lang)
        build_privacy(lang)
    build_404()
    print("Built", sum(len(f) for _, _, f in os.walk(OUT)), "files into", OUT)
