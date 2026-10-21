# 骨灰盒.cn · 殡葬资讯与骨灰盒选购指南

中文域名：骨灰盒.cn（punycode：xn--0nx29kk17a.cn）
仓库：https://github.com/mfujun2025/guhuihe

## 站点简介
殡葬行业资讯站，提供殡葬政策法规、节地生态安葬、骨灰盒材质选购与价格参考等实用信息。

## 站点结构
- `index.html` — 首页（头条、政策速览、材质速览、资讯列表）
- `news/` — 资讯文章目录
- `sitemap.xml` — 站点地图
- `robots.txt` — 爬虫协议
- `404.html` — 404 页面
- `CNAME` — 自定义域名（骨灰盒.cn）
- `.github/workflows/deploy.yml` — GitHub Pages 自动部署

## 部署
推送到 main 分支后，GitHub Actions 自动构建并部署到 GitHub Pages。
域名解析：CNAME 记录指向 `mfujun2025.github.io`（按仓库 Pages 提示的地址）。

## 更新文章流程
1. 在 `news/` 下新建文章 HTML（参考现有文章模板）；
2. 更新 `index.html` 资讯列表（置顶新文章）；
3. 更新 `sitemap.xml`（新增 URL）；
4. 提交推送，等待 Actions 部署完成后验证。

## 联系方式
mfujun@agent.qq.com
