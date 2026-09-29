# Laras Corporate Services — website

A static, one-page site for a Malaysian corporate services firm (company secretarial,
accounting, audit and tax), modelled on the structure of ccmsecretarial.com.

Open `index.html` in a browser — no build step.

## Before launch, replace the placeholders
- Brand name and logo mark ("Laras", the `L` badge)
- Office address, phone, email (`#contact`) and the WhatsApp number in `.chat-fab`
- The three **Sample** testimonials in `#clients` with real, attributable client quotes
- Wire the contact form (`[data-form]` in `main.js`) to email or a CRM — it is front-end only

## Motion
Built with the `emil-design-eng` and `animate` skills: custom easing tokens in `:root`,
`transform`/`opacity` only, button press feedback, a clip-path segmented control,
measured-height FAQ accordion, Sonner-style toasts, once-only scroll reveals,
no animation on keyboard-driven actions, and a `prefers-reduced-motion` variant.
Run `/review-animations` to audit it.
