from labs.shared.html_processor import HtmlProcessor

class DocsService:
    """
    DocsService class manages the display of HTML content, allowing navigation between pages.
    """

    def __init__(self, folder_path: str):
        """
        Initializes a DocsService instance.

        Parameters:
            folder_path (str): The path to the folder containing HTML files.

        Returns:
            None
        """
        self._html_processor = HtmlProcessor(folder_path)
        self._current_page = 1

    @property
    def current_page(self):
        """
        Property: Gets the current page number.

        Returns:
            int: The current page number.
        """
        return self._current_page

    def display_page(self):
        """
        Display the HTML content of the current page.

        Returns:
            None
        """
        text_data = self._html_processor.get_text_data(self._current_page)
        print(text_data)

    def change_page(self, page_number):
        """
        Change the current page to the specified page number.

        Parameters:
            page_number (int): The page number to change to.

        Returns:
            None
        """
        try:
            if page_number < 1 or page_number > len(self._html_processor.files_data):
                raise ValueError("Invalid page number.")
            else:
                self._current_page = page_number
                self.display_page()
        except ValueError as e:
            print(f"Error: {e}")

    def next_page(self):
        """
        Move to the next page and display its content.

        Returns:
            None
        """
        if self._current_page < len(self._html_processor.files_data):
            self._current_page += 1
            self.display_page()
        else:
            print("No next page available.")

    def prev_page(self):
        """
        Move to the previous page and display its content.

        Returns:
            None
        """
        if self.current_page > 1:
            self._current_page -= 1
            self.display_page()
        else:
            print("Already at the first page.")

if __name__ == "__main__":
    # Example usage:
    docs_service = DocsService("/path/to/html/files")

    # Display the current page
    docs_service.display_page()

    # Change to a specific page
    docs_service.change_page(2)

    # Move to the next page
    docs_service.next_page()

    # Move to the previous page
    docs_service.prev_page()
