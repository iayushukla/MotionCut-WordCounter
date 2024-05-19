import tkinter as tk
from tkinter import scrolledtext

class WordCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor with Word Count")
        
        # Create a scrolled text widget
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack(padx=10, pady=10)
        
        # Create a label for word count
        self.word_count_label = tk.Label(root, text="Word Count: 0")
        self.word_count_label.pack(pady=5)
        
        # Bind the <KeyRelease> event to the update_word_count method
        self.text_area.bind('<KeyRelease>', self.update_word_count)
        
    def update_word_count(self, event=None):
        # Get the content of the text area
        text_content = self.text_area.get("1.0", tk.END)
        
        # Count the number of words
        words = text_content.split()
        word_count = len(words)
        
        # Update the word count label
        self.word_count_label.config(text=f"Word Count: {word_count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCounterApp(root)
    root.mainloop()
