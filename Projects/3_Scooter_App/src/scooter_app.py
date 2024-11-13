from scooter import Scooter
from user import User

class Scooter_App:
    def __init__(self):
        self.stations = {
        'Stockport': [],
        'Manchester': [],
        'Salford': []
        }
        self.registered_users = {}
    
    def register_user(self, username, password, age):
        if username in self.registered_users:
            raise Exception('Username is taken')
        if age < 18:
            raise Exception('User is too young')
        else:
            new_user = User(username, password, age)
            self.registered_users.update({username: new_user})