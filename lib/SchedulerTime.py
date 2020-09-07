def main():
    selfTest()

def selfTest():
    t1 = TimeSpan(
        Time.asClock(8,30,0),
        Time.asClock(5,30,4)
    )
    t2 = TimeSpan(
        Time.asClock(8,30),
        Time.asClock(5,30,4)
    )
    t3 = TimeSpan(
        Time.asClock(9,30),
        Time.asClock(9,40)
    )
    print(t1)
    print(t1==t2)
    print(t1==t3)
    print(t1<t3)
    print(t1>t3)
    print(len(t1))

class Time:
    """
    Time is a pure amount, without origin.
    Time should not be negative.
    """
    def __init__(self, minutes):
        if isinstance(minutes, int):
            self.minutes = abs(minutes)
        elif isinstance(minutes, Time):
            self.minutes = minutes.minutes
        else:
            raise Exception("Not a valid time.")
    @staticmethod
    def asClock(hours,minutes,days=0):
        return Time(Time.convertToMinutes(hours,minutes,days))

    @staticmethod
    def convertToMinutes(hours, minutes, days = 0):
        return minutes + (hours * 60) + (days * 24 * 60)
    @staticmethod
    def convertToClock(minutes):
        days = minutes / (24*60);   minutes -= days * (24*60)
        hours = minutes / 60;       minutes -= hours * 60
        return days, hours, minutes
    @staticmethod
    def convertToDayString(day):
        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        while day > 6:
            day -= 7
        return days.get(day, "Invalid Day")

    def clockString(self):
        t = Time.convertToClock(self.minutes)
        def z(n): #add zero to string if n<9
            return "0"+str(n) if n<10 else str(n)
        return "{}:{} {}".format(
            z(t[1]),
            z(t[2]),
            Time.convertToDayString(t[0])
        )
    
    def __add__(self, other):
        self.minutes += other.minutes
        return self
    def __sub__(self, other):
        self.minutes = abs(self.minutes-other.minutes)
        return self
    def __eq__(self, other):
        return self.minutes == other.minutes
    def __lt__(self, other):
        return self.minutes < other.minutes
    def __gt__(self, other):
        return self.minutes > other.minutes
    def __len__(self):
        return self.minutes
    def __str__(self):
        return "{} Minutes".format(self.minutes)
    def __repr__(self):
        return "Time: "+str(self)


class TimeSpan():
    """
    TimeSpan is an amount with reference to a local point of origin, or the distance (endpoint) from that point.
    """
    def __init__(self, start_time, end_time, name=""):
        # inherited from Time: minutes, type int
        if isinstance(start_time, Time) and isinstance(end_time, Time):
                self.start_time = start_time
                self.end_time = end_time
        else:
            raise Exception("One or more arguments are invalid times.")
        self.name = str(name)
    def length(self):
        return self.end_time-self.start_time

    def startTime(self,new_time=None):
        if new_time == None:
            return self.start_time
        else:
            self.start_time = new_time
            return self.start_time
    def endTime(self,new_time=None):
        if new_time == None:
            return self.end_time
        elif isinstance(new_time, Time):
            if new_time > self.start_time:
                self.end_time = new_time
            else:
                self.end_time = self.start_time
                self.start_time = new_time
        else:
            raise Exception("Not a valid time.")

    def __len__(self):
        return len(self.end_time-self.start_time)
    def __eq__(self, other):
        return (self.start_time == other.start_time) and \
            (self.end_time == other.end_time)
    def __lt__(self, other):
        return (self.start_time > other.start_time) and \
            (self.end_time < other.end_time)
    def __gt__(self, other):
        return (self.start_time < other.start_time) and \
            (self.end_time > other.end_time)
    def __str__(self):
        return "TimeSpan({}, {}{})".format(
            self.start_time.clockString(),
            self.end_time.clockString(),
            ", \"{}\"".format(self.name) \
                if self.name is not "" else ""
        )
    def __repr__(self):
        return str(self)

if  __name__ == "__main__":
    main()