# function to display the main menu

def display_menu():
    print("\n--- Journal App Menu ---\n")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entries")
    print("4. Exit")

# Main function to run the app

def main():
    while True:
        display_menu()
        option = input("\nchoose an option (1-4): ")
        if option == '1':
            add_entry()
        elif option == '2':
            view_entries()
        elif option == '3':
            search_entries()
        elif option == '4':
            print("\nExiting the journal app. Goodbye!\n")
            break
        else:
            print("\nInvalid option. Please try again.")

# function to add entry

def add_entry():
    print("\n--- Add Journal Entry ---\n")
    title = input("Enter the title of your entry: ").title()
    content = input("Enter the content of your entry: ")
    date = input("Enter the date (YYYY-MM-DD): ")

# Saving the entry to the file

    try:
        if not date:    # if no date provided, use the current date
            from datetime import datetime
            date = datetime.now().strftime("%Y-%m-%d")
        with open("journal.txt", "a") as file:
            file.write(f"\n--- {date} ----\n")
            file.write(title + "\n")
            file.write(content + "\n")
        print("\nEntry added successfully!\n")
    except FileNotFoundError:
        print("\nNo journal entries found. Please add an entry first.\n")
    except Exception as e:
        print(f"\nAn error occurred while writing the entries: {e}\n")

# function to  view entries

def view_entries():
    print("\n--- View Journal Entries ---\n")
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("\nNo entries found.\n")
    except FileNotFoundError:
        print("\nNo journal entries found. Please add an entry first.\n")
    except Exception as e:
        print(f"\nAn error occurred while reading the entries: {e}\n")

# function to search an entry

def search_entries():
    print("\n--- Search Journal Entries ---\n")
    date = input("Enter date to search (YYYY-MM-DD): ")
    try:
        with open("journal.txt", "r") as file:
            content = file.read()
            entries = content. split("---")
            found = False
            for entry in entries:
                if date in entry:
                    print(f"\nEntry found for {date}:")
                    print(entry.strip())
                    found = True
            if not found:
                print(f"\nNo entry found for {date}.\n")

    except FileNotFoundError:
        print("\nNo journal entry found. Please add an entry first\n")
    except Exception as e:
        print(f"\nAn error occurred while finding the entry: {e}\n")

# Entry point of the application

if __name__ == "__main__":
    main()
