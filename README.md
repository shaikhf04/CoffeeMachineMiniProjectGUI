# CoffeeMachineMiniProjectGUI ☕

A **GUI-based coffee machine simulator** built in Python using the `tkinter` library, designed to provide a realistic and interactive coffee ordering experience. The application features **ingredient stock management**, **intuitive user interface with dynamic screens**, and **automated billing**. Built with a modular and object-oriented design, it also incorporates a **custom logger** that tracks user actions and system events in log files — ensuring a practical and production-ready solution.

## 📌 Key Concepts Demonstrated

- 🔹 **Object-Oriented Programming (OOP)**
- 🔹 **Custom Exception Handling**
- 🔹 **Stock and Inventory Management**
- 🔹 **Logging to file for user actions and errors**
- 🔹 **User interaction via Terminal and Tkinter GUI**
- 🔹 **Clean, modular, and extensible code structure**

---

## 🚀 Features

- ✅ Checks ingredient availability before making coffee  
- ⚠️ Raises custom exceptions on insufficient stock  
- 📝 Logs important events and errors  
- 💬 Interactive menu and GUI interface for coffee orders  
- 💰 Handles billing and price calculations in a modular way  
- 🔄 Easy to extend with new coffee recipes or UI features

---

# Coffee Machine Mini Project ☕

## 🛠️ How to Run the Project

1. ✅ Ensure **Python 3.x** is installed:
   ```bash
   python --version

2. 📥 Clone this repository:

    ```bash
    git clone https://github.com/shaikhf04/CoffeeMachineMiniProjectGUI.git
    cd CoffeeMachineMiniProjectGUI
    ```

3. ▶️ Run the app:

    ```bash
    python WelcomeFrame.py

## 📁 Project Structure

   ```plaintext
   CoffeeMachineMiniProjectGUI/
   ├── assets/                # Images, icons, and other media assets for the GUI
   ├── backend/               # Core backend logic (coffee making, stock management, exceptions)
   ├── data/                  # Data files such as ingredient lists, recipes, and pricing
   ├── gui/                   # GUI-related modules and frames built using Tkinter
   ├── logs/                  # Automatically generated log files for user activity and errors
   ├── main.py                # Main entry point for running the GUI application
   ├── requirements.txt       # Python dependencies and versions required for the project
   ├── README.md              # Project documentation (this file)
   └── .gitignore             # Specifies files/folders to ignore in Git version control
   
