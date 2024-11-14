from scooter import Scooter
from user import User

class Scooter_App:
    def __init__(self):
        self.stations = {
        'Station A': [],
        'Station B': [],
        'Station C': []
        }
        self.rented_scooters = []
        self.registered_users = {}
    
    def __repr__(self):
        repr = f'\n{'*'*80}\n{'*'*80}\n{'*'*80}\n\nStations:'
        for station in self.stations:
            repr += f'\n\n  {station}\n'
            for scooter in self.stations.get(station):
                repr += f'\n    {scooter}'
        repr += f'\n\n{'*'*80}\n{'*'*80}\n\nRented Scooter:\n'
        for scooter in self.rented_scooters:
            repr += f'\n    {scooter}'
        repr += f'\n\n{'*'*80}\n{'*'*80}\n\nRegistered Users:\n'
        for username in self.registered_users:
            repr += f'{self.registered_users.get(username)}\n'
        repr += f'\n{'*'*80}\n{'*'*80}'
        return repr
        # return f'\nStations:\n{self.stations}\n\nRented Scooters:\n{self.rented_scooters}\n\nRegistered User:\n{self.registered_users}'
    
    def register_user(self, username, password, age):
        if username in self.registered_users:
            raise Exception('Username is taken')
        if age < 18:
            raise Exception('User is too young')
        else:
            new_user = User(username, password, age)
            self.registered_users.update({username: new_user})
    
    def login_user(self, username, password):
        if username not in self.registered_users:
            raise Exception('Username not found')
        else:
            self.registered_users.get(username).login(password)
    
    def logout_user(self, username):
        if username not in self.registered_users:
            raise Exception('Username not found')
        if not self.registered_users.get(username).logged_in:
            raise Exception('User is not logged in')
        else:
            self.registered_users.get(username).logout()
    
    def create_scooter(self, station):
        if station not in self.stations:
            raise Exception('Station does not exist')
        else:
            new_scooter = Scooter(station)
            self.stations.get(station).append(new_scooter)
    
    def rent_scooter(self, scooter_serial, username):
        if username not in self.registered_users:
            raise Exception('Cannot rent scooter to an unknown user')
        elif not self.registered_users.get(username).logged_in:
            raise Exception('User must be logged in to rent a scooter')
        else:
            user = self.registered_users.get(username)
        if not user.rented_scooter == None:
            raise Exception('User can only rent one scooter at a time')
        else:
            scooter_found = False
            for station in self.stations:
                for scooter in self.stations.get(station):
                    if scooter_serial == scooter.serial:
                        scooter_found = True
                        scooter.rent(user)
                        self.rented_scooters.append(scooter)
                        self.stations.get(station).remove(scooter)
                        user.rented_scooter = scooter
                        print(f'Scooter {scooter.serial} has been rented to {user.username}')
            if not scooter_found:
                raise Exception('Scooter is not available to rent or does not exist')
    
    def dock_scooter(self, username, station):
        if username not in self.registered_users:
            raise Exception('Unknown user cannot dock scooter')
        else:
            user = self.registered_users.get(username)
            scooter = None
            for rented_scooter in self.rented_scooters:
                if rented_scooter.user == username:
                    scooter = rented_scooter
            if scooter == None:
                raise Exception('User does not have a scooter to dock')
            elif station not in self.stations:
                raise Exception('Cannot dock a scooter in an unknown station')
            else:
                user.rented_scooter = None
                scooter.dock(station)
                self.stations[station].append(scooter)
                self.rented_scooters.remove(scooter)
                print(f'Scooter {scooter.serial} has been docked at {scooter.station} station by user {user.username}')

if __name__ == '__main__':
    scooter_app = Scooter_App()
    scooter_app.register_user('user1', 'password123', 19)
    scooter_app.register_user('user2', 'P4$$w0rD', 18)
    scooter_app.login_user('user1', 'password123')
    scooter_app.login_user('user2', 'P4$$w0rD')
    for i in range(2):
        scooter_app.create_scooter('Station A')
    for i in range(2):
        scooter_app.create_scooter('Station B')
    for i in range(2):
        scooter_app.create_scooter('Station C')
    scooter_app.rent_scooter(6, 'user1')
    scooter_app.rent_scooter(4, 'user2')
    scooter_app.dock_scooter('user1', 'Station A')
    print(scooter_app)