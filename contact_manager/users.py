from validators import UsernameDescriptor
import pickle
import hashlib


class User:
    # Descriptors
    username = UsernameDescriptor()

    def __init__(self, username:str, password:str):
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.id = self._id_generator()

    # Save Username
    @staticmethod
    def _save(data):
        with open('contact_manager\\data\\users.pkl', "wb") as file:
            pickle.dump(data, file)

    # Load Username
    @staticmethod
    def _load():
        try:
            with open('contact_manager\\data\\users.pkl', 'rb') as file:
                data = pickle.load(file)
                return data
        except FileNotFoundError:
            return {}

    # Auto Increament ID Generator
    def _id_generator(self):
        data = self._load()
        try:
            return data[list(data.keys())[-1]].id + 1
        except IndexError:
            return 1

    # Create user
    @classmethod
    def create(cls, username, password):
        data = cls._load()
        if username not in data:
            user = cls(username, password)
            data[username] = user
            cls._save(data)
        else:
            raise ValueError(f"username '{username}' already exist.")

    # Authenticate
    @classmethod
    def authenticate(cls, username, password):
        data = cls._load()
        if username in data:
            user = data[username]
            if user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
                return True
            else:
                raise ValueError("inlavid password.")
        else:
            raise ValueError(f"username '{username}' not exist.")

    # Modify User
    @classmethod
    def modify(cls, username, password, new_username, new_password):
        data = cls._load()
        if username in data:
            user = data[username]
            if cls.authenticate(username, password):
                user.username = new_username
                user.password = new_password
                data[new_username] = data.pop(username)
                cls._save(data)
            else:
                raise ValueError("inlavid password.")
        else:
            raise ValueError(f"username '{username}' not exist.")


    def __str__(self):
        return f"user: {self.username}"

    def __repr__(self):
        return f"User('{self.username}', ...)"
