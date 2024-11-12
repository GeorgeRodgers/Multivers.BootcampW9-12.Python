import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    
    # In both of the test below we had written code to set up the phonebook
    # We can override the setUp() method for the unittest class to create the phonebook before each test
    
    def setUp(self) -> None:
        self.phonebook = Phonebook()
        
    
    def test_lookup_by_name(self):
        # phonebook = Phonebook()
        self.phonebook.add('Bob', '12345') # We have to prefix the phonebook with 'self.' using this method
        number = self.phonebook.lookup('Bob')
        self.assertEqual(number, '12345')
        self.assertRaises
        
    def test_missing_name(self):
        # phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')