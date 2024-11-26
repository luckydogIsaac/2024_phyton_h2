# 初始化計數器
positive_count = 0
negative_count = 0
zero_count = 0

# 從鍵盤輸入5個整數
print("請輸入5個整數：")
for i in range(5):
    num = int(input(f"輸入第 {i+1} 個數字: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

# 輸出結果
print(f"正數的個數: {positive_count}")
print(f"負數的個數: {negative_count}")
print(f"零的個數: {zero_count}")
