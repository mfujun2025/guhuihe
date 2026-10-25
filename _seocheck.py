# -*- coding: utf-8 -*-
"""SEO 元信息核验：5篇新文章"""
import re, os

base = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe\news"
files = [
    "guhuihe-yidi-anzang-2026.html",
    "guhuihe-tuoyun-2026.html",
    "guhuihe-fangchao-2026.html",
    "guhuihe-guojia-biaozhun-2026.html",
    "guhuihe-gewei-xuanze-2026.html",
    "guhuihe-chicun-guige-2026.html",
    "guhuihe-pinpai-xuangou-2026.html",
    "guhuihe-wangshang-goumai-2026.html",
    "guhuihe-baocun-nianxian-2026.html",
    "guhuihe-anfang-liucheng-2026.html",
    "guhuihe-xiedai-jiaotong-2026.html",
    "guhuihe-sunhuai-chuli-2026.html",
    "guhuihe-shuangren-hezang-2026.html",
    "guhuihe-yanse-jiangjiu-2026.html",
    "guhuihe-kezi-2026.html",
]
for f in files:
    p = os.path.join(base, f)
    html = open(p, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()
    desc = re.search(r'name="description" content="(.*?)"', html, re.S).group(1).strip()
    h1s = re.findall(r"<h1>(.*?)</h1>", html, re.S)
    h2s = len(re.findall(r"<h2>", html))
    body = re.sub(r"<[^>]+>", "", html)
    lead = re.search(r'<p class="lead">(.*?)</p>', html, re.S).group(1)
    lead_txt = re.sub(r"<[^>]+>", "", lead)
    kw = re.search(r'name="keywords" content="(.*?)"', html, re.S).group(1).split(",")[0].strip()
    kc = body.count(kw)
    print("---", f)
    print("TITLE(%d字):" % len(title), title)
    print("DESC(%d字):" % len(desc), desc)
    print("H1数:", len(h1s), "| H2数:", h2s)
    print("主关键词[%s] 全文出现:%d次" % (kw, kc))
    print("首段100字含主词:", kw in lead_txt[:100])
