from labs.service.lab2.calculator_service import CalculatorService
from labs.ui.menu_builder import Menu

class CalculatorMenu(Menu):
    """A simple calculator menu class."""

    def run(self):
        """Run the calculator program."""
        calculator_service = CalculatorService()

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice (1 or 2): ")

                if choice == '1':
                    calculator_service.input_values()
                    print(f"\nThe result of the calculation is: {calculator_service.calculate()}\n")
                    another_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
                    if another_calculation != 'y':
                        break
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            except ValueError as ve:
                print(f"Invalid input: {ve}")

    @staticmethod
    def display_menu():
        """Display the calculator menu."""
        print("\n=== Calculator Menu ===")
        print("1. Perform calculation - Enter values and get the result")
        print("2. Exit - Quit the calculator program")
