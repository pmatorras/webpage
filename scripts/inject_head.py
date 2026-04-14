import os, re
EXCLUDED_FILES = {"footer.html"}
# Read tags from header.js
header_js = open("header.js", encoding="utf-8").read()
raw_tags = re.findall(r"'(<[^']+>)'", header_js)
injected = "\n  <!-- begin common head -->\n" + "\n".join(f"  {t}" for t in raw_tags) + "\n  <!-- end common head -->"

BLOCK_RE = re.compile(r"\s*<!-- begin common head -->.*?<!-- end common head -->", re.DOTALL)

for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in [".git", "assets", "data", "scripts"]]
    for fname in files:
        if not fname.endswith(".html"):
            continue
        if fname in EXCLUDED_FILES:
            continue
        path = os.path.join(root, fname)
        content = open(path, encoding="utf-8").read()

        if "<!-- begin common head -->" in content:
            # Replace existing block
            new_content = BLOCK_RE.sub(injected, content)
            action = "Updated"
        elif "<head>" in content:
            # Insert after <head>
            new_content = content.replace("<head>", f"<head>{injected}", 1)
            action = "Inserted"
        else:
            print(f"Skipped (no <head>): {path}")
            continue

        if new_content != content:
            new_content = re.sub(r'\s*<script src=["\']/?header\.js["\'][^>]*></script>', '', new_content)
            open(path, "w", encoding="utf-8").write(new_content)
            print(f"{action}: {path}")
        else:
            print(f"No change: {path}")
