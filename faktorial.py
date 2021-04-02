def faktorial(n):
    n = 5
    c = 0
    for i in range(1, n):
        c = n * i
        n = c
    return c
# print(faktorial(6))