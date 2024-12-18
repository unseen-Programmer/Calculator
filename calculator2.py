import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title(" Calculator")
        self.root.resizable(False, False)  
        self.root.configure(bg="#2E2E2E")  

    
        self.current_input = ""
        self.first_number = None
        self.operation = None

        
        self.display = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="ridge",
                                bg="#1C1C1C", fg="white", justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

        # Define button properties
        button_props = {
            "font": ("Arial", 18),
            "bg": "#4E4E4E",
            "fg": "white",
            "bd": 0,
            "activebackground": "#6E6E6E",
            "activeforeground": "white",
            "width": 4,
            "height": 2
        }

        # Define buttons
        buttons = [
            {'text': '7', 'row': 1, 'col': 0, 'cmd': lambda: self.button_click('7')},
            {'text': '8', 'row': 1, 'col': 1, 'cmd': lambda: self.button_click('8')},
            {'text': '9', 'row': 1, 'col': 2, 'cmd': lambda: self.button_click('9')},
            {'text': '/', 'row': 1, 'col': 3, 'cmd': lambda: self.set_operation('division')},

            {'text': '4', 'row': 2, 'col': 0, 'cmd': lambda: self.button_click('4')},
            {'text': '5', 'row': 2, 'col': 1, 'cmd': lambda: self.button_click('5')},
            {'text': '6', 'row': 2, 'col': 2, 'cmd': lambda: self.button_click('6')},
            {'text': '*', 'row': 2, 'col': 3, 'cmd': lambda: self.set_operation('multiplication')},

            {'text': '1', 'row': 3, 'col': 0, 'cmd': lambda: self.button_click('1')},
            {'text': '2', 'row': 3, 'col': 1, 'cmd': lambda: self.button_click('2')},
            {'text': '3', 'row': 3, 'col': 2, 'cmd': lambda: self.button_click('3')},
            {'text': '-', 'row': 3, 'col': 3, 'cmd': lambda: self.set_operation('subtraction')},

            {'text': '0', 'row': 4, 'col': 0, 'cmd': lambda: self.button_click('0')},
            {'text': '.', 'row': 4, 'col': 1, 'cmd': lambda: self.button_click('.')},
            {'text': '=', 'row': 4, 'col': 2, 'cmd': self.calculate},
            {'text': '+', 'row': 4, 'col': 3, 'cmd': lambda: self.set_operation('addition')},

            {'text': 'CLEAR', 'row': 5, 'col': 0, 'colspan': 4, 'cmd': self.clear_display, 'bg': "#FF5733"}
        ]

        
        for btn in buttons:
            self.create_button(btn, button_props)

    def create_button(self, btn, props):
        """
        Creates a button with the given properties and places it on the grid.
        """
        button = tk.Button(self.root, text=btn['text'], command=btn['cmd'], **props)
        if 'colspan' in btn:
            button.grid(row=btn['row'], column=btn['col'], columnspan=btn['colspan'],
                        padx=5, pady=5, sticky="nsew")
        else:
            button.grid(row=btn['row'], column=btn['col'], padx=5, pady=5)

    def button_click(self, value):
        """
        Handles number and decimal point button clicks.
        """
        if value == '.' and '.' in self.current_input:
            return  # Prevent multiple decimals
        self.current_input += value
        self.update_display(self.current_input)

    def clear_display(self):
        """
        Clears the display and resets the calculator state.
        """
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.update_display("")

    def set_operation(self, operation):
        """
        Sets the current operation and stores the first number.
        """
        if self.current_input == "":
            return  
        try:
            self.first_number = float(self.current_input)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return
        self.operation = operation
        self.current_input = ""
        self.update_display("")

    def calculate(self):
        """
        Performs the calculation based on the set operation and displays the result.
        """
        if self.operation is None or self.current_input == "":
            return  

        try:
            second_number = float(self.current_input)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        try:
            result = None
            if self.operation == "addition":
                result = self.first_number + second_number
            elif self.operation == "subtraction":
                result = self.first_number - second_number
            elif self.operation == "multiplication":
                result = self.first_number * second_number
            elif self.operation == "division":
                if second_number == 0:
                    messagebox.showerror("Math Error", "Cannot divide by zero.")
                    self.clear_display()
                    return
                result = self.first_number / second_number

            if result is not None:
                # Remove trailing .0 for whole numbers
                if result == int(result):
                    result = int(result)
                self.update_display(str(result))
                self.current_input = str(result)
                self.operation = None
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.clear_display()

    def update_display(self, value):
        """
        Updates the display Entry widget with the given value.
        """
        self.display.delete(0, tk.END)
        self.display.insert(0, value)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
