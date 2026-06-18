print("=============Welcome to the contact manager system===========")
contacts = [
    {"name": "Kabejja", "phone": "0757716179", "email": "kabejja@gmail.com"},
    {"name": "Katongole", "phone": "0757714379", "email": "kato@gmail.com"},
]


def validate_name():
    while True:
        name = input("Enter the name: ")
        if len(name) > 20:
            print("Name too long (Maxium = 20 characters)")
            continue
        else:
            name = name.title()
            return name


def validate_phone():
    while True:
        phone = input("Enter the phone number (like 07xxx): ")
        if len(phone) != 10:
            print("number too long/short, enter a valid number please! ")
            continue
        elif not phone.isdigit():
            print("Phone number should not contain characters, try again ")
            continue
        elif phone[0:2] != "07":
            print("Phine number should start with 07 ")
            continue
        else:
            return phone


def validate_email():
    while True:
        email = input("Enter the email: (e.g yourname@gmail.com): ")
        if "@" and "." not in email:
            print('invalid email, should contain "@" and "." ')
            continue
        elif (
            email.index("@") > email.index(".")
            or email.index("@") + 1 == email.index(".")
            or email.index("@") == 0
            or email.index(".") == len(email) - 1
        ):
            print("invalid email, try again")
            continue
        else:
            return email


def add_contact():
    name = validate_name()
    phone = validate_phone()
    email = validate_email()
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully")


def view_contact():
    query = input("Enter the name or email:")
    for contact in contacts:
        if contact["name"] == query.title() or contact["email"] == query.title():
            print("Contact info: ")
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")
            break
    else:
        print("No matching contact information found, try again ")


def update_contact():
    name = ""
    email = ""
    phone = ""
    query = input("Enter the name, email or phone number to update : ")
    for contact in contacts:
        if (
            contact["name"] == query.title()
            or contact["email"] == query.title()
            or contact["phone"] == query
        ):
            name1 = contact["name"]
            phone1 = contact["phone"]
            email1 = contact["email"]
            print("current contact info: ")
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")

            while True:
                selection = input("Would you like to change the name? Y/N: ")
                if selection not in ["Y", "y", "N", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection == "y" or selection == "Y":
                    name = validate_name()
                    break
                else:
                    name = name1
                    break
            while True:
                selection1 = input("Would you like to change the phone number? Y/N: ")
                if selection1 not in ["Y", "y", "N", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection1 == "y" or selection == "Y":
                    phone = validate_phone()
                    break
                else:
                    phone = phone1
                    break

            while True:
                selection = input("Would you like to change the email? Y/N: ")
                if selection not in ["Y", "y", "N", "n"]:
                    print("Invalid option, try again")
                    continue
                elif selection == "y" or selection == "Y":
                    email = validate_email()
                    break
                else:
                    email = email1
                    break

            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            print("Contact updated successfully. ")
            break
    else:
        print("No matching contact information found, try again ")


def delete_contact():
    query = input("Enter the name, email or phone number to delete:")
    flag = True
    for contact in contacts:
        if (
            contact["name"] == query
            or contact["email"] == query
            or contact["phone"] == query
        ):
            contacts.pop(contacts.index(contact))
            print("contact deleted successully")
            flag = False
    if flag:
        print("contact not found")


def search_contact():
    query = input("Enter the name, email or phone number to search :")
    flag = True
    for contact in contacts:
        if (
            query in contact["name"]
            or query in contact["email"]
            or query in contact["phone"] == query
        ):
            print(f"name: {contact['name']}")
            print(f"Phone number : {contact['phone']}")
            print(f"email: {contact['email']}")
            print("\n")
            flag = False
    if flag:
        print("no search contact found")


def all_contacts():
    print("contact list")
    for contact in contacts:
        print(f"name: {contact['name']}")
        print(f"Phone number : {contact['phone']}")
        print(f"email: {contact['email']}")
        print("\n")


while True:
    print(
        """
    === Contact Manager Menu ===
    1. Add Contact
    2. View Contact
    3. Update Contact
    4. Delete Contact
    5. Search Contacts
    6. List All Contacts
    7. Exit
    Choose an option (1-7):
    """
    )
    choice = input("")
    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid selection, try again")
        continue
    match choice:
        case "1":
            add_contact()
        case "2":
            view_contact()
        case "3":
            update_contact()
        case "4":
            delete_contact()
        case "5":
            search_contact()
        case "6":
            all_contacts()
        case "7":
            break
