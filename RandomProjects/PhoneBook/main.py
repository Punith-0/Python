from pb import PhoneBook

def main() :
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Export Contacts")
        print("7. Import Contacts")
        print("8. Clear Contacts")
        print("9. Sort Contacts")
        print("10. Count Contacts")
        print("Anything else to exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                PhoneBook(name, phone)

            case "2":
                name = input("Enter name to search: ")
                PhoneBook.search_contact(name)

            case "3":
                PhoneBook.display_contacts()

            case "4":
                name = input("Enter name to delete: ")
                PhoneBook.delete_contact(name)

            case "5":
                name = input("Enter name to update: ")
                new_phone = input("Enter new phone number: ")
                PhoneBook.update_contact(name, new_phone)

            case "6":
                PhoneBook.export_contacts()

            case "7":
                PhoneBook.import_contacts()

            case "8":
                PhoneBook.clear_contacts()

            case "9":
                PhoneBook.sort_contacts()

            case "10":
                PhoneBook.count_contacts()

            case _:
                print("Exiting PhoneBook. Goodbye!")
                break


if __name__ == "__main__" :
    main()
