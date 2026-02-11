# customer_class.py
# The customer class represents a customer at the lemondade stand.
# The customer has preferences for lemonade sweetness and ice level,
# and a price point they are willing to pay.
# All of these attributes will influence their purchasing decision and
# are returned as a list of attributes.

import random

class Customer:
    def __init__(self, sweetness_preference=2, ice_preference=1, price_point=1.75):
        self.sweetness_preference = (
            sweetness_preference if sweetness_preference is not None
            else random.randint(0, 3)
        )
        self.ice_preference = (
            ice_preference if ice_preference is not None
            else random.randint(0, 3)
        )
        self.price_point = (
            price_point if price_point is not None
            else round(random.uniform(1.00, 4.0),2)
        )

    def get_customer_attributes(self):
        return {
            "sweetness": self.sweetness_preference,
            "ice": self.ice_preference,
            "price": self.price_point
        }
     