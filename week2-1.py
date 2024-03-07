# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def calculate_circle_properties(radius):
    # 計算圓周長
    circumference = 2 * math.pi * radius
\

    # 計算圓面積
    area = math.pi * radius**2

    return circumference, area

# 使用者輸入半徑
radius_input = float(input("請輸入圓的半徑："))

# 計算圓周長與圓面積
circumference_result, area_result = calculate_circle_properties(radius_input)

# 輸出結果
print(f"圓周長：{circumference_result:.2f}")
print(f"圓面積：{area_result:.2f}")

