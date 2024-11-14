import pytest

from user import User

user = User('test_name', 'test_password', 20)

# Instance user created with correct details
def test_new_user_instance_details():
    assert user.username == 'test_name'
    assert user.age == 20
    assert not user.logged_in
    
# .login(password) raise exception if incorrect password provided
def test_login_with_incorrect_password():
    with pytest.raises(Exception, match='Password is incorrect'):
        user.login('password')

# .login(password) updates logged_in to true if correct password provided
def test_login_with_correct_password():
    user.login('test_password')
    assert user.logged_in

# .logout() updates logged_in to false
def test_logout():
    user.logout()
    assert not user.logged_in