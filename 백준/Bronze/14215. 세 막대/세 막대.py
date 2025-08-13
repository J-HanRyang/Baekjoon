x = list(map(int, input().split()))

if max(x) < (sum(x) - max(x)) :
    print(sum(x))
else :
    x[x.index(max(x))] = (sum(x)-max(x))-1
    print(sum(x))