class Light:
    def __init__(self):
        pass

    def on(self):
        pass

    def off(self):
        pass


class Door:
    def __init__(self):
        pass

    def open(self):
        pass

    def close(self):
        pass

    def lock(self):
        pass

    def unlock(self):
        pass


class HallLight(Light):

    def on(self):
        print("Hall light on")

    def off(self):
        print("Hall light off")


class LivingRoomLight(Light):

    def on(self):
        print("Living room light on")

    def off(self):
        print("Living room light off")


class MainDoor(Door):
    def open(self):
        print("Main door open")

    def close(self):
        print("Main room close")

    def lock(self):
        print("Main room lock")

    def unlock(self):
        print("Main room unlock")


class GarageDoor(Door):
    def open(self):
        print("Garage door open")

    def close(self):
        print("Garage room close")

    def lock(self):
        print("Garage room lock")

    def unlock(self):
        print("Garage room unlock")


class MainApi:
    def __init__(self):
        self.hallLight = HallLight()
        self.livingRoom = LivingRoomLight()
        self.mainDoor = MainDoor()
        self.garageDoor = GarageDoor()

    def lock_home(self):
        print("------ LOCK HOME ------")
        self.hallLight.off()
        self.livingRoom.off()
        self.garageDoor.lock()
        self.mainDoor.lock()

    def unlock_home(self):
        print("------ UNLOCK HOME ------")
        self.hallLight.on()
        self.livingRoom.on()
        self.garageDoor.unlock()
        self.mainDoor.unlock()

    def light_on(self):
        print("------ LIGHT ON ------")
        self.livingRoom.on()
        self.hallLight.on()

    def light_off(self):
        print("------ LIGHT OFF ------")
        self.hallLight.off()
        self.livingRoom.off()


if __name__ == "__main__":
    mainApi = MainApi()
    mainApi.unlock_home()
    mainApi.light_on()
    mainApi.light_off()
    mainApi.lock_home()
