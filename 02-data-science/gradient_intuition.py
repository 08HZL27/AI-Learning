# 梯度是什么？三张图看懂
# 函数：z = x² + y² （碗状，最低点在原点）
# 梯度：∇f = (2x, 2y) —— 指向"上升最快"的方向
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 梯度下降：从起点出发，每步沿"负梯度"（下山最快方向）走
def grad_descent(start, lr=0.15, steps=15):
    path = [start]
    x, y = start
    for _ in range(steps):
        x = x - lr * 2 * x    # 负梯度方向更新
        y = y - lr * 2 * y
        path.append((x, y))
    return np.array(path)

x = np.linspace(-2, 2, 40)
y = np.linspace(-2, 2, 40)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure(figsize=(16, 5.2))

# ---------- 图1：3D 碗 + 小球下山轨迹 ----------
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85)
path = grad_descent((1.5, 1.2), 0.15, 15)
zp = path[:, 0]**2 + path[:, 1]**2
ax1.plot(path[:, 0], path[:, 1], zp, 'r-o', lw=2, markersize=4)
ax1.scatter(path[0, 0], path[0, 1], zp[0], color='red', s=80, label='起点(高处)')
ax1.scatter(path[-1, 0], path[-1, 1], zp[-1], color='black', s=80, label='碗底(最低点)')
ax1.set_title('图1：小球下山\n沿最陡的方向一路滚到碗底')
ax1.legend()

# ---------- 图2：等高线 + 梯度箭头 ----------
ax2 = fig.add_subplot(1, 3, 2)
ax2.contour(X, Y, Z, levels=12, cmap='viridis')
for px, py in [(1.5, 0.5), (0.8, 1.2), (-1.2, 0.6), (-0.5, -1.4), (1.3, -0.9)]:
    gx, gy = 2 * px, 2 * py
    ax2.arrow(px, py, gx * 0.1, gy * 0.1, color='red', width=0.02, head_width=0.09)
    ax2.arrow(px, py, -gx * 0.1, -gy * 0.1, color='blue', width=0.02, head_width=0.09)
ax2.set_title('图2：等高线地形图\n红=梯度(上山) 蓝=负梯度(下山)\n箭头永远垂直等高线，越陡箭头越长')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.axis('equal')

# ---------- 图3：多个起点的梯度下降轨迹 ----------
ax3 = fig.add_subplot(1, 3, 3)
ax3.contour(X, Y, Z, levels=12, cmap='viridis')
for start in [(1.5, 1.2), (-1.6, 0.8), (0.3, -1.8)]:
    p = grad_descent(start, 0.15, 15)
    ax3.plot(p[:, 0], p[:, 1], 'o-', lw=1.5, markersize=3)
ax3.set_title('图3：从不同起点出发的梯度下降\n全部走到碗底——AI训练就是这样')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.axis('equal')

plt.tight_layout()
plt.savefig(r'C:\Users\hzl\AI-Learning\02-data-science\gradient_intuition.png', dpi=130)
print('✅ 图片已保存: 02-data-science/gradient_intuition.png')
