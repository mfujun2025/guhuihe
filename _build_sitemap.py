# -*- coding: utf-8 -*-
"""扫描 news 目录重建 sitemap.xml（含首页）"""
import os, re, glob

ROOT = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe"
news = os.path.join(ROOT, "news")

items = []
for path in glob.glob(os.path.join(news, "*.html")):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    m = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    loc = m.group(1) if m else "https://xn--0nx29kk17a.cn/news/" + os.path.basename(path)
    d = re.search(r'</svg>(2026-\d\d-\d\d)<', html)
    date = d.group(1) if d else "2026-10-21"
    # priority：选购/政策类 0.9，其余 0.8
    pri = "0.9" if re.search(r'选购指南|政策法规', html[:2000]) else "0.8"
    items.append((date, loc, pri))

items.sort(key=lambda x: (x[0], x[1]), reverse=True)
home_date = max(i[0] for i in items) if items else "2026-10-21"

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
         '  <url>',
         '    <loc>https://xn--0nx29kk17a.cn/</loc>',
         f'    <lastmod>{home_date}</lastmod>',
         '    <changefreq>weekly</changefreq>',
         '    <priority>1.0</priority>',
         '  </url>']
for date, loc, pri in items:
    lines += ['  <url>',
              f'    <loc>{loc}</loc>',
              f'    <lastmod>{date}</lastmod>',
              '    <changefreq>monthly</changefreq>',
              f'    <priority>{pri}</priority>',
              '  </url>']
lines.append('</urlset>')

with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines) + "\n")
print("sitemap 条目：", len(items) + 1, "| 首页 lastmod:", home_date)
