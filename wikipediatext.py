import tkinter as tk
import wikipedia

# Function to search Wikipedia
def search_wiki():
    topic = entry.get()
    try:
        result = wikipedia.summary(topic, sentences=5)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, result)
    except:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Topic not found. Please try another keyword.")

# Create main window
window = tk.Tk()
window.title("Wikipedia Search")
window.geometry("600x400")

# Label
label = tk.Label(window, text="Enter Keyword:", font=("Arial", 12))
label.pack(pady=5)

# Textbox (Entry)
entry = tk.Entry(window, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Search Button
button = tk.Button(window, text="Search", font=("Arial", 12), command=search_wiki)
button.pack(pady=10)

# Text area to display result
text_area = tk.Text(window, wrap=tk.WORD, font=("Arial", 11))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Run the application
window.mainloop()
