from math import pow, sqrt

a = int(input())
b = int(input())

if a > 0 and b > 0 and a <= 1000 and b <= 1000:
    print(sqrt(pow(a, 2) + pow(b, 2)))