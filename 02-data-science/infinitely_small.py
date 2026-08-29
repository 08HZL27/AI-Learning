# 验证：每个"固定位置"的因子都是无穷小，但 k 个相乘恒等于 1
for k in [2, 3, 5, 10, 20, 30]:
    prod = 1.0
    for n in range(1, k):          # 前 k-1 个因子：2^{-k}
        prod *= 2 ** (-k)
    prod *= 2 ** (k * (k - 1))     # 第 k 个因子：2^{k(k-1)}
    print(f"k = {k:3d} → 乘积 = {prod}")
