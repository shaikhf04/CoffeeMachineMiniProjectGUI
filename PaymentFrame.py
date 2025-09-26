import tkinter as tk
from data.menu import bill


def build_payment_frame(parent, go_back, selected_coffee):
    payment_frame = tk.Frame(parent)
    #payment_frame.pack(pady=10)
    label = tk.Label(payment_frame, text="Confirm payment!", font=("Arial", 14))
    label.pack(pady=10)

    print("Selected coffee in payment frame:", selected_coffee)
    
    # Create button with image
    back_img = tk.PhotoImage(file="img/previous.png")  # PNG format works best
    back_img = back_img.subsample(14,14)  
    back_button = tk.Button(payment_frame, image=back_img, command=go_back, borderwidth=0)
    back_button.image = back_img  
    back_button.pack(pady=10)
    

    return payment_frame
