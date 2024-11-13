class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.logged_in = False
    
    def login(self, password):
        if self.password == password:
            self.logged_in = True
        else:
            raise Exception('Password is incorrect')

    def logout(self):
        self.logged_in = False