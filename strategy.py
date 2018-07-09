# Algorithms
class RepairCar:
    def working(self):
        print("Work: repairs cars")


class Treatment:
    def working(self):
        print("Work: heals people")


class SendingLetters:
    def working(self):
        print("Work: sending letters")


class Car:
    def __init__(self):
        pass

    def commute(self):
        print("Commute: by car")


class Bike:
    def __init__(self):
        pass

    def commute(self):
        print("Commute: by bike")


class Gym:
    def __init__(self):
        pass

    def spending_free_time(self):
        print("Free time: gym")


class ReadingBook:
    def spending_free_time(self):
        print("Free time: reading book")


# Contekst class
class Worker:
    def __init__(self, profession):
        self.profession = profession.upper()
        if (self.profession == "MECHANIC"):
            self.introduce()
            RepairCar.working(self)
            Car.commute(self)
            Gym.spending_free_time(self)
        elif (self.profession == "DOCTOR"):
            self.introduce()
            Treatment.working(self)
            Car.commute(self)
            ReadingBook.spending_free_time(self)
        elif (self.profession == "POSTMAN"):
            self.introduce()
            SendingLetters.working(self)
            Bike.commute(self)
            Gym.spending_free_time(self)
        else:
            self.introduce()
            print("This profession doesn't exist")

    def introduce(self):
        print("-----> ", self.profession, "<-----")


if __name__ == "__main__":
    Worker("Fireman")  # .methods()
    print("#####################")
    Worker("Mechanic")  # .methods()
    print("#####################")
    Worker("doctor")  # .methods()
    print("#####################")
    Worker("POSTMAN")  # .methods()
    print("#####################")
