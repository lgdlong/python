import math
import timeit

# Đoạn mã thứ nhất
code1 = '''
n = 9 
for i in range(1, n+1):
    for j in range(1, 2 * n + 1 - 1):
        if (n-i+1 <= j <= n+i-1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
'''

# Đoạn mã thứ hai
code2 = '''
n = 9
mid = math.ceil(n)
first = mid
last = mid
for i in range(1, n+1):
    for j in range(1, 2 * n + 1 - 1):
        if (first <= j <= last):
            print("*", end="")
        else:
            print(" ", end="")
    first -= 1
    last += 1
    print()
'''

# Đo thời gian thực thi của đoạn mã thứ nhất
time1 = timeit.timeit(code1, number=1000)

# Đo thời gian thực thi của đoạn mã thứ hai
time2 = timeit.timeit(code2, number=1000)

print("Thời gian thực thi của đoạn mã thứ nhất:", time1)
print("Thời gian thực thi của đoạn mã thứ hai:", time2)