#!/usr/bin/env python3
"""Static site generator for CCM Secretarial.

Usage:  python3 build.py            -> writes the finished site into ./dist
Change SITE below to the live domain before deploying: it feeds canonical
URLs, Open Graph tags, JSON-LD and sitemap.xml.
"""
import html, json, os, shutil, datetime
from content import (TRUST, SERVICES, PERSONAS, QUIZ, QUOTES, HOME_FAQS, PAGES, GUIDES, BUSINESS)

SITE = "https://www.ccmsecretarial.com"
TODAY = datetime.date.today().isoformat()
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "dist")
B = BUSINESS
esc = html.escape

WA_SVG = ('<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.5-.3Z"/></svg>')


def wa(text=""):
    from urllib.parse import quote
    return "https://wa.me/%s%s" % (B["wa"], ("?text=" + quote(text)) if text else "")


def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(",", ":"))


def org_ref():
    return {"@id": SITE + "/#business"}


def business_ld():
    return {
        "@context": "https://schema.org",
        "@type": ["AccountingService", "ProfessionalService"],
        "@id": SITE + "/#business",
        "name": B["name"],
        "alternateName": B["legal"],
        "url": SITE + "/",
        "logo": SITE + "/assets/logo.png",
        "image": SITE + "/assets/og-image.png",
        "description": B["description"],
        "telephone": B["tel"],
        "email": B["email"],
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
                                                 "url": SITE + "/" + s["path"]}} for s in SERVICES]},
    }


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def crumbs_ld(trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + p}
                                for i, (n, p) in enumerate(trail)]}


class Ctx:
    """Per-page helper: relative URLs so the site works at a domain root or a sub-path."""
    def __init__(self, path, absolute=False):
        self.path = path  # e.g. "services/audit/" or ""
        self.depth = len([p for p in path.split("/") if p])
        self.absolute = absolute  # 404 page is served at arbitrary depths

    def u(self, target):
        if self.absolute:
            return SITE + "/" + target
        if target == "#contact":  # every content page carries its own contact section
            return "#contact"
        pre = "../" * self.depth
        return (pre + target) if (pre + target) else "./"


NAV = [("Company secretary", "services/company-secretary/"), ("Accounting & bookkeeping", "services/accounting-bookkeeping/"),
       ("Audit & assurance", "services/audit/"), ("Tax agent & advisory", "services/tax-agent/"),
       ("Register a Sdn Bhd", "services/sdn-bhd-registration/"), ("Switch company secretary", "services/switch-company-secretary/")]


def header(c):
    cur = c.path
    dd = "".join('<a href="%s"%s>%s</a>' % (c.u(p), ' aria-current="page"' if p == cur else "", esc(n)) for n, p in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{c.u("")}" aria-label="{esc(B["name"])} home"><img src="{c.u("assets/logo.png")}" alt="" width="40" height="40"><b>{esc(B["name"])}<small>{esc(B["legal"])}</small></b></a>
<button class="menu-btn" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">☰</button>
<nav class="nav" id="site-nav" aria-label="Main">
<details class="dd"><summary>Services</summary><div class="dd-menu">{dd}</div></details>
<a href="{c.u("#health") if c.path == "" else c.u("#health")}">Health check</a>
<a href="{c.u("guides/")}"{' aria-current="page"' if cur == "guides/" else ""}>Guides</a>
<a href="{c.u("#faq") if c.path == "" else c.u("#faq")}">FAQ</a>
<a href="{c.u("#contact")}" class="nav-cta">Talk to us</a>
</nav>
<a class="btn header-cta" href="{c.u("#contact")}">Talk to us</a>
</div></header>'''


def footer(c):
    svc = "".join('<li><a href="%s">%s</a></li>' % (c.u(p), esc(n)) for n, p in NAV)
    gd = "".join('<li><a href="%s">%s</a></li>' % (c.u(g["path"]), esc(g["short"])) for g in GUIDES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{c.u("")}"><img src="{c.u("assets/logo.png")}" alt="" width="36" height="36" loading="lazy"><b>{esc(B["name"])}<small>{esc(B["legal"])}</small></b></a>
<address style="margin-top:16px">{esc(B["street"])}<br>{esc(B["locality"])}<br><a href="tel:{B["tel"]}">{esc(B["tel_display"])}</a><br><a href="mailto:{B["email"]}">{esc(B["email"])}</a></address></div>
<div><h2>Services</h2><ul>{svc}</ul></div>
<div><h2>Guides</h2><ul>{gd}<li><a href="{c.u("guides/")}">All guides</a></li></ul></div>
<div><h2>Company</h2><ul><li><a href="{c.u("#contact")}">Free consultation</a></li><li><a href="{c.u("#faq")}">FAQ</a></li><li><a href="{wa()}" rel="noopener">WhatsApp</a></li></ul></div>
</div>
<p class="legal">© {datetime.date.today().year} {esc(B["name"])} ({esc(B["legal"])}), Shah Alam, Selangor, Malaysia. General information only, not legal or tax advice.</p>
</div></footer>
<a class="fab" href="{wa()}" rel="noopener" aria-label="Chat with us on WhatsApp">{WA_SVG}<span>How can we help?</span></a>
<script src="{c.u("assets/app.js")}" defer></script>'''


def head(c, title, desc, extra_ld=(), og_type="website", canonical_path=None, noindex=False):
    cp = c.path if canonical_path is None else canonical_path
    url = SITE + "/" + cp
    ldj = "\n".join(ld(x) for x in extra_ld)
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">'
    return f'''<!DOCTYPE html>
<html lang="en-MY">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{robots}
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en-MY" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#955857">
<meta name="geo.region" content="MY-10">
<meta name="geo.placename" content="Shah Alam">
<meta property="og:site_name" content="{esc(B["name"])}">
<meta property="og:locale" content="en_MY">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(B["name"])} — company secretarial, accounting, audit and tax for Malaysian SMEs">
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
            items.append('<li><a href="%s">%s</a></li>' % (c.u(p), esc(n)))
    return '<nav class="crumbs" aria-label="Breadcrumb"><div class="wrap"><ol>%s</ol></div></nav>' % "".join(items)


def faq_block(faqs, heading_tag="h3"):
    return "".join('<details><summary><%s class="faq-q">%s</%s></summary><p>%s</p></details>' %
                   (heading_tag, esc(q), heading_tag, esc(a)) for q, a in faqs)


def contact_section(c, heading="Tell us where you are. We’ll tell you what you need."):
    needs = ["Company secretarial", "Accounting", "Audit", "Tax", "Register a new company", "Not sure yet"]
    stages = ["Not registered yet", "Trading under 2 years", "Trading 2+ years", "Behind on filings"]
    nopts = "".join('<label><input type="checkbox" name="need" value="%s"><span>%s</span></label>' % (n, n) for n in needs)
    sopts = "".join('<label><input type="radio" name="stage" value="%s"><span>%s</span></label>' % (s, s) for s in stages)
    return f'''<section id="contact" class="alt-bg"><div class="wrap contact-grid">
<div>
<p class="eyebrow">Free consultation</p>
<h2 class="h2">{esc(heading)}</h2>
<p class="muted" style="margin-top:14px;font-size:1.05rem">Three quick steps, no obligation. You’ll get a fixed-fee quote for exactly the services that fit your Sdn Bhd, LLP or sole proprietorship.</p>
<dl class="details">
<div><dt>Phone</dt><dd><a href="tel:{B["tel"]}">{esc(B["tel_display"])}</a></dd></div>
<div><dt>WhatsApp</dt><dd><a href="{wa()}" rel="noopener">{esc(B["tel_display"])}</a></dd></div>
<div><dt>Office</dt><dd>{esc(B["street"])}<br>{esc(B["locality"])}</dd></div>
<div><dt>Email</dt><dd><a href="mailto:{B["email"]}">{esc(B["email"])}</a></dd></div>
<div><dt>Hours</dt><dd>{esc(B["hours"])}</dd></div>
</dl>
</div>
<div>
<form class="form" id="enquiry" action="mailto:{B["email"]}" method="post" enctype="text/plain">
<div class="pbars" aria-hidden="true"><i class="on"></i><i></i><i></i></div>
<p class="step-n" aria-live="polite">Step 1 of 3</p>
<fieldset data-step="0"><legend>What can we help with?</legend><div class="opts">{nopts}</div></fieldset>
<fieldset data-step="1"><legend>Where is the business today?</legend><div class="radios">{sopts}</div></fieldset>
<fieldset data-step="2"><legend>How do we reach you?</legend><div class="f">
<div class="two"><label>Your name<input name="name" autocomplete="name" required></label>
<label>Phone / WhatsApp<input name="phone" type="tel" autocomplete="tel" inputmode="tel" required></label></div>
<label>Company name <span class="opt">(optional)</span><input name="company" autocomplete="organization"></label>
<label>Anything we should know? <span class="opt">(optional)</span><textarea name="msg" rows="3"></textarea></label>
</div></fieldset>
<p class="err" role="alert"></p>
<div class="form-nav"><button type="button" class="btn btn-ghost" id="f-back" hidden>Back</button>
<button type="button" class="btn" id="f-next">Continue</button></div>
<noscript><div class="form-nav"><button type="submit" class="btn">Send enquiry by email</button></div></noscript>
<p class="form-foot">Prefer to chat? <a href="{wa()}" rel="noopener">WhatsApp us directly</a>.</p>
</form>
<div class="form thanks" id="thanks" hidden>
<div class="tick"><b>✓</b></div>
<h3>Almost there, <span id="thanks-name">there</span>.</h3>
<p>Send us your details so we can call <span id="thanks-phone"></span> to talk through <span id="thanks-need"></span> and prepare your fixed-fee quote.</p>
<a class="btn" id="thanks-wa" href="{wa()}" rel="noopener">Send via WhatsApp</a>
<a class="btn btn-ghost" id="thanks-mail" style="margin-top:10px;width:100%" href="mailto:{B["email"]}">Send via email</a>
<button type="button" class="form-foot" id="f-new" style="border:0;background:none;cursor:pointer;margin-top:16px;min-height:44px">Start a new enquiry</button>
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
    if not any(t.values()):
        return ""
    out = ['<section class="trust" aria-labelledby="trust-h" style="padding:clamp(40px,5vw,64px) 0"><div class="wrap">',
           '<h2 id="trust-h" class="eyebrow" style="margin-bottom:20px">Licensed, registered and accountable</h2>']
    if t["stats"]:
        out.append('<ul class="stats">%s</ul>' % "".join('<li><b>%s</b><span>%s</span></li>' % (esc(n), esc(l)) for n, l in t["stats"]))
    badges = ["<li><strong>%s</strong><span>%s</span></li>" % (esc(n), esc(v)) for n, v in t["credentials"]]
    badges += ["<li><strong>%s</strong><span>Member</span></li>" % esc(m) for m in t["memberships"]]
    if badges:
        out.append('<ul class="creds">%s</ul>' % "".join(badges))
    if t["clients"]:
        out.append('<p class="muted" style="margin-top:28px;font-size:.9rem">Trusted by Malaysian business owners including</p><ul class="logos">%s</ul>' %
                   "".join('<li><img src="%s" alt="%s" height="36" loading="lazy"></li>' % (c.u(p), esc(n)) for n, p in t["clients"]))
    out.append("</div></section>")
    return "".join(out)


def cta_band(c, h="Want this taken care of?", p="Book a free consultation and get a fixed-fee quote — no obligation."):
    return f'''<section style="padding-top:0"><div class="wrap"><div class="cta-band"><div><h2>{esc(h)}</h2><p>{esc(p)}</p></div>
<div class="cta-row" style="margin:0"><a class="btn btn-light btn-lg" href="{c.u("#contact")}">Get a free consultation</a><a class="btn btn-outline-d btn-lg" href="{wa()}" rel="noopener">WhatsApp us</a></div></div></div></section>'''


# ---------------------------------------------------------------- home
def build_home():
    c = Ctx("")
    planner = f'''<aside class="card planner" id="planner" aria-labelledby="planner-h">
<div class="planner-top"><p class="k">Try it · SSM &amp; LHDN deadline planner</p>
<h2 id="planner-h">Your next filing is due in <span id="p-days">about 30 days</span>.</h2>
<div class="fields"><label>Incorporation date<input type="date" id="p-inc" value="2024-03-15"></label>
<label>Financial year end<select id="p-fye">{"".join('<option value="%d"%s>%s</option>' % (i + 1, " selected" if i == 11 else "", m) for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"]))}</select></label></div></div>
<ol class="dl" id="p-list"><li><span class="d"><b>Form</b><span>C</span></span><span><strong>Form C to LHDN</strong><small>Within 7 months of year end</small></span><span class="chip">—</span></li>
<li><span class="d"><b>SSM</b><span>AR</span></span><span><strong>Annual return to SSM</strong><small>Within 30 days of incorporation anniversary · s.68</small></span><span class="chip">—</span></li></ol>
<div class="planner-foot"><a class="btn btn-dark" id="p-remind" href="{wa("Hi CCM, could you remind me before my SSM and LHDN deadlines?")}" rel="noopener">{WA_SVG.replace('width="22" height="22"', 'width="18" height="18"')} Remind me before these are due</a>
<p class="note">Indicative dates under the Companies Act 2016 and LHDN rules. We’ll confirm yours.</p></div></aside>'''

    hero = f'''<section class="hero"><div class="wrap">
<div>
<p class="pill"><i></i>For Malaysian SMEs · Based in Shah Alam, Selangor</p>
<h1 class="h1">Company secretary &amp; accounting for Malaysian SMEs — <em class="accent">compliant</em>, on time.</h1>
<p class="lead">You run the business; we keep it compliant. Company secretarial, accounting, audit and tax under one roof — one named team watching every SSM and LHDN deadline, so nothing sneaks up on you.</p>
<div class="cta-row"><a class="btn btn-lg" href="#contact">Get a free consultation</a><a class="btn btn-lg btn-ghost" href="#health">Take the 60-second health check →</a></div>
<ul class="ticks"><li>Fixed fees, agreed upfront</li><li>One team for SSM &amp; LHDN</li><li>A named contact, not a queue</li></ul>
</div>
{planner}
</div></section>
<div class="strip"><ul><li><strong>Four services, one team</strong><span>Secretarial, accounts, audit, tax</span></li><li><strong>SSM &amp; LHDN aligned</strong><span>Filings done under current law</span></li><li><strong>A named contact</strong><span>Not a ticket queue</span></li><li><strong>No surprises</strong><span>Fees agreed before we start</span></li></ul></div>'''

    tabs = "".join(f'<button type="button" class="tab" role="tab" data-persona-tab="{p["id"]}" aria-selected="{"true" if p["id"]=="run" else "false"}"><span class="n">0{i+1}</span><span class="t">{esc(p["label"])}</span><span class="s">{esc(p["sub"])}</span></button>'
                   for i, p in enumerate(PERSONAS))
    panels = ""
    for p in PERSONAS:
        panels += f'''<div class="persona" data-persona-panel="{p["id"]}" role="tabpanel">
<div class="card"><h3>{esc(p["headline"])}</h3><p class="muted">{esc(p["intro"])}</p><ul class="checks">{"".join("<li>%s</li>" % esc(n) for n in p["needs"])}</ul></div>
<div class="plan"><div class="top"><p>Recommended package</p><span>Fixed fee</span></div><h3>{esc(p["plan"])}</h3><p class="pd">{esc(p["planDesc"])}</p>
<ul>{"".join("<li>%s</li>" % esc(i) for i in p["includes"])}</ul>
<div class="acts"><a class="btn btn-light btn-lg" href="#contact" data-quote-persona="{esc(p["plan"])}" data-needs="{esc("|".join(p["need"]))}" data-stage="{esc(p["stage"])}">Get my fixed-fee quote</a>
<a class="btn btn-outline-d" href="{wa("Hi CCM, I’m %s and I have a question about your %s package." % (p["label"].lower(), p["plan"]))}" rel="noopener">Ask a quick question on WhatsApp</a>
<p class="alt">{esc(p["alt"])}</p></div></div></div>'''
    paths = f'''<section id="paths"><div class="wrap"><div class="sec-head"><p class="eyebrow">Start here</p><h2 class="h2">Where is your business right now?</h2>
<p class="muted">Pick the one that sounds like you. We’ll show exactly what you need — and nothing you don’t.</p></div>
<div class="tabs" role="tablist" aria-label="Business stage">{tabs}</div>{panels}</div></section>'''

    cards = "".join(f'''<a class="svc" href="{s["path"]}"><span class="n">0{i+1}</span><h3>{esc(s["title"])}</h3><p>{esc(s["desc"])}</p>
<ul>{"".join("<li>%s</li>" % esc(x) for x in s["items"])}</ul><span class="more">{esc(s["cta"])}</span></a>''' for i, s in enumerate(SERVICES))
    services = f'''<section id="services" style="padding-top:0"><div class="wrap"><div style="padding-top:40px;border-top:1px solid var(--line);margin-bottom:28px;max-width:760px">
<h2 class="h2" style="font-size:clamp(1.6rem,2.8vw,2.1rem)">Everything a Malaysian SME needs, under one roof.</h2>
<p class="muted" style="margin-top:12px">From Sdn Bhd registration and company secretary services to monthly bookkeeping, statutory audit and LHDN tax filing — use one service or all four.</p></div>
<div class="grid">{cards}</div></div></section>'''

    quiz_items = "".join("<li>%s</li>" % esc(q["q"]) for q in QUIZ)
    health = f'''<section id="health" class="dark"><div class="wrap split">
<div><p class="eyebrow">Compliance health check</p><h2 class="h2">Is your company quietly falling behind?</h2>
<p class="muted" style="margin-top:16px;font-size:1.05rem;max-width:30em">Five questions, sixty seconds. Late SSM and LHDN filings can mean compounds for the company <em>and</em> its directors — find out where you stand before they do.</p>
<ul class="badges"><li>No sign-up</li><li>Instant result</li><li>Free follow-up if you want it</li></ul></div>
<div class="quiz" id="quiz">
<div id="quiz-static"><p class="muted">The five questions we ask:</p><ol class="noscript-list">{quiz_items}</ol><p class="muted" style="margin-top:16px">Answer “no” or “not sure” to any of them? <a href="{wa("Hi CCM, I’d like a compliance health check.")}" style="color:var(--brand-on-dark)">Message us on WhatsApp</a>.</p></div>
<div id="quiz-run" hidden><div class="quiz-meta"><span id="quiz-n">Question 1 of 5</span><button type="button" id="quiz-back" hidden>← Back</button></div>
<div class="bar"><i id="quiz-bar" style="width:0"></i></div>
<p class="q" id="quiz-q" aria-live="polite"></p>
<div class="ans"><button type="button" data-ans="yes">Yes</button><button type="button" data-ans="no">No</button><button type="button" data-ans="unsure">Not sure</button></div></div>
<div id="quiz-done" hidden><div class="score"><div class="ring" id="quiz-ring"><b id="quiz-score">0/5</b></div><div><h3 id="quiz-title"></h3><p id="quiz-msg"></p></div></div>
<div class="gaps" id="quiz-gaps" hidden><h4>What we’d fix first</h4><ul></ul></div>
<div class="quiz-end"><a class="btn btn-light" id="quiz-wa" href="{wa()}" rel="noopener">Send my result</a><button type="button" class="btn btn-outline-d" id="quiz-reset">Retake</button></div></div>
<script type="application/json" id="quiz-data">{json.dumps(QUIZ, ensure_ascii=False)}</script>
</div></div></section>'''

    steps = [("1", "You · 15 min", "Talk to us", "A short call to understand your business and what’s coming due.", ""),
             ("2", "You · approve", "Agree a fixed fee", "A clear quote for the services you need. Nothing hidden.", ""),
             ("3", "Us", "We take it over", "Filings, accounts, audit and tax — prepared by us, signed by you.", "us"),
             ("4", "Us · every year", "Stay compliant", "Proactive reminders and updates, from a team that answers.", "us")]
    process = f'''<section id="process"><div class="wrap"><div class="sec-head"><p class="eyebrow">How it works</p><h2 class="h2">Four steps. Most of them ours.</h2></div>
<ol class="steps">{"".join(f'<li class="{cl}"><span class="top"><span class="num">{n}</span><span class="who">{w}</span></span><h3>{esc(t)}</h3><p>{esc(d)}</p></li>' for n, w, t, d, cl in steps)}</ol></div></section>'''

    quotes = "".join(f'''<figure class="quote"><blockquote><p class="lead-q">“{esc(q["lead"])}”</p><p class="body-q">{esc(q["body"])}</p></blockquote>
<figcaption><strong>{esc(q["name"])}</strong><span>{esc(q["role"])}</span><em>{esc(q["uses"])}</em></figcaption></figure>''' for q in QUOTES)
    clients = f'''<section id="clients" class="alt-bg"><div class="wrap"><div class="sec-head"><p class="eyebrow">Clients</p><h2 class="h2">Malaysian business owners like you, in their own words.</h2></div>
<div class="quotes">{quotes}</div></div></section>'''

    guides = "".join(f'''<a class="post" href="{g["path"]}"><span class="tag">{esc(g["tag"])}</span><h3>{esc(g["h1"])}</h3><p>{esc(g["excerpt"])}</p><span class="more">Read the guide</span></a>''' for g in GUIDES)
    guide_sec = f'''<section><div class="wrap"><div class="sec-head"><p class="eyebrow">Guides for SME owners</p><h2 class="h2">Plain-English answers on Malaysian compliance.</h2></div><div class="cards-3">{guides}</div></div></section>'''

    faq = f'''<section id="faq"><div class="wrap faq-wrap"><div><p class="eyebrow">FAQ</p><h2 class="h2">Common questions</h2>
<p class="muted" style="margin-top:14px;font-size:1.05rem">Can’t find your answer? <a href="{wa("Hi CCM, I have a question: ")}" rel="noopener">Ask us on WhatsApp.</a></p></div>
<div class="faq">{faq_block(HOME_FAQS)}</div></div></section>'''

    areas = f'''<section style="padding-top:0"><div class="wrap"><div style="border-top:1px solid var(--line);padding-top:40px;max-width:760px"><h2 class="h2" style="font-size:clamp(1.5rem,2.6vw,2rem)">Company secretary in Shah Alam, serving SMEs across Malaysia</h2>
<p class="muted" style="margin-top:12px">Our office is in Elmina, Shah Alam. Most SSM and LHDN work is done online, so we support Sdn Bhd, LLP and sole-proprietor clients throughout the Klang Valley and the rest of Malaysia — by phone, WhatsApp or in person.</p>
<ul class="areas"><li>Shah Alam</li><li>Klang</li><li>Petaling Jaya</li><li>Subang Jaya</li><li>Puchong</li><li>Kuala Lumpur</li><li>Nationwide (online)</li></ul></div></div></section>'''

    body = hero + trust_block(c) + paths + services + health + process + clients + guide_sec + faq + areas + contact_section(c)
    title = "Company Secretary & Accounting Shah Alam | CCM Secretarial"
    desc = "Company secretary, SSM registration, bookkeeping, audit & LHDN tax for Malaysian SMEs. Fixed fees, one named team. Based in Shah Alam. Free consultation."
    lds = [business_ld(),
           {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": B["name"],
            "inLanguage": "en-MY", "publisher": org_ref()},
           {"@context": "https://schema.org", "@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": title,
            "description": desc, "isPartOf": {"@id": SITE + "/#website"}, "about": org_ref(), "inLanguage": "en-MY"},
           faq_ld(HOME_FAQS)]
    write("", page(c, title, desc, body, lds))


# ---------------------------------------------------------------- service pages
def build_service(pg):
    c = Ctx(pg["path"])
    trail = [("Home", ""), ("Services", "#services"), (pg["crumb"], pg["path"])]
    # breadcrumb JSON-LD: "Services" points at the home anchor -> use home + page only for validity
    bl = crumbs_ld([("Home", ""), (pg["crumb"], pg["path"])])
    hero = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><p class="eyebrow">{esc(pg["eyebrow"])}</p><h1 class="h1" style="font-size:clamp(2.1rem,4.4vw,3.2rem)">{esc(pg["h1"])}</h1><p class="lead">{esc(pg["lead"])}</p>
<div class="cta-row"><a class="btn btn-lg" href="#contact">Get a fixed-fee quote</a><a class="btn btn-lg btn-ghost" href="{wa("Hi CCM, I’d like to ask about %s." % pg["crumb"].lower())}" rel="noopener">Ask on WhatsApp</a></div></div>
<div class="card"><h2 style="font-size:1.3rem">{esc(pg["box_title"])}</h2><ul class="checks">{"".join("<li>%s</li>" % esc(x) for x in pg["box"])}</ul></div>
</div></section>'''
    related = "".join('<li><a href="%s">%s</a></li>' % (c.u(p), esc(n)) for n, p in NAV if p != pg["path"])
    main = f'''<section style="padding-top:0"><div class="wrap two-col"><article class="prose">{pg["body"]}</article>
<aside class="aside-card"><h2>Talk to a named specialist</h2><p>Free 15-minute call. You’ll get a fixed fee before we start.</p>
<a class="btn" href="#contact">Get a free consultation</a><a class="btn btn-ghost" href="{wa()}" rel="noopener">WhatsApp {esc(B["tel_display"])}</a>
<ul>{related}</ul></aside></div></section>'''
    faqs = pg["faqs"]
    faq = f'''<section class="alt-bg"><div class="wrap faq-wrap"><div><p class="eyebrow">FAQ</p><h2 class="h2">{esc(pg["faq_h"])}</h2></div><div class="faq">{faq_block(faqs)}</div></div></section>'''
    body = breadcrumbs(c, [("Home", ""), (pg["crumb"], pg["path"])]) + hero + main + faq + contact_section(c)
    svc = {"@context": "https://schema.org", "@type": "Service", "@id": SITE + "/" + pg["path"] + "#service", "name": pg["crumb"],
           "serviceType": pg["crumb"], "description": pg["desc"], "url": SITE + "/" + pg["path"], "provider": org_ref(),
           "areaServed": {"@type": "Country", "name": "Malaysia"}, "audience": {"@type": "BusinessAudience", "name": "Small and medium enterprises in Malaysia"}}
    lds = [business_ld(), svc, bl, faq_ld(faqs)]
    if pg.get("howto"):
        lds.append({"@context": "https://schema.org", "@type": "HowTo", "name": pg["howto"]["name"],
                    "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t} for i, (n, t) in enumerate(pg["howto"]["steps"])]})
    write(pg["path"], page(c, pg["title"], pg["desc"], body, lds))


# ---------------------------------------------------------------- guides
def build_guide(g):
    c = Ctx(g["path"])
    others = [x for x in GUIDES if x["path"] != g["path"]]
    rel = "".join('<li><a href="%s">%s</a></li>' % (c.u(x["path"]), esc(x["h1"])) for x in others)
    svc = "".join('<li><a href="%s">%s</a></li>' % (c.u(s["path"]), esc(s["title"])) for s in SERVICES)
    body = breadcrumbs(c, [("Home", ""), ("Guides", "guides/"), (g["short"], g["path"])]) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">{esc(g["tag"])}</p><h1 class="h1" style="font-size:clamp(2rem,4.2vw,3rem);max-width:20em">{esc(g["h1"])}</h1>
<p class="lead">{esc(g["lead"])}</p><p class="meta">By {esc(B["name"])} · Updated {g["updated_human"]}</p></div></section>
<section style="padding-top:0"><div class="wrap two-col"><article class="prose">{g["body"]}
<div class="callout"><strong>Not sure where your company stands?</strong> Take the <a href="{c.u("#health")}">60-second compliance health check</a> or <a href="{c.u("#contact")}">talk to us</a> — we’ll confirm your exact deadlines.</div></article>
<aside class="aside-card"><h2>Related services</h2><ul>{svc}</ul><a class="btn" href="#contact">Get a free consultation</a>
<h3 style="margin-top:24px">More guides</h3><ul>{rel}</ul></aside></div></section>''' + (
        f'<section class="alt-bg"><div class="wrap faq-wrap"><div><p class="eyebrow">FAQ</p><h2 class="h2">Quick answers</h2></div><div class="faq">{faq_block(g["faqs"])}</div></div></section>' if g.get("faqs") else "") + contact_section(c)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": g["h1"], "description": g["desc"],
           "datePublished": g["published"], "dateModified": g["published"], "inLanguage": "en-MY",
           "mainEntityOfPage": SITE + "/" + g["path"], "image": SITE + "/assets/og-image.png",
           "author": {"@type": "Organization", "name": B["name"], "url": SITE + "/"}, "publisher": org_ref()}
    lds = [business_ld(), art, crumbs_ld([("Home", ""), ("Guides", "guides/"), (g["short"], g["path"])])]
    if g.get("faqs"):
        lds.append(faq_ld(g["faqs"]))
    write(g["path"], page(c, g["title"], g["desc"], body, lds, og_type="article"))


def build_guides_index():
    c = Ctx("guides/")
    cards = "".join(f'''<a class="post" href="{c.u(g["path"])}"><span class="tag">{esc(g["tag"])}</span><h2 style="font-size:1.3rem;line-height:1.25;margin-top:10px">{esc(g["h1"])}</h2><p>{esc(g["excerpt"])}</p><span class="more">Read the guide</span></a>''' for g in GUIDES)
    body = breadcrumbs(c, [("Home", ""), ("Guides", "guides/")]) + f'''
<section class="page-hero"><div class="wrap"><p class="eyebrow">Guides</p><h1 class="h1" style="font-size:clamp(2.1rem,4.4vw,3.2rem)">Company compliance guides for Malaysian SMEs</h1>
<p class="lead">Practical, plain-English guides on company secretarial, SSM, LHDN, audit and accounting requirements for Sdn Bhd owners.</p></div></section>
<section style="padding-top:0"><div class="wrap"><div class="cards-3">{cards}</div></div></section>''' + contact_section(c)
    title = "Compliance Guides for Malaysian SMEs | CCM Secretarial"
    desc = "Plain-English guides on company secretary rules, SSM annual returns, LHDN Form C and statutory audit for Sdn Bhd and SME owners in Malaysia."
    lds = [business_ld(), {"@context": "https://schema.org", "@type": "CollectionPage", "name": title, "url": SITE + "/guides/", "description": desc, "isPartOf": {"@id": SITE + "/#website"}},
           crumbs_ld([("Home", ""), ("Guides", "guides/")])]
    write("guides/", page(c, title, desc, body, lds))


def build_404():
    c = Ctx("", absolute=True)
    body = f'''<section class="page-hero"><div class="wrap" style="max-width:720px"><p class="eyebrow">404</p><h1 class="h1" style="font-size:clamp(2rem,4vw,3rem)">That page isn’t here</h1>
<p class="lead">The page may have moved. Try one of these instead:</p><ul class="checks">{"".join('<li><a href="%s">%s</a></li>' % (c.u(p), esc(n)) for n, p in NAV)}<li><a href="{c.u("guides/")}">Compliance guides</a></li></ul>
<div class="cta-row"><a class="btn" href="{c.u("")}">Back to home</a></div></div></section>'''
    write("404.html", page(c, "Page not found | CCM Secretarial", "Page not found.", body, [], noindex=True, canonical_path="404.html"))


def build_static():
    urls = [("", "1.0", "weekly")] + [(s["path"], "0.9", "monthly") for s in PAGES] + [("guides/", "0.7", "weekly")] + [(g["path"], "0.7", "monthly") for g in GUIDES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{SITE}/{p}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n" for p, pr, cf in urls) + "</urlset>\n"
    open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: {SITE}/sitemap.xml\n")
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)


def make_images():
    from PIL import Image, ImageDraw, ImageFont
    a = os.path.join(OUT, "assets")
    logo = Image.open(os.path.join(HERE, "assets", "logo.png")).convert("RGBA")
    fav = logo.resize((64, 64), Image.LANCZOS)
    fav.save(os.path.join(a, "favicon.png"))
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
    build_home()
    for p in PAGES:
        build_service(p)
    for g in GUIDES:
        build_guide(g)
    build_guides_index()
    build_404()
    print("Built", sum(len(f) for _, _, f in os.walk(OUT)), "files into", OUT)
