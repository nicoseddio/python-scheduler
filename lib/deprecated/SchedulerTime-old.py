def main():
    selfTest()

class Time:
    def __init__(self, hm, m=None):
        self.m = hm if m==None else (m+(hm*60))
    def __add__(self, other):
        return Time(self.m+other.m)
    def __sub__(self, other):
        return Time(self.m-other.m)
    def __str__(self):
        return "{} Minutes".format(self.m)
    def __repr__(self):
        return str(self)

class ClockTime:
    def __init__(self, h=0, m=0, d=0):
        self.h = h
        self.m = m
        self.d = d
        self.validate()
    
    def dayString(self):
        days = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday"
        }
        return days.get(self.d, "Invalid Day")

    def validate(self):
        def v(n,l,u): #return n within bounds of l and u
            return l if n<l else u if n>u else n
        h,m,d = self.h,self.m,self.d
        while m>59:
            h+=1
            m-=60
        while m<0:
            h-=1
            m+=60
        while h>23:
            d+=1
            h-=24
        while h<0:
            d-=1
            h+=24
        while d>6:
            d-=7
        while d<0:
            d+=7
        self.h = h
        self.m = m
        self.d = d

    def add(self,h=0,m=0,d=0):
        self.h += h
        self.m += m
        self.d += d
        self.validate()
        return self
    def subtract(self,h=0,m=0,d=0):
        self.h -= h
        self.m -= m
        self.d -= d
        self.validate()
        return self

    def copy(self,other=None):
        if other==None:
            self.h = other.h
            self.m = other.m
            self.d = other.d
            return self
        else:
            return Time(self.h,self.m,self.d)
    def __str__(self):
        def z(n): #add zero to string if n<9
            return "0"+str(n) if n<10 else str(n)
        return "{}:{} {}".format(
            z(self.h),
            z(self.m),
            self.dayString()
        )
    def __repr__(self):
        return str(self)

class TimeSpan:
    def __init__(self, start_time, end_time):
        self.start_time = start_time.copy()
        self.end_time = end_time.copy()
    def lenth(self):
        return self.end_time-self.start_time

        


def selfTest():
    print(ClockTime(12,50))
    print(ClockTime(13,15).add(12,50))
    print(ClockTime(13,15).subtract(13,16))
    print(Time(50))
    print(Time(40)-Time(60))


if  __name__ == "__main__":
    main()