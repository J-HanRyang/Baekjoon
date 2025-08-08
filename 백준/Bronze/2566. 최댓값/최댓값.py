a = []
b = []
for i in range (9) :
    a_2 = list(map(int, input().split()))
    a.append(a_2.index(max(a_2)))
    b.append(max(a_2))

print(max(b))
print(b.index(max(b))+1, end = " ")
print(a[b.index(max(b))] + 1)