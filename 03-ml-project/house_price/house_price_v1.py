# -*- coding: utf-8 -*-
"""
房价预测项目 v1 —— 单特征线性回归（基线版）
目标：跑通「数据 → 模型 → 评估 → 可视化」最小闭环
数据集：sklearn 内置 diabetes（糖尿病指标，10 个特征）
今日进度：冲刺计划 8/24 跑通基线 + 8/25 评估
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ========== 1. 加载数据 ==========
diabetes = datasets.load_diabetes()
X = diabetes.data      # 10 个特征
y = diabetes.target    # 目标：血糖指标
print("数据形状:", X.shape, "| 特征:", diabetes.feature_names)

# ========== 2. 先只用一个特征：bmi（身体质量指数）==========
X_bmi = X[:, 2].reshape(-1, 1)   # bmi 是第 3 个特征（索引 2）
print("单特征形状:", X_bmi.shape)

# ========== 3. 训练：找一条线 y = w*x + b ==========
model = LinearRegression()
model.fit(X_bmi, y)
w = model.coef_[0]
b = model.intercept_
print(f"\n拟合结果: y = {w:.2f} * bmi + {b:.2f}")

# ========== 4. 评估：这条线准不准 ==========
y_pred = model.predict(X_bmi)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE（均方误差）: {mse:.2f}")
print(f"R²  (决定系数):  {r2:.4f}")

# ========== 5. 画图：数据云 + 拟合线 ==========
plt.figure(figsize=(8, 5))
plt.scatter(X_bmi, y, alpha=0.5, s=25, label="真实数据")
x_line = np.linspace(X_bmi.min(), X_bmi.max(), 100)
plt.plot(x_line, model.predict(x_line.reshape(-1, 1)),
         color="red", lw=2.5, label="拟合直线")
plt.xlabel("bmi（标准化后）")
plt.ylabel("血糖指标 y")
plt.title(f"diabetes 单特征线性回归  |  y = {w:.2f}x + {b:.2f}  |  R² = {r2:.4f}")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("v1_bmi_fit.png", dpi=120)
print("\n✅ 图已保存: v1_bmi_fit.png")
