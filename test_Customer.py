from customer import production

inventory = {
    "p_sugar": 20,
    "p_lemons" : 20,
    "p_ice" : 20,
    "p_cups" : 20,
    "cash":100}

recipe = {
    "r_sugar":1,
    "r_lemons":1,
    "r_ice":1,
    "price": 1
}

production(recipe,inventory)