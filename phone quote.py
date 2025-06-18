import time

print("Enter Customer details")

companyname = input("Please enter the company's name: ")
companynumber = input("Please enter the company's phone number: ")

# Validating quantity
while True:
    quantity = int(input("Please enter the amount of smartphones needed: "))
    if quantity < 5:
        print("Minimum = 5")
    elif quantity > 100:
        print("Maximum = 100")
    else:
        break  # Valid quantity

# Choose phone type
print("Available Phone Types: \n1. Basic = £250 \n2. Standard = £450 \n3. Superior = £950")
phonetype = input("Please input the type of phone needed (Basic/Standard/Superior): ").strip().lower()

if phonetype == "basic":
    phoneprice = 250
elif phonetype == "standard":
    phoneprice = 450
elif phonetype == "superior":
    phoneprice = 950
else:
    print("Invalid phone type. Defaulting to Basic.")
    phoneprice = 250

# Setup cost
setup_needed = input("Will setup be necessary? yes/no: ").strip().lower()
setupprice = 0

if setup_needed == "yes":
    print("\nSetup options:\nA. Basic Setup £30\nB. Full Setup £50")
    setup_option = input("Choose Setup (A/B): ").strip().lower()

    if setup_option == "a":
        setupprice = 30 * quantity
    elif setup_option == "b":
        setupprice = 50 * quantity
    else: 
        print("Invalid option. Defaulting to Basic Setup.")
        setupprice = 30 * quantity

# Calculations
priceofphones = phoneprice * quantity
totalcost = priceofphones + setupprice
vat = totalcost * 0.20
total_with_vat = totalcost + vat

# Output
print("\nFinal quote")
print("Company Name: ", companyname)
print("Company Number: ", companynumber)
print("Quantity: ", quantity)
print("Price of smartphones: £", priceofphones)
print("Set-up cost: £", setupprice)
print("Total cost (before VAT): £", totalcost)
print("VAT (20%): £", vat)
print("Total cost (with VAT): £", total_with_vat)

time.sleep(5)
