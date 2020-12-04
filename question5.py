class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.seconds = seconds
        self.set_Clock(hours, minutes, seconds)

        if hours<0 or hours>=24:
            raise ValueError
        if minutes<0 or minutes>=60:
            raise ValueError
        if seconds<0 or seconds>=60:
            raise ValueError
    
    def set_Clock(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

        if hours<0 or hours>=24:
            raise ValueError
        if minutes<0 or minutes>=60:
            raise ValueError
        if seconds<0 or seconds>=60:
            raise ValueError
    
    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self.__hours, self.__minutes, self.__seconds)

    def tick(self):
        if self.__seconds==59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes==60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours==24:
                    self.__hours = 0
        else:
            self.__seconds += 1

class Calendar:
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        if (year%400==0 or (year%4==0 and year%100!=0)):
            return True
        elif (year%4!=0 and year%100==0):
            return False
        else:
            return False
    
    def __init__(self, d, m, y):
        self.set_Calendar(d, m, y)

    def set_Calendar(self, d, m, y):
        if d in range(1, Calendar.months[m-1]+1):
            self.__days = int(d)
        if m in range(1, len(Calendar.months)+1):
            self.__months = int(m)
        if y > 0:
            self.__years = 0000+int(y)
        
    def __str__(self):
        if Calendar.date_style == "British":
            return ("{0:02d}/{1:02d}/{2:02d}".format(self.__days,self.__months,self.__years))
        if Calendar.date_style == "American":
            return("{1:02d}/{0:02d}/{2:04d}".format(self.__days,self.__months,self.__years))

    def advance(self):

        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1


class CalendarClock(Calendar, Clock):
    def __init__(self , days, months, years, hours, minutes, seconds):     
        Calendar.__init__(self, days, months, years)
        Clock.__init__(self, hours, minutes, seconds)


    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)
    
    def tick(self):
        if Clock.__str__(self) == "23:59:59":
            self.advance()
            Clock.tick(self)
        else:
            Clock.tick(self)

x = CalendarClock(31, 12, 2013, 23, 59, 59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28, 2, 1900, 23, 59, 59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28, 2, 2000, 23, 59, 59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(7, 2, 2013, 13, 55, 40)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)
