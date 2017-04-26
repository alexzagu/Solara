import os
import subprocess
import tkFileDialog
from tkinter import *


# Erases the text in the text box area
def erase():
    entry.delete("1.0", END)

# Erases the text in the text box area
def exit_ide():
    root.destroy()


# Saves the text in the text area in a txt file
def save_text():
    text = entry.get("1.0", END)
    with open('testing/code_to_compile_and_execute.txt', 'w') as f:
        f.write(text)


# Checks if the file trying to execute is not empty
def check_file():
    with open('testing/code_to_compile_and_execute.txt', 'r') as f:
        text = f.read()
        if text.strip() == "":
            return False
        else:
            return True


# executes the parser
def execute():
    save_text()
    if check_file():
        subprocess.Popen('python parser/parser.py')
    else:
        message_box("ERROR: cant execute blank file")

    # os.system("python parser/parser.py")


# Opens a txt file in the text box
def upload():
    try:
        root.filename = tkFileDialog.askopenfilename(filetypes=(("howCode files", "*.txt"), ("All files", "*.*")))
        with open(str(root.filename), 'r') as f:
            text = f.read()
            if text != "":
                entry.insert("1.0", text)
                entry.configure(fg="#f5f97a")
            else:
                message_box("ERROR: cant open an blank file")
    except:
        pass


# Opens a error message box
def message_box(message_str):
    message = Tk()
    message.geometry('%dx%d+%d+%d' % (250, 90, screen_width / 2 - 125, screen_height / 2 - 80))
    message_frame = Frame(message)
    message_frame.pack(fill='both', expand='yes')
    message_label = Label(message_frame, text=message_str)
    message_label.pack(pady=40)


# creates the ide box using
# root as main screen
# top_frame is the frame where the buttons are
# bottom_frame is where the entry (text area) is
# entry is the text area
root = Tk()
top_frame = Frame(root, bg="#444444")
middle_frame = Frame(root, height=7, relief=RAISED, bg="#444444")
bottom_frame = Frame(root, relief=RIDGE)
entry = Text(root, bg="#363835", fg="#f5f97a")

# fixed screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screen_width / 2 - 20, screen_height - 80, 0, 0))

# packs the frames
top_frame.pack(fill="both")
middle_frame.pack(fill="both")
bottom_frame.pack(side=BOTTOM)
entry.configure(width=screen_width / 2, height=screen_height)
entry.pack()

# creates the buttons and packs them
button_borrar = Button(top_frame, text="Limpiar pantalla", command=erase, relief=GROOVE,
                       bg="#363835", fg="#ffffff")
button_cargar = Button(top_frame, text="Cargar programa", command=upload, relief=GROOVE,
                       bg="#363835", fg="#ffffff")
button_guardar = Button(top_frame, text="Guardar programa", command=save_text, relief=GROOVE,
                        bg="#363835", fg="#ffffff")
button_ejecutar = Button(top_frame, text="Ejecutar programa", command=execute, relief=GROOVE,
                         bg="#363835", fg="#ffffff")
button_salir = Button(top_frame, text="Salir", command=exit_ide, relief=GROOVE,
                         bg="#363835", fg="#ffffff")
button_borrar.pack()
button_cargar.pack()
button_guardar.pack()
button_ejecutar.pack()
button_salir.pack()

# main loop
root.mainloop()
