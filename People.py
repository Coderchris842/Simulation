import Locations
import Worldtime
# pop is how many peeps are in the universe
pop = {}
# Person model
class person:
    gender="male"
    class body:
        skincolor=2
        class head:
            class face:
                class eyes:
                    color = "brown"
                class mouth:
                    expression = "smile"
            class brain:
                emotion = "happy"
                IQ = 100
        class chest:
            class stomch:
                campacity = .2
            class heart:
                hearthp = 20
                bpm = 80
            class lungs:
                lung1hp = 20
                lung2hp = 20
            class body_fat:
                fats = 20
        class arms:
            size=2
        class legs:
            size=2
    class cloths:
        shirt = "red"
        pants = "blue"
        shoes = "on"
        hat = "off"
    class abstract:
        name="Bob"
        location = "void"
        birthday = Worldtime.readtime("year")
        age = 30
        def grow():
            age = Worldtime.readtime("year") - person.abstract.birthday
    def __init__(self, name):
        self.abstract.name= name
        pop[self.abstract.name] = self
# create people        
bob = person("Bob")
tim = person("Tim")

