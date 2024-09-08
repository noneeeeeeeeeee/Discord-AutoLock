import tkinter as tk
from tkinter import ttk

# Locking_Options.py


def create_locking_options_ui(locking_options_page):
    # Lock Options
    lock_options_frame = ttk.LabelFrame(locking_options_page, text="Lock Options")
    lock_options_frame.pack(padx=10, pady=10)

    lock_option_var = tk.StringVar()
    lock_option_var.set("Force Run in Background")

    lock_option_radio_buttons = [
        ("Force Run in Background", "Force Run in Background"),
        ("Force Close", "Force Close"),
        ("Overlay Lock", "Overlay Lock"),
        ("Auto Logout", "Auto Logout")
    ]

    for option_text, option_value in lock_option_radio_buttons:
        option_radio_button = ttk.Radiobutton(lock_options_frame, text=option_text, value=option_value, variable=lock_option_var)
        option_radio_button.pack(anchor=tk.W)

    def save_options():
        selected_option = lock_option_var.get()
        # Save the selected option
        print("Selected Option:", selected_option)

    save_button = ttk.Button(locking_options_page, text="Save", command=save_options)
    save_button.pack(pady=10)

    # Security Options
    security_options_frame = ttk.LabelFrame(locking_options_page, text="Security Options")
    security_options_frame.pack(padx=10, pady=10)

    security_var = tk.StringVar()
    security_var.set("None")

    def on_security_option_selected():
        selected_option = security_var.get()
        if selected_option == "Pin":
            # Enable only numeric input
            pin_entry.config(state=tk.NORMAL)
            pin_entry.config(validate="key")
            pin_entry.config(validatecommand=(pin_entry.register(validate_pin_input), "%P"))
            password_entry.config(state=tk.DISABLED)
            authenticator_entry.config(state=tk.DISABLED)
        elif selected_option == "Password":
            # Enable any character input
            pin_entry.config(state=tk.DISABLED)
            password_entry.config(state=tk.NORMAL)
            authenticator_entry.config(state=tk.DISABLED)
        elif selected_option == "Authenticator":
            # Disable all other inputs
            pin_entry.config(state=tk.DISABLED)
            password_entry.config(state=tk.DISABLED)
            authenticator_entry.config(state=tk.NORMAL)

    security_option_radio_buttons = [
        ("Pin", "Pin"),
        ("Password", "Password"),
        ("Authenticator (Soon)", "Authenticator")
    ]

    for option_text, option_value in security_option_radio_buttons:
        option_radio_button = ttk.Radiobutton(security_options_frame, text=option_text, value=option_value, variable=security_var, command=on_security_option_selected)
        option_radio_button.pack(anchor=tk.W)

        if option_value == "Authenticator":
            option_radio_button.config(state=tk.DISABLED)

    # Pin Entry
    def validate_pin_input(pin):
        return pin.isdigit() or pin == ""

    pin_entry = ttk.Entry(security_options_frame, state=tk.HIDDEN)
    pin_entry.pack(pady=5)

    # Password Entry
    password_entry = ttk.Entry(security_options_frame, show="*", state=tk.HIDDEN)
    password_entry.pack(pady=5)

    # Authenticator Entry
    authenticator_entry = ttk.Entry(security_options_frame, state=tk.HIDDEN)
    authenticator_entry.pack(pady=5)

    def save_options():
        selected_option = security_var.get()
        # Save the selected option
        print("Selected Security Option:", selected_option)
        if selected_option == "Pin":
            pin = pin_entry.get()
            # Save the pin
            print("Pin:", pin)
        elif selected_option == "Password":
            password = password_entry.get()
            # Save the password
            print("Password:", password)
        elif selected_option == "Authenticator":
            authenticator = authenticator_entry.get()
            # Save the authenticator
            print("Authenticator:", authenticator)

    save_button = ttk.Button(locking_options_page, text="Save", command=save_options)
    save_button.pack(pady=10)

    # Return the UI elements
    return lock_options_frame, security_options_frame
