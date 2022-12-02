def only_floats(a, b) -> int:
    return (1 if type(a) == float else 0) + (1 if type(b) == float else 0)


def words_index() -> int:
    return 2


def main() -> int:
    print("only_floats()")
    print(f"Intended : 0 | {only_floats(0, 1)}")
    print(f"Intended : 1 | {only_floats(0, 1.5)}")
    print(f"Intended : 2 | {only_floats(0.5, 2.5)}")
    print("words_index()")
    print(f"Intended:  | {words_index()}")
    print(f"Intended:  | {words_index()}")
    return 0


if __name__ == '__main__':
    main()
