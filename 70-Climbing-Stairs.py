def climbStairs(n: int) -> int:
    if n == 1 or n == 2:
        return n
    a = []
    b = 1
    for i in range(n+1):
        if i >= 2:
            b = a[i - 1] + a[i - 2]
        a.append(b)
    return b


print(climbStairs(123231))
