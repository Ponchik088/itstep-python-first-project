import tkinter as tk

window = tk.Tk()
window.geometry("500x700")
window.resizable(False, False)
window.title("MegaClicker")

monster1 = tk.PhotoImage(file =r".\img\Monster1.png")

greeting = tk.Label(text="Hello, Tkinter", fg="#ff0000")
greeting.pack()

monster = tk.Button(image = monster1)
monster.pack()

window.mainloop()