numbers = []

print("請輸入10個數字：")
for i in range(10):
    num = float(input(f"輸入第 {i+1} 個數字: "))
    numbers.append(num)


average = sum(numbers) / len(numbers)

print(f"這10個數字的平均值是: {average}")
