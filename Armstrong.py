def is_Armstrong(number):
    original_number = number
    armstrong_number = 0

    while number > 0:
        remainder = number % 10
        armstrong_number += (remainder * remainder * remainder)
        number = number // 10

    if original_number == armstrong_number:
        return True
    else:
        return False


number = int(input("Enter the number : "))

if is_Armstrong(number):
    print(number, "is armstrong number")
else:
    print(number, "is not armstrong number")
