a = int(input())
b = int(input())
c = int(input())

d = max(a, b, c)

print("YES" if a + b + c > 2 * d else "NO")