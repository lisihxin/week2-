# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:47:23 2024

@author: student
"""try:
    # 讓使用者輸入一個整數
    user_input = input("請輸入一個整數：")

    # 轉換輸入為整數
    user_number = int(user_input)

    # 判斷是否為偶數
    if user_number % 2 == 0:
        print(f"{user_number} 是偶數。")
    else:
        print(f"{user_number} 不是偶數。")

except ValueError:
    # 處理轉換失敗的異常
    print("請輸入有效的整數。")

except Exception as e:
    # 處理其他異常
    print(f"發生了一個錯誤：{e}")


