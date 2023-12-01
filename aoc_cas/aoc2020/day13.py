def part_a(data):
    earliest, schedules = data.splitlines()
    earliest = int(earliest)
    schedules = [int(busId) for busId in schedules.split(",") if busId != "x"]
    busToTake = min(schedules, key=lambda busId: (-earliest % busId))
    return busToTake * (-earliest % busToTake)


def part_b(data):
    schedule = [(i, int(busId)) for i, busId in enumerate(data.splitlines()[1].split(",")) if busId != "x"]
    jump = 1
    time = 0
    for offset, busId in schedule:
        while (time + offset) % busId != 0:
            time += jump
        jump *= busId
    return time
