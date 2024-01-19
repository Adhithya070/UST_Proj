import tkinter as tk
from tkinter.ttk import Frame,Button
from tkinter import (PhotoImage,Toplevel)


class UST(Frame):
    def __init__(self,master):
        super().__init__(master,relief='flat',borderwidth=40)
        self.master.title("UST TO MBCET")
        self.pack(fill=None,expand=False)
        self.photo=PhotoImage(file="UST.png")
        btn=(Button(self,text="test",image=self.photo,command=self.to_MBCET))
        btn.pack()

    def to_MBCET(self):
        MBCET(self.master,self).show()


class MBCET(Frame):

    def __init__(self, parent, main_page):
        super().__init__(parent)
        self.top = Toplevel(parent, relief="flat", borderwidth=20)
        self.main_page = main_page
        self.pack(fill=None, expand=False)
        self.photo = PhotoImage(file="MBCET.png")
        button = (Button(self.top, image=self.photo, command=self.to_UST))
        button.grid()

    def to_UST(self):
        self.top.destroy()
        self.destroy()
def main():
    root=tk.Tk()
    root.geometry("400x400")
    root.title("MAIN")
    root.resizable(False, False)
    UST(root)
    root.mainloop()

main()
