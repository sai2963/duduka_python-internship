import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operator.get()

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Error: Division by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Error: Invalid input")

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields for numbers and result
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)
result = tk.StringVar()
result.set("Result: ")

# Dropdown for selecting the operation
operator = tk.StringVar()
operator.set("+")
operator_dropdown = tk.OptionMenu(window, operator, "+", "-", "*", "/")

# Button to calculate
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Display result
result_label = tk.Label(window, textvariable=result)

# Layout the GUI elements
entry_num1.pack()
operator_dropdown.pack()
entry_num2.pack()
calculate_button.pack()
result_label.pack()

# Start the GUI main loop
window.mainloop()
