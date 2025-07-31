H, M = map(int, input().split())
time_cook = int(input())
time_M = M + time_cook

H += time_M // 60
M = time_M % 60

if (H > 23) :
    H %= 24
    
print(H, M)