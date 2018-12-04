#现在给定一系列待验证的数字，我们只需要验证其中的几个关键数，就可以不必再重复验证余下的数字。你的任务就是找出这些关键数字，并按从大到小的顺序输出它们。

answer_list = []
longest_list = []
n = int(input())
find_list = input().split(' ')
find_list = list(map(int, find_list))
j_list = []
for i in find_list:
    j = i
    while True:

        if j == 1:
            break
        if j % 2 == 0:
            j = j / 2
        else:
            j = (3 * j + 1) / 2
        j_list.append(int(j))
j_list = list(set(j_list))
for i in find_list:
    if i not in j_list:
        answer_list.append(i)
answer_list = sorted(answer_list, reverse=True)
for i in answer_list:
    if answer_list.index(i) + 1 == len(answer_list):
        print(i, end='')
    else:
        print(i, end=' ')

'''find_list = input().split(' ')
find_list = list(map(int, find_list))
while True:
    n_list.append(n)
    if n == 1:
        break
    if n % 2 == 0:
        n = n/2
    else:
        n = (3*n + 1)/2

n_list = list(map(int, n_list))
print(n_list)
print(find_list)
print(list(set(n_list).intersection(set(find_list))))'''