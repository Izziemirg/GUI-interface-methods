import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import messagebox


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='solar')
        self.root.title("Login Application")
        self.root.geometry("650x550")

        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.pack(expand=True, fill='both')

        self.title_label = ttk.Label(self.main_frame, text="Login", font=('Roboto', 24))
        self.title_label.pack(pady=20)

        self.username_frame = ttk.Frame(self.main_frame)
        self.username_frame.pack(fill='x', pady=5)

        self.username_label = ttk.Label(self.username_frame, text="Username:", font=('Roboto', 11))
        self.username_label.pack(anchor='w')

        self.username_entry = ttk.Entry(self.username_frame, font=('Roboto', 11))
        self.username_entry.pack(fill='x', pady=(5, 0))

        self.password_frame = ttk.Frame(self.main_frame)
        self.password_frame.pack(fill='x', pady=5)

        self.password_label = ttk.Label(self.password_frame, text="Password:", font=('Roboto', 11))
        self.password_label.pack(anchor='w')

        self.password_entry = ttk.Entry(self.password_frame, show="•", font=('Roboto', 11))
        self.password_entry.pack(fill='x', pady=(5, 0))

        self.login_button = ttk.Button(self.main_frame, text="Login", command=self.verify_login, bootstyle="success",
                                       width=20)
        self.login_button.pack(pady=20)

        self.root.bind('<Return>', lambda event: self.verify_login())

        self.username_entry.focus()

    def verify_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "main_admin" and password == "Lets_work":
            messagebox.showinfo("Success", "Login successful!", icon='info')
            self.clear_fields()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            self.password_entry.delete(0, tk.END)

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.username_entry.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()