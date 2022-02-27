n = int(input())
p = int(input())

cc = n
course_counter = 0
while cc > 0:
    cc -= p
    course_counter += 1
print(course_counter)
