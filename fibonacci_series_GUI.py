from tkinter import *

def fibonacci_series(start_value, num_terms):
    #if the number of terms is not positive integer
    if num_terms <= 0:
        return []
    #if number is 1 then the start value will be 1 and default series will execute
    if num_terms == 1:
        return [start_value]
    #initializing the series with the start value and another term to be incremented by1
    fib_series = [start_value, start_value + 1] 
    #logic of fibonacci series 
    while len(fib_series) < num_terms:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

#generating default series which will be called by the command attribute of tkinter button
def generate_default_series():
    try:
        n = int(default_terms_entry.get())
        series = fibonacci_series(0, n)  # Default starts with 0
        default_result_label.config(text=f"Default Fibonacci Series: {series}")  # Display result in default frame
    except ValueError:
        default_result_label.config(text="Invalid input. Please enter an integer.")

#generating custom series which will be called by the command attribute of tkinter button here -- custom buttom we created below
def generate_custom_series():
    try:
        start_value = int(custom_start_entry.get())
        num_terms = int(custom_terms_entry.get())
        series = fibonacci_series(start_value, num_terms)
        custom_result_label.config(text=f"Custom Fibonacci Series (starting from {start_value}): {series}")  # Display result in custom frame
    except ValueError:
        custom_result_label.config(text="Invalid input. Please enter integers.")

# Create the main window or design of the GUI 
window = Tk()
window.title("Fibonacci Series Generator")

# Default Fibonacci Series Frame
default_frame = LabelFrame(window, text="Default Fibonacci")
default_frame.grid(row=0, column=0, padx=10, pady=10)

default_terms_label = Label(default_frame, text="Number of Terms:")
default_terms_label.grid(row=0, column=0)
default_terms_entry = Entry(default_frame)
default_terms_entry.grid(row=0, column=1)

default_generate_button = Button(default_frame, text="Generate", command=generate_default_series)
default_generate_button.grid(row=1, column=0, columnspan=2)

default_result_label = Label(default_frame, text="")
default_result_label.grid(row=2, column=0, columnspan=2)

# Custom Fibonacci Series Frame
custom_frame = LabelFrame(window, text="Custom Fibonacci")
custom_frame.grid(row=1, column=0, padx=10, pady=10)

custom_start_label = Label(custom_frame, text="Starting Value:")
custom_start_label.grid(row=0, column=0)
custom_start_entry = Entry(custom_frame)
custom_start_entry.grid(row=0, column=1)

custom_terms_label = Label(custom_frame, text="Number of Terms:")
custom_terms_label.grid(row=1, column=0)
custom_terms_entry = Entry(custom_frame)
custom_terms_entry.grid(row=1, column=1)

custom_generate_button = Button(custom_frame, text="Generate", command=generate_custom_series)
custom_generate_button.grid(row=2, column=0, columnspan=2)

custom_result_label = Label(custom_frame, text="", wraplength=150) 
custom_result_label.grid(row=3, column=0, columnspan=2)

# Run the main event loop
window.mainloop()