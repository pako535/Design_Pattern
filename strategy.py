# class Working:
#     def __init__(self):
#         pass
    
#     def working(self):
#         pass


# class Commute:
#     def __init__(self):
#         pass
    
#     def commute(self):
#         pass


# class SpendingFreeTime:
#     def __init__(self):
#         pass

#     def spending_free_time(self):
#         pass


# Algorithms
class RepairCar(Working):
    def working(self):
        print("Work: repairs cars")


class Treatment(Working):
    def working(self):
        print("Work: heals people")


class SendingLetters(Working):
    def working(self):
        print("Work: sending letters")


class Car(Commute):
    def commute(self):
        print("Commute: by car")

class Bike(Commute):
    def commute(self):
        print("Commute: by bike")

class Gym(SpendingFreeTime):
    def spending_free_time(self):
        print("Free time: gym")

class ReadingBook(SpendingFreeTime):
    def spending_free_time(self):
        print("Free time: reading book")


# Contekst class
class Worker:
    def __init__(self, profession):
        self.working = Working()
        self.commute = Commute()
        self.spending_free_time = SpendingFreeTime()
        profession = profession.upper()
        if(profession == "MECHANIC"):
            self.working = RepairCar.working(self)
            self.commute = Car.commute(self)
            self.spending_free_time = Gym.spending_free_time(self) 
        elif(profession == "DOCTOR"):
            self.working = Treatment.working(self)
            self.commute = Car.commute(self)
            self.spending_free_time = ReadingBook.spending_free_time(self)
        elif(profession == "POSTMAN"):
            self.working = SendingLetters.working(self)
            self.commute = Bike.commute(self)
            self.spending_free_time = Gym.spending_free_time(self)
        else:
            print("This profession doesn't exist")


if __name__ == "__main__":
    Worker("Fireman")#.methods()
    print("#####################")
    Worker("Mechanic")#.methods()
    print("#####################")
    Worker("doctor")#.methods()
    print("#####################")
    Worker("POSTMAN")#.methods()
    print("#####################")
    