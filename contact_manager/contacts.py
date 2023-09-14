from validators import NameDescriptor, EmailDescriptor, PhoneDescriptor
import pickle
import os


class Contact:
    # Descriptors
    name = NameDescriptor()
    email = EmailDescriptor()
    phone = PhoneDescriptor()

    def __init__(self, user_id, name:str, email:str, phone:str, note:str=None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.note = note

    # Save Contact
    @staticmethod
    def _save(data):
        with open('contact_manager\\data\\contacts.pkl', "wb") as file:
            pickle.dump(data, file)

    # Load Contact
    @staticmethod
    def _load():
        try:
            with open('contact_manager\\data\\contacts.pkl', 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            return {}

    # Create Contact
    @classmethod
    def add(cls, user_id, name, email, phone, note=None):
        data = cls._load()
        contact = cls(user_id, name, email, phone, note)
        user_contacts = data.setdefault(user_id, {})
        if name not in user_contacts:
            user_contacts[name] = contact
            cls._save(data)
        else:
            raise ValueError(f"contact '{name}' already exist.")

    # Edit Contact
    @classmethod
    def edit(cls, user_id, name, new_name, new_email, new_phone, new_note=None):
        data = cls._load()
        if user_id in data:
            user_contacts = data.get(user_id)
            if name in user_contacts:
                user_contacts[name].name = new_name
                user_contacts[name].email = new_email
                user_contacts[name].phone = new_phone
                user_contacts[name].note = new_note
                user_contacts[new_name] = user_contacts.pop(name)
                cls._save(data)
            else:
                raise ValueError(f"contact '{name}' not exist.")
        else:
            raise ValueError(f"user id '{user_id}' not exist.")
    
    # Delete Contact
    @classmethod
    def delete(cls, user_id, name):
        data = cls._load()
        if user_id in data:
            user_contacts = data.get(user_id)
            if name in user_contacts:
                del user_contacts[name]
                cls._save(data)
            else:
                raise ValueError(f"contact '{name}' not exist.")
        else:
            raise ValueError(f"user id '{user_id}' not exist.")

    # Read All Contacts
    @classmethod
    def read_all_contacts(cls, user_id):
        data = cls._load()
        if user_id in data:
            return data[user_id]
        else:
            raise ValueError(f"user id '{user_id}' not exist.")

    # Search by Name
    @classmethod
    def search_by_name(cls, user_id, name):
        user_contacts = cls.read_all_contacts(user_id)
        if name in user_contacts:
            return user_contacts[name]
        else:
            return False
    
    # Search by Email
    @classmethod
    def search_by_email(cls, user_id, email):
        user_contacts = cls.read_all_contacts(user_id)
        for contact in user_contacts:
            if email == user_contacts[contact].email:
                return user_contacts[contact]
        else:
            return False
    
    # Search by Phone
    @classmethod
    def search_by_phone(cls, user_id, phone):
        user_contacts = cls.read_all_contacts(user_id)
        for contact in user_contacts:
            if phone == user_contacts[contact].phone:
                return user_contacts[contact]
        else:
            return False


    def __str__(self):
        return f"name : {self.name}\nemail: {self.email}\nphone: {self.phone}"

    def __repr__(self):
        return f"Contact('{self.name}', ...)"
