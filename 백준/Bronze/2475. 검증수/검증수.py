nums = list(map(int, input().split()))
total = sum(n**2 for n in nums)
print(total % 10)