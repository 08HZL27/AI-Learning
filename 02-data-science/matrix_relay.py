# 矩阵乘法 = 变换接力
# 验证：先旋转90°再缩放2倍 == 合成矩阵一步到位
import numpy as np

# 两条变换规则
R = np.array([[0, -1],   # 旋转 90°
              [1,  0]])
S = np.array([[2, 0],    # 缩放 2 倍
              [0, 2]])

p = np.array([1.0, 0.0])        # 测试点 (1, 0)

# --- 接力：一步一步来 ---
step1 = R @ p                   # 第 1 棒：旋转
step2 = S @ step1               # 第 2 棒：缩放

# --- 合成：直接乘 ---
M = S @ R                       # 合成矩阵（注意顺序：先 R 后 S）
direct = M @ p                  # 一步到位

print("点 p        =", p)
print("旋转后      =", step1, " <- (1,0) 转到 (0,1)")
print("再缩放后    =", step2)
print("合成一步    =", direct)
print("接力 == 合成:", np.allclose(step2, direct))

# --- 正方形四个顶点，看变换对形状做了什么 ---
square = np.array([[0, 1, 1, 0],   # 每列一个点
                   [0, 0, 1, 1]])
print("\n正方形顶点（每列一个点）:")
print(square)
print("\n旋转 90° 后:")
print(R @ square)
print("\n旋转 + 缩放后:")
print(M @ square)
