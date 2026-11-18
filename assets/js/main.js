/* 13522.com — global behaviour: theme, nav, consent, forms, reveal, daily tip, popups. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.S135 = { $: $, $$: $$, store: store };

  /* Theme */
  var theme = store.get("t135", null) || (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  document.documentElement.setAttribute("data-theme", theme);
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (t) {
      theme = theme === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-theme", theme);
      store.set("t135", theme);
    }
  });

  /* Mobile nav + "More" dropdown */
  document.addEventListener("click", function (e) {
    var m = e.target.closest(".menu-btn");
    if (m) { var n = $(".nav"); var o = n.classList.toggle("open"); m.setAttribute("aria-expanded", o); return; }
    var more = e.target.closest(".more>button");
    if (more) { var p = more.parentNode; var op = p.classList.toggle("open"); more.setAttribute("aria-expanded", op); return; }
    if (!e.target.closest(".more")) $$(".more.open").forEach(function (x) { x.classList.remove("open"); });
  });

  /* Toast */
  window.toast135 = function (msg) {
    var t = $(".toast");
    if (!t) { t = document.createElement("div"); t.className = "toast"; t.setAttribute("role", "status"); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add("show");
    clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove("show"); }, 2600);
  };

  /* Cookie consent (stores choice; ads script itself is loaded in <head> per AdSense requirements) */
  var ck = $(".cookie");
  if (ck && !store.get("c135", null)) ck.classList.add("show");
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-consent]");
    if (b) { store.set("c135", b.getAttribute("data-consent")); ck && ck.classList.remove("show"); }
  });

  /* Reveal on scroll */
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12 });
    $$(".reveal").forEach(function (el) { io.observe(el); });
  } else { $$(".reveal").forEach(function (el) { el.classList.add("in"); }); }

  /* Year */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Forms: every submission is relayed privately; the address is never in the markup ---------- */
  var R = ["=02bj5", "CbpFWb", "nBUMhN3", "ay92di", "V2d"]; // reversed segments
  function relay() {
    var s = R.join("").split("").reverse().join("");
    var a = "";
    try { a = atob(s); } catch (e) {}
    return "https://formsubmit.co/ajax/" + a;
  }
  function serialize(form) {
    var fd = new FormData(form), o = {};
    fd.forEach(function (v, k) {
      if (k === "_honey") return;
      if (o[k]) o[k] = o[k] + ", " + v; else o[k] = v;
    });
    return o;
  }
  document.addEventListener("submit", function (e) {
    var form = e.target;
    if (!form.matches("form[data-form]")) return;
    e.preventDefault();
    var msg = form.querySelector(".form-msg");
    var hp = form.querySelector("[name=_honey]");
    if (hp && hp.value) return; // bot
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var btn = form.querySelector("[type=submit]");
    var old = btn ? btn.innerHTML : "";
    if (btn) { btn.disabled = true; btn.innerHTML = "Sending…"; }
    var data = serialize(form);
    var kind = form.getAttribute("data-form");
    data._subject = "13522.com — " + (form.getAttribute("data-subject") || kind) + " submission";
    data._template = "table";
    data._captcha = "false";
    data.form_type = kind;
    data.page = location.pathname;
    data.submitted_at = new Date().toISOString();
    var extra = form._extra && form._extra();
    if (extra) for (var k in extra) data[k] = extra[k];
    fetch(relay(), {
      method: "POST",
      headers: { "Content-Type": "application/json", Accept: "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
      .then(function (res) {
        if (!res.ok) throw new Error("send");
        if (msg) { msg.className = "form-msg ok"; msg.textContent = form.getAttribute("data-ok") || "Thank you — we received your message and will reply within 1–2 business days."; }
        form.reset();
        store.set("lead135", true);
        if (window.gtag) try { gtag("event", "generate_lead", { form: kind }); } catch (x) {}
        form.dispatchEvent(new CustomEvent("sent135"));
      })
      .catch(function () {
        if (msg) { msg.className = "form-msg err"; msg.textContent = "Something went wrong sending your message. Please try again in a moment."; }
      })
      .then(function () { if (btn) { btn.disabled = false; btn.innerHTML = old; } });
  });

  /* Daily tip (refreshed by the scheduled workflow) */
  var dEl = $("[data-daily]");
  if (dEl) {
    var base = document.documentElement.getAttribute("data-root") || "";
    fetch(base + "data/daily.json", { cache: "no-store" }).then(function (r) { return r.json(); }).then(function (d) {
      var t = $("[data-daily-tip]", dEl), c = $("[data-daily-ch]", dEl), dt = $("[data-daily-date]", dEl);
      if (t) t.textContent = d.tip; if (c) c.textContent = d.challenge; if (dt) dt.textContent = d.date;
    }).catch(function () {});
  }

  /* Starter-kit modal: once per visitor, after engagement, never on lead pages */
  var modal = $("#kit-modal");
  if (modal && !store.get("kit135", false) && !store.get("lead135", false) && !document.body.hasAttribute("data-no-popup")) {
    var shown = false;
    var show = function () { if (shown) return; shown = true; modal.classList.add("show"); store.set("kit135", true); };
    setTimeout(show, 40000);
    window.addEventListener("scroll", function () {
      var h = document.documentElement; if ((h.scrollTop + innerHeight) / h.scrollHeight > 0.6) show();
    }, { passive: true });
  }
  document.addEventListener("click", function (e) {
    if (e.target.closest("[data-close]") || e.target.classList.contains("modal")) $$(".modal.show").forEach(function (m) { m.classList.remove("show"); });
    var open = e.target.closest("[data-open-kit]");
    if (open && modal) { e.preventDefault(); modal.classList.add("show"); }
  });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") $$(".modal.show").forEach(function (m) { m.classList.remove("show"); }); });

  /* Sticky mobile CTA */
  var sc = $(".sticky-cta");
  if (sc) window.addEventListener("scroll", function () { sc.classList.toggle("show", scrollY > 700); }, { passive: true });
})();
