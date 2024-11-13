import pytest

from src.scooter import Scooter

scooter1 = Scooter('Stockport')
scooter2 = Scooter('Manchester')
scooter3 = Scooter('Salford')

# Test if the scooter station is set to provided value when an instance of the scooter is created
def test_new_scooter_station():
    assert scooter1.station == 'Stockport'
# Test if the scooter user is set to null hen an instance of the scooter is created
def test_new_scooter_user():
    assert scooter1.user == None
# Test charge and isBroken attributes have the correct values when when an instance of the scooter is created
def test_new_scooter_charge_and_is_broken():
    assert scooter1.charge == 100
    assert scooter1.is_broken == False

# test serial numbers are sequentially applied to new instances of scooters
# Test next serial is updated upon creation of a new instance of the scooter
def test_serial_sequentially_updates():
    assert scooter1.serial == 1
    assert scooter2.serial == 2
    assert scooter3.serial == 3

# Test '.rent(user)' method updates the scooters user and station, throws an error if the charge is below 20% or the scooter is broken
def test_scooter_can_be_rented():
    scooter1.rent('test_user')
    assert scooter1.user == 'test_user'
    assert scooter1.station == None

def test_scooter_cannot_be_rented_if_low_charge():
    scooter1.charge = 20
    with pytest.raises(Exception, match='Scooter need to charge'):
        scooter1.rent('test_user')

def test_scooter_cannot_be_rented_if_is_broken():
    scooter1.is_broken = True
    with pytest.raises(Exception, match='Scooter is broken'):
        scooter1.rent('test_user')

# Test '.dock(station)' method updates the scooters station and user
def test_scooter_can_be_docked():
    scooter1.dock('test_station')
    assert scooter1.station == 'test_station'
    assert scooter1.user == None

# Test '.dock(station)' calls '.recharge()' and '.requestRepair()'
def test_dock_repairs_broken_scooter():
    scooter1.is_broken = True
    scooter1.dock('test_station')
    assert scooter1.is_broken == False

def test_dock_recharges_scooter():
    scooter1.charge = 0
    scooter1.dock('test_station')
    assert scooter1.charge == 100

# Test '.recharge()' recharges the scooter and logs the progress

def test_recharge_charges_the_scooter_and_logs_progress(capsys):
    scooter1.charge = 0
    scooter1.recharge()
    captured = capsys.readouterr() # This code captures code logged to the console
    assert captured.out == 'Scooter charge progress: |||||||||||||||||||||||||\nScooter fully charged\n'
    assert scooter1.charge == 100

# Test '.requestRepair()' method check if the scooter need repairing and repairs

def test_recharge_charges_the_scooter_and_logs_progress(capsys):
    scooter1.repair()
    captured = capsys.readouterr()
    assert captured.out == ''
    scooter1.is_broken = True
    scooter1.repair()
    captured = capsys.readouterr() # This code captures code logged to the console
    assert captured.out == 'Scooter repair progress: |||||||||||||||||||||||||\nScooter repaired\n'
    assert scooter1.is_broken == False