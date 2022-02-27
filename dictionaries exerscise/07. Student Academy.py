n = int(input())
student_grades = dict()
counter = dict()
for i in range(n):
    name = input()
    grade = float(input())
    if name not in student_grades:
        student_grades[name] = 0.0
    student_grades[name] += grade
    if name not in counter:
        counter[name] = 0
    counter[name] += 1
avg_student_grades = {name: student_grades[name]/counter[name] for name in student_grades and counter}
filtered = {name: avg_student_grades[name] for name in avg_student_grades if avg_student_grades[name] >= 4.5}
ordered = dict(sorted(filtered.items(), key=lambda x: (-x[1], x[0])))
for name, grade in ordered.items():
    print(f'{name} -> {grade:.2f}')
