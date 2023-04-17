import unittest
import requests

class TestServerResponse(unittest.TestCase):
    def setUp(self):
        print("Setup Called")

    def tearDown(self):
        print("Tearing Down Now")

    def test_connection(self):
        print("Executing test")
        response = requests.get("https://www.google.com")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
