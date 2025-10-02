import tkinter as tk
from SuccessFrame import show_success_frame
from data.menu import bill


def build_payment_frame(parent, go_back, selected_coffee):
    payment_frame = tk.Frame(parent)
    label = tk.Label(payment_frame, text="Confirm payment!", font=("Arial", 16, "bold"))
    label.pack(pady=10)
    
    # Display selected coffee details
    price = bill.get(selected_coffee, "Price not found")
    details = f"You selected: {selected_coffee}\nPrice: ${price:.2f}"
    details_label = tk.Label(payment_frame, text=details, font=("Arial", 14, "bold" ))
    details_label.pack(pady=40)
       
    print("Selected coffee in payment frame:", selected_coffee)
    
    # Confirm Payment button
    def on_confirm():
        payment_frame.pack_forget()
        show_success_frame(parent, go_back, price)
    
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
