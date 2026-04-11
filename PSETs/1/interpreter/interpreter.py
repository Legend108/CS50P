import re

text = input("Expression: ")

if math := re.match(r"^([0-9]+) ?(\+|-|\*|/) ?([0-9]+)$", text):
    num1, num2 = float(math.group(1)), float(math.group(3))
    result = None
    match math.group(2):
        case "+":
            result = num1 + num2
        case "-":
            result= num1 - num2
        case "/":
            if not num2 == 0:
                result=num1/num2
            else:
                print("Cannot divide by zero")
        case "*":
            result=num1*num2
    print(f"{result:.1f}")
else:
    print("Invalid syntax")