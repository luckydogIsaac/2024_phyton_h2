def calculate_average(grades):
    total = sum(grades)
    count = len(grades)
    average = total / count
    return average

式
if __name__ == "__main__":

    grades = []
    for i in range(5):
        grade = float(input(f"輸入第 {i+1} 個學生的成績: "))
        grades.append(grade)
    

    average = calculate_average(grades)
    
    
    print(f"這5個學生的平均成績是: {average:.2f}")
