class DeltaClock:
    def __init__(self, clock1, clock2):

        self.dt = clock1.get_time() - clock2.get_time()
        if self.dt < 0:
            self.dt = 0
        self.hours = self.dt // 3600
        self.minutes = (self.dt - self.hours * 3600) // 60
        self.seconds = self.dt % 60

    def __str__(self):
        return f"{str(self.hours).zfill(2)}: {str(self.minutes).zfill(2)}: {str(self.seconds).zfill(2)}"

    def __len__(self):
        return self.dt
        pass


class Clock:
    def __init__(self, hours, minutes, seconds):
        self.time = hours * 3600 + minutes * 60 + seconds

    def get_time(self):
        return self.time

dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt) # 01: 30: 00
len_dt = len(dt) # 5400