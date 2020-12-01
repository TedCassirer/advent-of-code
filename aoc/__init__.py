from . import (
    day1,
)

solvers = {
    2020: {
        1: day1,
    },
}


def solve(day, year, data):
    return (part1(day, year, data), part2(day, year, data))


def part1(day, year, data):
    return solvers[year][day].part1(data)


def part2(day, year, data):
    return solvers[year][day].part2(data)
