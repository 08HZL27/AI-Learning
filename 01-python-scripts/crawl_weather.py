# -*- coding: utf-8 -*-
"""
淄博天气爬虫 —— 抓取中国天气网，提取当天天气/温度/风力

功能：请求淄博天气页面 -> 解析 HTML -> 提取"今天"的天气、温度、风力并打印
用到的库：requests（发请求）、BeautifulSoup（解析 HTML）

调试过程中踩过的坑（真实经历）：
  1. 第一次请求没带 User-Agent，被网站拒绝 -> 加上请求头伪装浏览器
  2. 出现 NoneType 报错 -> find() 没找到元素，说明定位写错了
  3. 把 class_="tem" 拼成了 "tam" -> 拼写错误导致找不到元素
  4. 风力定位写成 find("win") -> win 是 class 名不是标签，应为 find("i")
  5. 页面结构会变：白天显示"高温/低温"，夜间只显示当前温度
     -> 加容错判断，两种结构都能处理

作者：黄XX | 2026.8
"""
import requests
from bs4 import BeautifulSoup

url = "https://www.weather.com.cn/weather/101120301.shtml"   # 101120301 = 淄博
headers = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36")
}

# ---------- ① 发请求拿页面 ----------
resp = requests.get(url, headers=headers, timeout=10)
resp.encoding = "utf-8"          # 防止中文乱码
html = resp.text

# ---------- ② 解析 HTML ----------
soup = BeautifulSoup(html, "html.parser")
today = soup.find("li", class_="sky")     # 第一个 sky 标签 = 今天

# ---------- ③ 提取数据 ----------
wea = today.find("p", class_="wea").text            # 天气（如"晴"）

# 温度：兼容两种页面结构
tem_p = today.find("p", class_="tem")               # 温度盒子
span = tem_p.find("span")                           # 白天：<span>高温</span>
i_tag = tem_p.find("i")                             # 低温 / 当前温度
if span:
    tem_str = f"{span.text}℃/{i_tag.text}"          # 白天：33℃/25℃
else:
    tem_str = i_tag.text                            # 夜间：15℃

wind = today.find("p", class_="win").find("i").text  # 风力

# ---------- ④ 输出 ----------
print(f"今天：{wea} | {tem_str} | {wind}")
