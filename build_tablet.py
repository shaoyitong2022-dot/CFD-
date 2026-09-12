#!/usr/bin/env python
"""把 lessons/ 和 reference/ 下的 HTML 课页转换为自包含平板版。
将课程样式表(course.css)内联进每个 HTML，产出 tablet/ 目录，单文件可离线阅读。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ASSETS_CSS = ROOT / "assets" / "course.css"
OUT = ROOT / "tablet"


def inline(html_path: Path) -> str:
    text = html_path.read_text(encoding="utf-8")
    css = ASSETS_CSS.read_text(encoding="utf-8")
    # 替换外链样式表为内联 <style>
    pattern = re.compile(
        r"<link rel=\"stylesheet\" href=\"\.\./assets/course\.css\">", re.I
    )
    if not pattern.search(text):
        return text
    css_inline = "<style>\n" + css + "\n</style>"
    return pattern.sub(css_inline, text, count=1)


def main():
    OUT.mkdir(exist_ok=True)
    targets = sorted((ROOT / "lessons").glob("*.html")) + sorted(
        (ROOT / "reference").glob("*.html")
    )
    for src in targets:
        html = inline(src)
        if not html:
            print(f"skip (no course.css link): {src.name}")
            continue
        dst = OUT / src.name
        dst.write_text(html, encoding="utf-8")
        print(f"ok: {src.name} -> tablet/{dst.name}")


if __name__ == "__main__":
    main()