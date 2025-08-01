N = int(input())
array = []
for _ in range(N) :
    array.append(int(input()))

for j in range (len(array)-1) :
    for i in range ((len(array)-1) - j) :
        if array[i] > array[i+1] :
            temp = array [i]
            array[i] = array[i+1]
            array[i+1] = temp
            
for i in range (N) :
    print(array[i])