from tkinter import *

root = Tk()


def translate():
    text = var1.get()
    retarded_text = ""
    for k, i in enumerate(text.lower()):
        if k % 2 == 1:
            retarded_text += i.upper()
        else:
            retarded_text += i
    var2.set(retarded_text)



root.geometry("500x180+700+300")
root.title("Retard text Translator")
Label(root, text="Text: ", font=("Arial", 14)).place(x=10, y=20)

var1 = StringVar()
e1 = Entry(root, textvariable = var1, font=("Arial", 14)).place(x=120, y=20, width=370)
Label(root, text="Translation: ", font=("Arial", 14)).place(x=10, y=70)

var2 = StringVar()
e2 = Entry(root,  textvariable = var2, font=("Arial", 14)).place(x=120, y=70, width=370)
Button(root, text="Translate", command=translate, font=("Arial", 14)).place(x=10, y=120, width = 480)

root.mainloop()
