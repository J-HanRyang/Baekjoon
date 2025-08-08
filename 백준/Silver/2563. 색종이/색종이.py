N = int(input())
white = [[0]*100 for _ in range(100)]

for i in range (N) :
    black = list(map(int, input().split()))
    for j in range (10) :
        for k in range (10) :
            white[black[0]+j][black[1]+k] = 1

total = sum(sum(row) for row in white)
print(total)