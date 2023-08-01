from behave import *
from order import Order

def before_scenario(context, scenario):
	context = {}
 
@given('the meal order is entered')
def meal_order_enter(context):
    order_list = []
    for row in context.table:
        order = Order()
        order_list.append(order)
    context.orders = order_list
  
@when('the user enters a not positive quantity of the meal: {quantity}')
def meal_quantity_enter(context, quantity):
    context.quantity = quantity
     
@then('the user receives an error message of invalid quantity: {message}')
def receive_error_message(context, message):
    assert context.message == message

@given('the selected meal for the order')
def meal_order_selected(context):
    order_list = []
    for row in context.table:
        order = Order()
        order_list.append(order)
    context.orders = order_list
    
@when('the total cost of the meal order exceeds $50')
def total_cost_exceeds(context):
    total_cost = 0
    for meal, quantity in context.orders:
        base_cost = meal.price
        total_cost = base_cost * quantity 
    if total_cost > 50:
        result = True
    else:     
        result = False 
    context.total_cost = total_cost
    context.result = result
 
@then('the system should apply a discount of $10 to the total cost')
def receive_discount(context):
    if context.result == True:
        assert context.total_cost == context.total_cost - 10
    else:
        assert context.total_cost == context.total_cost
    
@when('any meals from the special meal category are included in the order')
def special_meal_category(context):
    for meal, quantity in context.orders:
        if meal.is_special() == True:
            result = True
    context.result = result
    
@then('the system should apply an additional 5% surcharge to the total cost of those meals')    
def receive_surcharge(context):
    if context.result == True:
        assert context.total_cost == context.total_cost * 1.05
    
@when('the user enters a exceed quantity of the meal')
def meal_exceed_quantity(context):
    for meal, quantity in context.orders:
        if quantity > 100:
            result = True
    context.result = result

@then('the user receives an error message of exceed: {message}')
def receive_error_message(context, message):
    if context.result == True:
        assert context.message == message

