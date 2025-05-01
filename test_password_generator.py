import pytest
from password_generator import PasswordGeneratorLogic
import string

@pytest.fixture
def password_generator():
    return PasswordGeneratorLogic()

def test_default_settings(password_generator):
    """Test that default settings are correct"""
    assert password_generator.uppercase is True
    assert password_generator.lowercase is True
    assert password_generator.special is True
    assert password_generator.numbers is True
    assert password_generator.length == 12

def test_generate_password_with_default_settings(password_generator):
    """Test password generation with default settings"""
    password = password_generator.generate_password()
    assert password is not None
    assert len(password) == 12
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert any(c in string.punctuation for c in password)
    assert any(c in string.digits for c in password)

def test_password_length(password_generator):
    """Test password generation with different lengths"""
    # Test minimum valid length
    password_generator.length = 4
    password = password_generator.generate_password()
    assert len(password) == 4

    # Test longer length
    password_generator.length = 20
    password = password_generator.generate_password()
    assert len(password) == 20

    # Test invalid length
    password_generator.length = 3
    password = password_generator.generate_password()
    assert password is None

def test_character_types(password_generator):
    """Test password generation with different character type combinations"""
    # Test only uppercase
    password_generator.uppercase = True
    password_generator.lowercase = False
    password_generator.special = False
    password_generator.numbers = False
    password = password_generator.generate_password()
    assert all(c in string.ascii_uppercase for c in password)

    # Test only lowercase
    password_generator.uppercase = False
    password_generator.lowercase = True
    password = password_generator.generate_password()
    assert all(c in string.ascii_lowercase for c in password)

    # Test only special characters
    password_generator.lowercase = False
    password_generator.special = True
    password = password_generator.generate_password()
    assert all(c in string.punctuation for c in password)

    # Test only numbers
    password_generator.special = False
    password_generator.numbers = True
    password = password_generator.generate_password()
    assert all(c in string.digits for c in password)

def test_no_character_types(password_generator):
    """Test password generation with no character types selected"""
    password_generator.uppercase = False
    password_generator.lowercase = False
    password_generator.special = False
    password_generator.numbers = False
    password = password_generator.generate_password()
    assert password is None

def test_mixed_character_types(password_generator):
    """Test password generation with mixed character types"""
    password_generator.uppercase = True
    password_generator.lowercase = True
    password_generator.special = False
    password_generator.numbers = False
    password = password_generator.generate_password()
    assert any(c in string.ascii_uppercase for c in password)
    assert any(c in string.ascii_lowercase for c in password)
    assert not any(c in string.punctuation for c in password)
    assert not any(c in string.digits for c in password) 