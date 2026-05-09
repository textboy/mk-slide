#!/usr/bin/env python3
"""
generate-pptx.py — MK Slide PPTX converter via HTML screenshot (Playwright).

Usage:
    python scripts/generate-pptx.py test/deck.html --output test/deck.pptx

Supports any HTML presentation — opens in headless Chromium, screenshots each
slide at 1920x1080, and embeds as full-slide images in the PPTX.
"""

import argparse
import os
import sys
import tempfile

from pptx import Presentation
from pptx.util import Inches


def convert_html_to_pptx(html_path, output_path):
    """Convert HTML presentation to PPTX via Playwright screenshots."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Error: playwright not installed.")
        print("  pip install playwright && playwright install chromium")
        sys.exit(1)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    file_url = f"file://{os.path.abspath(html_path)}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(file_url, wait_until="networkidle")

        slide_count = page.evaluate("() => document.querySelectorAll('.slide').length")
        if slide_count == 0:
            slide_count = 1

        print(f"   Detected slides: {slide_count}")

        for i in range(slide_count):
            if slide_count > 1:
                page.evaluate(f"""
                    (function() {{
                        var go = window.go;
                        if (go) {{ go({i}); return; }}
                        var slides = document.querySelectorAll('.slide');
                        slides.forEach(function(s) {{ s.classList.remove('active'); }});
                        if (slides[{i}]) slides[{i}].classList.add('active');
                    }})()
                """)
                page.wait_for_timeout(800)

            tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
            tmp.write(page.screenshot(full_page=False))
            tmp.close()

            slide = prs.slides.add_slide(blank)
            slide.shapes.add_picture(tmp.name, Inches(0), Inches(0),
                                     Inches(13.333), Inches(7.5))
            os.unlink(tmp.name)

        browser.close()

    prs.save(output_path)
    print(f"✅ Generated: {os.path.basename(html_path)} → {os.path.basename(output_path)}")
    print(f"   Slides: {slide_count}")
    print(f"   Size:   {os.path.getsize(output_path) / 1024:.1f} KB")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert HTML presentation to PPTX via screenshots"
    )
    parser.add_argument("input", help=".html file")
    parser.add_argument("--output", "-o", help="Output .pptx file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: File not found: {args.input}")
        sys.exit(1)

    output = args.output
    if not output:
        base = os.path.splitext(os.path.basename(args.input))[0]
        output = os.path.abspath(base + '.pptx')
    elif not output.startswith('/'):
        output = os.path.abspath(output)

    convert_html_to_pptx(os.path.abspath(args.input), output)
