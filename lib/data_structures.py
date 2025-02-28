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
    return[spicy_food['name']for spicy_food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
   # return[spiciest_food['heat_level']for spiciest_food in spicy_foods]
    return[spiciest_food for spiciest_food in spicy_foods if spiciest_food.get('heat_level',0)>5]
    pass

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶" * spicy_food ["heat_level"]
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'heat_level'}")

    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
         return spicy_food 
       
    pass
 


def print_spiciest_foods(spicy_foods):
    for spicy_food in spicy_foods:
        heat_level = "🌶"* spicy_food["heat_level"]
        if spicy_food ["heat_level"] >5:
            print(f"{spicy_food['name']}({spicy_food['cuisine']})|Heat Level:{'heat_level'}")
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(spicy_food["heat_level"]for spicy_food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
