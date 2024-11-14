import pytest

from scooter_app import Scooter_App

scooter_app = Scooter_App()

# Test 'scooter_app.__init__()'
def test_new_scooter_app_instance():
    assert scooter_app.__dict__ == {'registered_users': {}, 'rented_scooters': [], 'stations': {'Station B': [], 'Station C': [], 'Station A': []}}

# Tests for 'scooter_app.register_user()'
def test_can_register_new_user_aged_over_18():
    assert len(scooter_app.registered_users) == 0
    scooter_app.register_user('test_user', 'test_password', 18)
    assert len(scooter_app.registered_users) == 1
    test_user = scooter_app.registered_users.get('test_user')
    assert test_user.username == 'test_user'
    assert test_user.age == 18
    assert test_user.logged_in == False
    assert test_user.rented_scooter == None

def test_cannot_register_new_user_with_same_username():
    with pytest.raises(Exception, match='Username is taken'):
        scooter_app.register_user('test_user', 'test_password', 18)

def test_cannot_register_new_user_under_18():
    with pytest.raises(Exception, match='User is too young'):
        scooter_app.register_user('underage_test_user', 'test_password', 17)

# Tests for 'scooter_app.login_user()'
def test_user_can_login():
    test_user = scooter_app.registered_users.get('test_user')
    assert test_user.logged_in == False
    scooter_app.login_user('test_user', 'test_password')
    assert test_user.logged_in == True

def test_cannot_login_with_unknown_username():
    with pytest.raises(Exception, match='Username not found'):
        scooter_app.login_user('unknown_test_user', 'test_password')

def test_cannot_login_with_incorrect_password():
    with pytest.raises(Exception, match='Password is incorrect'):
        scooter_app.login_user('test_user', 'wrong_password')

# Tests for 'scooter_app.logout_user()'
def test_user_can_logout():
    test_user = scooter_app.registered_users.get('test_user')
    assert test_user.logged_in == True
    scooter_app.logout_user('test_user')
    assert test_user.logged_in == False

def test_cannot_logout_with_unknown_username():
    with pytest.raises(Exception, match='Username not found'):
        scooter_app.logout_user('unknown_test_user')

def test_cannot_logout_if_user_is_not_logged_in():
    with pytest.raises(Exception, match='User is not logged in'):
        scooter_app.logout_user('test_user')

# Tests for 'scooter_app.create_scooter()'
def test_can_create_new_scooters():
    # Test scooters can be created at Station A station
    assert len(scooter_app.stations['Station A']) == 0 # No scooter
    scooter_app.create_scooter('Station A')
    assert len(scooter_app.stations['Station A']) == 1 # 1 scooter
    test_scooter1 = scooter_app.stations['Station A'][0]
    assert test_scooter1.serial == 1
    assert test_scooter1.station == 'Station A'
    assert test_scooter1.user == None
    assert test_scooter1.charge == 100
    assert test_scooter1.is_broken == False
    
    # Test scooters can be created at Station B station
    scooter_app.create_scooter('Station B')
    assert len(scooter_app.stations['Station B']) == 1
    test_scooter2 = scooter_app.stations['Station B'][0]
    assert test_scooter2.serial == 2
    assert test_scooter2.station == 'Station B'
    assert test_scooter2.user == None
    assert test_scooter2.charge == 100
    assert test_scooter2.is_broken == False
    
    # Test scooters can be created at Station C station
    scooter_app.create_scooter('Station C')
    assert len(scooter_app.stations['Station C']) == 1
    test_scooter3 = scooter_app.stations['Station C'][0]
    assert test_scooter3.serial == 3
    assert test_scooter3.station == 'Station C'
    assert test_scooter3.user == None
    assert test_scooter3.charge == 100
    assert test_scooter3.is_broken == False
    
    # Test second scooter can be created at Station A station
    scooter_app.create_scooter('Station A')
    assert len(scooter_app.stations['Station A']) == 2 # 2 scooters

def test_cannot_create_new_scooters_at_unknown_station():
    with pytest.raises(Exception, match='Station does not exist'):
        scooter_app.create_scooter('unknown_station')

# Tests for 'scooter_app.rent_scooter()'
def test_can_rent_scooter_to_user(capsys):
    scooter_app.login_user('test_user', 'test_password')
    scooter_app.rent_scooter(1, 'test_user')
    # Checks logged information
    captured = capsys.readouterr()
    assert captured.out == 'Scooter 1 has been rented to test_user\n'
    # Checks the user object is updated with the scooter and the scooter object information is updated
    test_user = scooter_app.registered_users.get('test_user')
    assert test_user.rented_scooter.serial == 1
    assert test_user.rented_scooter.station == None
    assert test_user.rented_scooter.user == 'test_user'
    # Rented scooter list is updated
    assert len(scooter_app.rented_scooters) == 1
    assert scooter_app.rented_scooters[0].serial == 1
    assert scooter_app.rented_scooters[0].station == None
    assert scooter_app.rented_scooters[0].user == 'test_user'

def test_cannot_rent_unknown_scooter():
    with pytest.raises(Exception, match='Cannot rent scooter to an unknown user'):
        scooter_app.rent_scooter(1, 'unknown_test_user')

def test_cannot_rent_scooter_to_logged_out_user():
    scooter_app.register_user('second_test_user', 'test_password', 18)
    with pytest.raises(Exception, match='User must be logged in to rent a scooter'):
        scooter_app.rent_scooter(1, 'second_test_user')

def test_cannot_rent_second_scooter_user():
    with pytest.raises(Exception, match='User can only rent one scooter at a time'):
        scooter_app.rent_scooter(1, 'test_user')

def test_cannot_rent_scooter_to_two_user():
    scooter_app.login_user('second_test_user', 'test_password')
    with pytest.raises(Exception, match='Scooter is not available to rent or does not exist'):
        scooter_app.rent_scooter(1, 'second_test_user')

def test_cannot_rent_unknown_scooter_to_user():
    scooter_app.register_user('third_test_user', 'test_password', 18)
    scooter_app.login_user('third_test_user', 'test_password')
    with pytest.raises(Exception, match='Scooter is not available to rent or does not exist'):
        scooter_app.rent_scooter(100, 'third_test_user')

# Tests for 'scooter_app.dock_scooter()'
def test_can_dock_scooter_to_user(capsys):
    scooter_app.dock_scooter('test_user', 'Station C')
    # Checks logged information
    captured = capsys.readouterr()
    assert captured.out == 'Scooter 1 has been docked at Station C station by user test_user\n'
    # Checks the user object is updated with the scooter removed
    test_user = scooter_app.registered_users.get('test_user')
    assert test_user.rented_scooter == None
    # Check station list is updated
    assert len(scooter_app.rented_scooters) == 0
    assert len(scooter_app.stations['Station C']) == 2
    assert scooter_app.stations['Station C'][1].serial == 1
    assert scooter_app.stations['Station C'][1].user == None
    assert scooter_app.stations['Station C'][1].station == 'Station C'

def test_unknown_user_cannot_dock_scooter():
    with pytest.raises(Exception, match='Unknown user cannot dock scooter'):
        scooter_app.dock_scooter('unknown_test_user', 'Station A')

def test_user_cannot_dock_scooter_not_rented():
    with pytest.raises(Exception, match='User does not have a scooter to dock'):
        scooter_app.dock_scooter('second_test_user', 'Station A')

def test_user_cannot_dock_scooter_to_unknown_station():
    scooter_app.rent_scooter(1, 'second_test_user')
    with pytest.raises(Exception, match='Cannot dock a scooter in an unknown station'):
        scooter_app.dock_scooter('second_test_user', 'unknown_station')