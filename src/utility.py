from itertools import islice

def take(n, iterable):
    return list(islice(iterable, n))

color = {"R": (255, 0, 0), "G": (0, 255, 0), "B": (0, 0, 255)}
axes_misc = {"X": [15, 100], "Y": [30, 100], "Z": [45, 1]}
