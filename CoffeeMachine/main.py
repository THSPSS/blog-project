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
# TODO: 8. get ingredients and costs from nested dictionary
espresso_ing = MENU["espresso"]["ingredients"]
latte_ing = MENU["latte"]["ingredients"]
cappuccino_ing = MENU["cappuccino"]["ingredients"]

espresso_cost = MENU["espresso"]["cost"]
latte_cost = MENU["latte"]["cost"]
cappuccino_cost = MENU["cappuccino"]["cost"]

# TODO: 1. print coffee Machine's resources
water_s = resources["water"]
milk_s = resources["milk"]
coffee_s = resources["coffee"]
money_s = 0


# TODO: 7. informed what resources are off
# TODO: 2. check resources sufficient to make drink order


def check_resources(order_c):
    if order_c == "espresso":
        if espresso_ing["water"] < water_s:
            if espresso_ing["coffee"] < coffee_s:
                return True
            else:
                print( f"Sorry, coffee is out.")
        else:
            print( f"Sorry, water is out.")
    elif order_c == "latte":
        if latte_ing["water"] < water_s:
            if latte_ing["milk"] < milk_s:
                if latte_ing["coffee"] < coffee_s:
                    return True
                else:
                    print( f"Sorry, coffee is out.")
            else:
                print( f"Sorry, milk is out." )
        else:
            print( f"Sorry, water is out.")
    elif order_c == "cappuccino":
        if latte_ing["water"] < water_s:
            if latte_ing["milk"] < milk_s:
                if latte_ing["coffee"] < coffee_s:
                    return True
                else:
                    print( f"Sorry, coffee is out." )
            else:
                print( f"Sorry, milk is out.")
        else:
            print( f"Sorry, water is out.")


# TODO: 3. sum-up the money
def calculating(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


# TODO 9. print report if it wanted
def print_report(water, milk, coffee, money):
    print(f"Water : {water_s}ml") #resources['water']
    print(f"Milk : {milk_s}ml")
    print(f"Coffee : {coffee_s}g")
    print(f"Money : ${money_s}")


coffee_machine_on = True
while coffee_machine_on:

    order = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if order == "off":
        coffee_machine_on = False
    elif order == "report":
        print_report(water_s, milk_s, coffee_s, money_s)
    else:
        checking_resource = check_resources(order)

    if not checking_resource:
        break
    print("Please, insert the coins.")
    quart = int(input("how many quarters?"))
    dime = int(input("how many dimes?"))
    nickle = int(input("how many nickles?"))
    penny = int(input("how many pennies?"))

    total = round(calculating(quart, dime, nickle, penny), 2)

    change = 0
    # TODO: 4. add money to profit
    cost = MENU[order]["cost"]

    # TODO: 5. add to the profit and offer changes
    if total > cost:
        money_s += cost
        change = total - cost
        final_change = round(change, 2)
        print(f"Here is your ${final_change} in change.")
    else:
        print(f"You didn't purchased enough")

    # add something to do loop

    # TODO: 6. deducted from coffee machine resources
    if order == "espresso":   #use for loop
        water_s -= espresso_ing["water"]
        coffee_s -= espresso_ing["coffee"]
        print("Your espresso is here. enjoy your coffee.☕")
    elif order == "latte":
        water_s -= latte_ing["water"]
        coffee_s -= latte_ing["coffee"]
        milk_s -= latte_ing["milk"]
        print("Your latte is here. enjoy your coffee.☕")
    else:
        water_s -= cappuccino_ing["water"]
        coffee_s -= cappuccino_ing["coffee"]
        milk_s -= cappuccino_ing["milk"]
        print("Your cappuccino is here. enjoy your coffee.☕")
