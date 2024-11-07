import tkinter as tk
from tkinter import messagebox
import random

from Rajz.rajzok_mentese import mentes
from VV_rajzok_tarolasa import VV_rajz_valasztas, allatok_lista, viragok_lista


def display_drawing(drawing):
    drawing_text.config(state=tk.NORMAL)
    drawing_text.delete(1.0, tk.END)
    drawing_text.insert(tk.END, drawing)
    drawing_text.config(state=tk.DISABLED)


def save_drawing():
    drawing = drawing_text.get(1.0, tk.END).strip()
    if drawing:
        mentes(drawing)
        messagebox.showinfo("Sikeres mentés", "A rajz mentve lett.")
    else:
        messagebox.showwarning("Figyelmeztetés", "Nincs menthető rajz.")


def choose_drawing():
    choice_type = type_var.get()
    choice = drawing_var.get()

    if choice_type == "állatokat":
        if choice == "véletlen":
            choice = random.choice(allatok_lista)
    elif choice_type == "virágokat":
        if choice == "véletlen":
            choice = random.choice(viragok_lista)
    else:
        messagebox.showwarning("Figyelmeztetés", "Érvénytelen választás.")
        return

    drawing = VV_rajz_valasztas(choice_type, choice)
    display_drawing(drawing)


# Alapértelmezett Tkinter ablak
root = tk.Tk()
root.title("App")

# Fix szélességű betűtípus
drawing_text = tk.Text(root, font=("Courier", 10), wrap=tk.NONE)
drawing_text.config(state=tk.DISABLED)
drawing_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Kategória kiválasztása
type_var = tk.StringVar(value="állatokat")
drawing_var = tk.StringVar(value="kutya")

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="Válassz kategóriát:").grid(row=0, column=0)
tk.Radiobutton(frame, text="Állatok", variable=type_var, value="állatokat").grid(row=0, column=1)
tk.Radiobutton(frame, text="Virágok", variable=type_var, value="virágokat").grid(row=0, column=2)

tk.Label(frame, text="Rajz típus:").grid(row=1, column=0)
choices = ["kutya", "cica", "elefánt", "rózsa", "pitypang", "napraforgó", "véletlen"]
choices_menu = tk.OptionMenu(frame, drawing_var, *choices)
choices_menu.grid(row=1, column=1, columnspan=2)

# Kiválasztás és mentés gombok
choose_button = tk.Button(root, text="Rajz kiválasztása", command=choose_drawing)
choose_button.pack(pady=5)

save_button = tk.Button(root, text="Rajz mentése", command=save_drawing)
save_button.pack(pady=5)

root.mainloop()