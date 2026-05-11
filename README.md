<p align="right">
  <strong>English</strong> | <a href="README_CN.md">中文</a>
</p>

# MK Present

Works on **Claude Code** · **Hermes Agent** · **OpenClaw**

> Describe what you want. Pick a style. Get a beautiful HTML presentation. No PowerPoint, no build tools, no dependencies.

> **Forked from** [next-slide](https://github.com/codesstar/next-slide) — extended with diagram generation and PPTX conversion.

---

## What It Does

You talk to your AI assistant in natural language. MK Slide turns your words into a polished, animated HTML presentation — a single file you can open in any browser.

```
You: "Make me a 10-slide presentation about AI agents, with a strong tech vibe"

→ AI asks you to pick a style (50+ options with live preview)
→ Generates a complete HTML presentation
→ Opens in your browser, ready to present
```

**Input:** natural language, markdown, or even an existing .pptx file
**Output:** one self-contained HTML file — animations, responsive layout, keyboard navigation, all built in

---

## 3 Skills in This Repository

This repository (forked from `mk-slide`) contains three related skills, each handling a different stage of the presentation workflow:

| Skill | Directory | Forked From | Purpose |
|-------|-----------|-------------|---------|
| **present-workflow** | `present-workflow/` | [ppt-agent-workflow-san/ppt-workflow](https://github.com/mucsbr/ppt-agent-workflow-san/tree/main/ppt-workflow) | Complete the storyline / workflow of the deck |
| **present-html** | `present-html/` | [next-slide](https://github.com/codesstar/next-slide) | Generate HTML presentations with architecture & flow diagram support |
| **present-ppt** | `present-ppt/` | [ppt-agent-workflow-san/html-slide-to-pptx](https://github.com/mucsbr/ppt-agent-workflow-san/tree/main/html-slide-to-pptx) | Convert HTML to editable PowerPoint (.pptx) |

- **present-workflow** — Prepares the presentation storyline as the first stage: clarify brief, research, outline, plan, review.
- **present-html** — Generates zero-dependency, animation-rich HTML presentations from natural language. 50+ curated styles, bilingual support. Also supports architecture and flow diagram generation (enterprise house-architecture, logical/system/physical architecture, flow charts, API sequence diagrams) via Drawio → PNG → embed or direct HTML.
- **present-ppt** — Converts structured single-slide or small deck HTML files into editable PPTX slides with native text boxes, shapes, chips, arrows, and panels. Preset-driven, not a generic browser renderer.

---

## Quick Start

```bash
# 1. Install as Claude Code skill
git clone https://github.com/textboy/mk-present ~/.claude/skills/mk-present

# 2. Use — just talk naturally
# "Make me a presentation about..."
# "Make me a slide about XX" (in Chinese)
# or invoke directly:
/mk-present

# 3. Present
open my-presentation.html    # One file. Zero dependencies.
```

### Also works with

| Platform | Install |
|----------|---------|
| **Claude Code** | `git clone https://github.com/textboy/mk-present ~/.claude/skills/mk-present` |
| **Hermes Agent** | `git clone https://github.com/textboy/mk-present ~/.hermes/skills/mk-present` |
| **OpenClaw** | `clawhub install mk-present` |
| **Any AI tool** | Paste `SKILL.md` as system prompt + reference the support files |

> Or run `bash install.sh` from a clone — it auto-detects all three and symlinks for you.

No runtime, no API keys, no vendor lock-in. Just markdown instructions + CSS/HTML references.

---

## 50+ Styles, 7 Categories

| Category | Count | Styles | Vibe |
|----------|-------|--------|------|
| **Dark** | 11 | Keynote Noir, Bold Signal, Neon Cyber, Terminal Green, Midnight Corporate, Cinema Scope, Dark Botanical, Starfield, Dark Premium, Dark Cinema, Futuristic Blue | Conferences, launches, tech talks |
| **Light** | 11 | Swiss Modern, Paper & Ink, Notebook Tabs, Pastel Geometry, Morning Brief, Campus White, Soft Landing, Watercolor Wash, Korean Soft, Claymorphism 3D, Wabi-Sabi Zen | Academic, business, teaching |
| **Editorial** | 4 | Editorial Serif, Fashion Editorial, Newsprint Broadsheet, Vintage Editorial | Magazine layouts, thought leadership |
| **Bold** | 7 | Electric Studio, Creative Voltage, Split Pastel, Pop Art, Bold Typography, Neon Brutalism, Memphis Pop | Startups, creative pitches |
| **Retro** | 5 | Grainy Retro, Art Deco Gatsby, Risograph Overprint, Vintage Poster, Retro Arcade | Nostalgic, stylized |
| **Artistic** | 7 | Surrealism Gallery, Scrapbook Portfolio, Blue Collage, Pink Handwritten, Art Nouveau Botanical, Soft Dreamy, Terracotta Earth | Art, design, portfolio |
| **Cultural** | 8 | Ink Wash, Wafu, Gradient Dreams, Blueprint, Bauhaus Primary, Swiss Grid, Aurora Mesh, Chinese Ink Wash | Cultural events, themed talks |

Each style is a complete design system: curated typography, color palette, layout patterns, signature animations, and responsive breakpoints.

**Browse all styles:** [Style Gallery](https://next-slide-jet.vercel.app/gallery) or run `open style-gallery.html` locally after installing.

---

## How It Works

```
┌─────────────────────────────────────────────────────┐
│  1. CONTENT                                         │
│     Describe your topic, paste markdown,            │
│     or drop a .pptx file                            │
├─────────────────────────────────────────────────────┤
│  2. STYLE                                           │
│     Browse 50+ styles → pick a mood →               │
│     see 3 live previews → choose one                │
│     (or say "match this screenshot")                │
├─────────────────────────────────────────────────────┤
│  3. GENERATE                                        │
│     AI builds the full deck: proper layout,         │
│     animations, responsive CSS, navigation          │
├─────────────────────────────────────────────────────┤
│  4. DELIVER                                         │
│     Opens in browser. Press E to edit inline.       │
│     Deploy to Vercel with one command.              │
└─────────────────────────────────────────────────────┘
```

---

## Features

- **50+ curated styles** — not just color swaps, each is a distinct design language with Layout DNA
- **Zero dependencies** — single HTML file, all CSS/JS inline
- **Bilingual native** — English + Chinese with proper CJK font support
- **5 input modes** — new from scratch, markdown, PPT conversion, enhancement, reference match
- **Responsive** — fits any screen, from phone to 4K projector
- **Keyboard navigation** — arrows, space, home/end
- **Inline editing** — press `E` to edit text directly in the browser
- **One-click deploy** — `npx vercel --prod` and you have a live URL
- **Quality assurance** — auto-checks overflow, fonts, density after generation
- **Typography precision** — every style has exact clamp() values extracted from hand-crafted references
- **Architecture & flow diagrams** — generate from natural language: enterprise house-architecture, logical/system/physical architecture, flow charts, API sequence diagrams. Supports Drawio → PNG → embed in HTML, or direct HTML with CSS-positioned cards + SVG connectors. See `diagram/` for specs and samples.
- **HTML to PPTX conversion** — export any HTML presentation to PowerPoint with native shapes (text boxes, rectangles, rounded rectangles, styled text, borders, background fills). Not 100% pixel-perfect due to python-pptx limitations (gradients → solid fill, box-shadow ignored), but text remains editable and structure is preserved.

---

## Input Formats

| Format | Example |
|--------|---------|
| Natural language | "Make a 10-slide pitch deck about AI agents" |
| Markdown | Provide a `.md` file — headings become slides |
| PowerPoint | Drop a `.pptx` — content extracted and restyled |
| Reference image | Share a screenshot — AI matches the closest style |
| Enhancement | Point to an existing HTML deck — AI improves it |

---

## Design Philosophy

MK Slide isn't a template engine. It's an opinionated design system that teaches AI to think like a designer:

1. **No AI Slop** — Every style is hand-crafted with intentional typography, spacing, and motion. The AI follows exact specifications, not vibes.
2. **Layout DNA** — Each style defines its structural patterns: slide mechanism, title alignment, navigation style, background treatment, animation approach, and component structure.
3. **Typography Scale** — Precise `clamp()` values for every element ensure the AI reproduces exact font sizes, weights, line-heights, and letter-spacing.
4. **Viewport First** — Every slide fits exactly in 100vh. No scrolling. Content too long? Split into multiple slides automatically.
5. **Zero Dependencies** — One HTML file. Open it anywhere. No npm, no build step, no CDN that might go down.

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `←` `→` `↑` `↓` | Navigate slides |
| `Space` | Next slide |
| `Home` / `End` | First / Last |
| `E` | Toggle edit mode |

---

## Customize

Every presentation uses CSS custom properties. Override in `:root`:

```css
:root {
    --bg-primary: #0a0a0a;
    --accent: #ff6b35;
    --font-display: 'Your Font', sans-serif;
}
```

---

## File Structure

```
mk-present/
├── CLAUDE.md                    # Behavioral guidelines
├── LICENSE                      # MIT license
├── README.md                    # This file
│
├── present-workflow/            # Stage 1: storyline preparation
│   ├── SKILL.md
│   ├── README.md
│   └── references/
│       ├── agent-integration.md
│       ├── method.md
│       └── prompts.md
│
├── present-html/                # Stage 2: HTML presentation generation
│   ├── SKILL.md                 # AI instructions (the brain)
│   ├── STYLE_PRESETS.md         # 50+ style definitions with Layout DNA
│   ├── html-template.md         # HTML architecture reference
│   ├── animation-patterns.md    # Animation snippets
│   ├── viewport-base.css        # Responsive CSS base
│   ├── gallery.html             # Style gallery (full)
│   ├── style-gallery.html       # Style browser (lightweight)
│   ├── SCENARIO_TEMPLATES.md    # Content scenario templates
│   ├── PROJECT_CONTEXT.md       # Project context
│   ├── README.md / README_CN.md # Documentation
│   ├── openclaw.plugin.json     # OpenClaw plugin manifest
│   ├── install.sh               # Auto-detect & install
│   ├── package.json             # Dev metadata
│   ├── vercel.json              # Deploy config
│   │
│   ├── styles/                  # 56 reference presentations for each style
│   ├── scenarios/               # 114 scenario-based template decks
│   │   └── images/              # Scenario images
│   ├── diagram/                 # Diagram generation specs & samples
│   │   ├── *.md                 # Spec docs (cross-cutting, flow, shape, etc.)
│   │   └── samples/
│   │       ├── *.drawio.xml     # Drawio XML sample diagrams
│   │       └── *.html           # HTML sample diagrams
│   ├── scripts/
│   │   ├── extract-pptx.py     # PPT content extraction
│   │   ├── generate-pptx.py    # HTML → PPTX (native shapes)
│   │   └── generate-drawio.py  # Drawio diagram → PNG generation
│   ├── spec/                   # 10 specification documents
│   └── landing/                # Landing page
│
├── present-ppt/                 # Stage 3: HTML → PPTX conversion
│   ├── SKILL.md
│   ├── README.md
│   ├── package.json / package-lock.json
│   ├── references/
│   │   ├── presets.md
│   │   ├── preset-template.md
│   │   ├── preset-decision-rules.md
│   │   ├── setup.md
│   │   ├── usage-principles.md
│   │   ├── qa-heuristics.md
│   │   └── roadmap.md
│   └── scripts/
│       ├── html_to_pptx.js / html_to_pptx_v9.js
│       ├── layout_v9.js / layout_template.js / layout_utils.js
│       ├── ai_runtime_preset.js / data_strategy_deck_preset.js
│       ├── preset_template.js / preflight_qa.js / check_env.js
│       └── layout_ai_runtime.js
│
├── test/                        # Test & sample outputs
│
├── .claude/
│   └── settings.local.json
└── .loci/
    └── memory.md
```

---

## License

MIT. Copyright 2026 Callum.
