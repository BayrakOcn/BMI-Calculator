import tkinter

# window
window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=280, height=230)
window.config(padx=20, pady=20)


def calculate_bmi():
    w = float(weight.get())
    h = float(height.get())
    bmi = (w / (h ** 2)) * 10000
    if bmi < 18.5:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Underweight")
    elif 18.5 <= bmi <= 24.9:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Normal Weight")
    elif 25.0 <= bmi <= 29.9:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Overweight")
    elif 30 <= bmi <= 34.9:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Obesity Class I")
    elif 35 <= bmi <= 39.9:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Obesity Class II")
    else:
        result_label.config(text=f"Your BMI is {bmi:.1f} : Obesity Class III")


# weight
your_weight = tkinter.Label(text="Your Weight (kg):")
your_weight.pack()
weight = tkinter.Entry(width=15)
weight.config(justify="center")
weight.pack()

# height
your_height = tkinter.Label(text="Your Height (cm):")
your_height.pack()
height = tkinter.Entry(width=15)
height.config(justify="center")
height.pack()

# calculate button
calculate = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate.pack()

# result
result_label = tkinter.Label(text="")
result_label.config(padx=20, pady=20)
result_label.pack()

x, y = calculate.winfo_rootx(), calculate.winfo_rooty()
print(calculate.winfo_rootx(), calculate.winfo_rooty())

window.mainloop()
