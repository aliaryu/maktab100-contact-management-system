import re


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            instance._name = value
        else:
            raise ValueError(f"name '{value}' must be string.")


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            if re.match(r"^\S+@\S+\.\S+$", value):
                instance._email = value
            else:
                raise ValueError(f"'{value}' is not valid email.")
        else:
            raise ValueError(f"email '{value}' must be string.")


class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            if re.match(r"^\S+@\S+\.\S+$", value):
                instance._email = value
            else:
                raise ValueError(f"'{value}' is not valid email.")
        else:
            raise ValueError(f"email '{value}' must be string.")


class PhoneDescriptor:
    def __get__(self, instance, owner):
        return instance._phone
    
    def __set__(self, instance, value):
        if isinstance(value, str):
            if re.match(r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", value):
                instance._phone = value
            else:
                raise ValueError(f"'{value}' is not valid phone.")
        else:
            raise ValueError(f"phone '{value}' must be string.")

