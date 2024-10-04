import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Checker")
root.geometry("300x200")


def cal_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi =(weight*10000)/(height**2)
        bmi_result = round(bmi, 2)
        
        if bmi<18.5:
            category = "Underweight"
        elif 18.5<= bmi<24.9:
            category = "Normal weight"
        elif 25<= bmi <29.9:
            category= "Overweight"
        else:
            category= "Obesity"

        messagebox.showinfo("BMI Result", f"Your BMI is {bmi_result}.\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")


weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack(pady=10)
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (cm):")  
height_label.pack(pady=10)
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=cal_bmi)
calculate_button.pack(pady=20)

root.mainloop()
