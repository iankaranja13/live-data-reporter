import tkinter as tk
from tkinter import scrolledtext
from astronauts import get_astronauts
from iss_tracker import get_iss_position
from news_or_stock import get_news  # or replace with get_stock_price if using stock
import sys

# --- GUI logic ---
def display_output(func):
    output_text.delete("1.0", tk.END)
    try:
        result = func()
        if result:
            output_text.insert(tk.END, result)
    except Exception as e:
        output_text.insert(tk.END, f"Error: {str(e)}")

# --- Setup window ---
root = tk.Tk()
root.title("🛰️ Live Data Reporter")
root.geometry("700x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# --- Title label ---
title = tk.Label(root, text="Live Data Reporter", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#2c3e50")
title.pack(pady=10)

# --- Output area ---
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, font=("Courier", 10))
output_text.pack(padx=10, pady=10)

# --- Buttons ---
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

tk.Button(button_frame, text="👨‍🚀 Astronauts", width=20, command=lambda: display_output(get_astronauts)).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="🛰️ ISS Position", width=20, command=lambda: display_output(get_iss_position)).grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="📰 News", width=20, command=lambda: display_output(get_news)).grid(row=0, column=2, padx=10, pady=5)
tk.Button(button_frame, text="❌ Exit", width=20, command=sys.exit).grid(row=0, column=3, padx=10, pady=5)

# --- Run the app ---
root.mainloop()
