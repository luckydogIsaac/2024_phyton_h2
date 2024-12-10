scores = []

print("請輸入10名學生的成績：")
for i in range(10):
    score = float(input(f"第 {i + 1} 名學生的成績："))
    scores.append(score)

highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)

print("最高分：", highest_score)
print("最低分：", lowest_score)
print("平均分：", average_score)
