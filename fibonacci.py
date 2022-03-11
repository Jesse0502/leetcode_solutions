def fib(num):
    a = []
    b = 1
    for i in range(num):
        if i >= 2:
            b = a[i - 1] + a[i - 2]
        a.append(b)
    return a

fib(7)
# 1, 1, 2, 3, 5, 8, 13
