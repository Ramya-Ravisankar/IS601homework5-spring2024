'''app/plugins/subtract/__init__.py'''
from commands import Command
from calculator import Calculator
from utils.validation import validate_decimal_input

class SubtractCommand(Command):
    '''A command class to perform subtraction.'''
    def execute(self):
        '''
        Execute the SubtractCommand.

        This method prompts the user to enter two numbers and performs subtraction.
        '''
        num1 = validate_decimal_input("Enter the first number: ")
        num2 = validate_decimal_input("Enter the second number: ")
        result = Calculator.subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
        return result