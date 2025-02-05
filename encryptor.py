import tkinter as tk
from tkinter import filedialog, messagebox
import os

def collatz_encrypt(data, key):
    encrypted_data = []
    for char in data:
        encrypted_char = ord(char) ^ key
        encrypted_data.append(encrypted_char)
        key = (key * 3 + 1) if key % 2 else (key // 2)
    return bytes(encrypted_data), key

def collatz_decrypt(encrypted_data, key):
    decrypted_data = []
    for byte in encrypted_data:
        decrypted_char = byte ^ key
        decrypted_data.append(chr(decrypted_char))
        key = (key * 3 + 1) if key % 2 else (key // 2)
    return ''.join(decrypted_data)

def encrypt_file():
    file_path = filedialog.askopenfilename(
        title="Choose Python File:", 
        filetypes=[("Python files", "*.py")]
    )
    if not file_path:
        return
    
    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be an Integer")
        return
    key = int(key)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        
        encrypted_data, _ = collatz_encrypt(data, key)
        
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_dir = os.path.dirname(file_path)
        
        encrypted_file = os.path.join(output_dir, f"{base_name}_encrypted.bin")
        with open(encrypted_file, 'wb') as f:
            f.write(encrypted_data)
        
        key_file = os.path.join(output_dir, f"{base_name}_key.txt")
        with open(key_file, 'w') as f:
            f.write(str(key))
        
        messagebox.showinfo(
            "Success", 
            f"Encrypted as:\n{encrypted_file}\n"
            f"Key saved in:\n{key_file}"
        )
    
    except Exception as e:
        messagebox.showerror("Error", f"Encryption Failed: {str(e)}")

def decrypt_file():
    encrypted_file = filedialog.askopenfilename(
        title="Choose encrypted file",
        filetypes=[("Encrypted files", "*.bin")]
    )
    if not encrypted_file:
        return
    
    key_file = filedialog.askopenfilename(
        title="Choose Key File",
        filetypes=[("Key files", "*.txt")]
    )
    if not key_file:
        return
    
    try:
        with open(key_file, 'r') as f:
            key = int(f.read().strip())
        
        with open(encrypted_file, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = collatz_decrypt(encrypted_data, key)
        
        base_name = os.path.splitext(os.path.basename(encrypted_file))[0].replace("_encrypted", "")
        output_file = os.path.join(os.path.dirname(encrypted_file), f"{base_name}_decrypted.py")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(decrypted_data)
        
        messagebox.showinfo("Success", f"Decrypted as:\n{output_file}")
    
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {str(e)}")

root = tk.Tk()
root.title("Collatz Encryptor Free")
root.geometry("450x250")

root.configure(bg="#2e2e2e")
button_style = {
    "bg": "#4CAF50", 
    "fg": "white", 
    "activebackground": "#45a049",
    "font": ("Arial", 12)
}
label_style = {"bg": "#2e2e2e", "fg": "white", "font": ("Arial", 11)}

tk.Label(root, text="Decryption Key:", **label_style).pack(pady=10)
key_entry = tk.Entry(root, font=("Arial", 12))
key_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack(pady=20)

tk.Button(
    button_frame, 
    text="📄 Encrypt File", 
    command=encrypt_file,
    **button_style
).pack(side=tk.LEFT, padx=10)

tk.Button(
    button_frame, 
    text="🔓 Decrypt File", 
    command=decrypt_file,
    **button_style
).pack(side=tk.LEFT, padx=10)

root.mainloop()
