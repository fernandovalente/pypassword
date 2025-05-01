import random
import string
import pyperclip
import tkinter as tk
from tkinter import ttk, messagebox


class PasswordGeneratorLogic:
    def __init__(self):
        self.uppercase = True
        self.lowercase = True
        self.special = True
        self.numbers = True
        self.length = 12

    def generate_password(self):
        if self.length < 4:
            return None
            
        if not any([self.uppercase, self.lowercase, self.special, self.numbers]):
            return None
            
        chars = ""
        if self.uppercase:
            chars += string.ascii_uppercase
        if self.lowercase:
            chars += string.ascii_lowercase
        if self.special:
            chars += string.punctuation
        if self.numbers:
            chars += string.digits
            
        return ''.join(random.choice(chars) for _ in range(self.length))

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Create menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)
        
        # Add About menu item directly to menu bar
        self.menu_bar.add_command(label="About", command=self.show_about)
        
        self.logic = PasswordGeneratorLogic()
        
        # Style configuration
        style = ttk.Style()
        style.configure("TCheckbutton", background="#f0f0f0")
        style.configure("TButton", padding=5)
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="Password Generator",
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        # Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(
            options_frame,
            text="Uppercase Letters (A-Z)",
            variable=self.uppercase_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Lowercase Letters (a-z)",
            variable=self.lowercase_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Special Characters (!@#$%^&*)",
            variable=self.special_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Numbers (0-9)",
            variable=self.numbers_var
        ).pack(anchor=tk.W, pady=2)
        
        # Length frame
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(
            length_frame,
            text="Password Length:"
        ).pack(side=tk.LEFT)
        
        self.length_var = tk.StringVar(value="12")
        length_entry = ttk.Entry(
            length_frame,
            textvariable=self.length_var,
            width=5
        )
        length_entry.pack(side=tk.LEFT, padx=5)
        
        # Generate button
        generate_button = ttk.Button(
            main_frame,
            text="Generate Password",
            command=self.generate_password
        )
        generate_button.pack(pady=10)
        
        # Password display frame
        password_frame = ttk.LabelFrame(main_frame, text="Generated Password", padding="10")
        password_frame.pack(fill=tk.X, pady=10)
        
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=("Courier", 12),
            state="readonly"
        )
        password_entry.pack(fill=tk.X)
        
        # Copy button
        copy_button = ttk.Button(
            main_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        copy_button.pack(pady=10)
        
    def generate_password(self):
        try:
            self.logic.length = int(self.length_var.get())
            self.logic.uppercase = self.uppercase_var.get()
            self.logic.lowercase = self.lowercase_var.get()
            self.logic.special = self.special_var.get()
            self.logic.numbers = self.numbers_var.get()
            
            password = self.logic.generate_password()
            
            if password is None:
                if self.logic.length < 4:
                    messagebox.showerror("Error", "Password must be at least 4 characters long!")
                else:
                    messagebox.showerror("Error", "Please select at least one option!")
                return
                
            self.password_var.set(password)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the length!")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "Generate a password first!")

    def show_about(self):
        about_text = """Password Generator
Version 1.0

A secure and user-friendly password generator application.

Author: Fernando Valente
fernandovalente.com.br
Source: https://github.com/fernandovalente/pypassword"""
        
        messagebox.showinfo("About", about_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
