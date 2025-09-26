import tkinter as tk
from tkinter import ttk
import time
import threading

class CoffeeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Machine")
        self.geometry("300x300")
        self.resizable(False, False)

        self.selected_drink = tk.StringVar()
        self.strength = tk.StringVar(value="Medium")
        self.milk = tk.BooleanVar(value=True)
        self.sugar = tk.IntVar(value=1)

        # Container for all screens
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary of all screens
        self.frames = {}

        for F in (WelcomeScreen, DrinkSelection, CustomizationScreen, BrewingScreen, FinishedScreen):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomeScreen)

    def show_frame(self, screen_class):
        frame = self.frames[screen_class]
        frame.tkraise()

class WelcomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="☕ CoffeeMate 3000", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self, text="Welcome!", font=("Helvetica", 14)).pack(pady=10)
        tk.Button(self, text="Start Brewing", command=lambda: controller.show_frame(DrinkSelection)).pack(pady=20)

class DrinkSelection(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Choose Your Drink", font=("Helvetica", 14)).pack(pady=10)

        for drink in ["Espresso", "Americano", "Latte", "Cappuccino"]:
            tk.Button(self, text=drink, width=20,
                      command=lambda d=drink: self.select_drink(controller, d)).pack(pady=5)

        tk.Button(self, text="Back", command=lambda: controller.show_frame(WelcomeScreen)).pack(pady=10)

    def select_drink(self, controller, drink):
        controller.selected_drink.set(drink)
        controller.show_frame(CustomizationScreen)

class CustomizationScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Customize Your Brew", font=("Helvetica", 14)).pack(pady=10)

        # Strength
        tk.Label(self, text="Strength:").pack()
        ttk.Combobox(self, textvariable=controller.strength,
                     values=["Mild", "Medium", "Strong"]).pack()

        # Milk
        tk.Label(self, text="Milk:").pack(pady=(10, 0))
        tk.Checkbutton(self, text="Add Milk", variable=controller.milk).pack()

        # Sugar
        tk.Label(self, text="Sugar (tsp):").pack(pady=(10, 0))
        tk.Spinbox(self, from_=0, to=3, textvariable=controller.sugar, width=5).pack()

        tk.Button(self, text="Confirm", command=lambda: controller.show_frame(BrewingScreen)).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: controller.show_frame(DrinkSelection)).pack()

class BrewingScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label = tk.Label(self, text="Brewing your coffee...", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

        self.after(500, self.start_brewing)

    def start_brewing(self):
        def brew():
            self.progress["value"] = 0
            for i in range(5):
                time.sleep(1)
                self.progress["value"] += 20
            self.controller.show_frame(FinishedScreen)

        threading.Thread(target=brew).start()

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.label.config(text=f"Brewing your {self.controller.selected_drink.get()}...")
        self.start_brewing()

class FinishedScreen(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.label = tk.Label(self, text="", font=("Helvetica", 14))
        self.label.pack(pady=20)

        tk.Label(self, text="☕ Enjoy your drink!").pack(pady=10)

        tk.Button(self, text="Make Another", command=lambda: controller.show_frame(WelcomeScreen)).pack(pady=10)
        tk.Button(self, text="Exit", command=controller.destroy).pack()

    def tkraise(self, *args, **kwargs):
        drink = self.controller.selected_drink.get()
        self.label.config(text=f"Your {drink} is ready!")
        super().tkraise(*args, **kwargs)

if __name__ == "__main__":
    app = CoffeeApp()
    app.mainloop()
