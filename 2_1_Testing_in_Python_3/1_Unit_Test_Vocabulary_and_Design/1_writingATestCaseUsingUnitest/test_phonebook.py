# A phonebook is a collection of names correlating to a number
# If a phonebook is consistent no numbers are a prefix of the other

# 'unittest' is a class that can be imported and inherited from
import unittest

# We also need to import the Phonebook class from phonebook.py

from .phonebook import Phonebook

# In order for the tests to run properly we need to mark the folder containing the test files as a package
# This is done by adding a empty '__init__.py'to the folder

class PhonebookTest(unittest.TestCase):
    # Each test is defined as a function
    def test_lookup_by_name(self):
        phonebook = Phonebook()
        phonebook.add('Bob', '12345')
        number = phonebook.lookup('Bob')
        self.assertEqual(number, '12345')

# Given the class function doesn't do anything, this test fails

# run cmd 'python -m unittest'