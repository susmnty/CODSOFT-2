import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        else:
            messagebox.showerror("Error", "Invalid operation")
            return

        label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input, please enter numerical values")

root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack(pady=20)

label_num1 = tk.Label(frame, text="Enter first number:")
label_num1.grid(row=0, column=0, padx=10, pady=5)

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(frame, text="Enter second number:")
label_num2.grid(row=1, column=0, padx=10, pady=5)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

label_operation = tk.Label(frame, text="Enter operation (+, -, *, /):")
label_operation.grid(row=2, column=0, padx=10, pady=5)

entry_operation = tk.Entry(frame)
entry_operation.grid(row=2, column=1, padx=10, pady=5)

btn_calculate = tk.Button(frame, text="Calculate", command=perform_calculation)
btn_calculate.grid(row=3, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=10)

root.mainloop()
