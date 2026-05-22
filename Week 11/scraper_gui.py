from scrapper import get_cars_data, save_to_file
import tkinter as tk
from tkinter import ttk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Car Price Scraper")
root.geometry("750x500")
root.resizable(False, False)

# ---------------- DATA STORAGE ----------------
current_data = []

# ---------------- STATUS LABEL ----------------
status = tk.StringVar()
status.set("Select a brand and click Search")

status_label = tk.Label(root, textvariable=status, fg="blue")
status_label.pack(pady=5)

# ---------------- TOP FRAME (INPUT) ----------------
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

car_manufact = ['toyota', 'honda', 'suzuki']

dropdown = ttk.Combobox(top_frame, values=car_manufact, width=20)
dropdown.current(0)
dropdown.grid(row=0, column=0, padx=10)

# ---------------- SEARCH FUNCTION ----------------
def search():
    global current_data
    brand = dropdown.get()

    status.set("🔍 Searching data...")
    root.update()

    current_data = get_cars_data(brand)

    set_textarea(current_data)
    status.set(f"✅ Found {len(current_data)} records for {brand}")

# ---------------- SAVE FUNCTION ----------------
def save_data():
    if current_data:
        save_to_file(current_data, "cars.csv")
        status.set("💾 Data saved to cars.csv")
    else:
        status.set("⚠️ No data to save!")

# ---------------- BUTTONS ----------------
search_btn = tk.Button(top_frame, text="Search", width=12, command=search)
search_btn.grid(row=0, column=1, padx=5)

save_btn = tk.Button(top_frame, text="Save CSV", width=12, command=save_data)
save_btn.grid(row=0, column=2, padx=5)

# ---------------- TEXT FRAME ----------------
text_frame = tk.Frame(root)
text_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

textarea = tk.Text(text_frame, height=20, width=85, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)

# ---------------- DISPLAY FUNCTION ----------------
def set_textarea(data):
    textarea.delete(1.0, tk.END)

    if not data:
        textarea.insert(tk.END, "No data found.\n")
        return

    for car in data:
        textarea.insert(
            tk.END,
            f"Name: {car['name']}\nPrice: {car['price']}\n----------------------\n"
        )

# ---------------- START ----------------
root.mainloop()