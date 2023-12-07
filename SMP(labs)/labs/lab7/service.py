import json
import pyfiglet
from colorama import Fore
import requests
from prettytable import PrettyTable
import regex
import config as config

fonts = {index: font for index, font in enumerate(sorted(pyfiglet.FigletFont.getFonts()))}

class UserProfileService:
    def get_personal_profile(self, username: str):
        if not username or not isinstance(username, str) or not regex.match(
            "^[\w](?!.*?\.{2})[\w.]{1,28}[\w]$", username
        ):
            raise ValueError("Invalid username format!")

        query_params = {"username": username}
        headers = {
            "X-RapidAPI-Key": config.X_RapidAPI_Key,
            "X-RapidAPI-Host": config.X_RapidAPI_Host
        }

        response = requests.get(config.get_personal_profile, headers=headers, params=query_params)

        if response.status_code != 200:
            error_message = response.json().get('message', 'Unknown error occurred!')
            raise ValueError(f"Error occurred! {error_message}")
        else:
            return response.json()


class ProfileTableDisplayer:

    def display_profile(self, json_data: str):
        data = json.loads(json_data)
        table = PrettyTable()
        table.field_names = ["Attribute", "Value"]

        allowed_keys = {
            "id", "biography", "full_name", "is_business_account", "category_name", "is_private", "username"
        }

        for key, value in data.items():
            if key in allowed_keys:
                table.add_row([f"{Fore.YELLOW + key + Fore.RESET}", value])

        return table.get_string()
