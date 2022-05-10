import time
# Keeps track of time (duh)
class meas:
    # Measures each unit of time and conversions
    intime=0
    minsize=30
    hoursize=30
    daysize=6
    yearsize=132
    def second(amount):
        return amount
    def minute(amount):
        return minsize*amount
    def hour(amount):
        return amount*meas.minsize*meas.hoursize
    def day(amount):
        return amount*meas.minsize*meas.hoursize*meas.daysize
    def year(amount):
        return amount*meas.minsize*meas.hoursize*meas.daysize*meas.yearsize
# Pushes time forward (only forward) by units
def second():
    time.sleep(0.05)
    meas.intime+=1
def minute():
    for i in range(30):
        second()
def hour():
    for i in range(30):
        minute()
def day():
    for i in range(6):
        hour()
# Reads how much time has passes
def readtime(unit):
    if unit=="second":
        return meas.intime
    elif unit=="minute":
        return meas.intime/30
    elif unit=="hour":
        return (meas.intime/30)/30
    elif unit=="day":
        return ((meas.intime/30)/30)/6
    elif unit=="year":
        return ((meas.intime/30)/30)/6/132
def multitime(unit, lstime):
    if unit == "second":
        for i in range(lstime):
            second()
    elif unit == "minute":
        for i in range(lstime):
            minute()
    elif unit == "hour":
        for i in range(lstime):
            hour()
    elif unit == "day":
        for i in range(lstime):
            day()
    
        
