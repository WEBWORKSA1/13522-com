#!/usr/bin/env python3
"""Daily auto-refresh for 13522.com.

Rotates the tip / challenge of the day in data/daily.json and stamps
sitemap.xml <lastmod> values. Run by .github/workflows/deploy.yml on a
schedule; safe to run locally: `python3 _src/refresh.py`.
"""
import datetime
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

TIPS = [
    "Pick tomorrow's Big task before you close your laptop tonight — mornings go to doing, not deciding.",
    "If your Big task takes more than 3 hours, it's a project. Today's Big task is its next 90-minute chunk.",
    "Do your Big task before you open email. Inboxes are other people's priority lists.",
    "Small tasks are batchable. Run all five back-to-back in one 45-minute block.",
    "A medium task that keeps getting carried over is usually an unclear task. Rewrite it as a verb + outcome.",
    "Put minutes next to every item. If the total is over 7 hours, cut a medium, not your Big.",
    "Your two focus sprints belong in your highest-energy hours. Guard them like meetings.",
    "Say the Big task out loud in your morning review. It sounds silly and it works.",
    "Evening review question: what made today's Big task easier or harder than expected?",
    "When everything feels urgent, ask: which single task would make the rest easier or unnecessary?",
    "Close every tab not related to the sprint before you press start.",
    "If you finish all nine items before 3 p.m., you under-planned. Raise tomorrow's Big task.",
    "Carry-overs are data, not failure. Three carry-overs in a row means delegate, drop or redefine.",
    "Two 50-minute sprints beat four interrupted hours. Measure output, not time at desk.",
    "Turn recurring small tasks into automations or checklists — they shouldn't need willpower.",
    "Meetings count. A 60-minute meeting is a medium task; plan around it honestly.",
    "Write the Big task as a finish line: 'Send v1 of the proposal', not 'work on proposal'.",
    "Phone in another room for sprint one. Measure the difference.",
    "Use the 2-minute rule only for small tasks. Never let quick wins eat your sprint time.",
    "Friday's evening review becomes your weekly review: pick next week's five Big tasks.",
    "Energy low? Swap order, not commitment: do small tasks first, then one short sprint on the Big.",
    "Plan for 80% of your available time. Interruptions are a certainty, not a surprise.",
    "A 13522 day isn't about doing more. It's about knowing exactly what 'done' means today.",
    "When a new urgent task arrives, it replaces a medium task. The list never grows past nine.",
    "Start the first sprint within 10 minutes of sitting down. Momentum compounds.",
    "Track your score for two weeks before changing anything. Patterns beat hunches.",
    "Group small tasks by tool: all calls, then all emails, then all admin.",
    "Your morning review is 3 minutes: check calendar, confirm the nine, start sprint one.",
    "Name the obstacle: 'If I get stuck on the Big task, I will…' Pre-decided exits prevent drift.",
    "Rest is a task too. A proper break after each sprint protects the second one.",
]

CHALLENGES = [
    "Finish your Big task before noon.",
    "Complete both focus sprints with notifications off.",
    "Clear all five small tasks in one 45-minute batch.",
    "Write tomorrow's 1·3·5 in your evening review.",
    "Estimate minutes for all nine tasks — then compare with reality tonight.",
    "Delegate or delete one task that's been carried over twice.",
    "Do sprint one before checking email or messages.",
]


def main() -> None:
    today = datetime.date.today()
    idx = today.toordinal()
    daily = {
        "date": today.isoformat(),
        "tip": TIPS[idx % len(TIPS)],
        "challenge": CHALLENGES[idx % len(CHALLENGES)],
        "generated": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    }
    out = ROOT / "data" / "daily.json"
    out.write_text(json.dumps(daily, indent=2) + "\n", encoding="utf-8")

    sm = ROOT / "sitemap.xml"
    if sm.exists():
        text = sm.read_text(encoding="utf-8")
        text = re.sub(r"<lastmod>[^<]*</lastmod>", f"<lastmod>{today.isoformat()}</lastmod>", text)
        sm.write_text(text, encoding="utf-8")
    print("refreshed", daily["date"])


if __name__ == "__main__":
    main()
