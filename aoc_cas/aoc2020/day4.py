import re

passportRegex = re.compile(r"(\w{3}):(\S+)\s?")
hairColorRegex = re.compile(r"^#[a-f0-9]{6}$")
pidRegex = re.compile(r"^\d{9}$")
eyeColorRegex = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
heightRegex = re.compile(r"^(\d+)(in|cm)")


def getPassports(data):
    for line in data.split("\n\n"):
        yield {field: value for field, value in passportRegex.findall(line)}


def verifyHeight(f):
    match = heightRegex.match(f)
    if not match:
        return False
    val, unit = match.groups()
    if unit == "cm":
        return 150 <= int(val) <= 193
    elif unit == "in":
        return 59 <= int(val) <= 76
    raise Exception("What the!?")


passportFields = {
    "byr": lambda f: 1920 <= int(f) <= 2002,
    "iyr": lambda f: 2010 <= int(f) <= 2020,
    "eyr": lambda f: 2020 <= int(f) <= 2030,
    "hgt": verifyHeight,
    "hcl": hairColorRegex.match,
    "ecl": eyeColorRegex.match,
    "pid": pidRegex.match,
    "cid": lambda f: True,
}
requiredFields = frozenset(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def containsRequiredFields(passport):
    return requiredFields.issubset(passport)


def verifyFields(passport):
    return all(passportFields[f](v) for f, v in passport.items())


def part_a(data):
    passports = getPassports(data)
    return sum(containsRequiredFields(p) for p in passports)


def part_b(data):
    passports = getPassports(data)
    return sum(containsRequiredFields(p) and verifyFields(p) for p in passports)
