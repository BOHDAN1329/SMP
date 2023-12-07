import math

def check_operator(operator):
    valid_operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
    if operator not in valid_operators:
       return False
    return True

def calculate(num1, operator, num2):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:
                raise ValueError("Division by zero is not allowed!")
        elif operator == '^':
            return num1 ** num2
        elif operator == 'sqrt':
            return num1 ** (1 / num2)
        elif operator == '%':
            return num1 % num2
    except Exception as e:
        print("Division by zero is not allowed!")
        return -1

memory = 0

def save_to_memory(result):
    global memory
    memory = result

history = []

def add_to_history(expression):
    history.append((expression))

def display_history():
    try:
        print("Calculation History:")
        if len(history) < 1:
            raise Exception
        else:
            print(history)
    except Exception as e:
        print("\n\nHistory is empty")


# Main Calculator Loop
global result
def main():
    isFirstStart = True
    result = 0
    decNum = 2
    while True:
        print("\nMenu:")
        print("1: Start Calculate")
        print("2: See History")
        print("3: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            num1, operator, num2 = get_user_input()
            if isFirstStart == False and input("use previous result?(yes/no)") == 'yes':
                num1 = result

            decNum = input("Enter num of decimal: ")
            if(check_operator(operator) == False):
                print("Invalid operator")
                continue

            result = calculate(num1, operator, num2)
            info = f'{num1} {operator} {num2} = {result}'
            add_to_history(info)
            print(f"{result:.{decNum}f}")
            choice = input("Do you want to save the result to memory? (yes/no): ").lower()
            if choice == 'yes':
                save_to_memory(result)
        elif choice == '2':
            display_history()
        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        isFirstStart = False

def get_user_input():
    while (True):
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operator (+, -, *, /, ^, sqrt, %): ")
            num2 = float(input("Enter the second number: "))
            return num1, operator, num2
        except ValueError as e:
            print("Float required!")

if __name__ == "__main__":
    main()
