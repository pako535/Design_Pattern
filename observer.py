from random import randint


class Observer:
    def __init__(self, name, totolotek):
        self.name = name
        self.results = [0, 0, 0, 0, 0]
        self.totolotek = totolotek

    def __repr__(self):
        return "\nThe result of today's draw: {} is: {}".format(str(self.name), str(self.results))

    def update(self, results):
        self.results = results

    def leave(self):
        self.totolotek.observers.remove(self)


class TV(Observer):

    def __init__(self, totolotek):
        super().__init__("TV", totolotek)

    def notify(self):
        print("Wynik dzisejszego losowania on the TV to: {}").format(self.results)


class Internet(Observer):

    def __init__(self, totolotek):
        super().__init__("INTERNET", totolotek)

    def notify(self):
        print("the result of today's draw on the INTERNET to: {}").format(self.results)


class TotoLotek:
    def __init__(self):
        self.observers = []
        self.results = [0, 0, 0, 0, 0]

    def __str__(self):
        return "\n\nResults: {}\nAssigned observers: {}".format(str(self.results), str([i for i in self.observers]))

    def random(self):
        self.results = []
        for i in range(5):
            self.results.append(randint(1, 100))

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, name):
        self.observers = [observer for observer in self.observers if observer.name != name]

    def notify_observers(self):
        for i in self.observers:
            i.update(self.results)


if __name__ == "__main__":
    totlotek = TotoLotek()
    tv = TV(totlotek)
    internet = Internet(totlotek)
    totlotek.add_observer(tv)
    totlotek.add_observer(internet)

    # firts rand
    totlotek.random()
    print(totlotek)
    totlotek.notify_observers()

    #second rand
    totlotek.random()
    print(totlotek)

    # tv now not observing totoltek
    tv.leave()
    totlotek.random()
    totlotek.notify_observers()
    print(totlotek)
    print(tv)

