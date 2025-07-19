class Calculator:
    def calculate(self, a, b, operation):
        operations = {
            '+': a + b,
            '-': a - b,
            '*': a * b,
            '/': a / b if b != 0 else "Error: Division by zero"
        }
        return operations.get(operation, "Error: Invalid operation")

calculator = Calculator()
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
print(calculator.calculate(a, b, operation))
