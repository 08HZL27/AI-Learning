# 旋转 + 缩放 可视化：一眼看懂矩阵变换
import numpy as np
import matplotlib.pyplot as plt

# 一个正方形（5 个点，最后一个回到起点形成闭合图形）
square = np.array([
    [0, 1, 1, 0, 0],   # x 坐标
    [0, 0, 1, 1, 0],   # y 坐标
])

# 两条变换规则
R = np.array([[0, -1], [1,  0]])   # 旋转 90°（转角度）
S = np.array([[2, 0],  [0, 2]])    # 放大 2 倍（边长 ×2）

rotated = R @ square               # 只旋转
scaled  = S @ square               # 只放大
both    = (S @ R) @ square         # 旋转 + 放大（接力）

plt.figure(figsize=(7, 7))
plt.plot(square[0],  square[1],  'o-', label='原始正方形',  linewidth=2)
plt.plot(rotated[0], rotated[1], 's-', label='旋转90°',      linewidth=2)
plt.plot(scaled[0],  scaled[1],  'd-', label='放大2倍',      linewidth=2)
plt.plot(both[0],    both[1],    '^-', label='旋转+放大',    linewidth=2)
plt.axhline(0, color='gray', linewidth=0.8)
plt.axvline(0, color='gray', linewidth=0.8)
plt.grid(alpha=0.3)
plt.axis('equal')
plt.legend(loc='best')
plt.title('矩阵变换：同一个正方形被旋转、被放大')
plt.savefig(r'C:\Users\hzl\AI-Learning\02-data-science\matrix_transform.png', dpi=120)
print("✅ 图片已保存: 02-data-science/matrix_transform.png")
