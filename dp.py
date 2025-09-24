import os

# Get values from environment variables
a = int(os.getenv('NUM1', '0'))    # Default to 0 if not set
b = int(os.getenv('NUM2', '0'))
oper = os.getenv('OP', '+')        # Default operator +

print(f"Number 1: {a}")
print(f"Number 2: {b}")
print(f"Operator: {oper}")

if oper == '+':
    print("Result:", a + b)
elif oper == '-':
    print("Result:", a - b)
elif oper == '*':
    print("Result:", a * b)
elif oper == '/':
    print("Result:", a / b)
else:
    print("Invalid operator")
