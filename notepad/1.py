from tkinter import *
from tkinter import filedialog
root=Tk()
root.title("Notepad")
root.geometry("500x600")

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear():
    entry.delete(1.0,END)

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
        print(content)
    entry.insert(INSERT,content)

b1=Button(root,text="Save",command=save_file)
b1.place(x=10,y=10)

b2=Button(root,text="Clear",command=clear)
b2.place(x=60,y=10)

b3=Button(root,text="Open",command=open_file)
b3.place(x=110,y=10)



entry=Text(root,height=33,width=59,wrap=WORD)
entry.place(x=10,y=50)
root.mainloop()
