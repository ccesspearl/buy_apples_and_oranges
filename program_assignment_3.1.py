import tkinter as tk
from PIL import Image, ImageTk
from art import *

# Window
window = tk.Tk()
window.geometry("950x550")
window.title("Fruity Corner Shop")
window.iconbitmap(r'favicon.ico')
window.configure(bg="black")
window.resizable(False, False)

# Left Frame
left_frame = tk.Frame(window, bg="orange")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Left Frame Image
img_pil = Image.open("pic2.png")
img_tk = ImageTk.PhotoImage(img_pil)
bg_img = tk.Label(master=left_frame, image=img_tk, bg="orange")
bg_img.pack(padx=60, pady=70, anchor='nw')

# Right Frame 
right_frame = tk.Frame(window, bg="#267894")  
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Calculation for Fruits Quantity 
def calculation (apple_quantity, orange_quantity):
    apple = 20  # Price of Apple 
    orange = 25  # Price of Orange
    
    product_apple = apple_quantity * apple
    product_orange = orange_quantity * orange
    
    total_sum = product_apple + product_orange
    return total_sum

# Getting Information from Users
def calculate():
    apple_input = int(apple_entry.get())
    orange_input = int(orange_entry.get())
    total_amount = calculation (apple_input, orange_input)
    output_label.config(text=f"The total amount is ₱{total_amount}.")

# Welcome Text 
welcome_label = tk.Label(right_frame, text= "\nFRUITY CORNER SHOP", font=("8514oem", 35), fg= "yellow", bg="#267894")
welcome_label.pack(anchor=tk.CENTER, padx=20, pady=10)

# Welcome Text 
welcome_label = tk.Label(right_frame, text= '"Fresh Picks for Fresh Starts"', font=("8514oem", 20), fg= "#59FF00", bg="#267894")
welcome_label.pack(anchor=tk.CENTER, padx=20, pady=10)

# Apple Icon 
apple_icon = Image.open("apple.png")  
apple_icon = apple_icon.resize((30, 30))  
apple_icon_tk = ImageTk.PhotoImage(apple_icon)

# Apple Price with Icon
apple_price_frame = tk.Frame(right_frame, bg="#267894")
apple_price_frame.pack(anchor=tk.CENTER, padx=20, pady=10)

apple_icon_label = tk.Label(apple_price_frame, image=apple_icon_tk, bg="#267894")
apple_icon_label.pack(side=tk.LEFT)

apple_price_text = "Apple Price: ₱20"
apple_price_label = tk.Label(apple_price_frame, text= apple_price_text, font=("Times New Roman", 15, "bold"), fg="yellow", bg="#267894")
apple_price_label.pack(side=tk.LEFT)

# Orange Icon
orange_icon = Image.open("orange.png")  
orange_icon = orange_icon.resize((30, 30))  
orange_icon_tk = ImageTk.PhotoImage(orange_icon)

# Orange Price with Icon
orange_price_frame = tk.Frame(right_frame, bg="#267894")
orange_price_frame.pack(anchor=tk.CENTER, padx=20, pady=10)

orange_icon_label = tk.Label(orange_price_frame, image=orange_icon_tk, bg="#267894")
orange_icon_label.pack(side=tk.LEFT)

orange_price_text = "Orange Price: ₱25"
orange_price_label = tk.Label(orange_price_frame, text= orange_price_text, font=("Times New Roman", 15, "bold"), fg="yellow", bg="#267894")
orange_price_label.pack(side=tk.LEFT)

# User Input Widgets
apple_label = tk.Label(right_frame, text="How many apples you want to buy?", fg="cyan", bg="#267894", font=("Terminal", 15, "bold"))
apple_label.pack(anchor=tk.CENTER, padx=20, pady=5)
apple_entry = tk.Entry(right_frame, bg="white")
apple_entry.pack(anchor=tk.CENTER, padx=20, pady=5)

orange_label = tk.Label(right_frame, text="How many oranges you want to buy?", fg="cyan", bg="#267894", font=("Terminal", 15, "bold"))
orange_label.pack(anchor=tk.CENTER, padx=20, pady=5)
orange_entry = tk.Entry(right_frame, bg="white")
orange_entry.pack(anchor=tk.CENTER, padx=20, pady=5)

# Button
calculate_button = tk.Button(right_frame, text="Calculate", command=calculate)
calculate_button.pack(anchor=tk.CENTER, padx=20, pady=10)

# Display the output
output_label = tk.Label(right_frame, text="", font=("Terminal", 14, "bold"), fg="yellow", bg="#267894")
output_label.pack(anchor=tk.CENTER, padx=15, pady=10)

window.mainloop()
