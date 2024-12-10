array = []
print("請輸入5個整數：")
for i in range(5):
    num = int(input(f"第 {i + 1} 個整數："))
    array.append(num)

array.reverse()

print("逆序後的陣列:", array)
