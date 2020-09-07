from .SchedulerTime import Time, TimeSpan

def main():
    chris = Employee("Christopher Robin")
    chris.addAvailability(   TimeSpan(Time.asClock(12,30),Time.asClock(4,30))  )
    chris.addShift(TimeSpan( Time.asClock(1,0),Time.asClock(2,0)) )
    print(chris)


class Employee:
    def __init__(self, name):
        self.name = name
        self.availability = []
        self.shifts = []
    def addAvailability(self, timespan):
        self.availability.append(timespan)
    def addShift(self, timespan):
        self.shifts.append(timespan)

    def __str__(self):
        s = "\n\nEMPLOYEE:      {}".format(self.name)
        s +=  "\nAVAILABILITY:"
        for a in self.availability:
            s += "\n               {}".format(a)
        s += "\nSHIFTS:"
        for a in self.shifts:
            s += "\n               {}".format(a)
        s += "\n\n"
        return s


if  __name__ == "__main__":
    main()