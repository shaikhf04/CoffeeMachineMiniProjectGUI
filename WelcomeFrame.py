import tkinter as tk
from OrderFrame import build_order_frame
from PaymentFrame import build_payment_frame

def welcome():
    print("Welcome to Coffee Bot!")
root = tk.Tk()
root.title("Coffee Bot")
root.geometry("300x400")
root.resizable(False, False)

# Build order frame but keep it hidden initially do not pack it
#order_frame = build_order_frame(root) 

# Create a frame for the welcome screen
welcome_frame = tk.Frame(root)
welcome_frame.pack(pady=10)

label = tk.Label(welcome_frame, text="Welcome to Coffee Bot!", font=("Arial", 16, "bold"))
label.pack(pady=20)

# Load the image
image = tk.PhotoImage(file="img/coffee-shop.png")  # PNG format works best
image = image.subsample(4,4)  # Resize the image if it's too large
image_label = tk.Label(welcome_frame, image=image)
image_label.pack(pady=10)

# Create a button with the image
start = tk.PhotoImage(file="img/start-button.png")  # PNG format works best
start = start.subsample(5,5)  # Resize the image if it's too large

def go_to_order():
    welcome_frame.pack_forget() # Hide welcome frame
    order_frame.pack()          # Show order frame we are now packing it

def go_back():
    order_frame.pack_forget()
    welcome_frame.pack()

# Now pass `go_back` to the function:
order_frame = build_order_frame(root, go_back)

img_button = tk.Button(welcome_frame, image=start, command=go_to_order, borderwidth=0)
img_button.pack(pady=20)

welcome_frame.pack()

root.mainloop()
