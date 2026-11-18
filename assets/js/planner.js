/* 13522 Planner — 1 big · 3 medium · 5 small · 2 focus sprints · 2 reviews. Runs entirely in the browser. */
(function () {
  "use strict";
  var root = document.getElementById("planner");
  if (!root) return;
  var S = window.S135, $ = S.$, $$ = S.$$, store = S.store;
  var TIERS = [
    { key: "big", n: 1, label: "1 Big task", hint: "The one thing that makes today a win", color: "var(--big)", w: 40, ph: ["e.g. Ship the landing page"] },
    { key: "med", n: 3, label: "3 Medium tasks", hint: "Meaningful, 30–90 minutes each", color: "var(--med)", w: 10, ph: ["e.g. Draft client proposal", "e.g. Review analytics", "e.g. Record a tutorial"] },
    { key: "small", n: 5, label: "5 Small tasks", hint: "Quick wins, under 15 minutes", color: "var(--small)", w: 4, ph: ["e.g. Reply to Sam", "e.g. Pay invoice", "e.g. Book dentist", "e.g. Update bio", "e.g. Clear inbox to 10"] }
  ];
  function today() { return dkey(new Date()); }
  function dkey(d) { return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0"); }
  function blank() {
    var o = { date: today(), sprints: [false, false], am: "", pm: "" };
    TIERS.forEach(function (t) { o[t.key] = []; for (var i = 0; i < t.n; i++) o[t.key].push({ t: "", d: false, m: "" }); });
    return o;
  }
  var hist = store.get("h135", {});
  var st = store.get("p135", null);
  if (!st || st.date !== today()) {
    if (st && st.date) { hist[st.date] = score(st); store.set("h135", hist); }
    var carry = st && st.date ? st : null;
    st = blank();
    if (carry && store.get("autocarry135", true)) carryOver(carry, st);
  }
  function carryOver(from, to) {
    TIERS.forEach(function (t) {
      var left = from[t.key].filter(function (x) { return x.t && !x.d; });
      left.forEach(function (x) {
        var slot = to[t.key].find(function (y) { return !y.t; });
        if (slot) { slot.t = x.t; slot.m = x.m; }
      });
    });
  }
  function save() { store.set("p135", st); hist[st.date] = score(st); store.set("h135", hist); render(true); }
  function score(s) {
    var v = 0;
    TIERS.forEach(function (t) { s[t.key].forEach(function (x) { if (x.d && x.t) v += t.w; }); });
    s.sprints.forEach(function (x) { if (x) v += 5; });
    return Math.min(100, v);
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  var slots = $("#slots", root);
  function build() {
    var h = "";
    TIERS.forEach(function (t) {
      h += '<div class="tier"><div class="tier-h"><span class="pill" style="background:' + t.color + '">' + t.n + "</span><h3>" + t.label + '</h3><small style="color:var(--muted)">' + t.hint + "</small></div>";
      st[t.key].forEach(function (x, i) {
        h += '<div class="slot' + (x.d ? " done" : "") + '" style="--c:' + t.color + '">' +
          '<input type="checkbox" aria-label="Done" data-k="' + t.key + '" data-i="' + i + '" data-f="d"' + (x.d ? " checked" : "") + ">" +
          '<input type="text" maxlength="140" aria-label="' + t.label + " " + (i + 1) + '" placeholder="' + esc(t.ph[i] || "") + '" value="' + esc(x.t) + '" data-k="' + t.key + '" data-i="' + i + '" data-f="t">' +
          '<input class="mins" type="number" min="0" max="600" placeholder="min" aria-label="Minutes" value="' + esc(x.m) + '" data-k="' + t.key + '" data-i="' + i + '" data-f="m">' +
          "</div>";
      });
      h += "</div>";
    });
    slots.innerHTML = h;
    var am = $("#rev-am", root), pm = $("#rev-pm", root);
    if (am) am.value = st.am; if (pm) pm.value = st.pm;
    render(false);
  }
  slots.addEventListener("input", function (e) {
    var el = e.target, k = el.getAttribute("data-k"); if (!k) return;
    var i = +el.getAttribute("data-i"), f = el.getAttribute("data-f");
    if (f === "d") { st[k][i].d = el.checked; el.parentNode.classList.toggle("done", el.checked); if (el.checked && st[k][i].t) window.toast135 && toast135(k === "big" ? "Big task done — today is already a win." : "Nice. Keep the momentum."); }
    else st[k][i][f] = el.value;
    save();
  });
  ["am", "pm"].forEach(function (k) {
    var el = $("#rev-" + k, root);
    if (el) el.addEventListener("input", function () { st[k] = el.value; save(); });
  });

  function render() {
    var sc = score(st);
    var ring = $("#ring", root);
    if (ring) {
      var c = 2 * Math.PI * 62, off = c * (1 - sc / 100);
      ring.innerHTML = '<svg viewBox="0 0 150 150" class="ring" role="img" aria-label="Day score ' + sc + '%"><circle cx="75" cy="75" r="62" fill="none" stroke="var(--line)" stroke-width="14"/><circle cx="75" cy="75" r="62" fill="none" stroke="var(--accent)" stroke-width="14" stroke-linecap="round" stroke-dasharray="' + c + '" stroke-dashoffset="' + off + '" transform="rotate(-90 75 75)" style="transition:stroke-dashoffset .5s"/><text x="75" y="83" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="30" font-weight="700" fill="var(--ink)">' + sc + "%</text></svg>";
    }
    var plan = 0;
    TIERS.forEach(function (t) { st[t.key].forEach(function (x) { plan += +x.m || 0; }); });
    var pe = $("#planned", root); if (pe) pe.textContent = plan ? Math.floor(plan / 60) + "h " + (plan % 60) + "m planned" + (plan > 420 ? " — that's over 7h, consider trimming" : "") : "Add minutes to see your load";
    var d = $("#plan-date", root); if (d) d.textContent = new Date().toLocaleDateString(undefined, { weekday: "long", month: "long", day: "numeric" });
    // streak
    var s = 0, dt = new Date();
    if ((hist[today()] || 0) < 60) dt.setDate(dt.getDate() - 1);
    for (var i = 0; i < 365; i++) { var k = dkey(dt); if ((hist[k] || 0) >= 60) { s++; dt.setDate(dt.getDate() - 1); } else break; }
    var se = $("#streak", root); if (se) se.textContent = s + (s === 1 ? " day" : " days");
    var sp = $$("[data-sprint]", root); sp.forEach(function (b, i) { b.textContent = (st.sprints[i] ? "✓ " : "") + "Sprint " + (i + 1); b.classList.toggle("on", !!st.sprints[i]); });
    // history bars
    var he = $("#hist", root);
    if (he) {
      var out = "", dd = new Date(); dd.setDate(dd.getDate() - 13);
      for (var j = 0; j < 14; j++) {
        var key = dkey(dd), v = hist[key] || 0;
        out += '<div title="' + key + ": " + v + '%" style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;height:70px"><i style="display:block;height:' + Math.max(3, v * 0.7) + 'px;border-radius:4px;background:' + (v >= 60 ? "var(--small)" : "var(--line)") + '"></i></div>';
        dd.setDate(dd.getDate() + 1);
      }
      he.innerHTML = '<div style="display:flex;gap:4px;align-items:flex-end">' + out + "</div>";
    }
  }

  /* Smart Sort: classifies a brain dump into big / medium / small using effort cues */
  var BIG = /(launch|ship|finish|write|build|design|plan|strategy|proposal|report|presentation|deck|chapter|redesign|migrate|record|film|deep|research|study|exam|pitch|budget|hire|interview)/i;
  var SMALL = /(email|reply|call|text|pay|book|schedule|buy|order|send|check|confirm|print|sign|file|update|clean|tidy|remind|renew|cancel|post|share|backup)/i;
  function est(line) {
    var m = line.match(/(\d+(?:\.\d+)?)\s*(h|hr|hrs|hour|hours|m|min|mins|minutes)\b/i);
    if (m) { var v = parseFloat(m[1]); return /^h/i.test(m[2]) ? Math.round(v * 60) : Math.round(v); }
    var w = line.split(/\s+/).length;
    if (BIG.test(line)) return 120; if (SMALL.test(line)) return 10;
    return w > 7 ? 60 : 30;
  }
  var sortBtn = $("#sort-btn", root);
  if (sortBtn) sortBtn.addEventListener("click", function () {
    var raw = ($("#brain", root).value || "").split(/\n|;/).map(function (x) { return x.replace(/^[-*•\d.)\s]+/, "").trim(); }).filter(Boolean);
    if (!raw.length) { toast135("Type or paste a few tasks first — one per line."); return; }
    var items = raw.map(function (t) { return { t: t.replace(/\(?\s*\d+(\.\d+)?\s*(h|hr|hrs|hour|hours|m|min|mins|minutes)\s*\)?/i, "").trim(), m: est(t) }; });
    items.sort(function (a, b) { return b.m - a.m; });
    var nb = blank(); nb.am = st.am; nb.pm = st.pm; nb.sprints = st.sprints;
    var bigs = items.filter(function (x) { return x.m >= 90; }), meds = items.filter(function (x) { return x.m >= 25 && x.m < 90; }), sm = items.filter(function (x) { return x.m < 25; });
    // promote / demote to fill the 1-3-5 shape
    if (!bigs.length && meds.length) bigs.push(meds.shift());
    while (bigs.length > 1) meds.unshift(bigs.pop());
    while (meds.length < 3 && sm.length > 5) meds.push(sm.shift());
    var parked = [];
    [["big", bigs], ["med", meds], ["small", sm]].forEach(function (p) {
      p[1].forEach(function (x, i) { if (i < nb[p[0]].length) nb[p[0]][i] = { t: x.t, d: false, m: String(x.m) }; else parked.push(x.t); });
    });
    st = nb; save(); build();
    var pk = $("#parked", root);
    if (pk) pk.innerHTML = parked.length ? "<strong>Parked for another day (" + parked.length + "):</strong> " + parked.map(esc).join(" · ") : "";
    toast135("Sorted into 1 · 3 · 5. Adjust anything that looks off.");
  });

  /* Focus sprint timer */
  var mins = store.get("sm135", 25), left = mins * 60, run = null, cur = 0;
  var tEl = $("#timer", root);
  function fmt(s) { return String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }
  function paint() { if (tEl) tEl.textContent = fmt(left); if (run) document.title = fmt(left) + " · Sprint " + (cur + 1) + " · 13522"; }
  $$("[data-min]", root).forEach(function (b) {
    if (+b.getAttribute("data-min") === mins) b.classList.add("on");
    b.addEventListener("click", function () {
      $$("[data-min]", root).forEach(function (x) { x.classList.remove("on"); }); b.classList.add("on");
      mins = +b.getAttribute("data-min"); store.set("sm135", mins); stop(); left = mins * 60; paint();
    });
  });
  function beep() { try { var a = new (window.AudioContext || window.webkitAudioContext)(); [0, .25, .5].forEach(function (t) { var o = a.createOscillator(), g = a.createGain(); o.frequency.value = 880; o.connect(g); g.connect(a.destination); g.gain.setValueAtTime(.2, a.currentTime + t); g.gain.exponentialRampToValueAtTime(.001, a.currentTime + t + .2); o.start(a.currentTime + t); o.stop(a.currentTime + t + .2); }); } catch (e) {} }
  function stop() { clearInterval(run); run = null; var b = $("#t-start", root); if (b) b.textContent = "Start sprint"; document.title = document.title.replace(/^\d\d:\d\d · Sprint \d · /, ""); }
  var startBtn = $("#t-start", root);
  if (startBtn) startBtn.addEventListener("click", function () {
    if (run) { stop(); return; }
    cur = st.sprints[0] ? 1 : 0;
    startBtn.textContent = "Pause";
    run = setInterval(function () {
      left--; paint();
      if (left <= 0) { stop(); beep(); st.sprints[cur] = true; save(); left = mins * 60; paint(); toast135("Sprint complete. Take a real break."); }
    }, 1000);
  });
  var rs = $("#t-reset", root); if (rs) rs.addEventListener("click", function () { stop(); left = mins * 60; paint(); });
  $$("[data-sprint]", root).forEach(function (b, i) { b.addEventListener("click", function () { st.sprints[i] = !st.sprints[i]; save(); }); });

  /* Actions */
  function asText() {
    var out = "13522 Day Plan — " + st.date + "\n\n";
    TIERS.forEach(function (t) { out += t.label.toUpperCase() + "\n"; st[t.key].forEach(function (x) { if (x.t) out += (x.d ? "[x] " : "[ ] ") + x.t + (x.m ? " (" + x.m + "m)" : "") + "\n"; }); out += "\n"; });
    out += "FOCUS SPRINTS: " + st.sprints.filter(Boolean).length + "/2\nMORNING INTENTION: " + (st.am || "-") + "\nEVENING REVIEW: " + (st.pm || "-") + "\n\nScore: " + score(st) + "% · planned with 13522.com\n";
    return out;
  }
  root.addEventListener("click", function (e) {
    var b = e.target.closest("[data-act]"); if (!b) return;
    var a = b.getAttribute("data-act");
    if (a === "copy") { (navigator.clipboard ? navigator.clipboard.writeText(asText()) : Promise.reject()).then(function () { toast135("Plan copied to clipboard."); }, function () { toast135("Copy not available in this browser."); }); }
    if (a === "txt") { var bl = new Blob([asText()], { type: "text/plain" }), u = URL.createObjectURL(bl), l = document.createElement("a"); l.href = u; l.download = "13522-plan-" + st.date + ".txt"; l.click(); setTimeout(function () { URL.revokeObjectURL(u); }, 500); }
    if (a === "print") window.print();
    if (a === "clear") { if (confirm("Clear today's plan?")) { st = blank(); save(); build(); } }
  });
  build(); paint();
})();
