/* 13522.com — page widgets: tabs, calculators, directory, videos, team assessment, support tiers. */
(function () {
  "use strict";
  var S = window.S135, $ = S.$, $$ = S.$$;
  var base = document.documentElement.getAttribute("data-root") || "";
  function money(v, c) { return (c || "$") + Math.round(v).toLocaleString(); }
  function num(id) { var e = document.getElementById(id); return e ? parseFloat(e.value) || 0 : 0; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* Tabs */
  $$("[data-tabs]").forEach(function (box) {
    var btns = $$("[data-tab]", box), panes = $$(".tool", box.parentNode);
    function go(id) {
      btns.forEach(function (b) { b.classList.toggle("on", b.getAttribute("data-tab") === id); b.setAttribute("aria-selected", b.getAttribute("data-tab") === id); });
      panes.forEach(function (p) { p.classList.toggle("on", p.id === id); });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { go(b.getAttribute("data-tab")); history.replaceState(null, "", "#" + b.getAttribute("data-tab")); }); });
    var h = location.hash.slice(1); if (h && document.getElementById(h)) go(h); else if (btns[0]) go(btns[0].getAttribute("data-tab"));
  });

  /* Calculators */
  var calcs = {
    meeting: function () {
      var c = num("m-people") * num("m-rate") * num("m-mins") / 60, w = c * num("m-week");
      return "<div class='result'>" + money(c) + "</div><p>per meeting · <strong>" + money(w) + "</strong> per week · <strong>" + money(w * 48) + "</strong> per year (48 working weeks).</p><p>Cutting this meeting by 15 minutes saves " + money(num("m-people") * num("m-rate") * 0.25 * num("m-week") * 48) + " a year.</p>";
    },
    hourly: function () {
      var hrs = num("h-hours") * num("h-weeks"), v = hrs ? num("h-income") / hrs : 0;
      return "<div class='result'>" + money(v) + "/hour</div><p>Your time is worth about <strong>" + money(v / 60 * 15) + "</strong> per 15 minutes. Any small task you can delegate or automate for less than that is a net gain.</p>";
    },
    estimate: function () {
      var b = num("e-base"), conf = num("e-conf"), buf = conf >= 80 ? 1.2 : conf >= 50 ? 1.5 : 2, n = b * buf;
      var tier = n >= 90 ? "a Big task" : n >= 25 ? "a Medium task" : "a Small task";
      return "<div class='result'>" + Math.round(n) + " minutes</div><p>Buffer ×" + buf + " applied (planning-fallacy correction). Treat this as <strong>" + tier + "</strong> in your 1·3·5.</p>";
    },
    capacity: function () {
      var h = num("c-hours"), mtg = num("c-mtg"), free = Math.max(0, h - mtg), need = 2 * 1.0 + 3 * 1.0 + 5 * 0.2 + 0.5;
      var ok = free >= need;
      return "<div class='result'>" + free.toFixed(1) + "h focus time</div><p>A full 13522 day needs roughly <strong>" + need.toFixed(1) + "h</strong> (1 big ≈2h, 3 medium ≈1h each, 5 small ≈12 min each, reviews 30 min). " + (ok ? "You have room — protect it on your calendar." : "You're short by " + (need - free).toFixed(1) + "h. Use a 1·2·3 day instead, or decline one meeting.") + "</p>";
    },
    procrast: function () {
      var c = num("p-mins") / 60 * num("p-rate") * num("p-days") * 52;
      return "<div class='result'>" + money(c) + "/year</div><p>That's the value of the time lost to " + num("p-mins") + " minutes of daily drift. Two focus sprints a day are the cheapest fix.</p>";
    },
    team: function () {
      var c = num("t-size") * num("t-lost") * num("t-rate") * 48;
      return "<div class='result'>" + money(c) + "/year</div><p>Estimated cost of unfocused time across your team. Recovering even a third of it is worth <strong>" + money(c / 3) + "</strong>.</p><p><a class='btn btn-primary btn-sm' href='" + base + "teams.html'>Get a free team focus plan →</a></p>";
    }
  };
  $$("[data-calc]").forEach(function (f) {
    var k = f.getAttribute("data-calc"), out = $(".out", f);
    function run() { if (calcs[k] && out) out.innerHTML = calcs[k](); }
    f.addEventListener("input", run); f.addEventListener("submit", function (e) { e.preventDefault(); run(); }); run();
  });

  /* AI & productivity tools directory */
  var dir = $("#directory");
  if (dir) {
    fetch(base + "data/tools.json").then(function (r) { return r.json(); }).then(function (list) {
      var cats = ["All"].concat(list.map(function (x) { return x.cat; }).filter(function (v, i, a) { return a.indexOf(v) === i; }));
      var cur = "All", q = "";
      var fb = $("#dir-filters"), si = $("#dir-search");
      fb.innerHTML = cats.map(function (c) { return "<button type='button' data-cat='" + esc(c) + "'" + (c === "All" ? " class='on'" : "") + ">" + esc(c) + "</button>"; }).join("");
      fb.addEventListener("click", function (e) { var b = e.target.closest("[data-cat]"); if (!b) return; cur = b.getAttribute("data-cat"); $$("[data-cat]", fb).forEach(function (x) { x.classList.toggle("on", x === b); }); draw(); });
      si.addEventListener("input", function () { q = si.value.toLowerCase(); draw(); });
      function draw() {
        var f = list.filter(function (x) { return (cur === "All" || x.cat === cur) && (!q || (x.name + x.desc + x.cat + x.fit).toLowerCase().indexOf(q) > -1); });
        dir.innerHTML = f.map(function (x) {
          return "<div class='card'><span class='tag'>" + esc(x.cat) + "</span><h3>" + esc(x.name) + "</h3><p>" + esc(x.desc) + "</p><p style='font-size:.88rem'><strong>13522 fit:</strong> " + esc(x.fit) + "</p><a class='btn btn-ghost btn-sm' href='" + esc(x.url) + "' target='_blank' rel='noopener nofollow sponsored'>Visit site ↗</a></div>";
        }).join("") || "<p>No tools match that search.</p>";
        var c = $("#dir-count"); if (c) c.textContent = f.length + " tools";
      }
      draw();
    });
  }

  /* Videos: lite embeds when an id is set, otherwise a YouTube search card */
  var vids = $("#videos");
  if (vids) {
    var limit = +vids.getAttribute("data-limit") || 99;
    fetch(base + "data/videos.json").then(function (r) { return r.json(); }).then(function (list) {
      vids.innerHTML = list.slice(0, limit).map(function (v, i) {
        var pal = [["#2a1f4d", "#ff5a36"], ["#0f3d3a", "#12a594"], ["#3b2a05", "#f2a516"], ["#241a5e", "#6d5efc"], ["#4b1235", "#e0479e"]][i % 5];
        var thumb = v.id
          ? "<div class='vid' data-yt='" + esc(v.id) + "' style='background-image:url(https://i.ytimg.com/vi/" + esc(v.id) + "/hqdefault.jpg)' role='button' tabindex='0' aria-label='Play " + esc(v.title) + "'><span class='play'>▶</span></div>"
          : "<a class='vid gen' style='--c1:" + pal[0] + ";--c2:" + pal[1] + "' href='https://www.youtube.com/results?search_query=" + encodeURIComponent(v.q || v.title) + "' target='_blank' rel='noopener'><span class='play'>▶</span><span class='vt'>" + esc(v.title) + "</span></a>";
        return "<div class='card'>" + thumb + "<span class='tag'>" + esc(v.topic) + "</span><h3>" + esc(v.title) + "</h3><p>" + esc(v.desc) + "</p></div>";
      }).join("");
    });
    vids.addEventListener("click", play); vids.addEventListener("keydown", function (e) { if (e.key === "Enter") play(e); });
    function play(e) {
      var v = e.target.closest("[data-yt]"); if (!v || v.querySelector("iframe")) return;
      v.innerHTML = "<iframe src='https://www.youtube-nocookie.com/embed/" + v.getAttribute("data-yt") + "?autoplay=1&rel=0' title='YouTube video' allow='accelerometer; autoplay; encrypted-media; picture-in-picture' allowfullscreen></iframe>";
    }
  }

  /* Team Focus Assessment — multi-step lead funnel */
  var quiz = $("#assessment");
  if (quiz) {
    var qs = $$(".q", quiz), bars = $$(".steps i", quiz), i = 0, ans = {};
    function show(n) { i = n; qs.forEach(function (q, k) { q.classList.toggle("on", k === n); }); bars.forEach(function (b, k) { b.classList.toggle("on", k <= n); }); }
    quiz.addEventListener("click", function (e) {
      var o = e.target.closest(".opts button"); if (o) {
        var q = o.closest(".q"); $$(".opts button", q).forEach(function (x) { x.classList.remove("sel"); }); o.classList.add("sel");
        ans[q.getAttribute("data-key")] = { v: +o.getAttribute("data-v"), t: o.textContent.trim() };
        setTimeout(function () { if (i < qs.length - 1) { show(i + 1); if (i === qs.length - 1) result(); } }, 220);
      }
      if (e.target.closest("[data-back]") && i > 0) show(i - 1);
    });
    function result() {
      var risk = 0; for (var k in ans) if (k !== "size") risk += ans[k].v;
      var head = ans.size ? [5, 15, 40, 120, 300][ans.size.v] : 10, lostH = Math.max(2, risk) * 0.9;
      var cost = head * lostH * 45 * 48;
      var label = risk >= 12 ? "High focus leakage" : risk >= 7 ? "Moderate focus leakage" : "Low focus leakage";
      var r = $("#q-result", quiz);
      if (r) r.innerHTML = "<span class='tag'>Your result</span><h3>" + label + "</h3><p>Estimated <strong>" + lostH.toFixed(1) + " hours per person per week</strong> lost to unclear priorities and context switching — roughly <strong>" + money(cost) + " a year</strong> at a $45/h blended rate.</p><p>Get the full plan below: a 1-page team rollout of the 13522 method tailored to your answers, plus an optional 30-minute call.</p>";
      var form = $("#lead-form");
      if (form) form._extra = function () { var o = { assessment_result: label, est_hours_lost_pp_week: lostH.toFixed(1), est_annual_cost: money(cost) }; for (var k in ans) o["q_" + k] = ans[k].t; return o; };
    }
    show(0);
  }

  /* Support / donation tiers */
  var tiers = $("#tiers");
  if (tiers) {
    var amt = $("#d-amount");
    tiers.addEventListener("click", function (e) {
      var t = e.target.closest(".tierbtn"); if (!t) return;
      $$(".tierbtn", tiers).forEach(function (x) { x.classList.toggle("sel", x === t); });
      if (amt) { amt.value = t.getAttribute("data-amt") || ""; if (!amt.value) amt.focus(); }
      var tn = $("#d-tier"); if (tn) tn.value = t.getAttribute("data-name");
      var f = $("#support-form"); if (f) f.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }
})();
