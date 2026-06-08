import tkinter as tk

# ---------- FUNCTIONS ----------
def save_credentials():
    username = username_entry.get()
    password = password_entry.get()

    with open("credentials.txt", "a") as f:
        f.write(f"{username},{password}\n")

    result_label.config(text="Account created successfully!")


def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    try:
        with open("credentials.txt", "r") as f:
            credentials = f.readlines()
    except FileNotFoundError:
        result_label.config(text="No users found!")
        return

    for credential in credentials:
        stored_username, stored_password = credential.strip().split(",")

        if username == stored_username and password == stored_password:
            result_label.config(text="Login successful!")
            return

    result_label.config(text="Invalid credentials!")


# ---------- GUI ----------
root = tk.Tk()
root.title("Sign In System")
root.geometry("300x250")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Button(root, text="Sign In", command=check_credentials).pack(pady=5)
tk.Button(root, text="Sign Up", command=save_credentials).pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()