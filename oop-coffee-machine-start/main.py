from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




#make object 'coffee_maker'and money_machine  class CoffeMaker and class MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

#making menu item


#making while loop
coffee_machine_on = True

while coffee_machine_on:
#get an order from customer
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) :" )

#if it puts 'report' #show the resources
    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)

        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)






