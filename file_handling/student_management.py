import csv
import json
import logging
import os
import numpy as np
import pandas as pd
import seaborn as sns


print(np.__version__)
print(pd.__version__)
print(sns.__version__)

# Logging Configuration
FOLDER = "file_handling"
logging.basicConfig(
    filename=os.path.join(FOLDER, "student_management_system.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



os.makedirs(FOLDER, exist_ok=True)

CSV_FILE = os.path.join(FOLDER, "students_system.csv")
JSON_FILE = os.path.join(FOLDER, "students_system.json")

class StudentNotFoundExeption(Exception):
    pass

# Creating files if they don't exist
def initialize_files():
    try:
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["RegNo", "Name", "Age", "Gender"])
        if not os.path.exists(JSON_FILE):
            with open(JSON_FILE, "w") as file2:
                json.dump({}, file2, indent=4)
    except Exception as e:
        logging.error(e)
        print("Error initializing files:", e)

def add_student():
    try:
        reg = input("Registration Number: ")
        # Checking duplicate registration number
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == reg:
                    print("Student already exists.")
                    return
        name = input("Student Name: ")
        while True:
                age = input("Age: ")
                if age.isdigit() and int(age) > 0 and int(age) < 31:
                    age = int(age)
                    break
                else:
                    print("Please enter a valid age.")
        while True:
            gender = input("Gender: (M/F): ")
            if gender.upper() in ["M", "F"]:
                break
            else:
                print("Please enter a valid gender.")

        address = input("Address: ")
        while True:
                contact = input("Contact: (07XXXXXXXXX)")
                if contact.isdigit() and len(contact) == 10:
                    break
                else:
                    print("Please enter a valid 10-digit contact number.")
        program = input("Program: ")
        
        # Saving basic information in CSV
        with open(CSV_FILE, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([reg, name, age, gender])

        # Saving extra details in JSON
        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        data[reg] = {
            "Address": address,
            "Contact": contact,
            "Program": program
        }
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Added student {reg}")
        print("Student added successfully.")
    except ValueError:
        logging.error("Invalid age entered.")
        print("Age must be a number.")
    except Exception as e:
        logging.error(e)
    finally:
        print("Operation Completed.\n")

def view_students():
    try:
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            print("\n------ STUDENTS ------")
            for row in reader:
                print(row)
        logging.info("Viewed all students")
    except Exception as e:
        logging.error(e)
    finally:
        print()

def search_student():
    try:
        reg = input("Enter Registration Number: ")
        found = False
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == reg:
                    print("\nBasic Details")
                    print(row)
                    found = True
                    break
        if not found:
            raise StudentNotFoundExeption("Student not found.")
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        print("Additional Details")
        print(data.get(reg))
        logging.info(f"Searched student {reg}")
    except StudentNotFoundExeption as e:
        logging.error(e)
        print(e)
    finally:
        print()

def update_student():
    try:
        reg = input("Registration Number: ")
        rows = []
        found = False
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] == reg:
                    found = True
                    row[1] = input("New Name: ")
                    row[2] = input("New Age: ")
                    row[3] = input("New Gender: ")
                rows.append(row)
        if not found:
            raise StudentNotFoundExeption("Student not found.")
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        data[reg]["Address"] = input("New Address: ")
        data[reg]["Contact"] = input("New Contact: ")
        data[reg]["Program"] = input("New Program: ")
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Updated student {reg}")
        print("Updated Successfully.")
    except StudentNotFoundExeption as e:
        logging.error(e)
        print(e)
    except Exception as e:
        logging.error(e)
    finally:
        print()

def delete_student():
    try:
        reg = input("Registration Number: ")
        rows = []
        found = False
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                if row[0] != reg:
                    rows.append(row)
                else:
                    found = True
        if not found:
            raise StudentNotFoundExeption("Student not found.")
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
        if reg in data:
            del data[reg]
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
        logging.info(f"Deleted student {reg}")
        print("Student Deleted.")
    except StudentNotFoundExeption as e:
        logging.error(e)
        print(e)
    finally:
        print()

def menu():
    initialize_files()
    while True:
        print("********** STUDENT MANAGEMENT **********")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose Option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            logging.info("Program Closed")
            print("Goodbye.")
            break
        else:
            print("Invalid Choice.")
if __name__ == "__main__":
    menu()