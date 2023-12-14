"""
Module: interactive_docs_menu

This module provides a text-based interactive menu for navigating through HTML documentation.

Classes:
    - DocsMenu: Provides a text-based interactive menu for navigating through HTML documentation.
"""

from labs.service.docs_service import DocsService

class DocsMenu:
    """
    DocsMenu class provides a text-based interactive menu for navigating through HTML documentation.

    Attributes:
        docs_service (DocsService): An instance of DocsService for managing HTML content.

    Methods:
        __init__(folder_path: str)
            Initializes a DocsMenu instance with a specified folder path.

        print_menu()
            Static method to print the interactive menu options.

        display_current_page()
            Displays the current page.

        change_page()
            Changes to a specific page based on user input.

        move_to_next_page()
            Moves to the next page.

        move_to_previous_page()
            Moves to the previous page.

        run()
            Runs the interactive menu loop, allowing the user to navigate through the documentation.
    """

    def __init__(self, folder_path: str):
        """
        Initializes a DocsMenu instance with a specified folder path.

        Parameters:
            folder_path (str): The path to the folder containing HTML files.

        Returns:
            None
        """
        self.docs_service = DocsService(folder_path)

    @staticmethod
    def print_menu():
        """
        Static method to print the interactive menu options.

        Returns:
            None
        """
        print("1. Display current page")
        print("2. Change to a specific page")
        print("3. Move to the next page")
        print("4. Move to the previous page")
        print("0. Exit")

    def display_current_page(self):
        """
        Displays the current page.

        Returns:
            None
        """
        print("Current Page:", self.docs_service.current_page)

    def change_page(self):
        """
        Changes to a specific page based on user input.

        Returns:
            None
        """
        try:
            page_number = int(input("Enter the page number: "))
            self.docs_service.change_page(page_number)
        except ValueError:
            print("Invalid input. Please enter a valid page number.")

    def move_to_next_page(self):
        """
        Moves to the next page.

        Returns:
            None
        """
        self.docs_service.next_page()

    def move_to_previous_page(self):
        """
        Moves to the previous page.

        Returns:
            None
        """
        self.docs_service.prev_page()

    def run(self):
        """
        Runs the interactive menu loop, allowing the user to navigate through the documentation.

        Returns:
            None
        """
        while True:
            self.display_current_page()
            self.print_menu()

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.docs_service.display_page()
                elif choice == 2:
                    self.change_page()
                elif choice == 3:
                    self.move_to_next_page()
                elif choice == 4:
                    self.move_to_previous_page()
                elif choice == 0:
                    break
                else:
                    print("Invalid choice. Please enter a corresponding number")

            except ValueError:
                print("Invalid input. Please enter a number.")
