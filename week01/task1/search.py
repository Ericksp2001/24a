import os
import tkinter as tk
from tkinter import messagebox, ttk

def search_word(word):
    directory = r"C:\Users\erick\OneDrive\Escritorio\RI\24a\data"  # Ruta fija del directorio
    matching_files = []
    txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]

    for txt_file in txt_files:
        file_path = os.path.join(directory, txt_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if word.lower() in content.lower():  # Realiza una búsqueda de la palabra en minúsculas
                matching_files.append(txt_file)

    return matching_files

def search_word_in_files():
    word = entry_word.get()
    if not word:
        messagebox.showwarning("Advertencia", "Ingrese una palabra para buscar.")
        return

    matching_files = search_word(word)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    if matching_files:
        result_text.insert(tk.END, f"La palabra '{word}' se encuentra en los siguientes archivos:\n")
        for file_name in matching_files:
            result_text.insert(tk.END, f"- {file_name}\n")
    else:
        result_text.insert(tk.END, f"La palabra '{word}' no se encuentra en ningún archivo en el directorio.\n")
    result_text.config(state=tk.DISABLED)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Buscador de Palabras")
ventana.geometry("400x250")

# Etiqueta y entrada para la palabra a buscar
tk.Label(ventana, text="Palabra a buscar:").pack()
entry_word = tk.Entry(ventana)
entry_word.pack()

# Botón para iniciar la búsqueda
tk.Button(ventana, text="Buscar", command=search_word_in_files).pack()

# Resultado de la búsqueda
result_text = tk.Text(ventana, height=7, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

# Ejecutar la interfaz
ventana.mainloop()
