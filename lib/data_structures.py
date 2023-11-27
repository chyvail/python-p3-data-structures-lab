# python pass is used as a placeholder for future code
spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # using list comprehension to get values
    '''
        for key in spicy_foods:
            print(key["name"]) # loop through the spicy foods
    '''
    return [value["name"] for value in spicy_foods]

def get_spiciest_foods(spicy_foods):
    '''
        for value in spicy_foods:
        if (value["heat_level"]) > 3:
            print(value)
    '''
    return [value for value in spicy_foods if (value["heat_level"]) > 5]

def print_spicy_foods(spicy_foods):

    for value in spicy_foods:
        spice = "🌶" * value["heat_level"]
        name = value["name"]
        cuisine = value["cuisine"]
        print(f"{name} ({cuisine}) | Heat Level: {spice}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for value in spicy_foods:
        if(value["cuisine"] == cuisine):
            return value

def print_spiciest_foods(spicy_foods):
    for value in spicy_foods:
        if (value["heat_level"]) > 5:
            spice = "🌶" * value["heat_level"]
            name = value["name"]
            cuisine = value["cuisine"]
            print(f"{name} ({cuisine}) | Heat Level: {spice}")

def get_average_heat_level(spicy_foods):
    total = 0
    for value in spicy_foods:
        total+=value["heat_level"]
    return total // len(spicy_foods)

get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
