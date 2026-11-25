# -*- coding: utf-8 -*-
import re, os
base = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe\news"
files = [
    "guhuihe-lingtang-buzhi-2026.html",
    "guhuihe-wuzhu-guhui-2026.html",
    "guhuihe-fenzang-2026.html",
    "guhuihe-jiaquan-huanbao-2026.html",
    "guhuihe-tiepi-shibie-2026.html",
]
for f in files:
    h = open(os.path.join(base, f), encoding="utf-8").read()
    m = re.search(r'<article class="art-body">(.*?)</article>', h, re.S).group(1)
    t = re.sub(r"<[^>]+>", "", m)
    cn = len(re.findall(r"[\u4e00-\u9fa5]", t))
    src_n = len(re.findall(r'class="src"', m))
    print(f, "| 正文中文字数:", cn, "| 引用出处数:", src_n)
