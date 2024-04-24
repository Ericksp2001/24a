import os
import tkinter as tk
from tkinter import messagebox, ttk
from time import time

def boyer_moore(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Preprocessing the pattern
    jump_table = [-1] * 256
    for i in range(m):
        jump_table[ord(pattern[i])] = i

    # Boyer-Moore search
    count = 0
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            count += 1
            i += 1
        else:
            text_index = i + j
            if text_index < len(text) and 0 <= ord(text[text_index]) < len(jump_table):
                jump = max(1, j - jump_table[ord(text[text_index])])
            else:
                jump = 1
            i += jump

    return count

def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []

    # Calculate prefix for the pattern
    prefix = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix[i] = j

    # KMP search
    j = 0
    positions = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            positions.append(i - m + 1)
            j = prefix[j - 1]

    return positions

def search_word():
    method = combo_method.get()
    if method == "Boyer-Moore":
        search_with_method(boyer_moore)
    elif method == "KMP":
        search_with_method(kmp)

def search_with_method(search_method):
    directory = r"C:\Users\erick\OneDrive\Escritorio\RI\24a\task1\lib"  # Fixed directory path
    word = entry_word.get()
    if not word:
        messagebox.showwarning("Warning", "Enter a word to search.")
        return

    start_time = time()
    total_count = 0
    txt_files = [file for file in os.listdir(directory) if file.endswith(".txt")]

    for file in txt_files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            occurrences = search_method(content, word)
            word_count = len(occurrences) if isinstance(occurrences, list) else occurrences
            total_count += word_count

    end_time = time()
    total_time = end_time - start_time

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"The word '{word}' appears {total_count} times in the files in the directory.\n")
    result_text.insert(tk.END, f"Search time: {total_time:.4f} seconds")
    result_text.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Word Searcher")
window.geometry("400x250")

# Label and entry for the word to search
tk.Label(window, text="Word to search:").pack()
entry_word = tk.Entry(window)
entry_word.pack()

# ComboBox to select the search method
combo_method = ttk.Combobox(window, values=["Boyer-Moore", "KMP"])
combo_method.current(0)
combo_method.pack()

# Button to start the search
tk.Button(window, text="Search", command=search_word).pack()

# Search result display
result_text = tk.Text(window, height=7, width=40)
result_text.pack()
result_text.config(state=tk.DISABLED)

# Run the interface
window.mainloop()
