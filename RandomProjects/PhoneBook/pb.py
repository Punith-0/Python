import json
class PhoneBook :
    contacts = [] 

    def __init__(self , name , phone_number ):
        self.name = name
        self.phone_number = phone_number
        PhoneBook.contacts.append(self) if PhoneBook.val_number(phone_number) else print("Invalid phone number")

    @staticmethod
    def val_number(phone_number):
        if len(phone_number) == 10 and phone_number.isdigit():
            return True
        return False

    @classmethod
    def search_contact(cls, name):
        for contact in cls.contacts:
            if contact.name.lower() == name.lower():
                print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
                return 
        print("Contact not found") 

    @classmethod
    def display_contacts(cls):
        for contact in cls.contacts:
            print(f"Name: {contact.name}, Phone Number: {contact.phone_number}")
    
    @classmethod
    def delete_contact(cls, name):
        for contact in cls.contacts:
            if contact.name == name:
                cls.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print("Contact not found")
    
    @classmethod
    def update_contact(cls, name, new_phone_number):
        for contact in cls.contacts:
            if contact.name == name:
                if cls.val_number(new_phone_number):
                    contact.phone_number = new_phone_number
                    print(f"Contact {name} updated.")
                else:
                    print("Invalid phone number")
                return
        print("Contact not found")
    
    @staticmethod
    def export_contacts(filename = "contacts.json") :
        with open(filename , 'w') as f :
            json.dump([contact.__dict__ for contact in PhoneBook.contacts] , f , indent = 4)
        print("Contacts exported successfully")

    @classmethod
    def import_contacts(cls , filename = "contacts.json") :
        try :
            with open(filename , 'r') as f :
                contacts_data = json.load(f)
                for contact_data in contacts_data :
                    cls(contact_data['name'] , contact_data['phone_number']) if not cls.chek_duplicates(contact_data['name']) else None
            print("Contacts imported successfully")
        except FileNotFoundError :
            print("File not found")
        
    @classmethod
    def chek_duplicates(cls , name) :
        for contact in cls.contacts :
            if contact.name.lower() == name.lower() :
                return True
        return False
    
    @classmethod
    def clear_contacts(cls):
        cls.contacts.clear()
        print("All contacts cleared")
    
    @staticmethod
    def clear_screen() :
        import os
        os.system('cls')
    
    @classmethod
    def sort_contacts(cls) :
        cls.contacts.sort(key = lambda contact : contact.name.lower())
        print("Contacts sorted alphabetically")

    @classmethod
    def count_contacts(cls) :
        print(f"Total contacts : {len(cls.contacts)}")


if __name__ == "__main__" :
    pass  #any test code can be written here