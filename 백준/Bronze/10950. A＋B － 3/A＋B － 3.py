T = int(input())
temp = []

for i in range (T) :
    A, B = map(int, input().split())
    temp.append(A+B)

for i in range (T) :
    print(temp[i])