def validate_and_assign_grade(mark):
    try:
        mark = float(mark)
        if mark < 0 or mark > 100:
            return "Invalid mark. Must be between 0 and 100."
    except ValueError:
        return "Invalid input. Please enter a numeric value."
    if mark >= 90:
        grade = 'A'
    elif mark >= 80:
        grade = 'B'
    elif mark >= 70:
        grade = 'C'
    elif mark >= 60:
        grade = 'D'
    elif mark >= 50:
        grade = 'E'
    else:
        grade = 'F'
    return f"The grade for the mark {mark} is: {grade}"
test_marks = ["95", "85", "75", "65", "55", "45", "invalid", "110", "-10"]

for mark in test_marks:
    result = validate_and_assign_grade(mark)
    print(result)

