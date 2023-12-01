# import argparse
# import importlib
# from aocd import get_data
# parser = argparse.ArgumentParser(description="Process some integers.")
# parser.add_argument("--year", "-y", type=int, default=2021)
# parser.add_argument("--day", "-d", type=int)
# parser.add_argument("--file", "-f", type=argparse.FileType("r"))
#
# args = parser.parse_args()
#
#
#
#
# def main():
#     moduleName = "aoc{}.day{}".format(args.year, args.day)
#     try:
#         mod = importlib.import_module(moduleName)
#     except:
#         raise Exception(f"Unable to load module %s" % moduleName)
#     if args.file:
#         data = args.file.read()
#     else:
#         data = get_data(day=args.day, year=args.year)
#     part1 = mod.part1(data)
#     part2 = mod.part2(data)
#
#     return part1, part2
#
#
# if __name__ == "__main__":
#     print(main())


import click


@click.command()
def mycommand():
    """Your command description."""
    # Your command logic here
    print("Running my command...")


print("poop")
