import time # required for timer 

class Scooter:
    next_serial = 1
    
    def __init__(self, station):
        self.station = station
        self.user = None
        self.serial = Scooter.next_serial
        Scooter.update_serial()
        self.charge = 100
        self.is_broken = False

    @classmethod # class methods need the class passing as an argument
    def update_serial(cls):
        cls.next_serial += 1
    
    def rent(self, user):
        if self.is_broken == True:
            raise Exception('Scooter is broken')
        elif self.charge <= 20:
            raise Exception('Scooter need to charge')
        else:
            self.user = user
            self.station = None
    
    def dock(self, station):
        self.station = station
        self.user = None
        self.repair()
        self.recharge()

    def recharge(self):
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
    
    scooter1 = Scooter('Stockport')
    scooter2 = Scooter('Manchester')
    scooter1.charge = 45
    scooter1.is_broken = True

    print(scooter1.__dict__)
    print(scooter2.__dict__)
    print(scooter1.dock('Salford'))