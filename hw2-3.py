positive_count = 0
negative_count = 0
zero_count = 0


print("請輸入10個整數：")
for i in range(10):
    num = int(input(f"輸入第 {i+1} 個數字: "))
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1


print(f"正數的個數: {positive_count}")
print(f"負數的個數: {negative_count}")
print(f"零的個數: {zero_count}")
