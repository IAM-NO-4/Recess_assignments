def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("*********Welcome********")
print("Options: ")


while True:
    print("1. addition (+)")
    print("2. subtraction (-)")
    print("3. multiplication (*)")
    print("4. division (/)")
    print("5. Exit")

    print("\n")
    option = input("Select your option : ")

    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    print("\n")
    match option:
        case "1":
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is : {result}")
        case "2":
            result = sub(num1, num2)
            print(f"The result of {num1} - {num2} is : {result}")
        case "3":
            result = mul(num1, num2)
            print(f"The result of {num1} * {num2} is : {result}")
        case "4":
            if num2 == 0:
                print("Cannot divide by zero, try again")
                continue
            result = div(num1, num2)
            print(f"The result of {num1} / {num2} is : {result}")
        case "5":
            print("See you again soon!")
            break
        case _:
            print("Wrong selection option, try again. valid options: 1,2,3,4 or 5")
            continue
    print("\n")
    print("press c to continue or any key to quit")
    selection = input()
    match selection:
        case "c":
            continue
        case _:
            break
