import time

car_prices = {
    1: ("Lamborghini Gallardo", 59.00),
    2: ("Lamborghini Huracan", 59.00),
    3: ("Ferrari F40", 49.00),
    4: ("Porsche Boxster", 39.00),
    5: ("Audi A5", 39.00),
    6: ("BMW i8", 39.00),
    7: ("Lotus Elise", 30.00)
}

name = input(f"Please enter your name: ")
address = input(f"Please enter your address: ")
phonenumber =input(f"Please enter your phone number: ")

while True:
    try:
        cars_driven = int(input("Please enter the number of cars you would like to drive (Maximum of 5): "))
        if 1 <= cars_driven <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Invalid input. Please enter a number.")

for i in range(carsdriven):
    print("Which cars would you like to Drive?: \n1#1 Lamborghini Gallardo \n2#2 Lamborghini Huracan, \n3#3 Ferrari F40, \n4#4 Porsche Boxter, \n5#5 Audi A5, \n6#6 BMW i8, \n7#7 Lotus Elise.")
    carchosen = int(input(f"Enter car number {i+1}"))
    carlist.append


while True:
    carschosen = input(f"Which cars would you like to Drive?: \n1#1 Lamborghini Gallardo \n2#2 Lamborghini Huracan, \n3#3 Ferrari F40, \n4#4 Porsche Boxter, \n5#5 Audi A5, \n6#6 BMW i8, \n7#7 Lotus Elise.")
    if carschosen in carlist:
        break

while True:
    additional_lap = input(f"Would you like to add any other laps (£15): ").strip().lower()
    if additional_lap == 'yes':
        additional_laps = input(f"How many laps?")
    else:
        break

additional_lap = 15.00

print("\nFinal Bill")
print("Customer details")
print(name)
print(address)
print(phonenumber)

time.sleep(5)