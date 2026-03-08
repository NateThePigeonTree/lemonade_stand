def set_recipe(recipe):
        print("======RECIPE======")
        recipe["r_lemons"] = 0
        recipe["r_sugar"] = 0
        recipe["r_ice"] = 0
        recipe["price"]= 0

        while recipe["r_lemons"] < 1 or recipe["r_lemons"] > 3:
                try:
                        recipe["r_lemons"]=int(input("How many lemons would you like per cup(1-3):"))

                except ValueError:
                        print("PLEASE ENTER A VALID ANSWER")

        while recipe["r_sugar"] < 1 or recipe["r_sugar"] > 3:
                try:
                        recipe["r_sugar"]=int(input("How much sugar would you like per cup (1-3):"))

                except ValueError:
                        print("PLEASE ENTER A VALID ANSWER")
        
        while recipe["r_ice"] < 1 or recipe["r_ice"] > 3:
                try:
                    recipe["r_ice"]=int(input("How many ice cubes would you like per cup (1-3):"))    
                except ValueError:
                        print("PLEASE ENTER A VALID ANSWER")
        
        
        print(f"In your recipe you have:\n{recipe['r_lemons']} lemons,\n{recipe['r_sugar']} sugar,\n{recipe['r_ice']} ice cubes")

        while True:
                try:
                        recipe["price"]=float(input("What do you want to price this lemonade as?:"))
                except ValueError:
                        print("PLEASE ENTER A VALID ANSWER")
                if recipe["price"] > 0:
                        break











