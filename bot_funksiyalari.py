def faktorial(x) -> None:
    x = int(x)
    result = 1
    for i in range(1, x+1):
        result = result * i

    return result


# print(faktorial(1000000000))