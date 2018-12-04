#让我们用字母 B 来表示“百”、字母 S 表示“十”，用 12...n 来表示不为零的个位数字 n（<10），换个格式来输出任一个不超过 3 位的正整数。例如 234 应该被输出为 BBSSS1234，因为它有 2 个“百”、3 个“十”、以及个位的 4。
n = input()
len_n = len(n)
str1 = '123456789'
if len_n == 3:
    for i in range(int(n[0])):
        print('B', end='')
    for i in range(int(n[1])):
        print('S', end='')
    for i in range(int(n[2])):
        print(str1[i], end='')
elif len_n == 2:
    for i in range(int(n[0])):
        print('S', end='')
    for i in range(int(n[1])):
        print(str1[i], end='')
else:
    for i in range(int(n[0])):
        print(str1[i], end='')
