MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_check(order):
    if order == "espresso":
        if MENU[order]["ingredients"]["water"] < resources["water"] and MENU[order]["ingredients"]["coffee"] < resources["coffee"]:
            return True
    if order == "latte" or "cappuccino":
        if MENU[order]["ingredients"]["water"] < resources["water"] and MENU[order]["ingredients"]["milk"] < resources["milk"] and MENU[order]["ingredients"]["coffee"] < resources["coffee"]:
            return True
    else:
        return False

def is_resources_sufficient(order):
    for item in order:
        if order[item] > resources[item]:
            print("Resourses are not available")
            return False
    return True

total_price = 0


def process_coins(order, pennies, nickles, dimes, quaters):
    global total_price
    total = pennies*0.25 + nickles*0.10 + dimes*0.05 + quaters*0.01
    order_price = MENU[order]["cost"]
    if total >= order_price:
        change = round(total - MENU[order]["cost"],2)
        print(f"Here's your change: {change}")
        print(f"Enjoy your {order}")
        total_price += order_price
        resources["cost"] = total_price
        # resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
        # resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
        # resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    elif total < MENU[order]["cost"]:
        print("Sorry that's not enough money")


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


price = 0
turn_on = True
while turn_on:
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user == "report":
        print(resources)
    elif user == "off":
        turn_on = False
    elif user == "espresso" or "latte" or "cappuccino":
        availability = resources_check(user)
        if availability:
            print("Please insert coin:")
            quaters = int(input("How many quaters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            process_coins(user,pennies,nickles,dimes,quaters)
            make_coffee(user,MENU[user]["ingredients"])
        else:
            print("Resourses are not available")
    # else:
    #     drink = MENU[user]
    #     is_resources_sufficient(drink["ingredients"])










