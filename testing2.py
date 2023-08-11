# PROGRAMMING AND ALGIRITHMS 2
# NAME = Rahul Kumar Thakur
# STUDENT ID = 220135
# COURSEWORK ASSIGNMENT = 1
#                         Unit Testing For Project 1

import unittest
from final1 import singleportinput

class TestPortScanner(unittest.TestCase):
    def test_singleportinput_valid_inputs(self):
        target = "127.0.0.1"
        port = "80"
        expected_result = "Some expected result"  # Define the expected result
        result = singleportinput(target, port)
        self.assertEqual(result, expected_result)

    def test_singleportinput_invalid_inputs(self):
        target = "invalid_ip"
        port = "invalid_port"
        with self.assertRaises(ValueError):
            singleportinput(target, port)

if __name__ == '__main__':
    unittest.main()
