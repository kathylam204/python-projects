import tkinter as tk
from tkinter import messagebox, simpledialog

PASSWORD_FILE = "passwords.txt"

# ***This is just for practice, this hardcoded password wouldn't be secure in real life.***
MASTER_PASSWORD = "mysecret123"


def load_passwords():
    """Load passwords from the text file into a dict."""
    passwords = {}
    try:
        with open(PASSWORD_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # split only on the first space in case password has spaces
                username, password = line.split(" ", 1)
                passwords[username] = password
    except FileNotFoundError:
        # It's fine if the file doesn't exist yet
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Error reading password file: {e}")
    return passwords


def save_passwords(passwords):
    """Save the passwords dict back to the text file."""
    try:
        with open(PASSWORD_FILE, "w") as f:
            for username, password in passwords.items():
                f.write(f"{username} {password}\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving password file: {e}")

def add():
    username = entryName.get().strip()
    password = entryPassword.get().strip()

    if username and password:
        passwords = load_passwords()
        passwords[username] = password
        save_passwords(passwords)
        messagebox.showinfo("Success", "Password added!")
        entryName.delete(0, tk.END)
        entryPassword.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both fields.")

def get():
    username = entryName.get().strip()
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("Passwords", "No passwords stored yet.")
        return

    if username in passwords:
        messagebox.showinfo("Password", f"Password for {username} is: {passwords[username]}")
    else:
        messagebox.showinfo("Password", f"No such username: {username}")

def getlist():
    passwords = load_passwords()
    if not passwords:
        messagebox.showinfo("Passwords", "No passwords stored yet.")
        return

    mess = "List of passwords:\n"
    for name, password in passwords.items():
        mess += f"Password for {name} is {password}\n"

    messagebox.showinfo("Passwords", mess)

def delete():
    username = entryName.get().strip()
    if not username:
        messagebox.showerror("Error", "Please enter a username to delete.")
        return

    passwords = load_passwords()
    if username not in passwords:
        messagebox.showinfo("Delete", f"No such username: {username}")
        return

    confirm = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete {username}?"
    )
    if not confirm:
        return

    del passwords[username]
    save_passwords(passwords)
    messagebox.showinfo("Success", f"User {username} deleted successfully!")

def require_master_password(root):
    """Prompt for master password before showing the main window."""
    attempts = 3
    for _ in range(attempts):
        pwd = simpledialog.askstring(
            "Master Password",
            "Enter master password:",
            show="*",
            parent=root
        )
        if pwd is None:
            # User cancelled
            break
        if pwd == MASTER_PASSWORD:
            return True
        else:
            messagebox.showerror("Error", "Incorrect master password.")

    # If we get here, login failed
    messagebox.showerror("Access Denied", "Too many failed attempts. Exiting.")
    return False

if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()  # hide main window until master password is verified

    if not require_master_password(app):
        app.destroy()
    else:
        app.deiconify()  # show main window after successful login
        app.geometry("560x270")
        app.title("Password Manager (with Master Password)")

        # Username block
        labelName = tk.Label(app, text="USERNAME:")
        labelName.grid(row=0, column=0, padx=15, pady=15, sticky="e")
        entryName = tk.Entry(app)
        entryName.grid(row=0, column=1, padx=15, pady=15)

        # Password block
        labelPassword = tk.Label(app, text="PASSWORD:")
        labelPassword.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entryPassword = tk.Entry(app, show="*")
        entryPassword.grid(row=1, column=1, padx=10, pady=5)

        # Add button
        buttonAdd = tk.Button(app, text="Add", command=add)
        buttonAdd.grid(row=2, column=0, padx=15, pady=8, sticky="we")

        # Get button
        buttonGet = tk.Button(app, text="Get", command=get)
        buttonGet.grid(row=2, column=1, padx=15, pady=8, sticky="we")

        # List Button
        buttonList = tk.Button(app, text="List", command=getlist)
        buttonList.grid(row=3, column=0, padx=15, pady=8, sticky="we")

        # Delete button
        buttonDelete = tk.Button(app, text="Delete", command=delete)
        buttonDelete.grid(row=3, column=1, padx=15, pady=8, sticky="we")

        app.mainloop()
