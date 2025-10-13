import tkinter as tk
from tkinter import messagebox
from SuccessFrame import show_success_frame
from data.menu import bill
from backend.MakeCoffee import make_coffee
from exception.stock_exception import OutOfStockError
from logger import logger


def build_payment_frame(parent, go_back, selected_coffee):
    payment_frame = tk.Frame(parent)
    label = tk.Label(payment_frame, text="Confirm payment!", font=("Arial", 16, "bold"))
    label.pack(pady=10)
    
    # Display selected coffee details
    price = bill.get(selected_coffee, "Price not found")
    details = f"You selected: {selected_coffee}\nPrice: ${price:.2f}"
    details_label = tk.Label(payment_frame, text=details, font=("Arial", 14, "bold"))
    details_label.pack(pady=40)
       
    logger(f"Selected coffee: {selected_coffee} selected. Price: ${price:.2f} confirmed.")
        
    # Confirm Payment button
    def on_confirm():
        try:
            make_coffee(selected_coffee)
            messagebox.showinfo("Success", f"{selected_coffee} is ready!")        
            payment_frame.pack_forget()
            show_success_frame(parent, go_back, price)
        except OutOfStockError as e:
            logger(f"Out of stock for {selected_coffee}.")
            messagebox.showerror("Out of Stock", str(e))
            payment_frame.after(2000, parent.quit)  # waits 2 seconds then exits
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong: {e}")
    
    logger(f"Payment for {selected_coffee} confirmed.")
    confirm_button = tk.Button(payment_frame, text="Confirm Payment", command=on_confirm)
    confirm_button.pack(pady=10)
    
    # Back button with image
    back_img = tk.PhotoImage(file="img/previous.png")
    back_img = back_img.subsample(14,14)  
    
    # Create button with image
    back_img = tk.PhotoImage(file="img/previous.png") 
    back_img = back_img.subsample(14,14)  
    
    def on_back():
        payment_frame.pack_forget()
        go_back()
    
    back_button = tk.Button(payment_frame, image=back_img, command=on_back, borderwidth=0)
    back_button.image = back_img  
    back_button.pack(pady=15)
    
    return payment_frame
