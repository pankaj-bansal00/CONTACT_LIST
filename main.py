import logging
import json
import tkinter as tk
import regex as re
import traceback

# Task Name

format = "%(levelname)s: %(name)s: %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format)
logging.info("Welcome to the contact list")

# Initialize the dictionary
contact_list = {}

username_pattern = r"^[A-Z][a-z A-Z0-9]+"
phone_pattern = r"\d{10}"
# Load the contact list from the JSON file
with open("CONTACT_LIST/file.json", "r") as file:
    contact_list = json.load(file)


def add_number():
    # Create a dictionary for the new contact
    try:
        while True:
            username = input("Enter the name: ").strip()
            #print(bool(re.findall(username_pattern, username)))
            if re.findall(username_pattern, username):
                print(username)
                break
            else:
                logging.warning("wrong input")
            

        while True: 
            try:
                phone_number = int(input("Enter the number: "))
            except ValueError:
                logging.error("input ten digit integer number")
                continue
            if re.findall(phone_pattern, str(phone_number)):
                print(phone_number)
            else:
                logging.warning("enter a valid ten digits numbers")
                continue

            # Add the new contact to the contact list
            contact_list[username] = {"phone_number": phone_number}

            with open("file.json", "w") as file:
                json.dump(contact_list, file)
            logging.info("Contact saved successfully")
            break
    except Exception as e:
        print(f"an occur error{e} {traceback.print_exc()}")


def view_number():
    # Load and display the contact list from the JSON file

    with open("file.json", "r") as file:
        contact_list = json.load(file)

    # Print the contact list
    print(contact_list)


def remove_number():

    while True:
        # firstly we give username for remove the number
        ask_name = input("enter the name to delete: ")

        try:
            contact_list.pop(ask_name)
            logging.info("name delete succesfully")
            with open("file.json", "w") as file:
                json.dump(contact_list, file)
            break

        except KeyError as err:
            logging.warning("name does not exist")


while True:
    # show operations
    print(
        """Operations:
                1. add_number
                2. veiw_number
                3. remove_number
                4. quit"""
    )

    # take inputs for perfoming the operation

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            add_number()
        elif choice == 2:
            view_number()
        elif choice == 3:
            remove_number()
        elif choice == 4:
            print("Exiting the Contact List application. Goodbye!")
            break
        else:
            print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Please enter a valid number.")
