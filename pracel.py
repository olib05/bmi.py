import time

name = input("Please enter your name: ")
address = input("Please enter your address: ")
number = input("Please enter your phone number: ")

while True:
    parcels = input("How many parcels are you sending?: ")
    if parcels > 6:
        print("Maximum = 6")
    else:
        break

parcellist = []

for i in range(parcellist):
    height = float(input(f"Enter the height of the parcel in cm: "))
    length = float(input(f"Enter the length of the parcel in cm: "))
    width = float(input(f"Enter the width of the parcel in cm: "))
    weight = float(input(f"Enter the weight of the parcel in kg: "))
    signature = str(input(f"Add signature to parcel?: "))
    tracking = str(input(f"Add tracking to parcel?: "))

parcelsize = height + length + width
parcel = 2.00
tracking = 5.00

if parcelsize < 95.00:
    print("Parcel size is small - £5.00", )
elif parcelsize > 95.00 and parcelsize <= 150.00:
    print("Parcel size is medium - £20.00")
elif parcelsize > 151.00 and parcelsize <= 450.00:
    print("Parcel size is large - £30.00")
elif parcelsize > 450.00:
    print("Parcel too big.")

time.sleep(5)