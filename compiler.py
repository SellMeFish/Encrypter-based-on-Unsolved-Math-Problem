import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os
import sys
import shutil
import ast

STUB_CODE = '''
import sys
import os
import tkinter as tk
from tkinter import messagebox  # Expliziter Import

def collatz_decrypt(encrypted_data, key):
    decrypted_data = []
    for byte in encrypted_data:
        decrypted_char = byte ^ key
        decrypted_data.append(chr(decrypted_char))
        key = (key * 3 + 1) if key % 2 else (key // 2)
    return ''.join(decrypted_data)

if getattr(sys, "frozen", False):
    base_dir = sys._MEIPASS
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

encrypted_code_path = os.path.join(base_dir, "data", "encrypted_code.bin")
key_file_path = os.path.join(base_dir, "data", "decryption_key.txt")

with open(encrypted_code_path, "rb") as f:
    encrypted_data = f.read()

with open(key_file_path, "r") as f:
    key = int(f.read())

decrypted_code = collatz_decrypt(encrypted_data, key)

if "messagebox" not in decrypted_code:
    decrypted_code = "from tkinter import messagebox\\n" + decrypted_code

exec(decrypted_code)
'''

def analyze_imports(code):
    imports = set()
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
    except Exception as e:
        raise RuntimeError(f"AST-Analyse fehlgeschlagen: {str(e)}")
    return list(imports)

def compile_exe():
    encrypted_code_file = filedialog.askopenfilename(
        title="Verschlüsselte Code-Datei auswählen",
        filetypes=[("Encrypted files", "*.bin")]
    )
    if not encrypted_code_file:
        return

    key_file = filedialog.askopenfilename(
        title="Decryption Key-Datei auswählen",
        filetypes=[("Key files", "*.txt")]
    )
    if not key_file:
        return

    try:
        with open(key_file, "r") as f:
            key = int(f.read().strip())
    except Exception as e:
        messagebox.showerror("Fehler", f"Ungültiger Schlüssel:\n{str(e)}")
        return

    try:
        with open(encrypted_code_file, "rb") as f:
            encrypted_data = f.read()
        
        decrypted_data = []
        current_key = key
        for byte in encrypted_data:
            decrypted_char = byte ^ current_key
            decrypted_data.append(chr(decrypted_char))
            current_key = (current_key * 3 + 1) if current_key % 2 else (current_key // 2)
        decrypted_code = "".join(decrypted_data)
    except Exception as e:
        messagebox.showerror("Fehler", f"Entschlüsselung fehlgeschlagen:\n{str(e)}")
        return

    required_modules = analyze_imports(decrypted_code) + [
        "tkinter",
        "tkinter.messagebox",
        "tkinter.ttk",
        "tkinter.font",
        "pkg_resources.py2_warn",
        "win32timezone"
    ]
    required_modules = list(set(required_modules))

    try:
        base_prefix = sys.base_prefix
        tcl_dir = os.path.join(base_prefix, "tcl", "tcl8.6")
        tk_dir = os.path.join(base_prefix, "tcl", "tk8.6")
        
        if not all([os.path.exists(tcl_dir), os.path.exists(tk_dir)]):
            messagebox.showerror(
                "Fehler", 
                "Tcl/Tk 8.6 nicht gefunden!\n"
                "Installieren Sie Python neu mit aktivierter Tcl/Tk-Option."
            )
            return
    except Exception as e:
        messagebox.showerror("Fehler", f"Tcl/Tk-Pfade:\n{str(e)}")
        return

    data_dir = "temp_pyinstaller_data"
    os.makedirs(data_dir, exist_ok=True)
    
    try:
        shutil.copy(encrypted_code_file, os.path.join(data_dir, "encrypted_code.bin"))
        shutil.copy(key_file, os.path.join(data_dir, "decryption_key.txt"))

        temp_stub = "temp_stub.py"
        with open(temp_stub, "w", encoding="utf-8") as f:
            f.write(STUB_CODE)

        hidden_imports = [f"--hidden-import={mod}" for mod in required_modules]
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--onefile",
            "--add-data", f"{data_dir}{os.pathsep}data",
            "--add-data", f"{tcl_dir}{os.pathsep}tcl",
            "--add-data", f"{tk_dir}{os.pathsep}tk",
            "--clean",
            "--name", "EncryptedApp",
            "--log-level=ERROR"
        ] + hidden_imports + [temp_stub]

        subprocess.run(cmd, check=True)
        messagebox.showinfo(
            "Erfolgreich", 
            "EXE erfolgreich erstellt!\n"
            f"Pfad: {os.path.abspath('dist/EncryptedApp.exe')}"
        )

    except subprocess.CalledProcessError as e:
        messagebox.showerror(
            "Kompilierungsfehler",
            f"Fehlercode {e.returncode}\n"
            "1. PyInstaller updaten: pip install --upgrade pyinstaller\n"
            "2. Als Administrator ausführen\n"
            "3. Tcl/Tk 8.6 prüfen"
        )
    finally:
        shutil.rmtree(data_dir, ignore_errors=True)
        for file in [temp_stub, "EncryptedApp.spec"]:
            if os.path.exists(file):
                os.remove(file)
        shutil.rmtree("build", ignore_errors=True)

root = tk.Tk()
root.title("Collatz EXE Compiler Ultimate by Cyberseall")
root.geometry("600x300")
root.configure(bg="#2d2d2d")

tk.Label(
    root,
    text="Collatz EXE Compiler",
    bg="#2d2d2d",
    fg="#4CAF50",
    font=("Arial", 20, "bold")
).pack(pady=20)

tk.Button(
    root,
    text="🚀 EXE kompilieren",
    command=compile_exe,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14),
    padx=30,
    pady=15
).pack()

root.mainloop()