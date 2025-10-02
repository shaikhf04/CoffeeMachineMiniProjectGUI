import tkinter as tk
from data.menu import bill

def show_success_frame(parent, go_back, price):
    success_frame = tk.Frame(parent)
    success_frame.pack(fill="both", expand=True)

    msg_label = tk.Label(success_frame, text="Payment Successful!", font=("Arial", 18, "bold"))
    msg_label.pack(pady=10)

    bill_label = tk.Label(success_frame, text=f"Total Paid: ${price:.2f}", font=("Arial", 14))
    bill_label.pack(pady=10)

    def on_done():
        success_frame.destroy()
        go_back()

    done_button = tk.Button(success_frame, text="Done", command=on_done)
    done_button.pack(pady=20)