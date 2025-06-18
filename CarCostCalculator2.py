import tkinter as tk
from tkinter import ttk
import os

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

        tk.Label(root, text="Car Cost:", bg="#fcd077").grid(row=1, column=2, sticky="e", padx=5)
        self.cost_entry = tk.Entry(root)
        self.cost_entry.grid(row=1, column=3, padx=5)

        tk.Label(root, text="Down Payment :", bg="#fcd077").grid(row=1, column=4, sticky="e", padx=5)
        self.down_entry = tk.Entry(root)
        self.down_entry.grid(row=1, column=5, padx=5)

        tk.Label(root, text="Loan Term (years):", bg="#fcd077").grid(row=2, column=2, sticky="e", padx=5)
        self.term_entry = tk.Entry(root)
        self.term_entry.grid(row=2, column=3, padx=5)

        tk.Label(root, text="APR (%):", bg="#fcd077").grid(row=2, column=4, sticky="e", padx=5)
        self.apr_entry = tk.Entry(root)
        self.apr_entry.grid(row=2, column=5, padx=5)

        self.calc_button = tk.Button(root, text="Calculate Loan", command=self.calculate_loan)
        self.calc_button.grid(row=3, column=0, columnspan=6, pady=10)

        self.details_box = tk.LabelFrame(root, text="Car Details", padx=10, pady=10, bg="#fcd077", fg="black")
        self.details_box.grid(row=4, column=0, rowspan=3, columnspan=2, sticky="nw", padx=10, pady=10)

        self.mpg_label = tk.Label(self.details_box, text="MPG: ", bg="#fcd077")
        self.mpg_label.pack(anchor="w", pady=(0, 5))

        self.tax_label = tk.Label(self.details_box, text="Road Tax: ", bg="#fcd077")
        self.tax_label.pack(anchor="w", pady=(0, 5))

        self.ins_label = tk.Label(self.details_box, text="Insurance Group: ", bg="#fcd077")
        self.ins_label.pack(anchor="w")

        self.car_img_label = tk.Label(root, text="Car Image", bg="#fcd077")
        self.car_img_label.grid(row=4, column=2, columnspan=4, rowspan=3, padx=10, pady=10)

        self.result_box = tk.LabelFrame(root, text="Loan Details", padx=10, pady=10, bg="#fcd077", fg="black")
        self.result_box.grid(row=7, column=0, columnspan=6, sticky="ew", padx=10, pady=10)

        self.loan_amount_label = tk.Label(self.result_box, text="Loan Amount: ", bg="#fcd077", anchor="w")
        self.loan_amount_label.pack(fill="x")

        self.monthly_payment_label = tk.Label(self.result_box, text="Monthly Payment: ", bg="#fcd077", anchor="w")
        self.monthly_payment_label.pack(fill="x")

        self.total_repay_label = tk.Label(self.result_box, text="Total Repayment: ", bg="#fcd077", anchor="w")
        self.total_repay_label.pack(fill="x")

        self.total_interest_label = tk.Label(self.result_box, text="Total Interest: ", bg="#fcd077", anchor="w")
        self.total_interest_label.pack(fill="x")

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

    def calculate_loan(self):
        try:
            cost = float(self.cost_entry.get())
            down = float(self.down_entry.get())
            term = int(self.term_entry.get())
            apr = float(self.apr_entry.get())

            if down > cost:
                self.loan_amount_label.config(text="Down payment can't exceed car cost.")
                return

            principal = cost - down
            total_interest = principal * apr * term / 100
            total_repayment = principal + total_interest
            monthly_payment = total_repayment / (term * 12)

            self.loan_amount_label.config(text=f"Loan Amount: {principal:.2f}")
            self.monthly_payment_label.config(text=f"Monthly Payment: {monthly_payment:.2f}")
            self.total_repay_label.config(text=f"Total Repayment: {total_repayment:.2f}")
            self.total_interest_label.config(text=f"Total Interest: {total_interest:.2f}")
        except ValueError:
            self.loan_amount_label.config(text="Please enter valid numeric inputs.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarCostCalculatorApp(root)
    root.mainloop()
