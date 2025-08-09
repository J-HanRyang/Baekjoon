A, B, V = map(int, input().split())

if A >= V :
    print(1)
else :
    days = (V - A) // (A - B) + 1
    if (V - A) % (A - B) != 0 :
        days += 1
    print(days)