import tkinter as tk
from Enhanced_lab3_formulas import add, subtract, multiply, divide, calculate_sin, calculate_cos, calculate_tan, calculate_square_area, calculate_rectangle_area, calculate_triangle_area, calculate_circle_area
import math

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        # Make the window resizable horizontally
        self.root.resizable(True, False)  # Allow horizontal resizing
        
        # Display for the input/output (make it readonly)
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        
        # Create the display
        self.display = tk.Entry(root, textvariable=self.result_var, font=('Arial', 24), bd=10, relief='sunken', width=14, justify='right', state='readonly')
        self.display.grid(row=0, column=0, columnspan=5)  # Increase columnspan to 5 to leave space for the area button
        
        # Button layout
        buttons = [
            ('C', 1, 0), ('Area', 1, 1), ('Del', 1 ,2), ('/', 1, 3), ('sin', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('+/-', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
        
        # Area related UI elements (initially hidden)
        self.area_frame = tk.Frame(root)
        self.shape_var = tk.StringVar(value="0")
        self.area_label = tk.Label(self.area_frame, text="Choose a shape:", font=('Arial', 14))
        self.area_label.pack()

        self.square_radio = tk.Radiobutton(self.area_frame, text="Square", variable=self.shape_var, value="square", font=('Arial', 12), command=self.update_area_inputs)
        self.square_radio.pack()
        self.rectangle_radio = tk.Radiobutton(self.area_frame, text="Rectangle", variable=self.shape_var, value="rectangle", font=('Arial', 12), command=self.update_area_inputs)
        self.rectangle_radio.pack()
        self.triangle_radio = tk.Radiobutton(self.area_frame, text="Triangle", variable=self.shape_var, value="triangle", font=('Arial', 12), command=self.update_area_inputs)
        self.triangle_radio.pack()
        self.circle_radio = tk.Radiobutton(self.area_frame, text="Circle", variable=self.shape_var, value="circle", font=('Arial', 12), command=self.update_area_inputs)
        self.circle_radio.pack()

        self.area_entry_label = tk.Label(self.area_frame, text="Enter dimensions:", font=('Arial', 14))
        self.area_entry_label.pack()
        
        # Entry fields for dimensions (hidden initially)
        self.dimension_entries = {}
        
        self.area_button = tk.Button(self.area_frame, text="Calculate Area", font=('Arial', 12), command=self.calculate_area)
        self.area_button.pack()

        self.dims_frame = tk.Frame(self.area_frame)  # Frame to hold input fields
        self.dims_frame.pack()

        # Configure columns to be resizable for expansion of window
        root.grid_columnconfigure(4, weight=1, minsize=300)

    def on_button_click(self, button_text):
        current = self.result_var.get()
        
        if button_text == 'C':
            self.result_var.set("0")
        elif button_text == '=':
            try:
                result = self.evaluate_expression(current)
                self.result_var.set(f"{result:.2f}")
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == '.':
            self.handle_decimal_point(current)
        elif button_text == 'Del':
            self.handle_delete(current)
        elif button_text == '+/-':
            self.toggle_sign(current)
        elif button_text in ['sin', 'cos', 'tan']:
            self.handle_trig_function(button_text, current)
        elif button_text == 'Area':
            self.toggle_area_frame()
        else:
            self.handle_number_or_operator(current, button_text)

    def toggle_area_frame(self):
        """Show or hide the area calculation frame with radio buttons."""
        if self.area_frame.winfo_ismapped():
            self.area_frame.grid_forget()  # Hide area frame
        else:
            self.area_frame.grid(row=1, column=5, rowspan=5, padx=10)  # Show area frame in column 5 (after trig buttons)

    def update_area_inputs(self):
        """Update the dimension entry fields based on the selected shape."""
        # Clear any previous entry fields
        for widget in self.dims_frame.winfo_children():
            widget.destroy()

        shape = self.shape_var.get()

        # Show input fields based on the selected shape
        if shape == "square":
            self.create_dimension_entry("side", "Side Length")
        elif shape == "rectangle":
            self.create_dimension_entry("length", "Length")
            self.create_dimension_entry("width", "Width")
        elif shape == "triangle":
            self.create_dimension_entry("base", "Base")
            self.create_dimension_entry("height", "Height")
        elif shape == "circle":
            self.create_dimension_entry("radius", "Radius")

    def create_dimension_entry(self, name, label_text):
        """Helper function to create dimension input fields."""
        label = tk.Label(self.dims_frame, text=label_text, font=('Arial', 12))
        label.pack()
        entry = tk.Entry(self.dims_frame, font=('Arial', 12))
        entry.pack()
        self.dimension_entries[name] = entry

    def calculate_area(self):
        """Calculate the area of the selected shape based on the entered values."""
        shape = self.shape_var.get()

        try:
            if shape == "square":
                side = float(self.dimension_entries["side"].get())
                area = calculate_square_area(side)
            elif shape == "rectangle":
                length = float(self.dimension_entries["length"].get())
                width = float(self.dimension_entries["width"].get())
                area = calculate_rectangle_area(length, width)
            elif shape == "triangle":
                base = float(self.dimension_entries["base"].get())
                height = float(self.dimension_entries["height"].get())
                area = calculate_triangle_area(base, height)
            elif shape == "circle":
                radius = float(self.dimension_entries["radius"].get())
                area = calculate_circle_area(radius)

            self.result_var.set(f"{area:.2f}")
        except ValueError:
            self.result_var.set("Error")

    def handle_decimal_point(self, current):
        # If current input is "0", set it to "0."
        if current == "0":
            self.result_var.set("0.")
            return
        
        # Split the current expression into numbers based on operators
        operators = "+-*/"
        # Replace operators with spaces so we can split on space
        current_without_operators = current
        for operator in operators:
            current_without_operators = current_without_operators.replace(operator, ' ')

        # Check the last number entered (after split)
        parts = current_without_operators.split()
        last_part = parts[-1] if parts else ""

        # If the last number doesn't contain a decimal point, append a decimal point
        if '.' not in last_part:
            self.result_var.set(current + '.')


    def handle_delete(self, current):
        if len(current) > 1:
            self.result_var.set(current[:-1])
        else:
            self.result_var.set("0")
    
    def toggle_sign(self, current):
        if current == "0":
            pass
        elif current[0] == '-':
            self.result_var.set(current[1:])
        else:
            self.result_var.set('-' + current)
    
    def handle_number_or_operator(self, current, button_text):
        if current == "0":
            self.result_var.set(button_text)
        else:
            self.result_var.set(current + button_text)

    def handle_trig_function(self, trig_func, current):
        # Check if current input is a valid number
        try:
            angle_in_degrees = float(current)
        except ValueError:
            self.result_var.set("Error")
            return
        
        # Convert degrees to radians
        angle_in_radians = math.radians(angle_in_degrees)
        
        # Calculate the result based on the trig function
        if trig_func == 'sin':
            result = calculate_sin(angle_in_radians)
        elif trig_func == 'cos':
            result = calculate_cos(angle_in_radians)
        elif trig_func == 'tan':
            result = calculate_tan(angle_in_radians)

        # Display the result
        self.result_var.set(f"{result:.7f}")

    def evaluate_expression(self, expression):
        # Use eval to evaluate simple expressions, like '1 + 1'
        try:
            result = eval(expression)
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
        return result
