import os, re

EXCLUDED_FILES = {"footer.html"}

footer_html = open("footer.html", encoding="utf-8").read().strip()
injected = "<!-- begin footer -->\n" + footer_html + "\n<!-- end footer -->"

BLOCK_RE = re.compile(r"<!-- begin footer -->.*?<!-- end footer -->", re.DOTALL)
PLACEHOLDER_RE = re.compile(r'<div id="footer-placeholder"></div>')
FOOTER_SCRIPT_RE = re.compile(
    r'\s*<script>\s*fetch\([\'"][^\'"]*footer\.html[\'"]\).*?</script>',
    re.DOTALL,
)

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in [".git", "assets", "data", "scripts"]]
    for fname in files:
        if not fname.endswith(".html"):
            continue
        if fname in EXCLUDED_FILES:
            continue
        path = os.path.join(root, fname)
        content = open(path, encoding="utf-8").read()

        if "<!-- begin footer -->" in content:
            new_content = BLOCK_RE.sub(injected, content)
            action = "Updated"
        elif PLACEHOLDER_RE.search(content):
            new_content = FOOTER_SCRIPT_RE.sub("", content)
            new_content = PLACEHOLDER_RE.sub(injected, new_content, count=1)
            action = "Inserted"
        elif "</body>" in content:
            new_content = content.replace("</body>", f"{injected}\n</body>", 1)
            action = "Inserted"
        else:
            print(f"Skipped (no placeholder/</body>): {path}")
            continue

        if new_content != content:
            open(path, "w", encoding="utf-8").write(new_content)
            print(f"{action}: {path}")
        else:
            print(f"No change: {path}")
