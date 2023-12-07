import unittest
from unittest.mock import patch
from service import UserProfileService

class TestUserProfileService(unittest.TestCase):

    @patch('service.requests.get')
    def test_get_personal_profile_success(self, mock_get):
        username = "apple"
        expected_response = {"id": "5821462185"}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        user_service = UserProfileService()
        result = user_service.get_personal_profile(username)

        self.assertEqual(result, expected_response)

    @patch('service.requests.get')
    def test_get_personal_profile_error_response(self, mock_get):
        username = "panfffffiv"
        error_message = "User not found"
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"message": error_message}

        user_service = UserProfileService()

        with self.assertRaises(ValueError) as context:
            user_service.get_personal_profile(username)

        self.assertIn(error_message, str(context.exception))

if __name__ == '__main__':
    unittest.main()
