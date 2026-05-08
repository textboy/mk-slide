# Presentation Generation Pipeline Specification

## 1. Phase 0: Mode Detection

Auto-detect user intent from the initial message:

| Mode | Description | Trigger Keywords |
|------|-------------|-----------------|
| **A: New Presentation** | Create from scratch | "make a presentation", "build slides", "create a deck" |
| **B: PPT Conversion** | Convert .pptx file | "convert pptx", "PPT to HTML" |
| **C: Enhancement** | Improve existing HTML | User provides existing HTML file |
| **D: Reference Match** | Match style from screenshot | User provides image as style reference |
| **E: Markdown Conversion** | Convert .md or markdown paste | Path ending in .md, or content with `---` / `##` slide patterns |
| **F: Style Comparison** | Post-delivery style comparison | "compare styles", "try another style" |

### 1.1 Mode E: Auto-Detection Rules

- User provides path ending in `.md` (not SKILL.md / CLAUDE.md / README.md)
- User pastes content with: `---` separators, multiple `##` headings, bullet-heavy structure
- On detection: confirm with user before converting

### 1.2 Mode C: Enhancement Flow

1. Read the full existing file
2. Count existing elements per slide, check density limits
3. Adding images: `max-height: min(50vh, 400px)`
4. After ANY modification: verify `overflow: hidden`, `clamp()`, viewport fitting
5. Proactively split overflowing content
6. Run Phase 3.5 QA before delivery

## 2. Phase 1: Content & Style Discovery

### 2.1 Auto-Detected (Don't Ask)

- **Language** — Detect from user message: Chinese → Chinese, English → English, Mixed → Bilingual
- **Inline editing** — Always enabled by default (opt-out only)

### 2.2 Questions to Ask (Single AskUserQuestion Call)

Four questions in one call:

| Question | Header | Options |
|----------|--------|---------|
| **Purpose** | Purpose | Pitch Deck / Tech Talk / Courseware / Internal Report / Product Launch |
| **Length** | Length | Short 5-10 slides / Medium 10-20 slides / Long 20+ slides |
| **Content** | Content | Content Ready / Rough Notes / Topic Only |
| **Mood** | Mood (multi-select, max 2) | Professional/Trustworthy / Exciting/Innovative / Clear/Focused / Playful/Creative / Emotional/Inspiring |

### 2.3 Image Evaluation (If Images Provided)

1. Scan all image files
2. View each via Read tool (multimodal)
3. Evaluate: USABLE or NOT USABLE, extract dominant colors
4. Co-design outline with user
5. Confirm outline + image selection

## 3. Phase 2: Style Selection

### 3.1 Recommendation Logic

Map mood to 3 recommended styles:

| Mood | Source Pool |
|------|------------|
| Professional/Trustworthy | keynote-noir, midnight-corporate, dark-premium, swiss-modern, editorial-serif |
| Exciting/Innovative | creative-voltage, electric-studio, bold-typography, pop-art, neon-brutalism |
| Clear/Focused | swiss-modern, paper-ink, watercolor, wabi-sabi-zen, soft-landing, campus-white |
| Emotional/Inspiring | cinema-scope, dark-botanical, ink-wash, starfield, gradient-dreams |
| Playful/Creative | split-pastel, memphis-pop, retro-arcade, pink-handwritten, scrapbook-portfolio |

### 3.2 Gallery URL Construction

```
https://next-slide-jet.vercel.app/gallery.html?recommend={id1},{id2},{id3}&reason={purpose},{mood}&reason_{id1}={reason1}&reason_{id2}={reason2}&reason_{id3}={reason3}
```

Opening priority: `open` command → print URL → local `style-gallery.html`

### 3.3 User Pick

Use `AskUserQuestion` with 3 recommended style names + "Custom Style" option.
If user picks custom style: ask for description, create entirely custom CSS.

### 3.4 Shortcut

If user already names a style: skip Phase 2 entirely.

## 4. Phase 3: Generation

### 4.1 Pre-Generation Reading (Required)

Before generating, read:
1. `html-template.md` — HTML architecture and JS features
2. `viewport-base.css` — Include FULL contents
3. `animation-patterns.md` — Animation reference for chosen mood
4. `styles/{id}.html` — Working demo of chosen style

### 4.2 Key Generation Requirements

- Single self-contained HTML file
- Include FULL contents of `viewport-base.css`
- Google Fonts or Fontshare (never system fonts alone)
- CJK font in stack for Chinese content
- `&display=swap` on all Google Font URLs
- For China audience: `fonts.googleapis.cn` mirror or base64 font embedding
- Navigation: Arrow keys, Space, click buttons, swipe on mobile
- `window.go = go;` exposed globally (for Phase 7 comparison sync)
- Progress bar at top
- Page counter at bottom
- NO EMOJI characters or HTML entities

### 4.3 Content Density Limits

| Slide Type | Maximum Content |
|------------|----------------|
| Title slide | 1 heading + 1 subtitle + optional tagline |
| Content slide | 1 heading + 4-6 bullets OR 1 heading + 2 paragraphs |
| Feature grid | 1 heading + 6 cards (2x3 or 3x2) |
| Comparison | 1 heading + 2 columns, 4 items each |
| Timeline | 1 heading + 4-5 timeline nodes |
| Stats | 1 heading + 3-4 numbers with labels |
| Quote slide | 1 quote (max 3 lines) + attribution |
| Image slide | 1 heading + 1 image (max 60vh) |
| Code slide | 1 heading + 8-10 lines of code |

### 4.4 Bilingual Support

- Chinese web fonts: `Noto Sans SC` (body), `Noto Serif SC` / `LXGW WenKai` (display)
- Font stack: `'LXGW WenKai', 'Noto Serif SC', serif`
- `<html lang="zh">` or `lang="zh-en"`
- CJK line-height: at least 1.8

## 5. Phase 3.5: Quality Assurance

Self-validation before delivery:

1. **Re-read generated file**
2. **Check overflow** — Every `.slide` must have `overflow: hidden`
3. **Check font links** — Valid Google Fonts / Fontshare URLs, `&display=swap`
4. **Check clamp() usage** — All font-size and spacing use `clamp()`
5. **Check content density** — Against limits table, split if exceeded
6. **Check CJK fonts** — Chinese text must have CJK font in imports + stack
7. **Check NO EMOJI** — No Unicode emoji or HTML emoji entities
8. **Check `window.go`** — Must expose global go() function
9. **Check nav dots overflow** — 15+ slides = scrollable nav container
10. **Fix before proceeding**

## 6. Phase 4A: PPT Conversion

1. Run `python scripts/extract-pptx.py <input.pptx> <output_dir>`
2. Install `python-pptx` if needed: `pip install python-pptx`
3. Present slide titles, content summaries, image counts to user
4. Proceed to Phase 2 for style selection
5. Generate HTML preserving all text, images, slide order, speaker notes

## 7. Phase 4B: Markdown Conversion

### 7.1 Parse Rules

Slide boundary detection (priority order):
1. `---` (horizontal rule) = explicit separator — highest priority
2. `## Heading` (h2) = new slide at each h2
3. `# Heading` (h1) = title slide
4. `### Heading` (h3) = fallback

Content mapping:
- `# Heading` → Title slide
- `## Heading` → Slide title
- `- ` / `* ` lists → Bullet content
- `1. ` lists → Ordered content
- `> Blockquote` → Quote slide
- Code blocks → Code slide
- `![alt](url)` → Image slide
- `**bold**` → Emphasis
- Tables → Comparison/data slide

### 7.2 Auto-Detect Slide Types

| Content Pattern | Slide Type |
|----------------|------------|
| Only heading + short line | Title slide |
| "vs" or two parallel sections | Comparison |
| 3-4 standalone numbers | Stats |
| `>` blockquote | Quote |
| Bullets with 4-6 items | Content |
| Bullets with sub-descriptions | Feature grid |
| Sequential items with dates | Timeline |
| Code block | Code |
| Image reference | Image |

### 7.3 Generation Rules

- Preserve ALL text — never summarize or omit
- Convert markdown formatting to HTML
- Respect content density limits
- Speaker notes: HTML comments from `<!-- notes: ... -->`

## 8. Phase 5: Delivery

1. Open file in browser: `open [filename].html`
2. Include "Made with MK Slide" watermark on last slide (opt-out)
3. Summarize to user: file location, style, slide count, navigation, customization

## 9. Phase 6: Share & Export (Optional)

### 9A: Vercel Deploy
- `npx vercel --prod`
- Check CLI and login first

### 9B: PDF Export
- Playwright screenshots at 1920×1080
- Combine into PDF

## 10. Phase 7: Style Comparison

Post-delivery only. Generate split-screen comparison page:
- Left half: Presentation A (iframe)
- Right half: Presentation B (iframe)
- Both iframes fully interactive
- Header bar with style names + "Select This" buttons
- Synced navigation: arrow keys advance both simultaneously via `window.go()`
- `pointer-events: none` on iframes to prevent independent clicking
- User picks winner, delete unchosen file
