# -*- coding: utf-8 -*-
"""SEO 元信息批量核验：自动扫描 news/ 下全部文章"""
import re, os, glob

base = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe\news"
files = sorted(glob.glob(os.path.join(base, "*.html")))
print("扫描文章数:", len(files))

issues = []
for p in files:
    f = os.path.basename(p)
    html = open(p, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()
    desc_m = re.search(r'name="description" content="(.*?)"', html, re.S)
    desc = desc_m.group(1).strip() if desc_m else ""
    h1s = re.findall(r"<h1>(.*?)</h1>", html, re.S)
    h2s = len(re.findall(r"<h2>", html))
    lead_m = re.search(r'<p class="lead">(.*?)</p>', html, re.S)
    lead_txt = re.sub(r"<[^>]+>", "", lead_m.group(1)) if lead_m else ""
    kw_m = re.search(r'name="keywords" content="(.*?)"', html, re.S)
    kw = kw_m.group(1).split(",")[0].strip() if kw_m else ""
    body = re.sub(r"<[^>]+>", "", html)
    kc = body.count(kw) if kw else 0
    cn = sum(1 for ch in body if "\u4e00" <= ch <= "\u9fff")

    bad = []
    if not title: bad.append("无Title")
    if len(title) > 60: bad.append("Title超长%d" % len(title))
    if not desc: bad.append("无Desc")
    if len(desc) > 155: bad.append("Desc超长%d" % len(desc))
    if len(h1s) != 1: bad.append("H1数=%d" % len(h1s))
    if h2s < 3: bad.append("H2过少%d" % h2s)
    if kw and kw not in lead_txt[:100]: bad.append("首段无主词")
    if kw and kc < 2: bad.append("主词仅%d次" % kc)
    if cn < 900: bad.append("正文过短%d" % cn)
    if not re.search(r'rel="canonical"', html): bad.append("无canonical")

    print("%-42s T%2d D%3d H1=%d H2=%d 主词%2d 中文字%4d %s" % (
        f[:42], len(title), len(desc), len(h1s), h2s, kc, cn, "OK" if not bad else "!! " + "/".join(bad)))
    if bad:
        issues.append((f, bad))

print("\n=== 问题汇总: %d 篇 ===" % len(issues))
for f, b in issues:
    print(f, b)
