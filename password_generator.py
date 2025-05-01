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
        self.root.title("Gerador de Senhas")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        self.logic = PasswordGeneratorLogic()
        
        # Configuração do estilo
        style = ttk.Style()
        style.configure("TCheckbutton", background="#f0f0f0")
        style.configure("TButton", padding=5)
        
        # Frame principal
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        title_label = ttk.Label(
            main_frame,
            text="Gerador de Senhas",
            font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)
        
        # Frame para opções
        options_frame = ttk.LabelFrame(main_frame, text="Opções", padding="10")
        options_frame.pack(fill=tk.X, pady=10)
        
        # Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(
            options_frame,
            text="Letras Maiúsculas (A-Z)",
            variable=self.uppercase_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Letras Minúsculas (a-z)",
            variable=self.lowercase_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Caracteres Especiais (!@#$%^&*)",
            variable=self.special_var
        ).pack(anchor=tk.W, pady=2)
        
        ttk.Checkbutton(
            options_frame,
            text="Números (0-9)",
            variable=self.numbers_var
        ).pack(anchor=tk.W, pady=2)
        
        # Frame para comprimento
        length_frame = ttk.Frame(main_frame)
        length_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(
            length_frame,
            text="Comprimento da senha:"
        ).pack(side=tk.LEFT)
        
        self.length_var = tk.StringVar(value="12")
        length_entry = ttk.Entry(
            length_frame,
            textvariable=self.length_var,
            width=5
        )
        length_entry.pack(side=tk.LEFT, padx=5)
        
        # Botão gerar
        generate_button = ttk.Button(
            main_frame,
            text="Gerar Senha",
            command=self.generate_password
        )
        generate_button.pack(pady=10)
        
        # Frame para exibir senha
        password_frame = ttk.LabelFrame(main_frame, text="Senha Gerada", padding="10")
        password_frame.pack(fill=tk.X, pady=10)
        
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=("Courier", 12),
            state="readonly"
        )
        password_entry.pack(fill=tk.X)
        
        # Botão copiar
        copy_button = ttk.Button(
            main_frame,
            text="Copiar para Área de Transferência",
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
                    messagebox.showerror("Erro", "A senha deve ter pelo menos 4 caracteres!")
                else:
                    messagebox.showerror("Erro", "Selecione pelo menos uma opção!")
                return
                
            self.password_var.set(password)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido para o comprimento!")
    
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Gere uma senha primeiro!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
