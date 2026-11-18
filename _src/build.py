#!/usr/bin/env python3
"""Generate every static page of 13522.com.

Usage: python3 _src/build.py   (writes HTML into the repo root)
Add a page: write a function returning (path, title, desc, body, js, schema[, no_popup])
and append it to PAGES. Add an article: append a dict to articles.ARTICLES.
"""
import datetime
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from layout import page, SITE, esc  # noqa: E402
import pages_core as C  # noqa: E402
import pages_biz as B  # noqa: E402
from articles import ARTICLES  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent

PAGES = [C.home, C.planner, C.tools, C.guide, C.templates, C.videos, C.ai_tools,
         B.teams, B.contests, B.careers, B.support, B.advertise, B.about, B.contact,
         B.privacy, B.terms, B.cookies, B.disclaimer, B.trademark, B.notfound]


def blog_pages():
    out = []
    cards = ""
    for i, a in enumerate(ARTICLES):
        nxt = ARTICLES[(i + 1) % len(ARTICLES)]
        body = f"""<article class="article"><div class="wrap narrow">
<div class="crumbs"><a href="../index.html">Home</a> › <a href="index.html">Blog</a> › {esc(a['tag'])}</div>
<span class="tag">{esc(a['tag'])}</span>
<h1>{esc(a['title'])}</h1>
<p class="meta">By the 13522 editorial team · {a['min']}-minute read</p>
{a['html']}
<div class="card" style="margin-top:36px"><span class="tag">Next read</span><h3><a href="{nxt['slug']}.html">{esc(nxt['title'])}</a></h3><p>{esc(nxt['desc'])}</p></div>
<div class="lead" style="margin-top:28px;grid-template-columns:1fr"><div><h2>Plan tomorrow in 3 minutes</h2><p>Use the free 13522 planner: one big task, three medium, five small, two focus sprints and two reviews.</p><a class="btn btn-primary" href="../planner.html">Open the planner →</a> <a class="btn btn-ghost" style="color:#fff;border-color:#ffffff40" href="#" data-open-kit>Get the starter kit</a></div></div>
</div></article>"""
        schema = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": a["title"], "description": a["desc"],
                  "author": {"@type": "Organization", "name": "13522 editorial team"}, "publisher": {"@type": "Organization", "name": "13522"},
                  "mainEntityOfPage": f"{SITE}/blog/{a['slug']}.html", "datePublished": "2026-11-18"}
        out.append((f"blog/{a['slug']}.html", a["title"], a["desc"], body, (), schema))
        cards += f'<a class="card reveal" href="{a["slug"]}.html"><span class="tag">{esc(a["tag"])}</span><h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p><span style="font-size:.88rem;color:var(--muted)">{a["min"]} min read</span></a>'
    idx = f"""<section class="hero" style="padding-bottom:10px"><div class="wrap narrow"><div class="crumbs"><a href="../index.html">Home</a> › Blog</div>
<h1>The 13522 blog</h1><p class="lede">Practical, original guides on prioritising, focus, reviews, teams and using AI to plan — no fluff.</p></div></section>
<section style="padding-top:20px"><div class="wrap"><div class="grid-3">{cards}</div>
<div class="callout" style="margin-top:28px">Want to write for us? See <a href="../careers.html">careers</a>. Want a topic covered? <a href="../contact.html">Suggest it</a>.</div></div></section>"""
    out.append(("blog/index.html", "Productivity Blog — Planning, Focus, Teams & AI", "Original guides on the 1-3-5 rule, focus sprints, daily reviews, team planning, meetings and AI-assisted planning.", idx, (), None))
    return out


def main():
    entries = [f() for f in PAGES] + blog_pages()
    urls = []
    for e in entries:
        path, title, desc, body, js, schema = e[:6]
        no_popup = e[6] if len(e) > 6 else False
        html = page(path, title, desc, body, js=js, schema=schema, no_popup=no_popup,
                    og_type="article" if path.startswith("blog/") and path != "blog/index.html" else "website")
        if path == "404.html":
            html = html.replace("<head>", "<head>\n<script>document.write('<base href=\"'+(location.hostname.endsWith('github.io')?'/'+location.pathname.split('/')[1]+'/':'/')+'\">')</script>", 1)
            html = html.replace('data-root=""', 'data-root=""')
        f = ROOT / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")
        if path != "404.html":
            urls.append(path)
    today = datetime.date.today().isoformat()
    pri = {"index.html": "1.0", "planner.html": "0.9", "teams.html": "0.9", "tools.html": "0.8", "guide.html": "0.8"}
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = SITE + "/" + ("" if u == "index.html" else u)
        sm.append(f"<url><loc>{loc}</loc><lastmod>{today}</lastmod><priority>{pri.get(u, '0.6')}</priority></url>")
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    print(f"built {len(entries)} pages")


if __name__ == "__main__":
    main()
