t = []

while True :
    t = list(map(int, input().split()))
    if sum(t) == 0 :
        break
    elif max(t) >= (sum(t)-max(t)) :
        print("Invalid")
    elif len(set(t)) == 1 :
        print("Equilateral")
    elif len(set(t)) == 2 :
        print("Isosceles")
    else :
        print("Scalene")