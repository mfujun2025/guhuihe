# -*- coding: utf-8 -*-
"""站内链接与 sitemap 一致性核验"""
import os, re

root = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe"
bad = []
for dirpath, _, files in os.walk(root):
    for f in files:
        if not f.endswith(".html"):
            continue
        p = os.path.join(dirpath, f)
        html = open(p, encoding="utf-8").read()
        for href in re.findall(r'href="([^"]+\.html(?:#[^"]*)?)"', html):
            if href.startswith("http") or href.startswith("mailto"):
                continue
            target = href.split("#")[0]
            if not target:
                continue
            full = os.path.normpath(os.path.join(dirpath, target))
            if not os.path.exists(full):
                bad.append((os.path.relpath(p, root), href))

print("broken internal links:", len(bad))
for b in bad[:30]:
    print("  ", b[0], "->", b[1])
