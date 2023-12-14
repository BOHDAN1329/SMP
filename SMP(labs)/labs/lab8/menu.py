# menu.py
from service import ConsumerServiceImpl

def get_yes_or_no_input(prompt):
    return input(prompt).lower() == 'y'

def display_menu(service):
    while True:
        print(
            "1. Display states histogram\n"
            "2. Display states pie chart\n"
            "3. Display combined states diagram\n"
            "0. Exit\n"
        )

        choice = input("Enter your choice: ")

        if choice == "1":
            has_to_be_downloaded = get_yes_or_no_input("Do you want to download the histogram? Enter 'y' or anything else not to download: ")
            service.create_chart('bar', has_to_be_downloaded)

        elif choice == "2":
            has_to_be_downloaded = get_yes_or_no_input("Do you want to download the pie chart? Enter 'y' or anything else not to download: ")
            try:
                max_quantity = int(input("Enter the maximum quantity of states: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            service.create_chart('pie', has_to_be_downloaded, max_quantity=max_quantity)

        elif choice == "3":
            has_to_be_downloaded = get_yes_or_no_input("Do you want to download the combined chart? Enter 'y' or anything else not for no: ")
            try:
                max_quantity = int(input("Enter the maximum quantity of states in the pie chart diagram included: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            service.create_chart('combined', has_to_be_downloaded, max_quantity=max_quantity)

        elif choice == "0":
            break

        else:
            print("Incorrect input. Enter again.")


