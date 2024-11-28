def main():
    
    my_dict = {}

    while True:
        print("\nDictionary Operations:")
        print("1. Print Dictionary")
        print("2. Add Key-Value Pair")
        print("3. Modify Value")
        print("4. Delete Key-Value Pair")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            
            if my_dict:
                print("Current Dictionary:", my_dict)
            else:
                print("The dictionary is empty.")

        elif choice == '2':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            my_dict[key] = value
            print(f"Added ({key}: {value}) to the dictionary.")

        elif choice == '3':
            key = input("Enter the key to modify: ")
            if key in my_dict:
                new_value = input("Enter the new value: ")
                my_dict[key] = new_value
                print(f"Updated {key} to {new_value}.")
            else:
                print(f"Key '{key}' not found in the dictionary.")

        elif choice == '4':
            key = input("Enter the key to delete: ")
            if key in my_dict:
                del my_dict[key]
                print(f"Deleted key '{key}' from the dictionary.")
            else:
                print(f"Key '{key}' not found in the dictionary.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Enter a valid choice(1-5)")


main()
