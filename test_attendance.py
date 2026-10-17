
import unittest


class TestAttendance(unittest.TestCase):
    """Sample test cases for the AttendX attendance module."""

    def test_valid_attendance_status(self):
        status = "Present"

        self.assertIn(status, ["Present", "Absent"])

    def test_absent_attendance_status(self):
        status = "Absent"

        self.assertIn(status, ["Present", "Absent"])

    def test_invalid_attendance_status(self):
        status = "Unknown"

        self.assertNotIn(status, ["Present", "Absent"])


if __name__ == "__main__":
    unittest.main()
