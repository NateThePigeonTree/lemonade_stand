def set_recipe(recipe):
        print("======RECIPE======")
        recipe["r_lemons"]=int(input("How many lemons would you like per cup(1-3):"))
        recipe["r_sugar"]=int(input("How much sugar would you like per cup (1-3):"))
        recipe["r_ice"]=int(input("How many ice cubes would you like per cup (1-3):"))
        print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,\n{recipe['r_sugar']} sugar,\n{recipe['r_ice']} ice cubes")













