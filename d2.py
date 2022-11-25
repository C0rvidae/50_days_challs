def convert_add(str_list: list) -> int:
    return sum([int(n) for n in str_list])


def check_duplicates(potential_dupes: list) -> list:
    dupes_set, dupes = set(potential_dupes), []
    if len(potential_dupes) == len(dupes_set):
        print("No duplicates")
    else:
        dupes = [dupe for dupe in dupes_set if potential_dupes.count(dupe) > 1]
    return dupes


def main() -> int:
    print("Convert Add")
    print(f"Intended : 9 | {convert_add(['1', '3', '5'])}")
    print(f"Intended : 55 | {convert_add(['10', '20', '25'])}")
    print("Duplicate Names")
    print(f"Intended: ['apple'] | {check_duplicates(['apple', 'orange', 'banana', 'apple'])}")
    print(f"Intended: No duplicates | {check_duplicates(['Yoda', 'Moses', 'Joshua', 'Mark'])}")
    return 0


if __name__ == '__main__':
    main()