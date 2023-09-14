from menu import Menu, Item
from users import User
from contacts import Contact
import os


# User Actions
def add_contact(user_id):
    os.system("cls")
    name  = input("Name:  ")
    email = input("Email: ")
    phone = input("Phone: ")
    print("\nYou can also save a note, if you don't want to,\nleave the note blank and press 'Enter', Done ^^")
    note  = input("Note:  ")
    os.system("cls")
    try:
        if not note:
            note = None
        Contact.add(user_id, name, email, phone, note)
        print(f"Contact '{name}' was created successfully *-*")
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)

def edit_contact(user_id):
    os.system("cls")
    print("Which contact do you want to edit?")
    name = input("Name: ")
    os.system("cls")
    print(f"Write new information for '{name}'")
    new_name  = input("New Name:  ")
    new_email = input("New Email: ")
    new_phone = input("New Phone: ")
    print("\nYou can also save a note, if you don't want to,\nleave the note blank and press 'Enter', Done ^^")
    new_note  = input("New Note:  ")
    os.system("cls")
    try:
        if not new_note:
            new_note = None
        Contact.edit(user_id, name, new_name, new_email, new_phone, new_note)
        print(f"Contact '{new_name}' was edited successfully :p")
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)

def delete_contact(user_id):
    os.system("cls")
    print("Which contact do you want to delete?")
    name = input("Name: ")
    try:
        Contact.delete(user_id, name)
        print(f"Contact '{name}' was deleted successfully :(")
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)

def view_all_contacts(user_id):
    try:
        data = Contact.read_all_contacts(user_id)
        for index, contact in data.items():
            print(contact)
            print("---")
        input("\nPress 'Enter' to exit.")
        os.system("cls")
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)

# SignIn Function & Its Menu
def signin_function():
    os.system("cls")
    print("- SignIn Panel -\n")
    username = input("Username: ")
    password = input("Password: ")
    os.system("cls")
    try:
        user = User.authenticate(username, password)
        if user:
            user_menu = Menu(username.title())

            item_add_contact = Item("Add Contact", add_contact, user.id)
            user_menu.add_item(item_add_contact)

            item_edit_contact = Item("Edit Contact", edit_contact, user.id)
            user_menu.add_item(item_edit_contact)

            item_delete_contact = Item("Delete Contact", delete_contact, user.id)
            user_menu.add_item(item_delete_contact)

            item_view_all_contacts = Item("View All Contacts", view_all_contacts, user.id)
            user_menu.add_item(item_view_all_contacts)

            user_menu.display()
            user_menu.execute()
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)

# SignUp Function
def signup_function():
    os.system("cls")
    print("- SignUp Panel -\n")
    username = input("Username: ")
    password = input("Password: ")
    os.system("cls")
    try:
        User.create(username, password)
        print(f"User '{username}' was created successfully :D")
        print("You can SignUp with your username now ...")
    except Exception as error:
        os.system("cls")
        print("Unexpected Error ...")
        print("More Detail:", error)


# configs
main_menu = Menu("Contact Management System")

item_signin = Item("SignIn", signin_function)
main_menu.add_item(item_signin)

item_signup = Item("SignUp", signup_function)
main_menu.add_item(item_signup)

main_menu.display()
main_menu.execute()
