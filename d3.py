def register_check(register: dict) -> int:
    return sum([1 for x in register.values() if x == 'yes'])


def lowercase_names(names: list[str]) -> tuple:
    return tuple(sorted([name for name in names if name.islower()]))


def main() -> int:
    print("register_check()")
    print(f"Intended : 3 | {register_check({'Michael':'yes','John': 'no', 'Peter':'yes', 'Mary': 'yes'})}")
    print(f"Intended : 0 | {register_check({'Michael':'no','John': 'no', 'Peter':'no', 'Mary': 'no'})}")
    print("lowercase_names()")
    print(f"Intended: ('adam', 'carol', 'dickson', 'kerry') | "
          f"{lowercase_names(['kerry', 'dickson', 'John', 'Mary', 'carol', 'Rose', 'adam'])}")
    print(f"Intended: ('ahmed', 'aryan', 'jasper') | "
          f"{lowercase_names(['jasper', 'Solis', 'eMmy', 'aryan', 'ahmed'])}")
    return 0


if __name__ == '__main__':
    main()