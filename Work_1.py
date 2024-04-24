def func(n: int) -> str:
    if n % 10 == 1 and n != 11:
        return f"{n} компьютер"
    elif n % 10 == 2 and n != 12:
        return f"{n} копьютера"
    else:
        return f"{n} компьютеров"


print(func(1))
print(func(2))
print(func(7))
print(func(11))
print(func(12))
print(func(16))
print(func(54))
print(func(101))
