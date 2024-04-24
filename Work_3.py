def func(f:int, s:int) -> list:
    res = []
    for i in range(f, s+1):
        detect = True
        for d in range(2, round(i//2)):
            if i % d == 0:
                detect = False
        if detect:
            res.append(i)

    return res

print(func(11, 23))