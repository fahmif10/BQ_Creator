# CCM Secretarial — website

A static, one-page redesign of ccmsecretarial.com (Corporate Consultant & Management):
company secretarial, accounting, audit and tax.

Open `index.html` in a browser — no build step.

## Before launch
- Add office address and email in `#contact` (see the TODO comment)
- Wire the contact form (`[data-form]` in `main.js`) to email or a CRM — it is front-end only
- Check the package contents and FAQ answers match what CCM actually offers

## Motion
Built with the `emil-design-eng` and `animate` skills: custom easing tokens in `:root`,
`transform`/`opacity` only, button press feedback, a clip-path segmented control,
measured-height FAQ accordion, Sonner-style toasts, once-only scroll reveals,
no animation on keyboard-driven actions, and a `prefers-reduced-motion` variant.
Run `/review-animations` to audit it.
