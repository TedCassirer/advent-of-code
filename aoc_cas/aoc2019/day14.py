from collections import Counter
from math import ceil


class Recipe:
    def __init__(self, name, quantity, required_chemicals):
        self.name = name
        self.quantity = quantity
        self.required_chemicals = required_chemicals  # Counter({name: quantity, ...})

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"{self.quantity} {self.name} => {self.required_chemicals}"


def get_input(data):
    recipes = {}
    for line in data.strip().split("\n"):
        chem_in, chem_out = line.split(" => ")
        chems_in = Counter({name: int(quantity) for quantity, name in [c.split(" ") for c in chem_in.split(", ")]})
        chem_out_quantity = int(chem_out.split(" ")[0])
        chem_out_name = chem_out.split(" ")[1].strip()
        recipe = Recipe(chem_out_name, chem_out_quantity, chems_in)

        recipes[chem_out_name] = recipe
    return recipes


def get_ores_required_for(recipes, required):
    leftover = Counter()
    ores_required = 0
    while required:
        chem, quantity = required.popitem()
        if chem == "ORE":
            ores_required += quantity
        else:
            from_leftover = min(leftover[chem], quantity)
            leftover[chem] -= from_leftover
            quantity_required = quantity - from_leftover
            recipe = recipes[chem]
            batches = ceil(quantity_required / recipe.quantity)
            leftover_quantity = recipe.quantity - quantity_required % recipe.quantity
            leftover[chem] += batches * recipe.quantity - quantity_required
            required.update({name: q * batches for name, q in recipe.required_chemicals.items()})
    return ores_required


def part_a(data):
    recipes = get_input(data)
    required = Counter({"FUEL": 1})
    return get_ores_required_for(recipes, required)


def part_b(data):
    target = 1000000000000
    recipes = get_input(data)
    lo, hi = 0, target // 1024
    while abs(hi - lo) > 1:
        guess = lo + (hi - lo) // 2
        required = Counter({"FUEL": guess})
        ores_required = get_ores_required_for(recipes, required)
        if ores_required < target:
            lo = guess
        elif ores_required > target:
            hi = guess
        else:
            return guess
    return guess
