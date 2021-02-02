import sys
from itertools import combinations

N = int(sys.stdin.readline())
player = [i for i in range(N)]
stats = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

start = []
link = []
sum_stats_lst = []
sum_stats_lst_link = []
div = []
for i in list(combinations(player, int(N/2))):
    start.append(i)
for i in range(int(len(start)/2)):
    link.append(start.pop())
for i in range(len(start)):
    sum_stats = 0
    for j in range(int(N/2)):
        for k in range(int(N/2)):
            sum_stats += stats[start[i][j]][start[i][k]]
    sum_stats_lst.append(sum_stats)
for i in range(len(link)):
    sum_stats = 0
    for j in range(int(N/2)):
        for k in range(int(N/2)):
            sum_stats += stats[link[i][j]][link[i][k]]
    sum_stats_lst_link.append(sum_stats)
for i in range(len(sum_stats_lst)):
    div.append(abs(sum_stats_lst[i] - sum_stats_lst_link[i]))
# print(start)
# print(link)
# print(sum_stats_lst)
# print(sum_stats_lst_link)
# print(div)
print(min(div))

# a = [1,2,3,4,5,6]
# b = []
# for i in list(combinations(a, 3)):
#     b.append(i)
# print(b)
