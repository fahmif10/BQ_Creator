# -*- coding: utf-8 -*-
"""All copy for the CCM Secretarial site. Edit text here, then run build.py."""

BUSINESS = {
    "name": "CCM Secretarial",
    "legal": "Corporate Consultant & Management",
    "wa": "60164779365",
    "tel": "+60164779365",
    "tel_display": "016-477 9365",
    "email": "corpsec@ccmsecretarial.com",
    "street": "1, Jalan Elmina Ilham 18, Seksyen U16",
    "locality": "Elmina, Shah Alam, Selangor, Malaysia",
    # The original site showed this in square brackets (placeholder). Confirm before launch.
    "hours": "Mon–Fri, 9:00am–6:00pm",
    "description": ("CCM Secretarial (Corporate Consultant & Management) is a Shah Alam firm providing company secretarial, "
                    "SSM registration, accounting and bookkeeping, statutory audit and LHDN tax services to Malaysian SMEs."),
}

SERVICES = [
    {"path": "services/company-secretary/", "title": "Company Secretarial", "cta": "Company secretary services",
     "desc": "Statutory compliance and documentation under the Companies Act 2016.",
     "items": ["Sdn Bhd, LLP & foreign company registration", "Annual returns, AGMs & resolutions",
               "Statutory registers & beneficial ownership", "Director, share & address changes"]},
    {"path": "services/accounting-bookkeeping/", "title": "Accounting & Bookkeeping", "cta": "Accounting services",
     "desc": "Accurate, timely accounts that help you manage the business better.",
     "items": ["Monthly bookkeeping & bank reconciliation", "Management accounts & reports",
               "Year-end financial statements", "Payroll, EPF, SOCSO & EIS"]},
    {"path": "services/audit/", "title": "Audit & Assurance", "cta": "Audit services",
     "desc": "Independent audit to meet statutory and regulatory requirements.",
     "items": ["Statutory audit of financial statements", "Audit preparation & coordination",
               "Special-purpose reviews", "Internal control recommendations"]},
    {"path": "services/tax-agent/", "title": "Tax Agent & Advisory", "cta": "Tax services",
     "desc": "Stay on the right side of LHDN and optimise your position.",
     "items": ["Corporate & personal tax filing", "CP204 tax estimates", "SST registration & returns",
               "Tax planning & LHDN queries"]},
]

PERSONAS = [
    {"id": "start", "label": "Starting a company", "sub": "Not registered yet",
     "headline": "Get your Sdn Bhd set up right, first time.",
     "intro": "Most first-year penalties come from steps founders didn’t know existed. We handle all of them.",
     "needs": ["Name search & SSM registration", "Constitution & first board resolutions",
               "Company secretary appointed within 30 days (Companies Act 2016)", "Tax file registration with LHDN",
               "Bank account opening documents"],
     "plan": "Launch", "planDesc": "Incorporation plus your first year of compliance.",
     "includes": ["Everything to incorporate", "12 months company secretary", "Bookkeeping set-up", "LHDN tax file registration"],
     "alt": "Only need registration? Ask about Incorporate.", "need": ["Register a new company"], "stage": "Not registered yet"},
    {"id": "run", "label": "Running an Sdn Bhd", "sub": "Trading, want it handled",
     "headline": "Hand over the whole yearly compliance cycle.",
     "intro": "One team runs secretarial, books, audit and tax together — so nothing falls between two firms.",
     "needs": ["Annual return & financial statements to SSM", "Monthly bookkeeping & payroll (EPF, SOCSO, EIS)",
               "Statutory audit coordination", "Form C and CP204 to LHDN"],
     "plan": "Full compliance", "planDesc": "Secretarial, accounts, audit and tax — one team.",
     "includes": ["Named company secretary", "Monthly bookkeeping", "Audit coordination", "Form C & CP204 filing"],
     "alt": "Just need a secretary? Ask about Secretarial.",
     "need": ["Company secretarial", "Accounting", "Audit", "Tax"], "stage": "Trading 2+ years"},
    {"id": "foreign", "label": "Overseas founder", "sub": "Branch, LLP or subsidiary",
     "headline": "Enter Malaysia with the paperwork handled.",
     "intro": "We help you pick the right structure, then register and keep it compliant from here.",
     "needs": ["Choosing branch, LLP or Sdn Bhd", "Document review & certification",
               "Resident agent or compliance officer", "Post-registration checklist"],
     "plan": "Foreign company / LLP", "planDesc": "For overseas founders and partnerships.",
     "includes": ["Branch or LLP registration", "Document review & certification", "Resident agent / compliance officer",
                  "Post-registration checklist"],
     "alt": "Not sure which structure? We’ll advise on the first call.", "need": ["Register a new company"],
     "stage": "Not registered yet"},
    {"id": "behind", "label": "Behind on filings", "sub": "Or unhappy with your firm",
     "headline": "Get back on track — without the stress.",
     "intro": "Overdue returns happen. We collect your records, fix what’s outstanding and keep it clean after.",
     "needs": ["Records collected from your previous firm", "Compliance health check", "Overdue filings regularised",
               "Then the package that fits"],
     "plan": "Switch to us", "planDesc": "Moving from another firm? We make it painless.",
     "includes": ["Records handover handled for you", "Full compliance health check", "Late filings regularised",
                  "Ongoing package after"],
     "alt": "Talk to us before the next compound arrives.", "need": ["Not sure yet"], "stage": "Behind on filings"},
]

QUIZ = [
    {"q": "Has your company appointed a licensed company secretary?",
     "fix": "Appoint a licensed company secretary (required under the Companies Act 2016)."},
    {"q": "Was your last annual return lodged with SSM on time?",
     "fix": "Lodge outstanding annual returns and regularise late ones."},
    {"q": "Were your latest audited accounts circulated and lodged on time?",
     "fix": "Bring audit and financial statement lodgement back on schedule."},
    {"q": "Was your last Form C filed within 7 months of year end?",
     "fix": "File Form C and review your CP204 estimates with LHDN."},
    {"q": "Are your books updated at least every month?",
     "fix": "Set up monthly bookkeeping so year end isn’t a scramble."},
]

QUOTES = [
    {"name": "En. Kamarul", "role": "Gold & jewellery retail", "uses": "Secretarial · Accounts · Audit · Tax",
     "lead": "With CCM, I have been able to expand my jewellery business through sound and effective consultations.",
     "body": "Their team handled everything — from SSM registration to monthly accounting, audit coordination, and tax filing — so we could focus on growing our gold retail business. They’re professional, fast, and always proactive with reminders and compliance updates."},
    {"name": "Pn. Adilla", "role": "Children’s Development Centre", "uses": "Secretarial · Accounts · Payroll",
     "lead": "CCM took that entire burden off our shoulders.",
     "body": "Our focus has always been on therapy and families — not paperwork or statutory filings. They handled our secretarial, accounting, and payroll with such professionalism and understanding, and were patient in explaining every compliance step."},
    {"name": "Prof Fadzil", "role": "Project Management Consultant", "uses": "Secretarial · Audit · Tax",
     "lead": "We see them as an extension of our management team.",
     "body": "With multiple projects, subcontractors and tenders, compliance and tax planning are critical. Their accounting team set up clear reporting that helped us track project profitability and prepare for audits with confidence — and their tax advice helped us optimise cash flow."},
]

HOME_FAQS = [
    ("Does every Sdn Bhd need a company secretary?",
     "Yes. Under the Companies Act 2016, every company must appoint at least one company secretary within 30 days of incorporation. The secretary must be licensed or registered with SSM."),
    ("Does my private company need an audit?",
     "Most do, although SSM allows certain dormant, zero-revenue and threshold-qualified small companies to be exempt. We’ll check whether your company qualifies before recommending an audit."),
    ("When is my company’s tax return due?",
     "Form C must be filed with LHDN within seven months after your financial year end. Tax estimates (CP204) are due 30 days before the start of each basis period, with instalments paid monthly."),
    ("What happens if a filing is late?",
     "SSM and LHDN can impose compounds and penalties on the company and its officers. If you already have overdue filings, we can help you regularise them when you switch to us."),
    ("Can I use only one of your services?",
     "Of course. Many clients start with secretarial or accounting only and add audit and tax later. Pricing is flexible and built around what you need."),
    ("Where is CCM Secretarial based, and do you serve SMEs outside Shah Alam?",
     "Our office is in Elmina, Shah Alam, Selangor. Most SSM and LHDN work is done online, so we support SMEs across the Klang Valley and the rest of Malaysia by phone, WhatsApp and in person."),
]


def tbl(head, rows):
    h = "".join("<th>%s</th>" % x for x in head)
    r = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % x for x in row) for row in rows)
    return '<div class="tbl-scroll"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (h, r)


# ============================================================ SERVICE PAGES
PAGES = []

PAGES.append({
    "path": "services/company-secretary/", "crumb": "Company secretary services", "eyebrow": "Company secretarial · Malaysia",
    "title": "Company Secretary Services Malaysia for SMEs | CCM",
    "desc": "Licensed company secretary for Sdn Bhd & LLP: SSM annual returns, statutory registers, resolutions and director changes. Fixed fee. Shah Alam.",
    "h1": "Company secretary services for Malaysian SMEs",
    "lead": "A named company secretary who keeps your Sdn Bhd, LLP or foreign company compliant with the Companies Act 2016 and SSM — so filings are never late.",
    "box_title": "What’s included", "box": ["Company secretary appointment", "Annual return filing with SSM", "Statutory registers & minute books",
                                        "Director, shareholder & address changes", "Beneficial ownership records", "Deadline reminders, every year"],
    "faq_h": "Company secretary questions",
    "body": """
<h2>Why every Malaysian company needs a company secretary</h2>
<p>Under the Companies Act 2016, every company incorporated in Malaysia must appoint at least one company secretary within 30 days of incorporation. The secretary must be a natural person who is ordinarily resident in Malaysia and is licensed or otherwise qualified under the Act. For most SMEs, hiring a full-time secretary makes no sense — which is why outsourcing to a company secretarial firm is the norm.</p>
<h2>What our company secretarial service covers</h2>
<ul>
<li><strong>Annual return filing</strong> — prepared and lodged with SSM within 30 days of your incorporation anniversary.</li>
<li><strong>Meetings and resolutions</strong> — board and shareholder resolutions, AGM notices and minutes, and circulation of audited accounts.</li>
<li><strong>Statutory registers</strong> — directors, members, charges and the other records the Act requires you to keep at your registered office.</li>
<li><strong>Changes to company particulars</strong> — appointing or removing directors, transferring shares, changing the registered address, business activity or company name.</li>
<li><strong>Beneficial ownership</strong> — keeping your register of persons with significant control accurate and lodged with SSM.</li>
<li><strong>Company secretary for Sdn Bhd, LLP and foreign companies</strong> — including resident agent or compliance officer arrangements for overseas founders.</li>
</ul>
<h2>A named secretary, not a ticket queue</h2>
<p>You get one named contact who knows your company, your directors and your year end. We track every SSM deadline for you and remind you before it arrives, so you don’t find out about a missed annual return from a compound notice.</p>
<h2>Key SSM deadlines we manage</h2>
""" + tbl(["Obligation", "Usual deadline"], [
        ["Appoint a company secretary", "Within 30 days of incorporation"],
        ["Annual return to SSM", "Within 30 days of the incorporation anniversary"],
        ["Circulate audited financial statements", "Within 6 months of financial year end"],
        ["Lodge financial statements with SSM", "Within 30 days of circulation"],
        ["Change of directors / address", "Generally within 14 days of the change"]]) + """
<p>See our full <a href="../../guides/sdn-bhd-compliance-calendar-malaysia/">Sdn Bhd compliance calendar</a> for the LHDN dates as well.</p>
<h2>Switching company secretary?</h2>
<p>If your current secretary is slow, unresponsive or you have overdue filings, we handle the handover of records and regularise late returns. <a href="../switch-company-secretary/">Learn how switching works</a>.</p>
""",
    "faqs": [
        ("How much does a company secretary cost in Malaysia?", "Fees depend on the company type, number of directors and filings involved. We quote a fixed fee after a short call, so you know the annual cost before we start."),
        ("Can I be my own company secretary?", "Only if you are a qualified person under the Companies Act 2016 — for example a member of a prescribed professional body or licensed by SSM. Most business owners appoint a licensed company secretary instead."),
        ("Do you act for LLPs and sole proprietorships?", "Yes. We support Sdn Bhd, LLP and foreign companies, and can help sole proprietors register or convert to a Sdn Bhd."),
        ("What happens if an annual return is filed late?", "SSM can issue compounds against the company and its officers. We can help regularise overdue returns and bring your filings back on schedule."),
    ],
})

PAGES.append({
    "path": "services/accounting-bookkeeping/", "crumb": "Accounting & bookkeeping", "eyebrow": "Accounting · Malaysia",
    "title": "Accounting & Bookkeeping for Malaysian SMEs | CCM",
    "desc": "Monthly bookkeeping, management accounts, payroll (EPF, SOCSO, EIS) and year-end financial statements for Sdn Bhd and SMEs. Fixed fee. Shah Alam.",
    "h1": "Accounting & bookkeeping services for Malaysian SMEs",
    "lead": "Accurate monthly books, payroll and year-end financial statements — prepared in line with Malaysian standards and ready for audit and LHDN.",
    "box_title": "What’s included", "box": ["Monthly bookkeeping & bank reconciliation", "Management accounts & reports",
                                        "Year-end financial statements", "Payroll: EPF, SOCSO, EIS & PCB", "SST and e-Invoice readiness support",
                                        "Audit-ready records"],
    "faq_h": "Accounting questions",
    "body": """
<h2>Bookkeeping that keeps you compliant all year</h2>
<p>Most SME tax and audit problems start with books that are updated once a year, in a rush. We keep your records current every month, so your financial statements, audit and Form C are built on clean numbers — not reconstructed from a shoebox of receipts.</p>
<h2>What we do each month</h2>
<ul>
<li>Record sales, purchases and expenses from your invoices, receipts and bank statements.</li>
<li>Reconcile your bank and payment accounts and follow up missing documents.</li>
<li>Prepare management accounts — profit and loss, balance sheet and simple cash-flow view.</li>
<li>Run payroll and file <strong>EPF, SOCSO and EIS</strong> contributions and monthly tax deductions (PCB).</li>
<li>Prepare and file SST returns if you are SST-registered.</li>
</ul>
<h2>Year-end financial statements</h2>
<p>At year end we prepare financial statements in line with the applicable Malaysian financial reporting framework, ready to go to your auditor, your directors and SSM. Because the books were kept monthly, audit preparation is faster and less disruptive.</p>
<h2>e-Invoice and digital readiness</h2>
<p>Malaysia’s LHDN e-Invoice (MyInvois) requirement is being phased in by business turnover. We help SMEs check which phase applies, set up the right accounting software or portal workflow, and keep records in the format LHDN expects. Talk to us about where your business stands.</p>
<h2>Why SMEs choose one team for accounts, audit and tax</h2>
<p>When the firm keeping your books also coordinates your <a href="../audit/">statutory audit</a> and files your <a href="../tax-agent/">corporate tax</a>, nothing falls between two providers and year end stops being a scramble.</p>
""",
    "faqs": [
        ("How often do you update our books?", "Monthly, as a minimum. You send documents through WhatsApp, email or shared folder and we reconcile and report each month."),
        ("Do you use accounting software like AutoCount, SQL or Xero?", "We work with the common platforms used by Malaysian SMEs and can advise on which fits your size and industry. Ask us about your current setup."),
        ("Can you handle payroll, EPF and SOCSO?", "Yes. We run payroll and prepare EPF, SOCSO, EIS and PCB submissions so your employer obligations are met on time."),
        ("Can I hire you for year-end accounts only?", "Yes, though we recommend monthly bookkeeping — it is usually cheaper than cleaning up a full year of records at year end."),
    ],
})

PAGES.append({
    "path": "services/audit/", "crumb": "Audit & assurance", "eyebrow": "Audit · Malaysia",
    "title": "Statutory Audit for Sdn Bhd & SMEs Malaysia | CCM",
    "desc": "Statutory audit, audit preparation and exemption checks for Malaysian private companies. Independent, on schedule with SSM. Fixed fee. Shah Alam.",
    "h1": "Statutory audit & assurance for Malaysian SMEs",
    "lead": "Independent audit of your financial statements that meets Companies Act 2016 and SSM requirements — coordinated with your accounts and tax so it runs on time.",
    "box_title": "What’s included", "box": ["Statutory audit of financial statements", "Audit-exemption eligibility check",
                                        "Audit preparation & coordination", "Special-purpose reviews", "Internal control recommendations"],
    "faq_h": "Audit questions",
    "body": """
<h2>Does your Sdn Bhd need to be audited?</h2>
<p>Most Malaysian private companies must have their financial statements audited each year by a licensed company auditor. The Companies Act 2016 lets certain companies — for example dormant companies and small, threshold-qualified private companies — claim an exemption. Whether yours qualifies depends on its revenue, assets and other conditions, so we check your eligibility before recommending an audit. Read our guide: <a href="../../guides/do-sdn-bhd-need-audit-malaysia/">Does my Sdn Bhd need an audit?</a></p>
<h2>What a statutory audit involves</h2>
<ul>
<li><strong>Planning</strong> — we agree the timetable backwards from your SSM and LHDN deadlines.</li>
<li><strong>Preparation</strong> — we confirm your schedules, bank confirmations and supporting documents are ready.</li>
<li><strong>Fieldwork</strong> — the audit of balances and transactions, with clear queries rather than surprises.</li>
<li><strong>Reporting</strong> — the audited financial statements and auditor’s report for directors to sign and for lodging with SSM.</li>
<li><strong>Management feedback</strong> — practical recommendations on internal controls and bookkeeping.</li>
</ul>
<h2>Audit deadlines to plan around</h2>
""" + tbl(["Step", "Deadline"], [
        ["Circulate audited accounts to members", "Within 6 months of financial year end"],
        ["Lodge audited accounts with SSM", "Within 30 days of circulation"],
        ["File Form C with LHDN", "Within 7 months of financial year end"]]) + """
<p>Because the Form C relies on finalised accounts, an audit that finishes late pushes your tax filing late too. Using the same team for <a href="../accounting-bookkeeping/">bookkeeping</a>, audit coordination and <a href="../tax-agent/">tax</a> keeps every deadline aligned.</p>
<h2>Special-purpose reviews</h2>
<p>We also help with reviews for bank financing, tenders, investors and due diligence, where a lender or counterparty asks for independent assurance beyond the statutory audit.</p>
""",
    "faqs": [
        ("Which Malaysian companies are exempt from audit?", "Certain dormant companies and small, threshold-qualified private companies may be exempt under the Companies Act 2016. We check your figures and conditions before advising."),
        ("How long does a statutory audit take?", "It depends on the size and the state of your books. Companies with current monthly bookkeeping are audited faster, which is why we plan the audit from the start of the year."),
        ("Can the firm doing my bookkeeping also do my audit?", "Independence rules apply. We coordinate the audit and make sure the right licensed professionals handle each role, so your books and audit stay aligned."),
        ("What happens if we lodge audited accounts late?", "SSM can impose compounds on the company and its officers. We can help you catch up and regularise overdue lodgements."),
    ],
})

PAGES.append({
    "path": "services/tax-agent/", "crumb": "Tax agent & advisory", "eyebrow": "Tax · LHDN · Malaysia",
    "title": "Tax Agent Malaysia: Form C, CP204 & SST for SMEs | CCM",
    "desc": "Corporate tax filing, Form C, CP204 estimates, SST and LHDN queries for Malaysian SMEs. One team for accounts and tax. Fixed fee. Shah Alam.",
    "h1": "Tax agent & advisory for Malaysian SMEs",
    "lead": "Corporate and personal tax filing, CP204 estimates, SST and LHDN queries — handled by the same team that keeps your books, so your numbers and your returns always agree.",
    "box_title": "What’s included", "box": ["Form C corporate tax filing", "CP204 tax estimate & revisions", "Personal income tax (Form BE / B)",
                                        "SST registration & returns", "Tax planning & computation", "LHDN queries & audits support"],
    "faq_h": "Tax questions",
    "body": """
<h2>Corporate tax filing for Sdn Bhd</h2>
<p>Every Malaysian company must file its income tax return (<strong>Form C</strong>) with LHDN within seven months after its financial year end — even a dormant or loss-making company. We prepare the tax computation from your finalised accounts, claim the allowances and deductions you are entitled to, and file through LHDN’s e-Filing system.</p>
<h2>CP204: estimating your tax payable</h2>
<p>A company must submit a tax estimate (<strong>CP204</strong>) before the start of each basis period and pay the tax in monthly instalments. Under-estimating can attract a penalty, so we review your estimate against the year’s results and submit revisions within the permitted windows.</p>
<h2>SST and other indirect tax</h2>
<p>If your turnover reaches the threshold for Sales and Service Tax registration, we handle registration, periodic returns and record-keeping so you stay on the right side of Royal Malaysian Customs.</p>
<h2>Tax planning and LHDN queries</h2>
<ul>
<li>Year-round advice on deductions, capital allowances and the tax impact of big decisions.</li>
<li>Replies to LHDN queries, review letters and audits.</li>
<li>Director and owner personal income tax filing.</li>
</ul>
<h2>Why accounting and tax work best together</h2>
<p>Tax returns are only as good as the accounts they rely on. Because our team also does your <a href="../accounting-bookkeeping/">bookkeeping</a> and coordinates your <a href="../audit/">audit</a>, your Form C is built from audited numbers without re-keying, and your CP204 reflects how the business is actually performing.</p>
<h2>LHDN dates for a typical Sdn Bhd</h2>
""" + tbl(["Obligation", "Usual deadline"], [
        ["Form C (corporate tax return)", "Within 7 months of financial year end"],
        ["CP204 tax estimate", "30 days before the start of the basis period"],
        ["CP204 instalments", "Monthly, by the 15th of each month"]]) + """
<p class="meta">Dates are indicative — we confirm the exact deadlines for your company.</p>
""",
    "faqs": [
        ("When is Form C due for my company?", "Within seven months after your financial year end. For a 31 December year end, that is 31 July of the following year."),
        ("Do dormant companies need to file tax returns?", "Yes. A company must still submit its return to LHDN even when it has no income or is dormant."),
        ("What is CP204 and do I need it?", "CP204 is the tax estimate a company submits before each basis period, paid in monthly instalments. New companies are generally exempt in the first two years, but the rules are specific — we’ll confirm for you."),
        ("Can you deal with LHDN on my behalf?", "Yes, as your tax agent we can respond to LHDN queries, review letters and audits, and represent the company in correspondence."),
    ],
})

PAGES.append({
    "path": "services/sdn-bhd-registration/", "crumb": "Register a Sdn Bhd", "eyebrow": "Company registration · SSM",
    "title": "Register a Sdn Bhd in Malaysia (SSM) | CCM Secretarial",
    "desc": "Step-by-step Sdn Bhd registration with SSM: requirements, documents, timeline and first-year compliance. Also LLP and foreign company. Shah Alam.",
    "h1": "Register a Sdn Bhd in Malaysia with SSM",
    "lead": "We handle name search, SSM incorporation, constitution, company secretary appointment and LHDN registration — so your company is set up right, first time.",
    "box_title": "You’ll need", "box": ["At least 1 director ordinarily resident in Malaysia", "At least 1 shareholder",
                                       "A Malaysian registered office address", "A licensed company secretary (we appoint one)",
                                       "ID copies for directors & shareholders", "2–3 company name choices"],
    "faq_h": "Company registration questions",
    "howto": {"name": "How to register a Sdn Bhd in Malaysia", "steps": [
        ("Choose and reserve a company name", "Submit two or three name options to SSM for a name search and approval."),
        ("Prepare incorporation details", "Confirm directors, shareholders, share capital, registered address and business activity."),
        ("Appoint a company secretary", "Appoint a licensed company secretary within 30 days of incorporation."),
        ("Submit the application to SSM", "File the incorporation application with the constitution and required declarations."),
        ("Receive the Certificate of Incorporation", "SSM issues the certificate and company registration number."),
        ("Register with LHDN and open a bank account", "Set up the tax file and use the incorporation documents for business banking.")]},
    "body": """
<h2>Sdn Bhd registration requirements in Malaysia</h2>
<p>A private limited company (Sdn Bhd) is the most common structure for Malaysian SMEs because it limits the owners’ liability to the capital they have committed. Under the Companies Act 2016 you need:</p>
<ul>
<li>At least <strong>one director</strong> who ordinarily resides in Malaysia;</li>
<li>At least <strong>one shareholder</strong> (the same person can be both director and shareholder);</li>
<li>A <strong>registered office address</strong> in Malaysia;</li>
<li>A <strong>company secretary</strong> appointed within 30 days of incorporation;</li>
<li>An available company name approved by SSM.</li>
</ul>
<h2>How Sdn Bhd registration works, step by step</h2>
<ol>
<li><strong>Name search</strong> — we check and reserve your preferred name with SSM.</li>
<li><strong>Prepare the details</strong> — directors, shareholders, share capital, address and business activity codes.</li>
<li><strong>File with SSM</strong> — we submit the application and constitution on your behalf.</li>
<li><strong>Certificate of Incorporation</strong> — SSM issues your certificate and company number.</li>
<li><strong>Post-incorporation set-up</strong> — statutory registers, first board resolutions, LHDN tax file registration and bank account opening documents.</li>
</ol>
<div class="callout"><strong>Don’t stop at the certificate.</strong> Most first-year penalties come from steps founders didn’t know existed — appointing the company secretary, lodging beneficial ownership information, your first annual return and your first Form C. Our <em>Launch</em> package covers incorporation plus your first year of compliance.</div>
<h2>Sdn Bhd, LLP, sole proprietorship or foreign branch?</h2>
""" + tbl(["Structure", "Best for", "Key point"], [
        ["Sole proprietorship / partnership", "Very small, low-risk businesses", "Owner personally liable; simple registration"],
        ["Sdn Bhd (private limited company)", "Growing SMEs, contracts, tenders, investors", "Limited liability; company secretary, annual return and usually audit"],
        ["LLP (limited liability partnership)", "Professional practices", "Partners’ liability limited; lighter filing than a Sdn Bhd"],
        ["Foreign company branch / subsidiary", "Overseas businesses entering Malaysia", "Choice depends on activities and ownership; resident agent or compliance officer needed"]]) + """
<p>Not sure which suits you? We advise on the first call, at no cost. Overseas founder? We also handle document review and certification and resident agent arrangements.</p>
<h2>After registration: what a new Sdn Bhd must do</h2>
<p>Set up <a href="../accounting-bookkeeping/">bookkeeping</a> from day one, keep your <a href="../company-secretary/">statutory registers</a> current, and diarise your first annual return and audit. Our <a href="../../guides/sdn-bhd-compliance-calendar-malaysia/">compliance calendar</a> shows what falls due and when.</p>
""",
    "faqs": [
        ("How long does it take to register a Sdn Bhd in Malaysia?", "Once the name is approved and documents are complete, SSM incorporation is typically quick. We confirm a realistic timeline on our first call."),
        ("What is the minimum capital for a Sdn Bhd?", "There is no high statutory minimum; the amount is set by the shareholders based on the business’s needs. We advise on a sensible figure for banking and credibility."),
        ("Can a foreigner own 100% of a Sdn Bhd?", "It depends on the business activity and any sector-specific guidelines or licensing conditions. We review your plans and advise on the structure before you file."),
        ("Do I need a company secretary before I register?", "The company secretary must be appointed within 30 days of incorporation. We appoint yours as part of the registration package."),
        ("Can you register an LLP or foreign branch too?", "Yes. We handle Sdn Bhd, LLP and foreign company registrations and the ongoing compliance afterwards."),
    ],
})

PAGES.append({
    "path": "services/switch-company-secretary/", "crumb": "Switch company secretary", "eyebrow": "Change of company secretary",
    "title": "Change Company Secretary in Malaysia | Switch to CCM",
    "desc": "Unhappy with your company secretary or behind on SSM filings? We handle the records handover, regularise late returns and keep you compliant.",
    "h1": "Change company secretary in Malaysia — without the stress",
    "lead": "Overdue returns happen. We collect your records from your previous firm, fix what’s outstanding and keep everything on schedule after.",
    "box_title": "How we make it painless", "box": ["We request the records from your current firm", "Compliance health check of SSM & LHDN status",
                                               "Overdue filings regularised", "Appointment & resignation forms handled",
                                               "Ongoing package that fits you"],
    "faq_h": "Switching questions",
    "body": """
<h2>When should you change your company secretary?</h2>
<p>Businesses switch for practical reasons: filings are going in late, nobody answers messages, fees keep changing, or the firm only deals with one part of your compliance while accounting and tax sit with somebody else. If any of that sounds familiar, changing your company secretary is simpler than most owners expect.</p>
<h2>How the switch works</h2>
<ol>
<li><strong>Free review</strong> — we check your company’s status with SSM and LHDN and list anything overdue.</li>
<li><strong>Appointment</strong> — the board appoints us as company secretary; we prepare the resolutions and SSM forms.</li>
<li><strong>Records handover</strong> — we request your statutory registers, minute books and filings from the previous secretary so you don’t have to chase.</li>
<li><strong>Catch-up</strong> — we regularise late annual returns and financial statement lodgements.</li>
<li><strong>Ongoing compliance</strong> — one named contact tracks every deadline from here.</li>
</ol>
<div class="callout"><strong>Already received a compound notice?</strong> Talk to us before the next one arrives. We’ll explain where you stand and what it takes to get back on track.</div>
<h2>Check where you stand first</h2>
<p>Take our <a href="../../#health">60-second compliance health check</a> to see which filings may be at risk, or read our guide on the <a href="../../guides/sdn-bhd-compliance-calendar-malaysia/">Sdn Bhd compliance calendar</a>.</p>
<h2>Bring accounting, audit and tax under the same roof</h2>
<p>Many clients who switch also move their <a href="../accounting-bookkeeping/">accounting</a>, <a href="../audit/">audit</a> and <a href="../tax-agent/">tax</a> to us, because one team watching every SSM and LHDN deadline means nothing falls between two firms.</p>
""",
    "faqs": [
        ("Will my current company secretary cooperate with the handover?", "Usually yes. We send the requests and follow up for you, and we know what records SSM requires to be handed over."),
        ("Is there any downtime in compliance when I switch?", "No. We diarise your upcoming deadlines during the review so nothing falls through the gap."),
        ("Can you fix overdue annual returns and accounts?", "Yes. We regularise late lodgements and help you understand any compounds that may apply."),
        ("Do I have to move my accounting too?", "No. You can switch only the company secretary and add accounting, audit or tax later."),
    ],
})

# ============================================================ GUIDES
GUIDES = []

GUIDES.append({
    "path": "guides/company-secretary-requirements-malaysia/", "short": "Company secretary requirements",
    "tag": "Company secretarial", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Company Secretary Requirements in Malaysia (2026 Guide)",
    "desc": "Who needs a company secretary in Malaysia, who can be one, when to appoint and what happens if you don’t. Plain-English guide for Sdn Bhd owners.",
    "h1": "Company secretary requirements in Malaysia: a guide for Sdn Bhd owners",
    "lead": "Every Malaysian company needs a company secretary. Here is who qualifies, when you must appoint one and what they do.",
    "excerpt": "Who needs a company secretary, who can act as one, when to appoint and what the role involves.",
    "faqs": [("Can a director be the company secretary?", "Yes, a director can also be the company secretary if they meet the qualification requirements in the Companies Act 2016. Many owners choose an outsourced secretary instead."),
             ("Can a foreigner be a company secretary in Malaysia?", "The secretary must be a natural person ordinarily resident in Malaysia and qualified under the Act, so a non-resident cannot act.")],
    "body": """
<h2>Is a company secretary compulsory in Malaysia?</h2>
<p>Yes. Under the Companies Act 2016, every company incorporated in Malaysia — a Sdn Bhd, a public company or a company limited by guarantee — must have at least one company secretary. The company must appoint the first secretary within <strong>30 days of incorporation</strong>. If the secretary leaves, the company must fill the vacancy within the period set by the Act.</p>
<h2>Who can be a company secretary?</h2>
<p>The secretary must be a natural person who ordinarily resides in Malaysia and is one of the following:</p>
<ul>
<li>A member of a prescribed professional body, such as the Malaysian Institute of Accountants or the Malaysian Bar;</li>
<li>A person licensed by SSM as a company secretary; or</li>
<li>Another person approved by SSM.</li>
</ul>
<p>Practically, most SMEs appoint a licensed company secretary from an outsourced firm, because the filing work is specialised and ongoing.</p>
<h2>What does a company secretary actually do?</h2>
<ul>
<li>Lodges your <strong>annual return</strong> and financial statements with SSM on time;</li>
<li>Prepares and keeps minutes of board and general meetings;</li>
<li>Maintains <strong>statutory registers</strong> (directors, members, charges);</li>
<li>Files notices of changes — directors, share transfers, registered address;</li>
<li>Advises directors on their statutory duties and company law compliance.</li>
</ul>
<h2>What if you don’t appoint one?</h2>
<p>Failing to have a company secretary is an offence under the Act and can result in compounds or penalties for the company and its officers, and it makes every other filing harder. If your company already missed the 30-day window, appoint a licensed secretary now and have them review outstanding filings.</p>
<p>Ready to appoint? See our <a href="../../services/company-secretary/">company secretary services</a> or <a href="../../services/switch-company-secretary/">how to change your company secretary</a>.</p>
""",
})

GUIDES.append({
    "path": "guides/sdn-bhd-compliance-calendar-malaysia/", "short": "Sdn Bhd compliance calendar",
    "tag": "SSM & LHDN deadlines", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Sdn Bhd Compliance Calendar Malaysia: SSM & LHDN Deadlines",
    "desc": "Annual return, audited accounts, Form C and CP204 — the SSM and LHDN deadlines every Malaysian Sdn Bhd must meet, with a worked example.",
    "h1": "Sdn Bhd compliance calendar: SSM and LHDN deadlines in Malaysia",
    "lead": "The filings every Malaysian private company has to make each year, who they go to and when they fall due.",
    "excerpt": "Annual return, audited accounts, Form C and CP204 — the yearly deadlines, with a worked example.",
    "faqs": [("What happens if I miss an SSM or LHDN deadline?", "SSM and LHDN can impose compounds and penalties on the company and its officers. The longer a filing is overdue, the more it tends to cost to regularise."),
             ("Do dormant companies still have deadlines?", "Yes. A dormant company must still lodge its annual return and submit its tax return, and may also need financial statements.")],
    "body": """
<p>Missing a compliance deadline is the most common — and most avoidable — cost for Malaysian SMEs. Use this calendar, or our interactive <a href="../../#planner">deadline planner</a>, to see what applies to your company.</p>
<h2>The yearly filings at a glance</h2>
""" + tbl(["Filing", "Who it goes to", "Deadline"], [
        ["Annual return", "SSM", "Within 30 days of the incorporation anniversary (s.68 Companies Act 2016)"],
        ["Circulate audited financial statements to members", "Shareholders", "Within 6 months of financial year end (s.258)"],
        ["Lodge financial statements", "SSM", "Within 30 days of circulation (s.259)"],
        ["Form C (corporate income tax return)", "LHDN", "Within 7 months of financial year end"],
        ["CP204 tax estimate", "LHDN", "30 days before the start of each basis period"],
        ["CP204 instalments", "LHDN", "Monthly"],
        ["EPF, SOCSO & EIS contributions", "KWSP / PERKESO", "Monthly (by the statutory due date)"],
        ["SST return (if registered)", "Royal Malaysian Customs", "Per taxable period"]]) + """
<h2>Worked example: incorporated 15 March, year end 31 December</h2>
""" + tbl(["Date", "What is due"], [
        ["15 March + 30 days (14 April)", "Annual return to SSM"],
        ["30 June", "Circulate audited accounts (6 months after 31 December)"],
        ["30 July", "Lodge accounts with SSM (30 days after circulation)"],
        ["31 July", "Form C to LHDN (7 months after 31 December)"],
        ["2 December", "CP204 estimate for the next basis period (30 days before 1 January)"]]) + """
<div class="callout"><strong>Tip:</strong> the audit is the bottleneck. If your books are finished late, every date after it gets squeezed. Monthly <a href="../../services/accounting-bookkeeping/">bookkeeping</a> is the easiest way to keep the whole calendar on track.</div>
<h2>How to stay on top of it</h2>
<ul>
<li>Fix your financial year end and plan the audit timetable backwards from the deadlines above.</li>
<li>Use a company secretary who tracks SSM dates for you — see our <a href="../../services/company-secretary/">company secretary services</a>.</li>
<li>Have your <a href="../../services/tax-agent/">tax agent</a> review your CP204 estimate against the year’s actual results.</li>
</ul>
<p class="meta">Indicative dates based on the Companies Act 2016 and LHDN rules. Exact dates depend on your company’s circumstances and any extensions announced by the authorities.</p>
""",
})

GUIDES.append({
    "path": "guides/do-sdn-bhd-need-audit-malaysia/", "short": "Does my Sdn Bhd need an audit?",
    "tag": "Audit", "published": "2026-09-30", "updated_human": "30 September 2026",
    "title": "Does My Sdn Bhd Need an Audit? Malaysia Exemptions",
    "desc": "Most Malaysian private companies must be audited. See who can claim exemption (dormant and threshold-qualified companies) and what to do next.",
    "h1": "Does my Sdn Bhd need an audit? Exemptions in Malaysia explained",
    "lead": "Most private companies must have their accounts audited every year — but some are exempt. Here’s how to tell which camp you’re in.",
    "excerpt": "Most private companies need an annual audit. Learn who is exempt and what to check first.",
    "faqs": [("Is an audit required if my company has no revenue?", "Zero-revenue or dormant companies may qualify for exemption under the Companies Act 2016, subject to the conditions. Check before you decide not to audit."),
             ("Who signs off the audited accounts?", "A licensed company auditor signs the auditor’s report, and the directors approve and sign the financial statements.")],
    "body": """
<h2>The default rule: audit every year</h2>
<p>Under the Companies Act 2016, a company’s financial statements must be audited by a licensed company auditor before they are circulated to members and lodged with SSM. That applies to most Sdn Bhds, whatever their size.</p>
<h2>Who can be exempt from audit?</h2>
<p>The Act allows exemption for certain companies. The two groups most relevant to SMEs are:</p>
<ul>
<li><strong>Dormant companies</strong> — companies that are not carrying on business and have no significant accounting transactions.</li>
<li><strong>Threshold-qualified private companies</strong> — small private companies that meet the statutory thresholds for revenue and other criteria set out in the Act and its regulations.</li>
</ul>
<p>Exemption is not automatic, and the conditions can be lost when circumstances change. A company that qualified one year may not qualify the next.</p>
<h2>Even if you’re exempt, you still have duties</h2>
<ul>
<li>You still need proper <strong>accounting records</strong> and financial statements approved by the directors.</li>
<li>You still must lodge your <strong>annual return</strong> and, where required, financial statements with SSM.</li>
<li>You still must file <strong>Form C</strong> with LHDN within seven months of year end.</li>
<li>Banks, investors and tenders may still ask for audited accounts.</li>
</ul>
<h2>How to decide</h2>
<ol>
<li>Confirm whether the company is dormant or trading.</li>
<li>Check revenue and other threshold conditions for the financial year.</li>
<li>Consider whether lenders, investors or clients will want audited figures anyway.</li>
<li>Document the decision in your directors’ records.</li>
</ol>
<p>We check eligibility for free before recommending an audit. Learn more about our <a href="../../services/audit/">audit and assurance services</a>, or review your full <a href="../sdn-bhd-compliance-calendar-malaysia/">compliance calendar</a>.</p>
""",
})

# ============================================================ TRUST SIGNALS
# Fill these in with REAL, verifiable details. Anything left empty is simply not shown on the site.
TRUST = {
    # Shown as badges, e.g. ("SSM licensed company secretary", "Licence no. CS 0000000")
    "credentials": [],
    # Professional bodies, e.g. "Malaysian Institute of Accountants (MIA)", "MAICSA", "CTIM"
    "memberships": [],
    # Headline numbers, e.g. ("250+", "companies served"), ("10 yrs", "in practice")
    "stats": [],
    # Client logos: list of (client name, "assets/clients/file.svg"). Only use with client permission.
    "clients": [],
}

# Every page that should appear in sitemap.xml and in build order
ALL_PAGES = PAGES
