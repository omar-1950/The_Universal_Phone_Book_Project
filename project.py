# telephone_book.py

telephone_book = {
    'Amal': '1111111111',
    'Mohammed': '2222222222',
    'Khadijah': '3333333333',
    'Abdullah': '4444444444',
    'Ammar': '5555555555',
    'Faisal': '6666666666',
    'Layla': '7777777777'
}
def display_menu():
    print("1. Search using name.")
    print("2. Search using number.")
    print("3. Add a new contact (authorized personnel only).")
    print("4. Quit.")

def search_by_name(name):
    for key, value in telephone_book.items():
        if name.lower() == key.lower():
            print(f"We found {key} in telephone directory and their number is: {value}")
            return
    print("Sorry, this name isn't found in telephone directory.")
def search_by_number(number):
    if number.isdigit() and len(number) == 10:
        for key, value in telephone_book.items():
            if number in value:
                print(f"This number belong to Mr./Miss. {key}")
                return
        print("Sorry, this number isn't found in telephone directory.")
    else:
        print("Please enter exactly 10 digits.")

def add_contact():
    employee_id = input("Enter your ID number: ")
    print(employee_id, "Welcome you have an access to add an contacts")
    new_name = input("Enter the new name: ")
    new_number = input("Enter the new number: ")
    telephone_book[new_name] = new_number
    print("The contact is added in telephone directory.")
    print(telephone_book)
def main():
    print("Hello! Welcome to the universal phone book.")
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            search_name = input("Enter the name you are looking for: ")
            search_by_name(search_name)
        elif choice == 2:
            search_number = input("Enter the number you are looking for: ")
            search_by_number(search_number)
        elif choice == 3:
            add_contact()
        elif choice == 4:
            print("Thank you for using the universal phone book, and we hope to see you again!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
