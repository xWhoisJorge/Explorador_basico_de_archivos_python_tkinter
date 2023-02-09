import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    print(file_path)

root = tk.Tk()
root.geometry("400x150")
root.config(bg="white")
root.title("Explorador de Archivos")
label = tk.Label(root, text="Explorador de archivos", font=("Arial", 16), bg="White")
label.pack(pady=10)

open_file_button = tk.Button(root, text="Abrir archivo", font=("Arial", 16), command=open_file)
open_file_button.pack(pady=10)

root.mainloop()