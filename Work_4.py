def func(n:int) -> list:
    res = []
    r = range(1, n+1)
    for i in r:
        res.append([elem * i for elem in r])
    print(' ', end='\t')
    print(*r, sep='\t')
    for j in res:
        print(res.index(j)+1, end='\t')
        print(*j, sep='\t')

func(5)
