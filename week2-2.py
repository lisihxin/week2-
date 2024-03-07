# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:46:55 2024

@author: student
"""

# 收集用戶個人資料
user_name = input("請輸入您的姓名：")
user_age = int(input("請輸入您的年齡："))
user_height = float(input("請輸入您的身高（米）："))
favorite_color = input("請輸入您喜愛的顏色：")

# 將資料存儲在字典中
user_data = {
    '姓名': user_name,
    '年齡': user_age,
    '身高': user_height,
    '喜愛的顏色': favorite_color
}

# 格式化個人資料摘要並輸出
summary = f"{user_data['姓名']}, {user_data['年齡']}歲, 身高{user_data['身高']}米, 喜愛的顏色是{user_data['喜愛的顏色']}。"
print(summary)
