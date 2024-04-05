import tkinter as tk
import random

class ATMInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure PIN Entry")

        self.pin_digits = [str(i) for i in range(10)]
        self.pin_entry = []
        self.pin_label = tk.Label(root, text="Enter PIN:")
        self.pin_label.pack()

        self.create_dynamic_keypad()

    def create_dynamic_keypad(self):
        # Randomize the layout of the keypad
        random.shuffle(self.pin_digits)

        for digit in self.pin_digits:
            button = tk.Button(self.root, text=digit, width=5, height=2, command=lambda d=digit: self.handle_keypress(d))
            button.pack(side=tk.LEFT)

    def handle_keypress(self, digit):
        # Process the keypress (e.g., display '*' on the screen)
        self.pin_entry.append(digit)
        self.display_masked_pin()

    def display_masked_pin(self):
        # Display '*' for each entered digit
        masked_pin = '*' * len(self.pin_entry)
        self.pin_label.config(text=f"Enter PIN: {masked_pin}")

        # Check if the PIN entry is complete (e.g., 4 digits)
        if len(self.pin_entry) == 4:
            self.verify_pin()

    def verify_pin(self):
        # Add your PIN verification logic here
        entered_pin = ''.join(self.pin_entry)

        # For demonstration purposes, printing the entered PIN
        print("Entered PIN:", entered_pin)

        # Clear PIN entry after verification
        self.clear_pin_entry()

    def clear_pin_entry(self):
        # Clear PIN entry and create a new dynamic keypad for the next entry
        self.pin_entry = []
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_dynamic_keypad()


if __name__ == "__main__":
    root = tk.Tk()
    atm_interface = ATMInterface(root)
    root.mainloop()
