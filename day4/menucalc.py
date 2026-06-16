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
    if option not in ["1", "2", "3", "4", "5"]:
        print("Invalid option, try again")
        continue
    num1 = input("Enter the first number : ")
    num2 = input("Enter the second number : ")
    if num1.isalpha() or num2.isalpha():
        print("Invalid input, try again (numbers only)")
        continue
    print("\n")
   
    match option:
        case "1":
            result = add(float(num1), float(num2))
            print(f"The result of {num1} + {num2} is : {result:.2f}")
        case "2":
            result = sub(float(num1), float(num2))
            print(f"The result of {num1} - {num2} is : {result:.2f}")
        case "3":
            result = mul(float(num1), float(num2))
            print(f"The result of {num1} * {num2} is : {result:.2f}")
        case "4":
            if float(num2) == 0:
                print("Cannot divide by zero, try again")
                continue
            result = div(float(num1), float(num2))

            print(f"The result of {num1} / {num2} is : {result:.2f}")
        case "5":
            print("See you again soon!")
            break
    print("\n")
    print("press c to continue or any key to quit")
    selection = input()
    match selection:
        case "c":
            continue
        case _:
            break
