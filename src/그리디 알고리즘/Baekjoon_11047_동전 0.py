N, Money = map(int, input().split())

lst = []
tmp = []
Num = 0


for i in range(N):
    tmp.append(int(input()))

for i in tmp:
    if i <= Money:
        lst.append(i)

while(Money != 0):
    coin = lst.pop()
    Num = Num + Money // coin
    Money %= coin

print(Num)
