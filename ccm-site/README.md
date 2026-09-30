# CCM Secretarial — SEO-optimised static site

The original single-file React bundle rendered everything in the browser, so search engines saw an empty page.
This is the same site rebuilt as pre-rendered static HTML, targeted at Malaysian SME search intent.

```
python3 build.py      # needs Pillow (pip install pillow); writes ./dist
```

Deploy the contents of `dist/` to the root of any static host. **Before launch, set `SITE` in `build.py`** to the real
domain (it drives canonical URLs, Open Graph, JSON-LD and `sitemap.xml`), then rebuild. All copy lives in `content.py`.

Pages: home, 6 service pages (company secretary, accounting, audit, tax agent, Sdn Bhd registration, switch company
secretary), 3 guides + index, 404. Interactivity (deadline planner, persona tabs, health-check quiz, enquiry form) is
progressive enhancement in `assets/app.js`; all content is in the HTML without JavaScript.

After deploying: submit `sitemap.xml` in Google Search Console, claim/verify the Google Business Profile for the
Elmina, Shah Alam address, and keep name/address/phone identical everywhere (NAP consistency).
