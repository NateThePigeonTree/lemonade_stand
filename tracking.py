lemons = -5
sugar = -1
ice= -3
cups=-3
p_sugar = 0
p_lemons = 0
p_ice = 0
p_cups = 0
cash = 100


def tracking(value, modifier):
    value += modifier
    return value

def shop():
    global cash
    global p_lemons 
    global p_sugar
    global p_ice
    global p_cups
    #p_ice, p_cups, p_sugar
    whichProduct= input("Which product do you want to buy? Lemons/Sugar/Ice/Cups\n")
    if whichProduct.lower()=="lemons":
        cash = tracking(cash,lemons)
        p_lemons = tracking(p_lemons,50)
        return
    elif whichProduct.lower()=="sugar":
        cash = tracking(cash,sugar)
        p_sugar = tracking(p_sugar,25)
        return
    elif whichProduct.lower()=="ice":
        cash = tracking(cash,ice)
        p_ice = tracking(p_ice,25)
        return
    elif whichProduct.lower()=="cups":
        cash== tracking(cash,cups)
        p_cups = tracking(p_cups,100)
        return
    else:
        return 0

    # BUY LEMONS

    # LEMONS ARE 5$

    # Money = tracking(Money, lemon_5)

while True:
    if shop() == 0:
        break
print(f"Cash: {cash}\nIce: {p_ice}\nLemons: {p_lemons}\nSugar: {p_sugar}\nCups: {p_cups}")

