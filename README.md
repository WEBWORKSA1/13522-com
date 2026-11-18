# 13522.com

**13522 — The 1·3·5·2·2 Day.** A free daily planner (1 big, 3 medium, 5 small tasks, 2 focus sprints, 2 reviews), productivity calculators, guides, an AI tools directory, a team lead-generation funnel, donations, contests, careers and sponsorships. Monetised with Google AdSense.

- Static site, no build dependencies; hosted on GitHub Pages from `main`.
- Edit content in `_src/` then run `python3 _src/build.py` to regenerate HTML.
- `_src/refresh.py` rotates the daily tip; run automatically by `.github/workflows/deploy.yml` every day.
- Data-driven sections: `data/tools.json`, `data/videos.json` (add a YouTube `id` to embed a specific video).

See `RESEARCH.md` for the concept research and `BUILD-PROMPTS.md` for the phase-wise build prompts.

## Go-live checklist
1. Settings → Pages: Source — or GitHub Actions is NOT needed; choose **Deploy from a branch → main → / (root)**.
2. Custom domain: add DNS (A records 185.199.108–111.153 + `www` CNAME to `webworksa1.github.io`), then add `13522.com` under Settings → Pages and tick Enforce HTTPS.
3. Submit one test form and confirm the one-time FormSubmit activation email.
4. Submit `https://13522.com/sitemap.xml` to Google Search Console, then apply in AdSense.
5. For EEA/UK traffic, enable Google's certified consent message (AdSense → Privacy & messaging).

© 2026 13522.com. "13522" is used only as the domain name; no trademark rights in the number are claimed.
