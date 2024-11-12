try:
    marks = float(input("Please enter the marks (0-100): "))
    # Validate the marks are within a plausible range (0-100)
    if 0 <= marks <= 100:
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        print("Grade:", grade)
    else:
        print("Invalid marks. Please enter a value between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

