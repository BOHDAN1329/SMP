import json
import requests
from prettytable import PrettyTable
import regex
from labs.config import urls_config, credentials_config
from labs.config.logger_config import logger


class UserService:
    @staticmethod
    def get_personal_profile(linkedin_url: str):
        if not isinstance(linkedin_url, str) or not linkedin_url:
            raise ValueError("URL must be a non-empty string.")

        if not regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                           "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url):
            raise ValueError("URL does not match the pattern.")

        querystring = {"linkedin_url": linkedin_url, "include_skills": "false"}
        headers = {"X-RapidAPI-Key": credentials_config.X_RAPID_API_KEY,
                   "X-RapidAPI-Host": credentials_config.X_RAPID_API_HOST}

        response = requests.get(urls_config.GET_PERSONAL_PROFILE, headers=headers, params=querystring, timeout=15)
        if response.status_code != 200:
            error_message = response.json().get('message', '')
            logger.error(f"The response status code is not 200. Error message: {error_message}")
            raise ValueError(f"Error occurred: {error_message}")

        return response.json()

    @staticmethod
    def get_profiles_posts(linkedin_url: str):
        if not isinstance(linkedin_url, str) or not linkedin_url:
            raise ValueError("URL must be a non-empty string.")

        if not regex.match("^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b(["
                           "-a-zA-Z0-9@:%._\\+~#?&//=]*)$", linkedin_url):
            raise ValueError("URL does not match the pattern.")

        querystring = {"linkedin_url": linkedin_url, "type": "posts"}
        headers = {"X-RapidAPI-Key": credentials_config.X_RAPID_API_KEY,
                   "X-RapidAPI-Host": credentials_config.X_RAPID_API_HOST}

        response = requests.get(urls_config.GET_PROFILES_PHOTO, headers=headers, params=querystring, timeout=15)
        if response.status_code != 200:
            error_message = response.json().get('message', '')
            logger.info(f"The response status code is not 200. Error message: {error_message}")
            raise ValueError(f"Error occurred: {error_message}")

        return response.json()


class DisplayInTableService:
    @staticmethod
    def display_personal_profile(json_data: str):
        data = json.loads(json_data)
        is_experiences = False
        is_educations = False
        outer_table = PrettyTable()
        outer_table.field_names = ["Attribute", "Value"]

        for key, value in data['data'].items():
            if key not in ['educations', 'experiences']:
                outer_table.add_row([key, value])

        if 'educations' in data['data']:
            inner_educations_table = PrettyTable()
            inner_educations_table.field_names = ["School", "Degree", "Date Range"]

            for education in data['data']['educations']:
                is_educations = True
                inner_educations_table.add_row(
                    [education.get('school', ''), education.get('degree', ''), education.get('date_range', '')])

            if is_educations:
                outer_table.add_row(["Educations", inner_educations_table.get_string()])

        if 'experiences' in data['data']:
            inner_experiences_table = PrettyTable()
            inner_experiences_table.field_names = ["Company", "Title", "Duration"]

            for experience in data['data']['experiences']:
                inner_experiences_table.add_row(
                    [experience.get('company', ''), experience.get('title', ''), experience.get('duration', '')])

            if is_experiences:
                outer_table.add_row(["Experiences", inner_experiences_table.get_string()])

        return outer_table.get_string()

    @staticmethod
    def display_profiles_posts(json_data: str, result=""):
        data = json.loads(json_data)
        outer_table = PrettyTable()
