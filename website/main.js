const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

/* Header border once the page scrolls */
const header = document.querySelector("[data-header]");
const onScroll = () => header.toggleAttribute("data-scrolled", window.scrollY > 8);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

/* Footer year */
document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

/* ---------------------------------------------------------------------------
   Mobile menu (drawer)
   --------------------------------------------------------------------------- */
const menu = document.querySelector("[data-mobile-menu]");
const menuToggle = document.querySelector("[data-menu-toggle]");
let menuCloseTimer;

function openMenu() {
  clearTimeout(menuCloseTimer);
  menu.hidden = false;
  menu.offsetHeight; // commit the closed state so the transition runs
  menu.setAttribute("data-open", "");
  menuToggle.setAttribute("aria-expanded", "true");
  menuToggle.querySelector(".sr-only").textContent = "Close menu";
  document.body.style.overflow = "hidden";
  menu.querySelector("a").focus({ preventScroll: true });
}

function closeMenu({ restoreFocus = true } = {}) {
  if (!menu.hasAttribute("data-open")) return;
  menu.removeAttribute("data-open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.querySelector(".sr-only").textContent = "Open menu";
  document.body.style.overflow = "";
  // Exit is 200ms in CSS; hide after it finishes
  menuCloseTimer = setTimeout(() => (menu.hidden = true), 200);
  if (restoreFocus) menuToggle.focus({ preventScroll: true });
}

menuToggle.addEventListener("click", () => (menu.hasAttribute("data-open") ? closeMenu() : openMenu()));
menu.querySelectorAll("[data-menu-close]").forEach((el) =>
  el.addEventListener("click", () => closeMenu({ restoreFocus: false }))
);
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") closeMenu();
});
window.matchMedia("(min-width: 861px)").addEventListener("change", (e) => {
  if (e.matches) closeMenu({ restoreFocus: false });
});

/* ---------------------------------------------------------------------------
   Scroll reveal — fires once per element, staggered within its group
   --------------------------------------------------------------------------- */
const reveals = document.querySelectorAll(".reveal");
const groups = new Map();
reveals.forEach((el) => {
  const siblings = groups.get(el.parentElement) || [];
  el.style.setProperty("--i", siblings.length);
  siblings.push(el);
  groups.set(el.parentElement, siblings);
});

if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.setAttribute("data-visible", "");
        io.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -80px 0px" }
  );
  reveals.forEach((el) => io.observe(el));
} else {
  reveals.forEach((el) => el.setAttribute("data-visible", ""));
}

/* ---------------------------------------------------------------------------
   Segmented control — the active copy is clipped to the selected tab
   --------------------------------------------------------------------------- */
const segmented = document.querySelector("[data-segmented]");
if (segmented) {
  const tabs = [...segmented.querySelectorAll("[role=tab]")];
  const active = segmented.querySelector("[data-segmented-active]");
  const panels = document.querySelectorAll("[data-panel]");

  const positionClip = (tab) => {
    const box = segmented.getBoundingClientRect();
    const r = tab.getBoundingClientRect();
    const left = r.left - box.left;
    const right = box.right - r.right;
    const top = r.top - box.top;
    const bottom = box.bottom - r.bottom;
    active.style.clipPath = `inset(${top}px ${right}px ${bottom}px ${left}px round 999px)`;
  };

  const select = (tab, { instant = false, focus = false } = {}) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute("aria-selected", on);
      t.tabIndex = on ? 0 : -1;
    });
    panels.forEach((p) => (p.hidden = p.dataset.panel !== tab.dataset.tab));
    // Keyboard-driven switches are instant: no animation on keyboard actions
    if (instant) active.style.transition = "none";
    positionClip(tab);
    if (instant) {
      active.offsetHeight;
      active.style.transition = "";
    }
    if (focus) tab.focus();
  };

  tabs.forEach((tab, i) => {
    tab.addEventListener("click", (e) => select(tab, { instant: e.detail === 0 }));
    tab.addEventListener("keydown", (e) => {
      const dir = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (!dir) return;
      e.preventDefault();
      select(tabs[(i + dir + tabs.length) % tabs.length], { instant: true, focus: true });
    });
  });

  const current = () => tabs.find((t) => t.getAttribute("aria-selected") === "true");
  const resync = () => select(current(), { instant: true });
  resync();
  window.addEventListener("resize", resync);
  document.fonts?.ready.then(resync);
}

/* ---------------------------------------------------------------------------
   FAQ accordion — animate between measured heights, not to `auto`
   --------------------------------------------------------------------------- */
document.querySelectorAll("[data-faq] .faq-item").forEach((item) => {
  const button = item.querySelector("button");
  const panel = item.querySelector(".faq-panel");
  let timer;

  const finish = (open) => {
    panel.style.height = "";
    panel.style.opacity = "";
    if (!open) panel.hidden = true;
  };

  button.addEventListener("click", (e) => {
    const open = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", open);
    clearTimeout(timer);

    // Keyboard toggles (Enter/Space report detail 0) are instant
    if (e.detail === 0) {
      panel.hidden = !open;
      finish(open);
      return;
    }

    const from = panel.hidden ? 0 : panel.getBoundingClientRect().height;
    panel.hidden = false;
    panel.style.height = "auto";
    const to = open ? panel.getBoundingClientRect().height : 0;

    panel.style.height = `${from}px`;
    panel.style.opacity = open ? "0" : "1";
    panel.offsetHeight;
    panel.style.height = `${to}px`;
    panel.style.opacity = open ? "1" : "0";

    timer = setTimeout(() => finish(open), 200);
  });
});

/* ---------------------------------------------------------------------------
   Package buttons pre-fill the contact form's subject
   --------------------------------------------------------------------------- */
const subject = document.querySelector("[data-need]");
document.querySelectorAll("[data-plan]").forEach((btn) =>
  btn.addEventListener("click", () => {
    if (subject) subject.value = btn.dataset.plan;
  })
);

/* ---------------------------------------------------------------------------
   Toasts
   --------------------------------------------------------------------------- */
const toaster = document.querySelector("[data-toaster]");

function toast(title, body) {
  const el = document.createElement("div");
  el.className = "toast";
  el.setAttribute("role", "status");
  el.innerHTML = `<span class="toast-dot" aria-hidden="true"></span><div><strong></strong><span></span></div>`;
  el.querySelector("strong").textContent = title;
  el.querySelector("span:last-child").textContent = body;
  toaster.replaceChildren(el);

  let remaining = 4000;
  let started = Date.now();
  let timer = setTimeout(dismiss, remaining);

  // Pause while the tab is hidden, so the message isn't missed
  const onVisibility = () => {
    if (document.hidden) {
      clearTimeout(timer);
      remaining -= Date.now() - started;
    } else {
      started = Date.now();
      timer = setTimeout(dismiss, remaining);
    }
  };
  document.addEventListener("visibilitychange", onVisibility);

  function dismiss() {
    document.removeEventListener("visibilitychange", onVisibility);
    el.setAttribute("data-leaving", "");
    setTimeout(() => el.remove(), reduceMotion.matches ? 200 : 400);
  }
}

/* ---------------------------------------------------------------------------
   Contact form (front-end only)
   --------------------------------------------------------------------------- */
const form = document.querySelector("[data-form]");
form?.addEventListener("submit", (e) => {
  e.preventDefault();
  let firstInvalid = null;
  form.querySelectorAll("[required]").forEach((field) => {
    const valid = field.checkValidity();
    field.setAttribute("aria-invalid", String(!valid));
    if (!valid && !firstInvalid) firstInvalid = field;
  });
  if (firstInvalid) {
    firstInvalid.focus();
    toast("A few details missing", "Please fill in your name, a valid email and your message.");
    return;
  }
  const name = form.elements.name.value.trim().split(" ")[0];
  form.reset();
  form.querySelectorAll("[aria-invalid]").forEach((f) => f.removeAttribute("aria-invalid"));
  toast(`Thanks, ${name}`, "We’ll get back to you within one working day.");
});

form?.addEventListener("input", (e) => {
  if (e.target.getAttribute("aria-invalid") === "true" && e.target.checkValidity()) {
    e.target.removeAttribute("aria-invalid");
  }
});
