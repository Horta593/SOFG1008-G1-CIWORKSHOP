# language: en

Feature: Dining Experience Manager

    Scenario: Meal Quantity Validation
        Given the meal order is entered
        |  MEAL  | 
        |  Pizza |
        When the user enters a not positive quantity of the meal: '-2'
        |  MEAL  | QUANTITY | 
        |  Pizza |    -2    |  
        Then the user receives an error message of invalid quantity: Invalid quantity! Please enter a positive integer between 1 and 100

    Scenario: Special Offer Discount - $10
        Given the selected meal for the order
        |  MEAL  | QUANTITY | 
        |  Pizza |     5    |   
        When the total cost of the meal order exceeds $50
        |  MEAL  | QUANTITY | PRICE |
        |  Pizza |     5    |   60  |
        Then the system should apply a discount of $10 to the total cost
        |  MEAL  | QUANTITY | PRICE |
        |  Pizza |     5    |   54  |

    Scenario: Special Meal Category Surcharge - 5%
        Given the meal order is entered
        |       MEAL    | 
        |  Chef's salad |
        When any meals from the special meal category are included in the order
        |      MEAL     | QUANTITY |    PRICE |
        |  Chef's salad |     1    |     25   |
        Then the system should apply an additional 5% surcharge to the total cost of those meals
        |      MEAL     | QUANTITY |    PRICE |
        |  Chef's salad |     1    |   26.25  |

    Scenario: Maximum Order Quantity Validation
        Given the meal order is entered
        |  MEAL  | 
        |  Pizza |
        When the user enters a exceed quantity of the meal
        |  MEAL  |  QUANTITY  | 
        |  Pizza |     101    |   
        Then the user receives an error message of exceed: Invalid quantity! Please enter a positive integer between 1 and 100
