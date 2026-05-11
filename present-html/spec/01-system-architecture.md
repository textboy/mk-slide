# System Architecture Specification

## 1. Product Overview

**Present HTML (a.k.a. Present HTML)** is an AI-agent skill that generates zero-dependency, animation-rich HTML presentations from natural language. It operates as a skill within Claude Code, Hermes Agent, and OpenClaw.

- **Slogan:** Your next PPT, doesn't have to be PPT.
- **License:** MIT
- **Author:** Callum
- **Version:** 1.1.0
- **Repository:** https://github.com/textboy/mk-present

### 1.1 Core Value Proposition

- Generate single-file HTML presentations from natural language
- 53 curated visual styles across 7 categories
- Bilingual (English / Chinese) with proper CJK typography support
- Zero dependencies — no npm, no build tools, no runtime
- 5 input modes: natural language, markdown, enhancement, reference match, style comparison
- One-click Vercel deploy for sharing

## 2. File Map

| File | Purpose |
|------|---------|
| `SKILL.md` | Core specification — Phase 0-7 flow, design rules, QA checklist |
| `STYLE_PRESETS.md` | 53 style specs (colors, fonts, Layout DNA) |
| `styles/{id}.html` | Working demo for each style — primary reference for generation |
| `viewport-base.css` | Mandatory responsive CSS (included in every presentation) |
| `html-template.md` | HTML skeleton + JS navigation controller + `window.go()` |
| `animation-patterns.md` | Animation snippets by mood |
| `SCENARIO_TEMPLATES.md` | Scenario structures, narrative arcs, 45+ example presentations |
| `gallery.html` | Online style gallery with recommendation system (Vercel-hosted) |
| `style-gallery.html` | Local lightweight gallery for offline use |
| `landing/` | Product landing page |
| `install.sh` | Auto-detection & install for Claude Code / Hermes / OpenClaw |
| `openclaw.plugin.json` | OpenClaw plugin manifest |
| `scripts/generate-drawio.py` | Drawio diagram generation → PNG embedding | Phase 8 |
| `diagram/shape.md` | Shape semantics, container logic, connectors | Phase 8 |
| `diagram/generate-diagram.md` | Diagram types and Mermaid.js integration | Phase 8 |
| `diagram/flow-with-branch.md` | Branch flow with elbow connectors | Phase 8 |
| `diagram/cross-cutting.md` | Cross-cutting layer design | Phase 8 |
| `diagram/samples/{name}.drawio.xml` | Drawio XML sample diagrams | Phase 8 |
| `diagram/samples/{name}.html` | HTML sample diagrams | Phase 8 |

## 3. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                   AI Agent (Claude Code / Hermes / OpenClaw)│
│  ┌───────────────────────────────────────────────────────┐  │
│  │  SKILL.md (Instructions + Rules + Phase Flow)         │  │
│  │  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐  │  │
│  │  │Phase 0  │ │Phase 1   │ │Phase 2   │ │Phase 3  │  │  │
│  │  │Detect   │→│Content   │→│Style     │→│Generate │  │  │
│  │  │Mode     │ │Discovery │ │Selection │ │HTML     │  │  │
│  │  └─────────┘ └──────────┘ └──────────┘ └────┬────┘  │  │
│  │                                              │       │  │
│  │  ┌─────────┐ ┌──────────┐ ┌──────────┐      │       │  │
│  │  │Phase 7  │ │Phase 6   │ │Phase 5   │      │       │  │
│  │  │Compare  │←│Share/    │←│Delivery  │←─────┘       │  │
│  │  │Styles   │ │Export    │ │          │              │  │
│  │  └─────────┘ └──────────┘ └──────────┘              │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  Reference Files:                                            │
│  ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐     │
│  │STYLE_PRESETS │ │html-template │ │animation-patterns│     │
│  │53 styles     │ │HTML skeleton │ │mood→animations   │     │
│  └──────────────┘ └──────────────┘ └─────────────────┘     │
│  ┌──────────────┐ ┌──────────────┐ ┌─────────────────┐     │
│  │viewport-base │ │SCENARIO_     │ │styles/{id}.html │     │
│  │.css          │ │TEMPLATES     │ │working demos    │     │
│  └──────────────┘ └──────────────┘ └─────────────────┘     │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌─────────────────────────┐
              │   Generated Output       │
              │   presentation.html      │
              │   (Single self-contained │
              │    HTML file)            │
              └─────────────────────────┘
```

## 4. Output Format

Every generated presentation is a **single self-contained HTML file**:

```
presentation.html
├── <head>
│   ├── Google Fonts / Fontshare @import
│   ├── <style>
│   │   ├── CSS Custom Properties (theme variables)
│   │   ├── viewport-base.css (FULL contents)
│   │   ├── Style-specific CSS
│   │   ├── Animation classes
│   │   ├── Responsive breakpoints
│   │   └── Print styles
│   └── </style>
├── <body>
│   ├── Progress bar (fixed top)
│   ├── Navigation dots (fixed right)
│   ├── Slide counter (fixed bottom-right)
│   ├── <section class="slide"> × N slides
│   │   ├── Title slide
│   │   ├── Content slides (various types)
│   │   └── Closing slide with watermark
│   └── <script>
│       └── SlidePresentation class
│           ├── IntersectionObserver
│           ├── Keyboard navigation
│           ├── Touch/swipe navigation
│           ├── Mouse wheel navigation
│           ├── Progress bar
│           ├── Navigation dots
│           ├── Slide counter
│           └── window.go() export
└── </html>
```

## 5. Design Principles

1. **Zero Dependencies** — Single HTML files with inline CSS/JS
2. **Show, Don't Tell** — Generate visual previews via style gallery
3. **Distinctive Design** — No generic "AI slop," every presentation custom-crafted
4. **Viewport Fitting (NON-NEGOTIABLE)** — Every slide fits exactly within 100vh
5. **Bilingual Native** — Full Chinese + English with CJK font fallbacks

### 5.1 Anti-AI-Slop Rules

- NO emoji in slide content
- `overflow-wrap: break-word` (never `break-all`)
- `clamp()` for all font sizes and spacing
- Tint neutrals (no pure `#000` or `#fff`)
- Avoid common AI patterns: cyan-on-dark, purple-to-blue gradients, glassmorphism-as-default, bounce easing

## 6. Platform Integrations

| Platform | Installation | Trigger |
|----------|-------------|---------|
| Claude Code | `git clone ... ~/.claude/skills/present-html` | Natural language or `/present-html` |
| Hermes Agent | `git clone ... ~/.hermes/skills/present-html` | Natural language or `/present-html` |
| OpenClaw | `clawhub install present-html` | Plugin manifest triggers |
| Any AI tool | Paste `SKILL.md` as system prompt | Manual |

## 7. New Features: Diagram Generation

Two new diagram features added in v1.2:

| Feature | Methods | Spec |
|---------|---------|------|
| **Architecture Diagram** | HTML Direct / Drawio → PNG | [spec/10-diagram-generation.md](spec/10-diagram-generation.md) |
| **Flow Diagram** | HTML Direct / Drawio → PNG | [spec/10-diagram-generation.md](spec/10-diagram-generation.md) |

See [spec/10-diagram-generation.md](spec/10-diagram-generation.md) for full details on:
- Architecture types (layered, tiered, swimlane, business, application, physical)
- Flow types (linear, branch, CI/CD, swimlane, system)
- Shape semantics, container logic, connector rules
- Actor color coding for flow diagrams
- Cross-cutting layer design
- Quality control checklist
