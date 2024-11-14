import time # required for timer 

class Scooter:
    next_serial = 1
    
    def __init__(self, station):
        self.serial = Scooter.next_serial
        Scooter.update_serial()
        self.station = station
        self.user = None
        self.charge = 100
        self.is_broken = False

    @classmethod # class methods need the class passing as an argument
    def update_serial(cls):
        cls.next_serial += 1
    
    def __repr__(self): # this is required so the dictionary is return to the console instead of the classes position in memory
        if self.user == None:
            return(
            f'Scooter {self.serial} - Station: {self.station}, '
            f'Charge: {self.charge}%, '
            f'Status: {"Broken" if self.is_broken else "Functional"}'
        )
        else:
            return(
                f'Scooter {self.serial} - User: {self.user}, '
                f'Charge: {self.charge}%, '
                f'Status: {"Broken" if self.is_broken else "Functional"}'
        )
    
    def rent(self, user):
        if self.is_broken == True:
            raise Exception('Scooter is broken')
        elif self.charge <= 20:
            raise Exception('Scooter need to charge')
        else:
            self.user = user.username
            self.station = None
    
    def dock(self, station):
        self.station = station
        self.user = None
        self.repair()
        self.recharge()

    def recharge(self):
        if self.charge == 100:
            pass
        else:
            print('Scooter charge progress: ', end='')
            for i in range(1, self.charge):
                if i % 4 == 0:
                    print('|', end='')
            while self.charge < 100:
                time.sleep(0.0125)
                self.charge += 1
                if self.charge % 4 == 0:
                    print('|', end='')
            print('\nScooter fully charged')

    def repair(self):
        if self.is_broken:
            print('Scooter repair progress: ', end='')
            for i in range(25):
                time.sleep(0.05)
                print('|', end='')
            print('\nScooter repaired')
            self.is_broken = False

if __name__ == '__main__': # This code stops the the code below running when the module is imported
    
    scooter1 = Scooter('Station A')
    scooter2 = Scooter('Station B')
    scooter1.charge = 45
    scooter1.is_broken = True

    print(scooter1.__dict__)
    print(scooter2.__dict__)
    print(scooter1.dock('Station C'))