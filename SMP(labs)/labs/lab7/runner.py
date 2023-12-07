from service import ProfileTableDisplayer, UserProfileService
from utility import FileProcessor
import json


def main():
    json_file_path = "./files/result.json"
    history = []
    successful_result = False
    json_data = {}
    user_profile_info = None
    user_service = UserProfileService()
    display_on_table = ProfileTableDisplayer()

    while True:
        print("Choose an option:")
        print("1. Display data of a personal profile")
        print("2. Show history")
        print("3. Save data into a file")
        print("0. Exit")

        option = input("Your choice: ")

        match option:
            case "1":
                username = input("Enter username: ")
                try:
                    json_data = user_service.get_personal_profile(username)
                    print("Choose an option:")
                    print("1. Display data in a table")
                    print("2. Display data in JSON format")

                    inner_option = input("Your choice: ")

                    match inner_option:
                        case "1":
                            user_profile_info = display_on_table.display_profile(json.dumps(json_data))
                        case "2":
                            user_profile_info = json.dumps(json_data, indent=4)
                        case _:
                            print("Invalid option. Enter again!")

                    print(user_profile_info)
                    history.append(
                        f"Data of a personal profile where username is {username}:\n{user_profile_info}")
                    successful_result = True
                except ValueError as e:
                    print(e)
                    successful_result = False

            case "2":
                if not history:
                    print("No history!")
                else:
                    for counter, item in enumerate(history, 1):
                        print(f"{counter}: {item}")

            case "3":
                if history and successful_result:
                    print("Choose an option in order to save into a file:")
                    print("1. Save into a txt file")
                    print("2. Save into a JSON file")
                    print("3. Save into a CSV file")

                    inner_option = input("Your choice: ")

                    match inner_option:
                        case "1":
                            FileProcessor.write_into_file("./files/result.txt", user_profile_info)
                        case "2":
                            FileProcessor.write_into_json(json_file_path, json_data)
                        case "3":
                            FileProcessor.write_into_csv("./files/result.csv", json_data)
                else:
                    print("No data to save!")

            case "0":
                exit(0)

            case _:
                print("Invalid option. Enter again!")


if __name__ == '__main__':
    main()
