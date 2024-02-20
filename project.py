Telephone_book = {'Amal': '1111111111', 'Mohammed': '2222222222', 'Khadijah': '3333333333',
                  'Abdullah': '4444444444', 'Ammar': '5555555555', 'Faisal': '6666666666', 'Layla': '7777777777'}

Name = input("Enter your name: ")
print("Hello "+Name+", welcome to the universal phone book.")

print("You have a list "+Name+", choice one of them.")

while True:
    print("1.Search using name.")
    print("2.Search using number.")
    print("3.Add a new contact if you have the authority.")
    print("4.Quit.")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        search_name = input("Enter the name you are looking for: ")
        found = False
        for key, value in Telephone_book.items():
            if search_name.lower() == key.lower():
                print("We found "+key+" in telephone directory and his/her number is:", value)
                found = True
                break
        if not found:
            print("Sorry, this name isn't found in telephone directory.")

    elif choice == 2:
        search_number = input("Enter the number you are looking for: ")
        if search_number.isdigit() and len(search_number) == 10:
            found = False
            for key, value in Telephone_book.items():
                if search_number in value:
                    print("We found "+key+" in telephone directory and his/her number is:", value)
                    found = True
                    break

            if not found:
                print("Sorry, this number isn't found in telephone directory.")
        else:
            print("Please enter exactly 10 digits.")

    elif choice == 3:
        Employee_ID = input("Enter your ID number: ")
        new_name = input("Enter the new name: ")
        new_number = input("Enter the new number: ")
        Telephone_book[new_name] = new_number
        print("The contact is added in telephone directory.")
        print(Telephone_book)

    elif choice == 4:
        print("Thank you for using the universal phone book, and we hope to see you again!.")
        break
    else:
        print("Invalid choice. Please try again.")
