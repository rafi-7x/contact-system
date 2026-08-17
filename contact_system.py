import __main__
contact_list = []
def add_contact():
    saved_contact = []
    answer = ""
    while answer != "exit":
        name = str(input("Enter a name : "))
        phone_number = int(input(f"Now {name}'s phone number : "))
        contact_adder = {"name": name,"phone number": phone_number}
        answer = str(input("Type exit if you wanna leave :"))
        saved_contact.append(contact_adder)
    else:
        print("Exiting...")
    return saved_contact
def search_contact():
    search_name = str(input("Enter the name you're looking for : "))
    answer = ""
    while answer != "exit":
        for contact in contact_list:
            if contact["name"] == search_name:
                print("Here is the results : ")
                print(f"The name : {contact['name']}")
                print(f"Phone number : {contact['phone number']}")
                answer = str(input("Type exit if you wanna leave : "))
                break
        else:
            print("Name not found :|")
            search_name = str(input("Try again or type exit to leave : "))
            if search_name == "exit":
                print("Exiting...")
                break
def display_contact():
    print("All your contact list : ")
    for contact in contact_list:
        print(f"The name : {contact['name']}")
        print(f"Phone number : {contact['phone number']}")

def main():
    print("   Contact Book  ") 
    options = ""
    while options != "exit":
        options = str(input("_Add\n_Display\n_Search\n_Exit\n"))
        if options == "Add" or options == "add":
            new_contact = add_contact()
            if new_contact:
                contact_list.extend(new_contact)
        elif options == "Display" or options == "display":
            display_contact()
        elif options == "Search" or options == "search":
            search_contact()
        elif options == "Exit" or options == "exit":
            print("Exiting...")
            break
if __name__ == "__main__":
    main()                        
                                   
