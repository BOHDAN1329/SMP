from functions import create_art, save_to_file, view_art, delete_art

while True:
    print("\nMenu:")
    print("1. Create Art")
    print("2. View Art")
    print("3. Delete Art")
    print("4. End the program")
    choice = input("Enter your choice: ")

    if choice == "1":
        art, characters = create_art()
        if art:
            save_to_file(art, characters)
    elif choice == "2":
        view_art()
    elif choice == "3":
        delete_art()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")