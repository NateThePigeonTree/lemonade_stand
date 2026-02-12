from customer_class import Customer

def production(recipe, inventory, new_customer = Customer()):
# Write what you are trying to do as a comment
# Get customer attributes and compare the attributes to the recipe
    val = new_customer.get_customer_attributes() 
    # Compare each aspect of "val" [sweetness, ice, price] to your recipe.
    # Decide if it will return a true/false for if they bought from you.
    #`if _they_bought:
    #       Do the thing`   
    if val["sweetness"] > 1:
        print("I like sweet lemonade")
        
    

