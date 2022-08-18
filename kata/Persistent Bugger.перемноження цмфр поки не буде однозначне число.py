def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count
#або

def persistence(n):
    if n < 10:
        return 0
    n_str = str(n)
    res = 1
    for i in n_str:
            res *= int(i)
    return 1 + persistence(res)