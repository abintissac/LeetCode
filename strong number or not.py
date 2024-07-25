def factorial_number(number):
    if number < 0:
        return 0  # Factorial is not defined for negative numbers
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial_number(number - 1)


def split_number(number):
    num = str(number)
    facto_sum = 0
    for i in num:
        digit = int(i)
        facto = factorial_number(digit)
        facto_sum += facto

    print(f"Sum of factorials of digits: {facto_sum}")
    if number == facto_sum:
        print(f"{number} is a strong number.")
    else:
        print(f"{number} is not a strong number.")


n = int(input("Enter a number: "))
split_number(n)
