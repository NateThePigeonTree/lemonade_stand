customers = [10]
for i in range(10):
    customers.append(customers(10))
customer1 = customers()
attributes = customers.get_customer_attributes()

{"sweetness": 2,
    "ice": 1,
    "price": 1.75}
sweetness_pref = attributes["sweetness"]
ice_pref = attributes["ice"]
price_limit = attributes["price"]
