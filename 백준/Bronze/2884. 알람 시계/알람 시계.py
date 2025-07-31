H, M = map(int, input().split())
M -= 45

if M < 0:
    M += 60
    H = (H - 1) % 24

print(H, M)