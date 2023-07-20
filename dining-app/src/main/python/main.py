from exceptions import InvalidQuantityError, InvalidMealError, InvalidConfirmationError 
from menu import Menu
from order import Order

def main():
    menu = Menu()
    print("Welcome to the Restaurant!")

    selected_meals = menu.select_meals()
    if not selected_meals:
        print("No meals selected. Order canceled.")
        return -1

    print("You have selected the following meals:")
    for meal_id, quantity in selected_meals:
        meal = menu.meals.get(meal_id)
        if not meal:
            print("Invalid meal ID. Order canceled.")
            return -1
        print(f"{meal.name} - Quantity: {quantity}")

    order = Order()
    for meal_id, quantity in selected_meals:
        meal = menu.meals.get(meal_id)
        if not meal:
            print("Invalid meal ID. Order canceled.")
            return -1
        order.add_meal(meal, quantity)

    total_cost = order.get_total_cost()
    print(f"Total cost: ${total_cost}")

    try:
        if order.confirm_order():
            print("Order confirmed! Thank you for your purchase.")
            return total_cost
        else:
            print("Order canceled.")
            return -1
    except InvalidConfirmationError:
        print("Invalid input. Please enter 'y' or 'n'.")
        return -1


if __name__ == "__main__":
    main()
