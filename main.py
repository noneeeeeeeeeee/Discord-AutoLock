import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def get_patchnotes():
    try:
        response = requests.get("https://github.com/noneeeeeeeeeee/Discord-AutoLock")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the patchnotes here
        patchnotes = soup.find("div", class_="release-notes").text
        return patchnotes
    except requests.exceptions.RequestException as e:
        return "Failed to connect: " + str(e)

def create_home_page():
    home_page = ttk.Frame(content_frame)
    patchnotes_label = ttk.Label(home_page, text=get_patchnotes())
    patchnotes_label.pack()
    return home_page

def create_locking_options_page():
    locking_options_page = ttk.Frame(content_frame)
    
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
        ("Authenticator", "Authenticator")
    ]

    for option_text, option_value in security_option_radio_buttons:
        option_radio_button = ttk.Radiobutton(security_options_frame, text=option_text, value=option_value, variable=security_var, command=on_security_option_selected)
        option_radio_button.pack(anchor=tk.W)

    # Pin Entry
    def validate_pin_input(pin):
        return pin.isdigit() or pin == ""

    pin_entry = ttk.Entry(security_options_frame, state=tk.DISABLED)
    pin_entry.pack(pady=5)

    # Password Entry
    password_entry = ttk.Entry(security_options_frame, show="*", state=tk.DISABLED)
    password_entry.pack(pady=5)

    # Authenticator Entry
    authenticator_entry = ttk.Entry(security_options_frame, state=tk.DISABLED)
    authenticator_entry.pack(pady=5)

    return locking_options_page
def create_customization_page():
    customization_page = ttk.Frame(content_frame)
    # Create the customization UI here
    return customization_page

def create_settings_page():
    settings_page = ttk.Frame(content_frame)
    # Create the settings UI here
    return settings_page

def switch_page(page):
    global current_page
    if current_page is not None:
        current_page.pack_forget()
    current_page = page
    current_page.pack()

def create_sidebar():
    sidebar = ttk.Frame(root, width=200)
    home_button = ttk.Button(sidebar, text="Home", command=lambda: switch_page(home_page))
    home_button.pack(fill=tk.X)
    locking_options_button = ttk.Button(sidebar, text="Locking Options", command=lambda: switch_page(locking_options_page))
    locking_options_button.pack(fill=tk.X)
    customization_button = ttk.Button(sidebar, text="Customization", command=lambda: switch_page(customization_page))
    customization_button.pack(fill=tk.X)
    settings_button = ttk.Button(sidebar, text="Settings", command=lambda: switch_page(settings_page))
    settings_button.pack(fill=tk.X)
    return sidebar

root = tk.Tk()
root.title("Discord AutoLock")
root.geometry("800x600")

sidebar = create_sidebar()
sidebar.pack(side=tk.LEFT, fill=tk.Y)

content_frame = ttk.Frame(root)
content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

home_page = create_home_page()
locking_options_page = create_locking_options_page()
customization_page = create_customization_page()
settings_page = create_settings_page()

current_page = None
switch_page(home_page)

root.mainloop()