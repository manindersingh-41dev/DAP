def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


a = float(input("Enter number 1: "))

while True:
    op = input("Enter operator: ")
    if op == "E":
        break

    b =  float(input("Enter number 2: "))
    if op == '+':
        res = add(a,b)
    
    if op == '-':
        res = sub(a,b)

    if op == '*':
        res = mul(a,b)

    if op == '/':
        res = div(a,b)
    
    print(f"\t\t\t\t Result: {res}")

    a = res


    
