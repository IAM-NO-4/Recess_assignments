admins = {
    "kabejja" : "1111",
    "admin1" : "2222",
    "admin2" : "0000"
}
customers = {
        "john" : "3333",
        "customer1" : "4444",
        "customer2" : "5555"
}
cashiers = {
    "alice" : "6666",
    "cashier1" : "7777",
    "cashier2" : "8888"
}



y = True
for i in range(1, 4):
    name = input("Enter your name : ")
    password = input("Enter your password : ")
    if name in admins:
        if password == admins[name]:
           print(f"Welcome Admin {name}")
           print("You can now access the admin system")
           y = False
           break
        else:
            print("Invalid password, try again")
    elif name in customers :
        if password == customers[name]:
            print(f"Welcome Customer {name}")
            print("You can now access the shopping system")
            y = False
            break
        else:
            print("Invalid password, try again")
    elif name in cashiers :
        if password == cashiers[name]:
            print(f"Welcome Cashier {name}")
            print("You can now access the cashier system")
            y = False
            break
        else:
            print("Invalid password, try again")
    else:
        print("Invalid credentials, try again")
if y:
    print("Too many failed attempts, try again later")