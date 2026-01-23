lemons = -5
sugar = -1
ice= -3
cups=-3
def tracking(cash, value):
    cash += value
    return cash

def shop(cash):
    whichProduct= input("Which product do you want to buy? Lemons/Sugar/Ice/Cups")
    if whichProduct=="lemons":
        cash = tracking(cash,lemons)
        return(cash)

print(shop(100))
    # BUY LEMONS
    # LEMONS ARE 5$
    # Money = tracking(Money, lemon_5)