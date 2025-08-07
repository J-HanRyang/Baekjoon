N = int(input())
is_group = True
cnt = 0

for i in range (N) :
    S = input()
    l = []

    for j in range(1, len(S)) :
        if S[j] in l :
            is_group = False
        else :            
            if S[j] != S[j-1] :
                l.append(S[j-1])

    if is_group :
        cnt += 1
    else :
        is_group = True
        
print(cnt)