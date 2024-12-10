scores = []

print("請輸入10名學生的成績：")
for i in range(10):
    score = float(input(f"第 {i + 1} 名學生的成績："))
    scores.append(score)

scores.sort(reverse=True)

print("按成績從高到低的順序排列：")
for i, score in enumerate(scores, 1):
    print(f"第 {i} 名學生的成績：{score}")
