import unittest

from application import app
from helpers import generate_password

class RandomPassTestCase(unittest.TestCase):
    def test_index(self):
        """
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid.
        """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Random Pass' in response.data)
        self.assertTrue(b'PASSWORD GENERATOR TOOL' in response.data)
        self.assertTrue(b'Password Length' in response.data)


    def test_new_password(self):
        """
        WHEN the '/new-password' page is requested (POST)
        THEN check that the response is valid.
        """
        tester = app.test_client(self)
        response = tester.get('new-password', content_type='html/text')
        self.assertEqual(response.status_code, 405)


    def test_upper(self):
        """ Check that first password character is uppercase."""
        result = generate_password(8)
        self.assertTrue(result[0].isupper())


    def test_special_char(self):
        """ Check that second password character is a special character."""
        result = generate_password(8)
        self.assertFalse(result[1].isdigit() or result[1].islower() or result[1].isupper())


    def test_digit(self):
        """ Check that third password character is a number."""
        result = generate_password(8)
        self.assertTrue(result[2].isdigit())


    def test_lower(self):
        """ Check that remaining password characters are lowercase."""
        result = generate_password(8)
        self.assertTrue(result[3:].islower())


    def test_lenght(self):
        """ Check password lenght."""
        result = generate_password(8)
        self.assertEqual(len(result), 8)


if __name__ == '__main__':
    unittest.main()
