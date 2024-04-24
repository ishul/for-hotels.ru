def func(l: list) -> list:
    res = []
    for i in range(2, min(l)+1):
        detect = True
        for elem in list(map(int, l)):
            if elem % i != 0:
                detect = False
        if detect:
            res.append(i)

    return res

print(func([4, 6]))