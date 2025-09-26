import tkinter as tk
from PaymentFrame import build_payment_frame

def build_order_frame(parent, go_back):
    order_frame = tk.Frame(parent)
    label = tk.Label(order_frame, text="Order your coffee here!", font=("Arial", 14))
    label.pack(pady=10)

    selected_coffee = tk.StringVar(value="")
    coffee_buttons = {}

    images = {
        "Black Coffee": tk.PhotoImage(file="img/black-coffee.png").subsample(12,12),
        "Latte": tk.PhotoImage(file="img/latte.png").subsample(12,12),
        "Cappuccino": tk.PhotoImage(file="img/cappuccino.png").subsample(12,12)
    }

    def select_coffee(name):
        selected_coffee.set(name)
        # Highlight selected button
        for btn_name, btn in coffee_buttons.items():
            if btn_name == name:
                btn.config(relief=tk.SUNKEN, borderwidth=5)
            else:
                btn.config(relief=tk.RAISED, borderwidth=1)

    for name, img in images.items():
        btn = tk.Button(order_frame, image=img, command=lambda n=name: select_coffee(n), borderwidth=1)
        btn.image = img
        btn.pack(pady=2)
        coffee_buttons[name] = btn
        label = tk.Label(order_frame, text=name)
        label.pack(pady=2)

    # Create button with image
    back_img = tk.PhotoImage(file="img/previous.png")
    back_img = back_img.subsample(14,14)
    back_button = tk.Button(order_frame, image=back_img, command=go_back, borderwidth=0)
    back_button.image = back_img
    back_button.pack(pady=5)

    # Create button to proceed to payment
    next_img = tk.PhotoImage(file="img/next.png")
    next_img = next_img.subsample(14,14)

    def go_to_payment():
        if selected_coffee.get():
            order_frame.pack_forget()
            payment_frame = build_payment_frame(parent, go_back, selected_coffee.get())
            payment_frame.pack()
        else:
            # Show a warning if no coffee is selected
            warning = tk.Label(order_frame, text="Please select a coffee!", fg="red")
            warning.pack()
            order_frame.after(1500, warning.destroy)

    next_button = tk.Button(order_frame, image=next_img, command=go_to_payment, borderwidth=0)
    next_button.image = next_img
    next_button.pack(pady=5)

    return order_frame
