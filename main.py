import tkinter as tk
from tkinter import*
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Aceitas?")
root.geometry("600x600")
root.configure(background = "#ffc8gg")

def mov_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randit(0, root.winfo_width() - button_1.winfo_width())
        y = random.randit(0, root.winfo_width() - button_1.winfo_width())
        

def accepted():
    messagebox.showinfo(
        "Meu amor", "Eu te amo meu amor", "lanchinho mais tarde?")
    
def denied():
    button_1.destroy()
    
margin = Canvas(root, width = 500, bg = "#ffc8dd", heigth = 100,
                bd = 0, highlightthickness = 0, relief = "ridge")

margin.pack()
text_id = Label(root, bg = "#ffc8dd", text = "Quer namorar comigo?", fg = "#590d22",
                font = ("Montserrat", 8, "bold"))

text_id.pack()
button_1 = tk.Button(root, text = "Não", bg = "#ffb3c1", command = denied,
                     relief = RIDGE, bd = 3, font = ("Montserrat", 8, "bold"))

button_1.pack()
root.bind('<Motion>', mov_button_1)
button_2 = tk.Button(root, text = "Sim", bg = "#ffb3c1", relief = RIDGE,
                     bd = 3, command = accepted, font = ("Montserrat", 14, "bold"))

button_2.pack()

root.mainloop()