print("CALCULATOR")
def add(a,b):
    result = a + b
    print(result)

def sub(a,b):
    result = a - b
    print(result)

def div(a,b):
    result = a / b
    print(result)

def multiply(a,b):
    result = a * b
    print(result)

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
op = input("Enter the operator: ")

if op == '+':
    add(a,b)
elif op == '-':
    sub(a,b)
elif op == '/':
    div(a,b)
elif op == '*':
    multiply(a,b)
else:
    print("Invalid opperator")




