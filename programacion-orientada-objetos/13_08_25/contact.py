from typing  import List
from contactlist import ContactLits

class Contact():

    all_contacts: List["Contact"] = ContactLits()

    def __init__(self, name : str, email : str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.email})"