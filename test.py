def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    
    return "error"

def mul(num1, num2):
        return num1 * num2

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

print(div(num1, num2))

print(mul(num1, num2))

print("good luck")