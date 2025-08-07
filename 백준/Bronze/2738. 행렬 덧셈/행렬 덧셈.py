N, M = map(int, input().split())
A = []
B = []

for i in range (N) :
    row_a = list(map(int, input().split()))
    A.append(row_a)

for i in range (N) :
    row_b = list(map(int, input().split()))
    B.append(row_b)

for i in range (N) :
    for j in range (M) :
        print(A[i][j] + B[i][j], end=" ")
    print()