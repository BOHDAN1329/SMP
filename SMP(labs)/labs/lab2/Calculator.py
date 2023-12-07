import math

class Calculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.decNum = 2

    def check_operator(self, operator):
        valid_operators = ['+', '-', '*', '/', '^', 'sqrt', '%']
        if operator not in valid_operators:
            return False
        return True

    def calculate(self, num1, operator, num2):
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
    def save_to_memory(self, result):
        self.memory = result


    def add_to_history(self, expression):
        self.history.append(expression)

    def display_history(self):
        try:
            print("Calculation History:")
            if len(self.history) < 1:
                raise Exception
            else:
                for expression in self.history:
                    print(expression)
        except Exception as e:
            print("\n\nHistory is empty")

    def run_calculator(self):
        isFirstStart = True
        result = 0
        while True:
            print("\nMenu:")
            print("1: Start Calculate")
            print("2: See History")
            print("3: Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                num1, operator, num2 = self.get_user_input()
                if not isFirstStart and input("use previous result?(yes/no)") == 'yes':
                    num1 = result

                self.decNum = input("Enter num of decimal: ")
                if (self.check_operator(operator) == False):
                    print("Invalid operator")
                    continue
                result = self.calculate(num1, operator, num2)
                info = f'{num1} {operator} {num2} = {result}'
                self.add_to_history(info)
                print(f"{result:.{self.decNum}f}")
                choice = input("Do you want to save the result to memory? (yes/no): ").lower()
                if choice == 'yes':
                    self.save_to_memory(result)
            elif choice == '2':
                self.display_history()
            elif choice == '3':
                print("Exiting the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
            isFirstStart = False

    @staticmethod
    def get_user_input():
        while(True):
            try:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter the operator (+, -, *, /, ^, sqrt, %): ")
                num2 = float(input("Enter the second number: "))
                return num1, operator, num2
            except ValueError as e:
                print("Float required!")
