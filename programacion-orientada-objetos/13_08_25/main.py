from contact import Contact
from contactlist import ContactLits
from supplier import Supplier
from pprint import pprint

"""
c_1 =Contact("Dusty", "dusty@gmail.com")
c_2 =Supplier("Steve", "steve@gmail.com")

print(c_1)
pprint(c_2)
pprint(c_1.all_contacts)
print(c_2.all_contacts)
"""
c1 = Contact("John A", "john@example.net")
c2 = Contact("John B", "john@sloop.net")
c1 = Contact("Jenna C", "cutty@sark.io")

[c.name for c in Contact.all_contacts.search('John')]