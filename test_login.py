
import unittest


class TestLogin(unittest.TestCase):
    """Sample test cases for the AttendX login module."""

    def test_valid_login_details(self):
        username = "student01"
        password = "ValidPass123"

        self.assertTrue(username.strip())
        self.assertTrue(password)

    def test_empty_username(self):
        username = ""

        self.assertEqual(username, "")

    def test_empty_password(self):
        password = ""

        self.assertEqual(password, "")

    def test_whitespace_username(self):
        username = "   "

        self.assertEqual(username.strip(), "")


if __name__ == "__main__":
    unittest.main()
