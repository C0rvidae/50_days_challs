def func1() -> int:
    return 1


def func2() -> int:
    return 2


def main() -> int:
    print("func1()")
    print(f"Intended:  | Result: {func1()}")
    print(f"Intended:  | Result: {func1()}")
    print("func2()")
    print(f"Intended:  | Result: {func2()}")
    print(f"Intended:  | Result: {func2()}")
    return 0


if __name__ == '__main__':
    main()