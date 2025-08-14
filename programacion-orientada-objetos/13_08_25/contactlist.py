from __future__ import annotations
from contact import Contact

class ContactLits(list["Contact"]):
    def search(self, name:str, mail: str) -> None:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts