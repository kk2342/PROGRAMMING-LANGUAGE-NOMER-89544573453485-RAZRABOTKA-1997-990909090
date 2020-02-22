import tkinter
from tkinter import *
from tkinter import messagebox

class InputWindow:
    def __init__(self):
        self.info = ""
        self.title = ""
        self.text = ""
        self.fontsize = 18
    def setting(self,title = "",text = "",fontsize = 18):
        self.text = text
        self.title = title
        self.fontsize = fontsize
    def set_info(self,string):
        self.info = string

    def close(self,string,window):
        window.destroy()
        self.info = string
    def open(self):
        win = Tk();
        win.resizable(width = False, height = False)
        win.geometry("300x150")
        win.title(self.title)
        win.protocol("WM_DELETE_WINDOW",lambda:self.close(enter.get(),win))
        
        lbl = Label(win, text = self.text,font = ("Arial Bold", self.fontsize))
        lbl.pack(side = TOP)
        enter = Entry(win,width = 30)
        enter.place(x=60,y=50)
        enter.focus()



        win.mainloop()
    def get_info(self):
        return self.info;


def inputbox(titles = "Some inputBox", texts = "Some text.", fontsizes = 18):
    j = InputWindow()
    j.setting(title = titles,text = texts, fontsize=fontsizes)
    j.open()
    return j.get_info()


def ask(titles = "Some asking.", texts = "Some text."):
    Tk().withdraw()
    bool = messagebox.askyesno(title = titles,message = texts)
    return bool

def info(titles = "", texts = ""):
    Tk().withdraw()
    messagebox.showinfo(title = titles,message= texts)

def error(titles = "", texts = ""):
    Tk().withdraw()
    messagebox.showerror(title = titles,message= texts)
    

def warning(titles = "", texts = ""):
    Tk().withdraw()
    messagebox.showwarning(title = titles,message= texts)
    

def okcancel(titles = "Some asking.", texts = "Some text."):
    Tk().withdraw()
    bool = messagebox.askokcancel(title = titles,message = texts)
    return bool