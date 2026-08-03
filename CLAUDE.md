# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Chinese web novel (网络小说) creation project targeting the **Tomato Novel (番茄小说)** platform. The repository contains the complete creative blueprint, character profiles, emotional arc designs, and chapter plans for a 200-chapter novel.

**Title:** 《摸鱼：我的小说首富成真了》

**Core Premise:** A 28-year-old backend developer named Chen Mo (陈默) discovers that whatever he writes in his novel on a writing platform becomes reality in the real world. He begins using this "keyboard god" ability to climb from a struggling programmer to the world's richest person — while trying to keep his identity secret.

**Target demographic:** 25–35 year old male office workers seeking escapist wish-fulfillment.

**Status:** All 200 chapters are written and complete (per `.learnings/STORY_BIBLE.md` 2026-08-01 progress note). The repository is in **maintenance/polish mode** — no new chapters needed unless revising published content.

## Repository Structure

```
.
├── 大纲.md                     # Creative blueprint (创意蓝图) — full outline, character profiles,
│                               #   chapter plans for all 200 chapters, PLUS a top
│                               #   "📌 执行校正与续写方向" segment (authoritative correction layer).
│                               #   Treat as directional plan, not live fact source.
├── CLAUDE.md                   # This file — AI collaboration instructions.
├── README.md                   # Project overview (public-facing).
├── content/                    # NOVEL TEXT — flat files, one per chapter:
│   ├── 第一章.txt ~ 第二百章.txt   # Chapter files use CHINESE NUMERAL names (第一章 not 第1章).
│   ├── Test.java               # Placeholder/test file (ignore).
│   └── 《摸鱼：我的小说首富成真了》全本.txt  # Auto-merged full-text output (from merge_all.py).
├── _RD/                        # Working/research directory (partially reorganized content).
├── .learnings/                 # LOCAL WORKING MEMORY — AI reads before every task (guards continuity):
│   ├── STORY_BIBLE.md          # SINGLE LIVE SOURCE OF TRUTH for 连载 consistency (10 power rules,
│                               #   8 suspense threads, hard red-lines, naming合规, storage约定).
│   │                           #   SUPERSEDES 大纲.md for factual disputes.
│   ├── CHARACTERS.md           # Character states (fixed attrs + current status; dead flagged, no revival).
│   ├── PLOT_POINTS.md          # Chapter progress, suspense advancement, next-chapter to-do, open-thread回收排期.
│   ├── LOCATIONS.md            # Place/location registry.
│   ├── 钩子索引.md              # Per-chapter hook/suspense mapping + coverage diagnosis.
│   ├── 续写路线图.md            # Executable chapter-level plan (hook type / active moves / thread回收 / face-slap pulse / word-count).
│   ├── ERRORS.md               # Structured generation-issue log + prevention checklist (from 15-question review).
│   └── 关键情节图解.md          # Mermaid diagrams: character relations / faction map / suspense-thread status.
├── count.sh                    # Word-count checker (filters # comment lines, flags chars outside 1500–3000).
├── scan_quality.py             # Quality scanner — detects "闷章" (stale chapters: low dialogue ratio + high internal monologue).
├── merge_all.py                # Merges all chapter files into 全本.txt (sorts by Chinese numeral).
├── add_*.py / clean_*.py / scan_*.py  # One-off editing/cleaning scripts (ad-hoc, task-specific).
└── .workbuddy/                 # External tool memory (not primary).
```

### Content File Naming Convention

Chapter files use **Chinese numeral names**: `第一章.txt`, `第二章.txt`, ... `第二百章.txt` (NOT `第1章.txt`, `第2章.txt`). The `scan_*.py` and `merge_all.py` scripts parse these via a `cn2int()` converter — do NOT rename to Arabic numerals.

### Content vs. Blueprint Split

- **Public (committed, shareable):** `content/` chapter files, `README.md`, `CLAUDE.md`.
- **Private (local-only, not pushed):** `大纲.md`, `.learnings/`, `_RD/`, all helper scripts. These contain the full creative apparatus and are gitignored or kept local.

## Novel Architecture

### Four-Act Structure (200 chapters, all complete)

| Act | Chapters | Arc | Status |
|-----|----------|-----|--------|
| 觉醒摸鱼 (Awakening) | 1–30 | Discovery of power, small-scale reality edits | ✅ Complete |
| 暗流涌动 (Undercurrents) | 31–90 | Silent acquisition of company shares, capital battles | ✅ Complete |
| 王者降临 (King Ascendant) | 91–150 | Identity semi-revealed, global富豪榜, national-level attention | ✅ Complete |
| 键盘上帝 (Keyboard God) | 151–200 | Source of power revealed, ultimate choice, apotheosis | ✅ Complete |

### Power System Rules (MUST be strictly followed)

These rules are the constraints that generate plot tension. Violating them breaks the novel's internal logic:

1. **Cannot directly rewrite death** — the protagonist cannot write someone dead
2. **Cannot change major historical events that have already occurred**
3. **3–24 hour delay** between writing and reality manifestation (creates urgency and uncertainty)
4. **Every ~15 chapters requires an "能力失控" (loss of control) incident** — e.g., writing a typo causes unintended chaotic consequences (see 第5章: Bitcoin crash)
5. **The protagonist doesn't fully understand the power's source** until late in the story (S-001 resolves at chapter 180)

Full 10-rule enumeration lives in `.learnings/STORY_BIBLE.md` 第二节 — that file is authoritative; never add new mechanics without updating it.

### Suspense Thread Tracker (Critical for Plot Consistency)

8 major suspense threads seeded and resolved across specific chapters:

| Thread | Name | Planted | Resolved | Type | Key Clue |
|--------|------|---------|----------|------|----------|
| S-001 | 金手指来源 (Source of power) | Ch.1 | Ch.180 | Core worldview | 番茄作家助手后台 |
| S-002 | 女主身份 (Heroine's identity) | Ch.4 | Ch.88 | Romance | 季晚晴 (神秘投资人) |
| S-003 | 神秘组织"守门人" (Gatekeeper org) | Ch.2伏笔/Ch.13对话/Ch.21正式 | Ch.150 | Antagonist | 猎头/资本大佬 |
| S-004 | 小说修改限制 (Writing limits) | Ch.5 | Ch.67 | Power rules | Cannot rewrite death |
| S-005 | 第二金手指持有者 (Second power holder) | Ch.89 | Ch.156 | Rival | 深夜作者榜一 |
| S-006 | 小说与现实时间差 (Time delay) | Ch.2 | Ch.33 | Rule exploration | 3–24 hour delay |
| S-007 | 国家部门介入 (State involvement) | Ch.91 | Ch.169 | Political | 国安/科技部门 |
| S-008 | 最终抉择代价 (Final choice cost) | Ch.181 | Ch.200 | Ending | Whether to reveal power |

### Key Structural Turning Points

Load-bearing chapters that pivot the entire narrative:
- **Ch. 28–30** — First major climax: company acquisition arc (压→小扬→压→爆)
- **Ch. 66** — Midpoint turn: protagonist realizes writing affects global markets; shifts from personal wish-fulfillment to social responsibility
- **Ch. 88–90** — Second major climax: identity exposure arc
- **Ch. 100** — Identity exposed to media (major reader-engagement milestone)
- **Ch. 131** — Golden ratio point: college reunion, shift from revenge to forgiveness
- **Ch. 168–170** — Third major climax: final showdown with rival who stole the power
- **Ch. 200** — Final resolution: protagonist chooses to remain a programmer, reveals the truth

## Writing Conventions & Workflow

### Single-Chapter Structure (target ~2000 words; hard rule 1500–3000 for Ch.24+)

| Words | Content |
|-------|---------|
| 0–300 | 憋屈场景 (humiliation: blamed, framed, disrespected) |
| 300–600 | 内心戏 + 发现机会 (internal monologue + discovers opening to write) |
| 600–1000 | 小爽点 (small payoff: writing manifests) |
| 1000–1300 | 新问题出现 (new problem: colleague suspects, boss pressures) |
| 1300–1600 | 紧张升级 (tension escalates: crisis closes in) |
| 1600–1900 | 反转 + 高潮 (reversal + climax: writing rewrites reality) |
| 1900–2000 | 悬念结尾 (cliffhanger pointing to next chapter's payoff) |

### 3-Chapter Emotional Unit: 压-小扬-压→爆 (pressure → small relief → pressure → explosion)

### Hard Rules

- **Word count (用户 2026-07-31):** each chapter body **1500–3000 Chinese characters**. Ch. 6–15 are exempt (written before the rule, already reviewed) — rule applies to **Ch. 24+ only**.
- **Chapter titles** must include a "爽点预告" (spoiler hook), e.g., 《第15章：我给CEO上了一课》
- **Every chapter ending** must include a cliffhanger pointing to the next chapter's payoff
- **Golden three chapters:** chapters 1–3 must complete a full "discover power → verify power → first face-slap" loop
- **Every payoff must be followed by a larger new crisis** (never let the protagonist win cleanly)
- **No "第 X 章" in narrative** — characters cannot refer to their own life events by chapter number (breaks the 4th wall). Exception: characters discussing the novel-as-fiction within the story (e.g., 林小鹿 discussing 陈默's novel, or 陈默 reviewing his own written chapters).
- **Naming compliance:** no real company/product names. Fictionalized names required (e.g., 赤兔汽车 not 特斯拉). Exception: 比特币 (Bitcoin) is explicitly allowed per user 2026-07-30.
- **No meta tags in body text:** chapter files must be pure fiction — no 【概要】【爽点】labels, no `> 概要` block quotes.

### Pre-Write Checklist (before generating any chapter)

1. Read `.learnings/STORY_BIBLE.md` (red lines + 10 power rules)
2. Read `.learnings/PLOT_POINTS.md` (current progress + next-chapter to-do)
3. Read `.learnings/续写路线图.md` (chapter-level plan if available)
4. Read `.learnings/ERRORS.md` (avoid known generation pitfalls)
5. Cross-reference `.learnings/CHARACTERS.md` + `LOCATIONS.md` for active character/location states

### Post-Write Updates (after generating a chapter)

1. Update `.learnings/钩子索引.md` (folder/word-count/hook/suspense line for the new chapter)
2. Update `.learnings/PLOT_POINTS.md` (progress + next-chapter to-do)
3. Update `.learnings/CHARACTERS.md` (if character states changed)
4. Run word-count check (`count.sh` or equivalent) to verify 1500–3000 range
5. Run `scan_quality.py` to check for "闷章" (stale chapter: low dialogue + high internal monologue)

## Commands & Tooling

All scripts are run from the project root (`D:\WZJ\摸鱼：他们都以为我只是个写小说的\`).

### Word Count Check

```bash
# Count characters for specific chapters (filters # comments, flags if outside 1500–3000)
bash count.sh content/第一章.txt content/第二章.txt

# Count all chapters at once
bash count.sh content/第*章.txt
```

`count.sh` logic: strips lines starting with `#` and lines containing `完）——`, removes all whitespace, counts remaining characters. Flags any file outside 1500–3000 range with `<== 超范围`.

### Quality Scan

```bash
# Detect stale chapters (闷章): low dialogue-line ratio + high internal-monologue count
python scan_quality.py
```

Outputs: list of stale chapters, dialogue-ratio distribution per 10-chapter block, lowest-dialogue top 12, highest-internal-monologue top 12.

### Merge Full Text

```bash
# Rebuild 全本.txt from individual chapter files (sorted by Chinese numeral)
python merge_all.py
```

### Ad-hoc Edit Scripts

Various `add_*.py`, `clean_*.py`, `scan_*.py` scripts exist for one-off tasks (e.g., `add_138.py` inserts paragraphs at anchor points, `clean_meta.py` strips meta tags, `scan_meta.py` scans for meta-tag contamination). These are task-specific — read each script's header before running.

## Key Characters

| Character | Role | Core Trait | Fate |
|-----------|------|------------|------|
| 陈默 (Chen Mo) | Protagonist — INTP backend dev, 28, 28K/month | Wants to lie flat but forced to grind; values freedom over money | Becomes "programmer-style" richest person, stays a coder |
| 赵子昂 (Zhao Zi'ang) | Antagonist — VP, Stanford MBA, wealthy family | Arrogant, sees coders as tools; wants to control the power | Hoist by his own petard |
| 张伟 (Zhang Wei) | Best friend / technical conscience | Conservative "risk-control partner"; thinks in unit tests | Becomes CTO |
| 林小鹿 (Lin Xiaolu) | Product Manager / first reader / 灵感缪斯 | Seems airheaded but perceptive; protagonist's secret crush | Becomes Chief Brand Officer |

### Heroine Identity Ambiguity (S-002 — critical伏笔)

The suspense table (S-002) lists the heroine as 季晚晴 (a mysterious investor), resolved at chapter 88, while the character profiles only list 林小鹿 (product manager). This discrepancy is **intentional** — the heroine's true identity is a mystery planted at chapter 4 and resolved at chapter 88. Chapters 4–88 must maintain ambiguity about whether 林小鹿 and 季晚晴 are the same person or different people.

## Reader-Engagement Trigger Chapters

Chapters designed to provoke comments/shares on the Tomato platform (include specified engagement hooks when touching these):

- **Ch.3** — "猜猜王磊什么时候滚蛋？" | **Ch.8** — "打赌陈默会不会被裁" | **Ch.15** — "完了完了，身份暴露了"
- **Ch.25** — "升职加薪预定！还是被开除了？" | **Ch.50** — "前老板的脸疼不疼？"
- **Ch.100** — "格子衫首富，666" | **Ch.150** — "是来复合还是来蹭热度？" | **Ch.200** — "神反转！我信你个鬼"

## Fact-Source Hierarchy

When facts conflict, resolve in this priority order:
1. **`.learnings/STORY_BIBLE.md`** — single live source of truth (immutable facts: rules, red lines, resolved outcomes)
2. **`.learnings/PLOT_POINTS.md`** — current progress + next-chapter intent
3. **`.learnings/CHARACTERS.md` / `LOCATIONS.md`** — character/location current states
4. **`大纲.md` top "📌 执行校正与续写方向"** — authoritative correction layer for blueprint-vs-actual drift
5. **`大纲.md` body** — original creative blueprint (may have been superseded by actual narrative)
6. **`CLAUDE.md`** — this file (collaboration instructions, must stay consistent with above)
