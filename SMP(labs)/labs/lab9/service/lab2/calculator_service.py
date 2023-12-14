import math

class CalculatorService:
    """
    Represents a calculator service with basic arithmetic operations.

    Attributes:
    - __first_value (float): The first operand for the arithmetic operation.
    - __operator (str): The operator indicating the type of arithmetic operation.
    - __second_value (float): The second operand for the arithmetic operation.

    Methods:
    - __init__(self): Initializes a CalculatorService object with default values.
    - input_values(self): Takes input for the first value, operator, and second value from the user.
    - __is_operator_correct(self, operator): Checks if the provided operator is a valid arithmetic operator.
    - calculate(self): Performs the arithmetic operation based on the provided values and operator.
    - __str__(self): Returns a string representation of the CalculatorService object.

    Example:
    # >>> calc_service = CalculatorService()
    # >>> calc_service.input_values()
    Enter the first value: 5
    Enter the operator ['+', '-', '*', '/', '**', '√', '%']: +
    Enter the second value: 3
    # >>> result = calc_service.calculate()
    # >>> print(result)
    8.0
    # >>> print(calc_service)
    CalculatorService: first_value=5.0, operator=+, second_value=3.0
    """

    def __init__(self):
        """
        Initializes a CalculatorService object with default values.
        """
        self.__first_value = None
        self.__operator = None
        self.__second_value = None

    def input_values(self):
        """
        Takes input for the first value, operator, and second value from the user.

        Raises:
        - ValueError: If the input format for the number is invalid.
        - RuntimeWarning: If the input operator is incorrect.
        """
        try:
            self.__first_value = float(input("Enter the first value: "))
            self.__operator = input("Enter the operator ['+', '-', '*', '/', '**', '√', '%']: ") or None
            if self.__is_operator_correct(self.__operator):
                if self.__operator != "√":
                    self.__second_value = float(input("Enter the second value: ")) if self.__operator != "%" else None
            else:
                raise RuntimeWarning("The input operator is incorrect")
        except ValueError as ve:
            raise ValueError(f"The format of the number is invalid: {ve}")

    @staticmethod
    def __is_operator_correct(operator):
        """
        Checks if the provided operator is a valid arithmetic operator.

        Parameters:
        - operator (str): The operator to be checked.

        Returns:
        - bool: True if the operator is valid, False otherwise.
        """
        valid_operators = ('+', '-', '*', '/', '**', '√', '%')
        return operator in valid_operators

    def calculate(self):
        """
        Performs the arithmetic operation based on the provided values and operator.

        Raises:
        - ZeroDivisionError: If attempting to divide by zero.
        - ArithmeticError: If calculating the square root of a negative number.

        Returns:
        - float: The result of the arithmetic operation.
        """
        result = 0

        if self.__operator in ('+', '-', '*', '/', '**', '%'):
            result = eval(f"self.__first_value {self.__operator} {self.__second_value}")

        elif self.__operator == "√":
            if self.__first_value < 0:
                raise ArithmeticError("Number is negative, therefore it is impossible "
                                      "to calculate the square root")
            result = math.sqrt(self.__first_value)

        return result

    def __str__(self):
        """
        Returns a string representation of the CalculatorService object.

        Returns:
        - str: A string containing calculator service information.
        """
        return f"CalculatorService: first_value={self.__first_value}, operator={self.__operator}," \
               f"second_value={self.__second_value}"
