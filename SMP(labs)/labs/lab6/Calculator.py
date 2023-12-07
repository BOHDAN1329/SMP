import math
import re


def add(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 + num2
    else:
        raise TypeError("Both arguments must be numerics")


def subtract(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 - num2
    else:
        raise TypeError("Both arguments must be numerics")


def multiply(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 * num2
    else:
        raise TypeError("Both arguments must be numerics")


def divide(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num2 == 0:
            raise ZeroDivisionError("Impossible to divide")
        return num1 / num2
    else:
        raise TypeError("Both arguments must be numerics")


def raise_to_a_power(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        return num1 ** num2
    else:
        raise TypeError("Both arguments must be numerics")


def compute_square_root(num):
    if isinstance(num, (int, float)):
        if num < 0:
            raise ArithmeticError("Number is negative, therefore it is impossible to  calculate the square root")
        return math.sqrt(num)
    else:
        raise TypeError("Both arguments must be numerics")


def divide_by_modulo(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):

        return num1 % num2
    elif num2 == 0:
        raise ZeroDivisionError("Impossible to divide")
    else:
        raise TypeError("Both arguments must be numerics")


def view_history():
    if not history_of_calculations:
        print("There is nothing in history")
    else:
        print("History of results:")
        for i in history_of_calculations:
            for j in i:
                if isinstance(j, float):
                    print(("{:." + str(decimal_places) + "f}").format(float(j)) + " ", end="")
                else:
                    print(str(j) + " ", end="")
            print()


def view_settings():
    print("\tSettings:")
    print("\tDecimal places are " + str(decimal_places))


def change_decimal_places(value):
    if value <= 0:
        raise ArithmeticError("Decimal digits can't be negative or 0")
    global decimal_places
    decimal_places = value


history_of_calculations = []
decimal_places = 2


def main():
    global history_of_calculations
    global decimal_places
    operand: str = ""
    result: float = 0.0

    while True:
        print("Options: ")
        print("1. Add numbers")
        print("2. Subtract numbers")
        print("3. multiply numbers")
        print("4. Divide numbers")
        print("5. Raise to a power")
        print("6. Divide by modulo")
        print("7. Compute the square root")
        print("8. View history")
        print("9. Open settings")
        print("0. Exit")

        input_value = input("Your option is ")

        if re.match("^[lab1-6]$", input_value):
            first_number = float(input("Enter first number: "))
            second_number = float(input("Enter second number: "))

            try:
                match input_value:
                    case "1":
                        operand = "+"
                        result = add(first_number, second_number)
                    case "2":
                        operand = "-"
                        result = subtract(first_number, second_number)
                    case "3":
                        operand = "*"
                        result = multiply(first_number, second_number)
                    case "4":
                        operand = "/"
                        result = divide(first_number, second_number)
                    case "5":
                        operand = "**"
                        result = raise_to_a_power(first_number, second_number)
                    case "6":
                        operand = "%"
                        result = divide_by_modulo(first_number, second_number)

                history_of_calculations.append([(first_number, operand, second_number, "=", result)])
                print("Result is " + (("{:." + str(decimal_places) + "f}").format(float(result)) + "\n"))
            except ZeroDivisionError as e:
                print(str(e) + "\n")
        elif input_value == "7":
            try:
                number = float(input("Enter number: "))
                result = compute_square_root(number)

                history_of_calculations += [("√", number, "=", result)]
                print("Result is " + (("{:." + str(decimal_places) + "f}").format(float(result)) + "\n"))
            except ArithmeticError as e:
                print(str(e) + "\n")
        elif input_value == "8":
            view_history()
            print()
        elif input_value == "9":
            while True:
                print("\tSettings options:")
                print("\tlab1. View settings")
                print("\tlab2. Change decimal places")
                print("\tlab3. Clean all records")
                print("\t0. Exit from the settings mode")

                inner_input_value = str(input("\tYour option is "))

                if inner_input_value == "lab1":
                    view_settings()
                    print()
                elif inner_input_value == "lab2":
                    new_value = int(input("\tEnter a new value for decimal places: "))

                    try:
                        change_decimal_places(new_value)
                        print()
                    except ArithmeticError as e:
                        print("\t" + str(e) + "\n")
                elif inner_input_value == "lab3":
                    history_of_calculations.clear()
                    print()
                elif inner_input_value == "0":
                    print()
                    break
                else:
                    print("\tYou have just entered a wrong option\n")
        elif input_value == "0":
            break
        else:
            print("You have just entered a wrong option\n")


if __name__ == "__main__":
    main()