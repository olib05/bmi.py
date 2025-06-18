import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

cars = [
    {"name": "Ford Fiesta", "mpg": 40, "tax": 145, "insuranceGroup": 5, "img": "images/ford-fiesta.gif"},
    {"name": "Vauxhall Corsa", "mpg": 45, "tax": 130, "insuranceGroup": 6, "img": "images/vauxhall-corsa.gif"},
    {"name": "Volkswagen Polo", "mpg": 48, "tax": 150, "insuranceGroup": 8, "img": "images/vw-polo.gif"},
    {"name": "Peugeot 208", "mpg": 52, "tax": 120, "insuranceGroup": 9, "img": "images/peugeot-208.gif"},
    {"name": "Mini Cooper", "mpg": 38, "tax": 160, "insuranceGroup": 12, "img": "images/mini-cooper.gif"},
    {"name": "Mazda MX-5", "mpg": 35, "tax": 180, "insuranceGroup": 25, "img": "images/mazda-mx5.gif"},
    {"name": "Ford Mustang (EcoBoost)", "mpg": 28, "tax": 290, "insuranceGroup": 35, "img": "images/ford-mustang.gif"},
    {"name": "Lamborghini Huracan", "mpg": 15, "tax": 570, "insuranceGroup": 50, "img": "images/lamborghini-huracan.gif"},
    {"name": "Ferrari 488 GTB", "mpg": 18, "tax": 600, "insuranceGroup": 50, "img": "images/ferrari-488.gif"},
]

class CarCostCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carr's Cost Calculator")
        self.root.configure(bg="#fcd077")

        title = tk.Label(root, text="Carr's Cost Calculator", font=("Arial", 16, "bold"), bg="#fcd077")
        title.grid(row=0, column=0, columnspan=6, sticky="ew", pady=10)

        tk.Label(root, text="Select a Car:", bg="#fcd077").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.car_dropdown = ttk.Combobox(root, values=[car['name'] for car in cars])
        self.car_dropdown.grid(row=1, column=1, padx=5)
        self.car_dropdown.bind("<<ComboboxSelected>>", self.update_car_details)

        tk.Label(root, text="Date of Birth (DD/MM/YYYY):", bg="#fcd077").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.dob_entry = tk.Entry(root)
        self.dob_entry.grid(row=1, column=3, padx=5)

        tk.Label(root, text="Annual Mileage:", bg="#fcd077").grid(row=1, column=4, sticky="e", padx=5, pady=5)
        self.mileage_entry = tk.Entry(root)
        self.mileage_entry.grid(row=1, column=5, padx=5)

        self.details_box = tk.LabelFrame(root, text="Car Details", padx=10, pady=10, bg="#fcd077", fg="black")
        self.details_box.grid(row=2, column=0, rowspan=3, columnspan=2, sticky="nw", padx=10, pady=10)

        self.mpg_label = tk.Label(self.details_box, text="MPG: ", bg="#fcd077")
        self.mpg_label.pack(anchor="w", pady=(0, 5))

        self.tax_label = tk.Label(self.details_box, text="Road Tax: ", bg="#fcd077")
        self.tax_label.pack(anchor="w", pady=(0, 5))

        self.ins_label = tk.Label(self.details_box, text="Insurance Group: ", bg="#fcd077")
        self.ins_label.pack(anchor="w")

        self.car_img_label = tk.Label(root, text="Car Image", bg="#fcd077")
        self.car_img_label.grid(row=2, column=2, columnspan=4, rowspan=3, padx=10, pady=10)

        self.calc_button = tk.Button(root, text="Calculate Insurance Price", command=self.calculate_insurance)
        self.calc_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.result_box = tk.LabelFrame(root, text="Insurance Price", padx=10, pady=10, bg="#fcd077", fg="black")
        self.result_box.grid(row=5, column=2, columnspan=4, pady=10, sticky="w")

        self.result_label = tk.Label(self.result_box, text="", font=("Arial", 12, "bold"), bg="#fcd077")
        self.result_label.pack()

        self.current_image = None

    def update_car_details(self, event=None):
        index = self.car_dropdown.current()
        if index == -1:
            return
        car = cars[index]

        self.mpg_label.config(text=f"MPG: {car['mpg']}")
        self.tax_label.config(text=f"Road Tax: {car['tax']}")
        self.ins_label.config(text=f"Insurance Group: {car['insuranceGroup']}")

        image_path = car["img"]
        if os.path.exists(image_path):
            try:
                self.current_image = tk.PhotoImage(file=image_path)
                self.car_img_label.config(image=self.current_image, text="")
            except Exception as e:
                print(f"Error loading image: {e}")
                self.car_img_label.config(image="", text="Image error")
        else:
            self.car_img_label.config(image="", text="Image not found")

    def calculate_insurance(self):
        index = self.car_dropdown.current()
        if index == -1:
            self.result_label.config(text="Please select a car.")
            return

        dob_str = self.dob_entry.get()
        try:
            dob = datetime.strptime(dob_str, "%d/%m/%Y")
        except ValueError:
            self.result_label.config(text="Invalid date format. Use DD/MM/YYYY.")
            return

        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        if age < 0 or age > 120:
            self.result_label.config(text="Please enter a valid date of birth.")
            return

        car = cars[index]
        insurance_group = car["insuranceGroup"]

        insurance_price = insurance_group * 50 + (100 - age) * 10
        self.result_label.config(text=f"{insurance_price:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarCostCalculatorApp(root)
    root.mainloop()