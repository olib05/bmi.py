import time


print("Welcome to the Pizza Staff portal")
print("Please enter the customer's details:")


size_prices = {
    "small": 3.25,
    "medium": 5.50,
    "large": 7.15
}


delivery_fee = 2.50


discount_threshold = 20.00
discount_rate = 0.10


topping_prices = {
    1: 0.75,
    2: 1.35,
    3: 2.00,
    4: 2.50  
}


name = input("Please enter the Customer's name: ")
address = input("Please enter the Customer's address: ")
number = input("Please enter the Customer's phone number: ")


while True:
    try:
        pizza = int(input("Enter amount of pizzas the Customer has ordered: "))
        if pizza > 6:
            print("Maximum amount of pizzas is 6")
        elif pizza < 1:
            print("Minimum amount of pizzas is 1")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


while True:
    size = input("Please enter the size of the pizza (Small, Medium, Large): ").lower()
    if size in ["small", "medium", "large"]:
        break
    else:
        print("Please enter a valid size.")


toppings = input("Does the customer want to add any extra toppings? (yes/no): ").lower()
while toppings not in ['yes', 'no']:
    toppings = input("Please enter 'yes' or 'no' for extra toppings: ").lower()


topping_cost = 0
if toppings == 'yes':
    while True:
        try:
            num_toppings = int(input("How many extra toppings does the customer want? (Enter a number): "))
            if num_toppings >= 4:
                topping_cost = topping_prices[4]
            elif num_toppings >= 1:
                topping_cost = topping_prices[num_toppings]
            else:
                print("Please enter a valid number of toppings (1 or more).")
                continue
            break
        except ValueError:
            print("Please enter a valid number of toppings.")


delivery = input("Does the Customer want to request delivery? (yes/no): ").lower()
while delivery not in ['yes', 'no']:
    delivery = input("Please enter 'yes' or 'no' for delivery: ")


base_price = size_prices[size] * pizza
total_price = base_price + (delivery_fee if delivery == 'yes' else 0)


total_price += topping_cost


discount_applied = False
if total_price > discount_threshold:
    discount_amount = total_price * discount_rate
    total_price -= discount_amount
    discount_applied = True


print("\n--- Customer Order Summary ---")
print(f"Name: {name}")  
print(f"Address: {address}")
print(f"Phone number: {number}")
print(f"Number of pizzas: {pizza}")
print(f"Pizza size: {size.capitalize()}")
print(f"Extra toppings: {toppings.capitalize()}")
if toppings == 'yes':
    print(f"Number of extra toppings: {num_toppings}")
    print(f"Extra toppings cost: £{topping_cost:.2f}")
print(f"Delivery: {delivery.capitalize()}")
if delivery == 'yes':
    print(f"Delivery fee: £{delivery_fee:.2f}")
if discount_applied:
    print(f"Discount (10% off): -£{discount_amount:.2f}")
print(f"Total bill: £{total_price:.2f}")


time.sleep(5)