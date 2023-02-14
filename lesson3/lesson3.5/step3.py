class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.tr = []

    def add_track(self, tr):
        self.tr.append(tr)

    def get_tracks(self):
        return tuple(self.tr)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __len__(self):
        start_x, start_y = self.start_x, self.start_y
        l = 0
        for i in self.tr:
            l += ((i.to_x - start_x) ** 2 + (i.to_y - start_y) ** 2) ** .5
            start_x, start_y = i.to_x, i.to_y
        return int(l)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))

res_eq = track2< track1
print(res_eq)
