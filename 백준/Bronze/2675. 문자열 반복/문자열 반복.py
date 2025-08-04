T = int(input())

for i in range (T) :
    R, S = map(str, input().split())
    for j in range (len(S)) :
        P = S[j] * int(R)
        print(P, end="")
    print()