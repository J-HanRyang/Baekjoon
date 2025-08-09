X = int(input())

line = 1
cnt = 0

while X > cnt + line:
    cnt += line
    line += 1

diff = X - cnt

if line % 2 == 0 :
    print(f"{diff}/{line-diff+1}")
else :
    print(f"{line-diff+1}/{diff}")