a = int(input("Entre first number: "))
b = int(input("Entre second number: "))

operation = input("Entre operation: ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        result = "Ділення на нуль!"
    else:
        result = a / b

print(result)