import Worldtime
import People
import Locations
while True:
    Worldtime.multitime(input("What unit of time to use?"), input("How many units should pass?"))
    if input("stop?(Y/N)") == "Y":
        break
