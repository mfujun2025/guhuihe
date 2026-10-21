# -*- coding: utf-8 -*-
"""骨灰盒.cn 站点自检：结构完整性、内链、sitemap 一致性"""
import os, re, sys

ROOT = r"C:\Users\Huawei\Doubao\chats\2026-10-21\new-chat-5\guhuihe"
errors = []
warns = []

def rel(path):
    return os.path.relpath(path, ROOT)

def check_html(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()
    base = os.path.dirname(path)
    # 1. 基本标签配对
    for tag in ["html", "head", "body"]:
        opens = len(re.findall(r"<%s[\s>]" % tag, html))
        closes = len(re.findall(r"</%s>" % tag, html))
        if opens != closes:
            errors.append(f"{rel(path)}: <{tag}> 开闭数量不一致 ({opens} vs {closes})")
    # 2. title / meta description
    if "<title>" not in html or "</title>" not in html:
        errors.append(f"{rel(path)}: 缺少 title")
    if 'name="description"' not in html:
        errors.append(f"{rel(path)}: 缺少 meta description")
    # 3. lang 与 charset
    if 'lang="zh-CN"' not in html:
        errors.append(f"{rel(path)}: 缺少 lang=zh-CN")
    if 'charset="UTF-8"' not in html:
        errors.append(f"{rel(path)}: 缺少 UTF-8 charset")
    # 4. 内链检查
    for href in re.findall(r'href="([^"#][^"]*)"', html):
        if href.startswith(("http", "mailto:", "data:", "tel:")):
            continue
        # 去掉 # 锚点部分后再检查文件
        clean = href.split("#")[0]
        if not clean:
            continue
        target = os.path.normpath(os.path.join(base, clean))
        if not os.path.exists(target):
            errors.append(f"{rel(path)}: 链接失效 -> {href}")
    # 5. 无残留模板/占位
    for bad in ["TODO", "{{", "Lorem", "待补充"]:
        if bad in html:
            warns.append(f"{rel(path)}: 疑似占位内容 {bad}")

def check_sitemap():
    sp = os.path.join(ROOT, "sitemap.xml")
    with open(sp, encoding="utf-8") as f:
        sm = f.read()
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    if not locs:
        errors.append("sitemap.xml: 无 <loc> 条目")
        return
    # 域名校验
    for loc in locs:
        if not loc.startswith("https://xn--0nx29kk17a.cn/"):
            errors.append(f"sitemap.xml: URL 域名异常 -> {loc}")
    # 本地文件校验
    for loc in locs:
        fname = loc.replace("https://xn--0nx29kk17a.cn/", "")
        if fname == "":
            fname = "index.html"
        if not os.path.exists(os.path.join(ROOT, fname)):
            errors.append(f"sitemap.xml: 文件不存在 -> {fname}")
    # 反向：news 下所有 html 都应进 sitemap
    news_dir = os.path.join(ROOT, "news")
    if os.path.isdir(news_dir):
        for f in os.listdir(news_dir):
            if f.endswith(".html"):
                if f"https://xn--0nx29kk17a.cn/news/{f}" not in sm:
                    errors.append(f"sitemap.xml: 缺少文章条目 -> news/{f}")
    # 优先级检查
    for p in re.findall(r"<priority>([^<]+)</priority>", sm):
        try:
            v = float(p)
            if not (0.0 <= v <= 1.0):
                errors.append(f"sitemap.xml: priority 越界 {p}")
        except ValueError:
            errors.append(f"sitemap.xml: priority 非法 {p}")

def main():
    # HTML 文件
    html_files = [os.path.join(ROOT, "index.html")] + [
        os.path.join(ROOT, "news", f) for f in os.listdir(os.path.join(ROOT, "news"))
        if f.endswith(".html")
    ] + [os.path.join(ROOT, "404.html")]
    for f in html_files:
        if not os.path.exists(f):
            errors.append(f"缺少文件: {rel(f)}")
            continue
        check_html(f)
    # robots / CNAME
    for name in ["robots.txt", "CNAME", "sitemap.xml", "README.md", r".github\workflows\deploy.yml"]:
        if not os.path.exists(os.path.join(ROOT, name)):
            errors.append(f"缺少文件: {name}")
    check_sitemap()
    # CNAME 内容
    with open(os.path.join(ROOT, "CNAME"), encoding="utf-8") as f:
        if f.read().strip() != "xn--0nx29kk17a.cn":
            errors.append("CNAME 内容不正确")

    print(f"检查 HTML 文件数: {len(html_files)}")
    print(f"错误: {len(errors)} | 警告: {len(warns)}")
    for e in errors:
        print("  [ERR]", e)
    for w in warns:
        print("  [WARN]", w)
    sys.exit(1 if errors else 0)

if __name__ == "__main__":
    main()
