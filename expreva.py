# Simple expression evaluator

expression = input("Enter a mathematical expression: ")

try:
    result = eval(expression)
    print("Result:", result)
except Exception as e:
    print("Invalid expression:", e)