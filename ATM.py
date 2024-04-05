import tkinter as tk
from tkinter import messagebox
import random

class ATMInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure PIN Entry")

        self.color_digits = [str(i) for i in range(10)]
        self.color_entry = []
        self.color_label = tk.Label(root, text="Enter Color Code:")
        self.color_label.pack()

        self.create_dynamic_keypad()

    def create_dynamic_keypad(self):
        # Create a dictionary to store colors for each digit
        digit_colors = {str(i): random.choice(['#FF5733', '#FFC300', '#DAF7A6', '#C70039', '#900C3F']) for i in range(10)}

        for digit in self.color_digits:
            button = tk.Button(self.root, text=digit, width=5, height=2, bg=digit_colors[digit], command=lambda d=digit: self.handle_color_keypress(d))
            button.pack(side=tk.LEFT)

    def handle_color_keypress(self, digit):
        # Process the keypress (e.g., display entered digits)
        self.color_entry.append(digit)
        self.display_entered_color()

    def display_entered_color(self):
        # Display entered color digits
        entered_color = ''.join(self.color_entry)
        self.color_label.config(text=f"Enter Color Code: {entered_color}")

        # Check if the color code entry is complete (e.g., 10 digits)
        if len(self.color_entry) == 10:
            self.show_pin_entry()

    def show_pin_entry(self):
        # Close the color entry interface
        self.root.withdraw()

        # Create a new window for displaying the PIN entry interface
        pin_window = tk.Toplevel()
        pin_window.title("PIN Entry")

        self.pin_digits = [str(i) for i in range(10)]
        self.pin_entry = []
        self.pin_label = tk.Label(pin_window, text="Enter PIN:")
        self.pin_label.pack()

        self.create_dynamic_pin_keypad(pin_window)

    def create_dynamic_pin_keypad(self, pin_window):
        # Randomize the layout of the keypad
        random.shuffle(self.pin_digits)

        for digit in self.pin_digits:
            button = tk.Button(pin_window, text=digit, width=5, height=2, command=lambda d=digit: self.handle_pin_keypress(d))
            button.pack(side=tk.LEFT)

    def handle_pin_keypress(self, digit):
        # Process the keypress (e.g., display '*' on the screen)
        self.pin_entry.append(digit)
        self.display_masked_pin()

    def display_masked_pin(self):
        # Display '*' for each entered digit
        masked_pin = '*' * len(self.pin_entry)
        self.pin_label.config(text=f"Enter PIN: {masked_pin}")

        # Check if the PIN entry is complete (e.g., 4 digits)
        if len(self.pin_entry) == 4:
            self.show_atm_interface()

    def show_atm_interface(self):
        # Close the PIN entry interface
        self.root.destroy()

        # Create a new window for the ATM interface
        atm_window = tk.Tk()
        atm_window.title("ATM Interface")

        # Create ATM instance
        atm = ATM(atm_window)

        atm_window.mainloop()

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM GUI")

        # Initialize balance
        self.balance = 1000

        # Create labels
        self.balance_label = tk.Label(root, text="Balance: $1000")
        self.amount_label = tk.Label(root, text="Enter Amount:")

        # Create entry widget
        self.amount_entry = tk.Entry(root)

        # Create buttons
        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.check_balance_button = tk.Button(root, text="Check Balance", command=self.check_balance)

        # Layout
        self.balance_label.grid(row=0, column=0, columnspan=2)
        self.amount_label.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)
        self.withdraw_button.grid(row=2, column=0)
        self.deposit_button.grid(row=2, column=1)
        self.check_balance_button.grid(row=3, column=0, columnspan=2)

    def withdraw(self):
        amount = self.get_amount()
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Error", "Insufficient funds")
            else:
                self.balance -= amount
                self.update_balance()

    def deposit(self):
        amount = self.get_amount()
        if amount is not None:
            self.balance += amount
            self.update_balance()

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your balance is: ${self.balance}")

    def get_amount(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero")
                return None
            return amount
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
            return None

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")
if __name__ == "__main__":
    root = tk.Tk()
    atm_interface = ATMInterface(root)
    root.mainloop()
