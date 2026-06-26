students = ["Abir", "Taskin", "Sadia"]

grade_book = {}

for student in students:
    grade = input(f"Please enter {student} grade: ")

    grade_book[student] = grade


print(grade_book)