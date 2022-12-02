def my_discount() -> float:
    final_price: float = 0
    price: str = input("Provide price: ")
    discount: str = input("Provide discount: ")
    try:
        price_fl: float = float(price)
        discount_fl: float = float(discount)
        final_price = price_fl - price_fl * (discount_fl / 100)
        return final_price
    except ValueError:
        print("Please provide a number!")
    return final_price


def gender_stat(students: list) -> list:
    students_str: str = " ".join(students).lower()
    count_f = students_str.count('female')
    count_m = students_str.count('male') - count_f
    return [('male', count_m), ('female', count_f)]


def main() -> int:
    print("my_discount()")
    # print(f"Intended: ? | Result: {my_discount()}")
    # print(f"Intended: ? | Result: {my_discount()}")
    print("gender_stat()")
    students = ['Male', 'Female', 'female', 'male', 'male', 'male', 'female',
                'male', 'Female', 'Male', 'Female', 'Male', 'female']
    print(f"Intended: [('male', 7), ('female', 6)] | {gender_stat(students)}")
    # print(f"Intended:  | {gender_stat()}")
    return 0


if __name__ == '__main__':
    main()