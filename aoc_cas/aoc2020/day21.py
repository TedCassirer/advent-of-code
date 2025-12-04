from collections import defaultdict, deque


def parseData(data):
    result = []
    for line in data.splitlines():
        ingredients, allergens = line.split(" (contains ")
        ingredients = tuple(ingredients.split())
        allergens = tuple(allergens[:-1].split(", "))
        result.append((ingredients, allergens))
    return result


def findAllergens(food):
    couldContainAllergen = defaultdict(list)
    for ingredients, allergens in food:
        for allergen in allergens:
            couldContainAllergen[allergen].append(set(ingredients))

    couldContainAllergen = {a: set.intersection(*i) for a, i in couldContainAllergen.items()}
    return couldContainAllergen


def part_a(data):
    food = parseData(data)
    couldContainAllergen = findAllergens(food)
    containsAllergens = set.union(*couldContainAllergen.values())
    ingredients = [i for ingredients, allergens in food for i in ingredients]
    allergenFree = set(ingredients) - containsAllergens

    return sum(ingredients.count(i) for i in allergenFree)


def part_b(data):
    food = parseData(data)
    couldContainAllergen = findAllergens(food)

    set.union(*couldContainAllergen.values())
    {i for ingredients, allergens in food for i in ingredients}

    seen = set()
    combos = []
    queue = deque(couldContainAllergen.items())
    while queue:
        allergen, ingredients = queue.popleft()
        ingredients -= seen
        if len(ingredients) > 1:
            queue.append((allergen, ingredients))
        else:
            ingredient = ingredients.pop()
            seen.add(ingredient)
            combos.append((allergen, ingredient))

    return ",".join(i for a, i in sorted(combos))
