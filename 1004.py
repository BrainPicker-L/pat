#读入 n（>0）名学生的姓名、学号、成绩，分别输出成绩最高和成绩最低学生的姓名和学号。

n = int(input())
info_list = []
low_grade = 100
high_grade = 0
for i in range(n):
    info = input().split(' ')
    info_list.append(info)

for student in info_list:
    if low_grade>int(student[2]):
        low_grade = int(student[2])
        low_pos = info_list.index(student)
    if high_grade<int(student[2]):
        high_grade = int(student[2])
        high_pos = info_list.index(student)

print(info_list[high_pos][0], info_list[high_pos][1])
print(info_list[low_pos][0], info_list[low_pos][1])