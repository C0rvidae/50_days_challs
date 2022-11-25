import math


def divide_or_square(number: int) -> int:
    return math.sqrt(number) if not number % 5 else number % 5


def longest_value(values_dict: dict) -> str:
    return str(max(values_dict.values(), key=len))


def main() -> int:
    print("Divide or Square")
    print(f"Intended : 4 | {divide_or_square(4)}")
    print(f"Intended : 3.16 | {divide_or_square(10)}")
    print("Longest Value")
    print(f"Intended: apple | {longest_value({'fruit': 'apple', 'color': 'green'})}")
    print(f"Intended: abcd | {longest_value({'a': 'abcd', 'b': 'a', 'c': 'dcba'})}")
    return 0


if __name__ == '__main__':
    main()
