n = int(input())

def sum_factorials(n):
    run_sum, total_sum = 1, 0
    for i in xrange(n):
        run_sum *= (i+1)
        total_sum += run_sum
    return total_sum

print sum_factorials(n)