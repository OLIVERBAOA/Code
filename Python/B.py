a, b = map(int, raw_input().split())
ans = 0
for i in range(2, 61, 1):
    for j in range(0, i - 1, 1):
        t = ((1L << i) - 1) ^ (1L << j)
        if a <= t and t <= b:
            ans += 1
print ans
