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
4. 运行 `python _check.py`（结构自检）与 `python _seocheck.py`（SEO 元信息核验）；
5. 提交推送，等待 Actions 部署完成后验证线上 URL 与首页置顶。

## 已发布文章索引（截至 2026-11-12，共 36 篇）

### 政策法规（6 篇）
| 文件名 | 标题 |
|---|---|
| guhuihe-tiaoli-jiedu-2026 | 新《殡葬管理条例》2026年3月30日施行：8大要点一次看懂 |
| guhuihe-shoufei-guiding-2026 | 殡葬服务收费新规：清单之外不得收费，家属如何核对账单？ |
| guhuihe-shengtai-anzang-2026 | 海葬、树葬、花葬、草坪葬怎么选？各地奖补政策一览 |
| guhuihe-guojia-biaozhun-2026 | 骨灰盒有国家标准吗？新国标 GB/T 23288—2023 解读 |
| guhuihe-zidai-zhengce-2026 | 殡仪馆骨灰盒为什么贵？可以自带骨灰盒吗 |
| guhuihe-huimin-buzhu-2026 | 骨灰盒能报销吗？惠民殡葬补贴与减免政策 |

### 选购指南（15 篇）
| 文件名 | 标题 |
|---|---|
| guhuihe-zenme-xuan-2026 | 骨灰盒怎么选？材质、尺寸、密封与预算一篇讲清 |
| guhuihe-caizhi-xuangou-2026 | 木、石、玉、陶瓷……骨灰盒材质怎么选？一张表看懂 |
| guhuihe-hongmu-heitian-2026 | 红木还是黑檀？骨灰盒两种主流木材怎么选 |
| guhuihe-jiage-cankao-2026 | 骨灰盒一般多少钱？价格区间与选购避坑参考 |
| guhuihe-pinpai-xuangou-2026 | 骨灰盒哪个品牌好？厂家选购避坑指南 |
| guhuihe-wangshang-goumai-2026 | 网上买骨灰盒靠谱吗？线上购买渠道与避坑指南 |
| guhuihe-chicun-guige-2026 | 骨灰盒尺寸多大合适？标准规格与格位匹配指南 |
| guhuihe-shougong-jizhi-2026 | 骨灰盒手工雕刻和机制的区别？榫卯工艺怎么看 |
| guhuihe-kezi-2026 | 骨灰盒刻字怎么写？内容格式与常见讲究 |
| guhuihe-yanse-jiangjiu-2026 | 骨灰盒颜色有什么讲究？常见颜色寓意与选择参考 |
| guhuihe-cixiang-2026 | 骨灰盒瓷像是什么？遗像照片制作工艺与价格参考 |
| guhuihe-shuangren-hezang-2026 | 双人骨灰盒怎么选？夫妻合葬尺寸、流程与注意事项 |
| guhuihe-tiqian-goumai-2026 | 骨灰盒提前买可以吗？提前购买与存放注意事项 |
| guhuihe-mifengxing-2026 | 骨灰盒密封性怎么判断？内袋、封口与防潮内衬 |
| guhuihe-weiquan-2026 | 骨灰盒买到瑕疵怎么维权？退换、赔付与投诉渠道 |

### 常识知识（15 篇）
| 文件名 | 标题 |
|---|---|
| guhuihe-anfang-liucheng-2026 | 骨灰盒安放流程与封盒注意事项全指南 |
| guhuihe-zhuanggu-2026 | 骨灰怎么装进骨灰盒？装盒流程与注意事项 |
| guhuihe-baocun-nianxian-2026 | 骨灰盒能保存多久？存放年限与密封保养指南 |
| guhuihe-fangchao-2026 | 骨灰盒受潮怎么办？防潮处理方法与保养指南 |
| guhuihe-sunhuai-chuli-2026 | 骨灰盒碎了、开裂了怎么办？处理与更换指南 |
| guhuihe-jiating-baifang-2026 | 骨灰盒能放家里吗？家里摆放位置与注意事项 |
| guhuihe-suizang-pin-2026 | 骨灰盒随葬品放什么合适？能放与禁忌物品清单 |
| guhuihe-xiedai-jiaotong-2026 | 骨灰盒能带上飞机火车吗？跨省携带骨灰规定与流程 |
| guhuihe-kuaidi-jigu-2026 | 骨灰盒可以快递吗？快递寄骨灰的规定与流程 |
| guhuihe-tuoyun-2026 | 骨灰盒托运怎么办理？铁路、汽车托运骨灰规定与流程 |
| guhuihe-yidi-anzang-2026 | 异地安葬怎么办理？跨省迁葬手续与流程 |
| guhuihe-jicun-changshi-2026 | 骨灰寄存与安葬的实用常识：尺寸、保存与常见问题 |
| guhuihe-gewei-xuanze-2026 | 骨灰格位怎么选？位置、层数、朝向与价格怎么看 |
| guhuihe-jicun-daoqi-2026 | 骨灰寄存到期了怎么办？续费、逾期与迁出流程 |
| guhuihe-kejiiejie-2026 | 可降解骨灰盒是什么？环保骨灰盒材料与适用场景 |

### 后续可拓选题（未写过，供下次更新选用）
- 告别仪式流程与时间表：从报丧到答谢的完整节点
- 墓碑碑文怎么写：称谓、生卒、立碑人格式与禁忌
- 寒衣节、冬至祭扫：供品、流程与骨灰盒清洁
- 回族等少数民族安葬习俗与政策衔接
- 烈士、因公牺牲人员安葬礼仪与骨灰盒规范
- 遗像相框与灵位牌：尺寸、材质与摆放
- 骨灰纪念品（骨灰钻石、纪念瓷）市场与合规风险
- 殡仪馆服务项目逐项拆解：哪些必须买、哪些可以省
- 丧事费用总账怎么算：一份可对照的预算清单


## 联系方式
mfujun@agent.qq.com
