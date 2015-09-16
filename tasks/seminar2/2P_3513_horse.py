row1 = int(input())
col1 = int(input())
row2 = int(input())
col2 = int(input())

horse_steps = [(-2, 1), (-1, 2), (1, 2), (2, 1),
               (2, -1), (1, -2), (-1, -2), (-2, -1)]

if (row2 - row1, col2 - col1) in horse_steps:
    print("YES")
else:
    print("NO")