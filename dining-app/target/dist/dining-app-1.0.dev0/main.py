# main.py
from meal import MealFactory

def display_menu(meal_type, meals):
    print(f"Select your {meal_type} (enter the number):")
    for i, meal in enumerate(meals, start=1):
        print(f"{i}. {meal.name} - ${meal.cost:.2f}")

def get_user_choice(prompt, num_choices):
    while True:
        choice = input(prompt)
        if choice.lower() == 'q':
            return None
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= num_choices:
                return choice_num
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    total_cost = 0

    while True:
        print("Select your meal type:")
        print("1. Starter")
        print("2. Main")
        print("3. Dessert")
        print("4. Quit")

        meal_type_choice = get_user_choice("Enter your choice (1/2/3), or 'q' to quit: ", num_choices=4)

        if meal_type_choice is None or meal_type_choice == 4:
            break

        meal_type_map = {
            1: 'starter',
            2: 'main',
            3: 'dessert',
        }

        meal_type = meal_type_map[meal_type_choice]

        predefined_meals = MealFactory.get_predefined_meals(meal_type)
        display_menu(meal_type, predefined_meals)

        meal_choice = get_user_choice(f"Enter your {meal_type} choice (1/{len(predefined_meals)}), or 'q' to go back: ",
                                      num_choices=len(predefined_meals))
        
        if meal_choice is None:
            continue

        meal = predefined_meals[meal_choice - 1]

        quantity = int(input("Enter the quantity: "))

        total_cost += meal.calculate_cost(quantity)
        print(f"Added {quantity} {meal.name}(s) to the total cost.")

    print(f"Total cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
