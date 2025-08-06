S = input().upper()
cnt = [0]*26

for char in S :
    cnt[ord(char) - ord("A")] += 1

if (cnt.count(max(cnt))) > 1 :
    print("?")
else :
    print(chr(ord("A") + cnt.index(max(cnt))))