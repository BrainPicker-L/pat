#读入一个正整数 n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

list1 = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
n = input()
n = list(n)
n = list(map(int, n))
sum = 0
for i in n:
    sum = sum + i

sum = str(sum)
for j in sum:
    if sum.index(j)+1 != len(sum):
        print(list1[int(j)], end=' ')
    else:
        print(list1[int(j)],end='')