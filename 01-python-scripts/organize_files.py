# -*- coding: utf-8 -*-
"""
文件批量整理器 —— 按扩展名把文件归类到子文件夹

功能：扫描指定文件夹中的所有文件，按扩展名移动到对应子文件夹
      例如 照片1.jpg -> jpg/照片1.jpg ；无扩展名的文件 -> others/
用到的库：os（路径/遍历/建目录）、shutil（移动文件）

作者：黄XX | 2026.8
"""
import os
import shutil

# 待整理的文件夹（可改成任意路径，测试时建议先备份）
folder = r"C:\Users\hzl\AI-Learning\01-python-scripts\test_folder"

count = 0                                  # 统计移动了多少个文件

for name in os.listdir(folder):            # ① 列出文件夹里所有名字
    full = os.path.join(folder, name)      # ② 拼出完整路径
    if os.path.isfile(full):               # ③ 只处理文件（跳过子文件夹）
        ext = os.path.splitext(name)[1]    # ④ 拆出扩展名，如 ".jpg"
        if ext:
            target = ext[1:]               # ⑤ 去掉点号 -> "jpg"
        else:
            target = "others"              # ⑥ 没有扩展名 -> others
        os.makedirs(os.path.join(folder, target), exist_ok=True)  # ⑦ 建目录（存在也不报错）
        print(name, "→", target)
        count += 1
        shutil.move(full, os.path.join(folder, target, name))     # ⑧ 移动文件

print("整理完成，共移动", count, "个文件")
