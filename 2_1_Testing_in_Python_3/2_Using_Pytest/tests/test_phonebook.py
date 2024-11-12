# Pytest is an alternative python testing framework that is more native to python
# Pytest can be install using the following cmd 'pip install -U pytest'
# Tests are run with the following cmd 'python -m pytest'
# Pytest doesn't require importing of the framework to the test file or the need to create an inherited test class
# However there are some useful methods that can be imported
import pytest

from src.phonebook import Phonebook # Because the phonebook is stored in the src folder this must be referenced

# To keep our code 'DRY' we can add fixtures so we don't repeat code, like that used to set up the phonebook

@pytest.fixture # decorator required for function
def phonebook():
    phonebook = Phonebook()
    phonebook.add("Bob", "12345")
    phonebook.add("Rob", "54321")
    return phonebook

def test_look_up_by_name(phonebook): # We need to pass the fixture to the test as an argument
    number = phonebook.lookup("Bob") # query dictionary
    assert number == "12345" # The assert keyword is used for testing

def test_find_all(phonebook):
    assert phonebook.all_names() == {"Bob", "Rob"} # Phonebook method should return a set with the correct names
    
def test_missing_name(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Greg")

# def test_is_consistent_with_different_entries(phonebook):
#     assert phonebook.is_consistent()

# def test_inconsistent_with_different_entries(phonebook):
#     phonebook.add("Sue", "12345")
#     assert not phonebook.is_consistent()

# def test_inconsistent_with_duplicate_prefix(phonebook):
#     phonebook.add("Sue", "123")
#     assert not phonebook.is_consistent()

# Instead of writing out the three separate test all run the same assertion we can parameterize them

@pytest.mark.parametrize(
    "entry, is_consistent", [
        (("anne", "54789"), True),
        (("Sue", "12345"), False),
        (("Sue", "123"), False)
    ]
)
def test_is_consistent_with_different_entries(phonebook, entry, is_consistent):
    phonebook.add(*entry)
    assert phonebook.is_consistent() == is_consistent