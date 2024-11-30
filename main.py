import tkinter as tk
monster1 = tk.PhotoImage(file =r"C:\Gfg\circle.png")

window = tk.Tk()
window.geometry("500x700")
window.resizable(False, False)
window.title("MegaClicker")



greeting = tk.Label(text="Hello, Tkinter", fg="#ff0000")
greeting.pack()

monster = tk.Button(image = monster1)
monster.pack()

window.mainloop()