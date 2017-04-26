import subprocess
import tkFileDialog

from tkinter import *


def erase():
    entry.delete("1.0", END)


def save_text():
    text = entry.get("1.0", END)
    with open('testing/TestSolutionCall.txt', 'w') as f:
        f.write(text)


def execute():
    save_text()
    subprocess.Popen('python parser/parser.py')


def upload():
    root.filename = tkFileDialog.askopenfilename(filetypes=(("howCode files", "*.txt"),("All files", "*.*")))
    with open(str(root.filename), 'r') as f:
        text = f.read()
        entry.insert("1.0", text)
        entry.configure(fg="#f5f97a")

root = Tk()
#root.configure(background='#f44242')
top_frame_root = Frame(root)
middle_frame = Frame(root, height=5, relief=RIDGE)
bottom_frame_root = Frame(root, relief=RIDGE)
entry = Text(root, bg="#363835", fg="#f5f97a")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screen_width / 2 - 20, screen_height - 80, 0, 0))

top_frame_root.pack()
middle_frame.pack()
bottom_frame_root.pack(side=BOTTOM)
entry.configure(width=screen_width / 2, height=screen_height)

button_borrar = Button(top_frame_root, text="Limpiar pantalla", command=erase, relief=RIDGE)
button_cargar = Button(top_frame_root, text="Cargar programa", command=upload)
button_guardar = Button(top_frame_root, text="Guardar programa", command=save_text)
button_ejecutar = Button(top_frame_root, text="Ejecutar programa", command=execute)
button_borrar.pack()
button_cargar.pack()
button_guardar.pack()
button_ejecutar.pack()
entry.pack()

root.mainloop()


