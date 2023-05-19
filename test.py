import tkinter as tk
from tkinter import ttk

def on_scale_change(value):
    print("滑块的当前值为:", int(float(value)))

root = tk.Tk()

scale = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=on_scale_change)
scale.pack()

root.mainloop()
