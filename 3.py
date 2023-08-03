# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

FIB_SET = (3, 6, 8, 10, 12, 14)


def fib_gen(n: int) -> list[int]:
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    for n in FIB_SET:
        print(*fib_gen(n))


if __name__ == "__main__":
    main()