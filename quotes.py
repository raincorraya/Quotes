import tkinter as tk
import requests
from tkinter import PhotoImage

api = "http://api.quotable.io/random"
quotes = []
quote_number = 0

def fetch_quote():
    global quotes, quote_number
    response = requests.get(api)
    if response.status_code == 200:
        data = response.json()
        quote = data["content"]
        author = data["author"]
        quotes.append((quote, author))
        quote_number = len(quotes) - 1
        update_quote_label()

def update_quote_label():
    global quote_number
    quote_label.config(text=quotes[quote_number][0])

def next_quote():
    fetch_quote()

window = tk.Tk()
window.geometry("900x400")
window.title("Quote generator")
window.grid_columnconfigure(0, weight=1)
window.resizable(False, False)

# Load the background image
image_path = PhotoImage(file=r"C:\Users\User\Pictures\n\usetldr_10384376_u_10691787_image_format_uRVnLon66oNHk1l.png")
bg_image = tk.Label(window, image=image_path)
bg_image.place(x=0, y=0, relwidth=1, relheight=1)  # This will cover the whole window

# Change the border color to red
window.config(bd=10, relief=tk.SOLID, highlightbackground="red")

# Create a label for the quote with transparent background
quote_label = tk.Label(window, text="Fetching quote...", wraplength=700, font=("Arial", 14), fg="Black", bg="green")
quote_label.pack(pady=40)


# Load the button image
button_icon = PhotoImage(file=r"C:\Users\User\Pictures\Saved Pictures\50.png")

# Create the button with the loaded image
next_button = tk.Button(window, image=button_icon, command=next_quote, bd=0)  # Set bd=0 to remove the button border
next_button.image = button_icon  # Keep a reference to the image to prevent garbage collection
next_button.pack(side=tk.BOTTOM, pady=16)

window.mainloop()
