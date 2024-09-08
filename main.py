import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import sys
import webbrowser 
from menu_items.Locking_Options import create_locking_options_ui




def get_patchnotes():
    try:
        response = requests.get(f"https://github.com/noneeeeeeeeeee/Discord-AutoLock/releases/latest")
        response.raise_for_status()
        latest_tag = response.url.split("/")[-1]
        current_version = "1.0.0"  # Replace with your current version
        if latest_tag != current_version:
            if "current_page" in globals() and current_page == home_page:
                update_button = ttk.Button(content_frame, text="Download Update", command=lambda: webbrowser.open("https://github.com/noneeeeeeeeeee/Discord-AutoLock/releases/latest"))
                update_button.grid(row=0, column=0, sticky="ne", padx=10, pady=10)
            else:
                update_button = ttk.Button(content_frame, text="Download Update")
                update_button.grid_forget()
        patchnotes = response.text
        soup = BeautifulSoup(patchnotes, "html.parser")
        patchnotes_body = soup.find("div", class_="markdown-body")
        if patchnotes_body:
            return patchnotes_body.get_text().strip()
        else:
            return "No patchnotes found"
    except requests.exceptions.RequestException as e:
        return "Failed to connect: " + str(e)

def create_home_page():
    home_page = ttk.Frame(content_frame)
    patchnotes_label = ttk.Label(home_page, text=get_patchnotes())
    patchnotes_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    return home_page


def create_locking_options_page():
    locking_options_page = ttk.Frame(content_frame)
    sys.path.append('./menu_items')

    create_locking_options_ui(locking_options_page)
   
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
        current_page.grid_forget()
    current_page = page
    current_page.grid(row=0, column=1, sticky="nsew")

def create_sidebar():
    sidebar = ttk.Frame(root, width=200)
    
    home_button = ttk.Button(sidebar, text="Home", command=lambda: switch_page(home_page))
    home_button.grid(row=0, column=0, sticky="ew", pady=5)
    
    locking_options_button = ttk.Button(sidebar, text="Locking Options", command=lambda: switch_page(locking_options_page))
    locking_options_button.grid(row=1, column=0, sticky="ew", pady=5)
    
    customization_button = ttk.Button(sidebar, text="Customization", command=lambda: switch_page(customization_page))
    customization_button.grid(row=2, column=0, sticky="ew", pady=5)
    
    settings_button = ttk.Button(sidebar, text="Settings", command=lambda: switch_page(settings_page))
    settings_button.grid(row=3, column=0, sticky="ew", pady=5)
    
    return sidebar

root = tk.Tk()
root.title("Discord AutoLock")
root.geometry("800x600")

sidebar = create_sidebar()
sidebar.grid(row=0, column=0, sticky="ns")

content_frame = ttk.Frame(root)
content_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

home_page = create_home_page()
locking_options_page = create_locking_options_page()
customization_page = create_customization_page()
settings_page = create_settings_page()

current_page = None
switch_page(home_page)

root.mainloop()
