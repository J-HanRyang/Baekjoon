N = int(input())

for _ in range (N) :
    cnt = 0
    num = 0
    s = list(input())
    for i in range (len(s)) :
        if i == 0 and s[i] == 'O' :
            cnt += 1
            num = 1
        elif s[i-1] == 'O' and s[i] == 'O' :
            num += 1
            cnt += num
        elif s[i] == 'O' :
            cnt += 1
            num = 1
        else :
            num = 0
    print(cnt)