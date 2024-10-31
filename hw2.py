import data
from data import Duration


# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1 : data.Point, p2 : data.Point) -> data.Rectangle:
    topleftcornerpoint = data.Point(min(p1.x, p2.x), max(p1.y, p2.y))
    bottomrightcornerpoint = data.Point(max(p1.x, p2.x), min(p1.y, p2.y))
    return data.Rectangle(topleftcornerpoint, bottomrightcornerpoint)

# Part 2
def shorter_duration_than(d1 : data.Duration, d2 : data.Duration) -> bool:
    d1secs = d1.minutes * 60 + d1.seconds
    d2secs = d2.minutes * 60 + d2.seconds

    if d1secs < d2secs:
        return True
    else:
        return False


# Part 3
def song_shorter_than(playlist : list[data.Song], time : data.Duration) -> list[data.Song]:
    shortsongs = []
    for i in range(len(playlist)):
        if shorter_duration_than(playlist[i].duration, time):
            shortsongs.append(playlist[i])
    return shortsongs


# Part 4
def running_time(songs : list[data.Song], playlist : list[int]) -> data.Duration:
    secs = 0
    for i in range(len(playlist)):
        if 0 <= i < len(songs):
            newtime = songs[i].duration
            secs += newtime.minutes * 60 + newtime.seconds
    fullmins = secs // 60
    extrasecs = secs % 60
    return Duration(fullmins, extrasecs)


# Part 5
def validate_route(citylinks : list[list[str]], route : list[str]) -> bool:
    if len(route) == 0 or len(route) == 1:
        return True
    for i in range(len(route) - 1):
        c1, c2 = route[i], route[i + 1]
        if [c1, c2] not in citylinks and [c2, c1] not in citylinks:
            return False
    return True


# Part 6
def longest_repetition(sumnums : list[int]) -> int:
    highestcount = 0
    highestplacement = None
    currentcount = 1
    currentindex = 0
    if len(sumnums) == 0:
        return None
    for i in range(1, len(sumnums)):
        if sumnums[i] == sumnums[i-1]:
            currentcount += 1
        else:
            if currentcount > highestcount:
                highestcount = currentcount
                highestplacement = currentindex
            currentcount = 1
            currentindex = i
    if currentcount > highestcount:
        highestplacement = currentindex
    return highestplacement



