# 🤖 AI-Learning

> **山东理工大学 2026 级人工智能专业 · 开学前冲刺仓库（2026.8）**
> 从零构建 AI 知识体系：数学 → 机器学习 → 深度学习

---

## 📦 项目清单

### 1. 📁 文件批量整理器 — `01-python-scripts/organize_files.py`
按扩展名自动归类文件（jpg → jpg/，pdf → pdf/，无扩展名 → others/）
- 技术：`os` / `shutil`
- 状态：✅ 已完成

### 2. 🌦️ 淄博天气爬虫 — `01-python-scripts/crawl_weather.py`
实时抓取淄博天气页面，解析并输出今日天气/温度/风力
- 技术：`requests` / `BeautifulSoup`（含 User-Agent 伪装、编码处理、超时保护）
- 状态：✅ 已完成

### 3. 🏠 房价预测（进行中）— `03-ml-project/house_price/`
线性回归预测——AI 最小完整闭环（数据 → 模型 → 评估 → 可视化）
- 技术：`numpy` / `sklearn` / `matplotlib`
- 当前：v1 参考实现已跑通（diabetes 数据集单特征基线）
- 待办：亲手实现 v2（多特征 + 完整评估）

### 4. 📝 数据科学练习 — `02-data-science/`
numpy / 矩阵 / 梯度直觉 / 无穷小 的学习练习与可视化

---

## 🛠️ 技术栈

`Python` · `numpy` · `pandas` · `matplotlib` · `requests` · `BeautifulSoup` · `sklearn` · `Git/GitHub`

---

## 📚 学习路线

```
高数（同济八版 Ch1-4 预习）→ 线性代数 → 机器学习 → 深度学习 → LLM
```

## 📅 进度

- [x] Python 语法基础（变量/循环/函数/列表/字典/文件）
- [x] 文件整理实战（30 行脚本，核心逻辑自己写）
- [x] 爬虫实战（AI 辅助理思路，4 轮报错自己排查）
- [x] Git/GitHub 全流程
- [x] 矩阵乘法 / 梯度直觉
- [ ] 数据三件套（numpy / pandas / matplotlib）
- [ ] 房价预测 v2（亲手实现）
- [ ] Titanic 入门赛
