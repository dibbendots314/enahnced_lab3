import sys
from Enhanced_lab3_formulas import add, subtract, multiply, divide
from Enhanced_lab3_gui import CalculatorApp  # Import the CalculatorApp class from gui.py
import tkinter as tk

def main():
    # Run the GUI
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
