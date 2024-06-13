class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    # Getter methods
    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    # Overloading the '+' operator
    def __add__(self, other_time):
        total_seconds = (self.__hour + other_time.get_hour()) * 3600 + \
                        (self.__minute + other_time.get_minute()) * 60 + \
                        (self.__second + other_time.get_second())
        
        new_hour = total_seconds // 3600
        total_seconds %= 3600
        new_minute = total_seconds // 60
        new_second = total_seconds % 60

        return Time(new_hour, new_minute, new_second)

    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

time1 = Time(5, 30, 45)
time2 = Time(3, 15, 20)
sum_time = time1 + time2

print(f"Time 1: {time1}")
print(f"Time 2: {time2}")
print(f"Sum of Time 1 and Time 2: {sum_time}")
