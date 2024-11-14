class User:
    def __init__(self, username, password, age):
        self.username = username
        self.__password = password
        self.age = age
        self.logged_in = False
        self.rented_scooter = None
    
    def __repr__(self): # this is required so the dictionary is return to the console instead of the classes position in memory
        return (
            f'\n    username: {self.username}, '
            f'\n    password: {'*'*len(self.__password)}, '
            f'\n    age: {self.age}, '
            f'\n    logged_in: {self.logged_in}, '
            f'\n    rented_scooter: {self.rented_scooter}'
        )
    
    def login(self, password):
        if self.__password == password:
            self.logged_in = True
        else:
            raise Exception('Password is incorrect')

    def logout(self):
        self.logged_in = False