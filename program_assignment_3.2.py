from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

class Window:
    def __init__(self, master):
        self.master = master
        self.master.geometry("950x600")
        self.master.title("Fruity Corner Shop")
        self.master.iconbitmap(r'favicon.ico')
        self.master.configure(bg="black")
        self.master.resizable(False, False)
        
        # Upper Frame 
        upper_frame = Frame(master, background="#CB5B3B")
        upper_frame.configure(height=50)
        label0 = Label(upper_frame, text="SHOP FRESH APPLES NOW!!", font=("8514oem", 50), fg="yellow", bg="#CB5B3B")
        label0.pack(padx=10, pady=10)
        upper_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Welcome Message 
        welcome_label = Label(upper_frame, text= "Here is the available apples in the shop:", font=("8514oem", 11), fg= "cyan", bg="#CB5B3B")
        welcome_label.pack(anchor=CENTER, padx=10, pady=10)
        
        # Left Frame 
        left_frame = Frame(master, background="#FFC34E", highlightbackground="black", highlightcolor="black", highlightthickness=2)
        left_frame.grid(row=1, column=0, sticky="nsew")
        left_frame.grid_rowconfigure(0, weight=1)  
        left_frame.grid_columnconfigure(0, weight=1)  

        # Red Apple Image 
        red_apple_img = Image.open("applee.png")
        red_apple_img = red_apple_img.resize((200, 200))
        red_apple_photo = ImageTk.PhotoImage(red_apple_img)
        red_apple_label = Label(left_frame, image=red_apple_photo, bg="#FFC34E")
        red_apple_label.image = red_apple_photo
        red_apple_label.pack(padx=20, pady=(10, 20), anchor="center", fill="both", expand=True)

        # Price of Red Apple 
        red_price_label = Label(left_frame, text="Php 25", font=("Terminal", 20), fg="black", bg="#FFC34E")
        red_price_label.pack(padx=20, pady=(1, 20))

        # Right Frame 
        right_frame = Frame(master, background="#91D474", highlightbackground="black", highlightcolor="black", highlightthickness=2)
        right_frame.grid(row=1, column=1, sticky="nsew")
        right_frame.grid_rowconfigure(0, weight=1)  
        right_frame.grid_columnconfigure(0, weight=1)  

        # Green Apple Image 
        green_apple_img = Image.open("greenapple.png")
        green_apple_img = green_apple_img.resize((200, 200))
        green_apple_photo = ImageTk.PhotoImage(green_apple_img)
        green_apple_label = Label(right_frame, image=green_apple_photo, bg="#91D474")
        green_apple_label.image = green_apple_photo
        green_apple_label.pack(padx=20, pady=(10, 20), anchor="center", fill="both", expand=True)

        # Price of Green Apple 
        green_price_label = Label(right_frame, text="Php 30", font=("Terminal", 20), fg="black", bg="#91D474")
        green_price_label.pack(padx=20, pady=(1, 20))

        # Bottom Frame 
        bottom_frame = Frame(master, background="#CB5B3B")
        bottom_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")
        bottom_frame.grid_rowconfigure(0, weight=1)  
        bottom_frame.grid_rowconfigure(1, weight=1)  
        bottom_frame.grid_columnconfigure(0, weight=1) 
        bottom_frame.grid_columnconfigure(1, weight=1)  

        # User Input Amount of Money 
        label_money = Label(bottom_frame, text="Enter the amount of money you have: Php", font=("Terminal", 11), fg="cyan", bg="#CB5B3B")
        label_money.grid(row=0, column=0, padx=10, pady=10, sticky="e") 
        entry_money = Entry(bottom_frame)
        entry_money.grid(row=0, column=1, padx=10, pady=5, sticky="w",)  

        # User Input Price of Apple 
        label_price = Label(bottom_frame, text="Enter the price of an apple that you want: Php", font=("Terminal", 11), fg="cyan", bg="#CB5B3B")
        label_price.grid(row=1, column=0, padx=10, pady=10, sticky="e")  

        entry_price = Entry(bottom_frame)
        entry_price.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Calculation 
        def calculate_and_display():
            money = float(entry_money.get())
            apple_price = float(entry_price.get())

            # Input User limited to Price 25 or 30 
            if apple_price not in [25.0, 30.0]:
                messagebox.showerror("Error", "Please enter a valid price: 25 or 30")
                return

            max_apples = money // apple_price
            remaining_money = money % apple_price
            messagebox.showinfo("Results", f"Maximum apples you can buy: {max_apples}\nRemaining money: {remaining_money}\n\nThank you for your purchase.")

        # Calculation Button
        calculate_button = Button(bottom_frame, text="Calculate", command=calculate_and_display, width=5, height=1, bg="yellow")
        calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")  
        calculate_button.configure(width=3, height=1)

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)

root = Tk()
window = Window(root)
root.mainloop()
