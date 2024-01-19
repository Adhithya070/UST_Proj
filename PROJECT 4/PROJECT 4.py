import tkinter as tk

def add(): result.config(text=int(entry1.get())+int(entry2.get()))

def subt(): result.config(text=int(entry1.get())-int(entry2.get()))

def mull(): result.config(text=int(entry1.get())*int(entry2.get()))

def divs(): result.config(text=int(entry1.get())/int(entry2.get()))

def modl(): result.config(text=int(entry1.get())%int(entry2.get()))

my_font=('Times New Roman', 10, 'bold')

#<root>main window obj
root=tk.Tk()
root.geometry("700x700")#size window
root.title("Calculator")#window title
root.resizable(0,0)#no maximize button

my_font=('Times New Roman', 10, 'bold')

heading=tk.Label(root,text="CALCULATOR",font=('Times New Roman', 20, 'bold'),foreground='white',background='black')
heading.grid(column=0,row=0,sticky=tk.W,padx=20,pady=20,columnspan=3)

num1=tk.Label(root,text="1ST DIGIT : ",background='black',foreground='white',font=my_font)
num1.grid(column=0,row=2,sticky=tk.W,padx=20,pady=20)

entry1=tk.Entry(root,background='black',foreground='white',font=my_font)
entry1.grid(column=1,row=2,sticky=tk.W,padx=20,pady=20)

num2=tk.Label(root,text="2ND DIGIT : ",background='black',foreground='white',font=my_font)
num2.grid(column=2,row=2,sticky=tk.W,padx=20,pady=20)

entry2=tk.Entry(root,background='black',foreground='white',font=my_font)
entry2.grid(column=3,row=2,sticky=tk.W,padx=20,pady=20)

sum=tk.Button(root,text="Addition",font=my_font,background='black',foreground='white',command=add)
sum.grid(column=0,row=3,sticky=tk.W,padx=20,pady=50,)

sub=tk.Button(root,text="Subtraction",font=my_font,background='black',foreground='white',command=subt)
sub.grid(column=1,row=3,sticky=tk.W,padx=20,pady=50,)

mul=tk.Button(root,text="Multiplication",font=my_font,background='black',foreground='white',command=mull)
mul.grid(column=2,row=3,sticky=tk.W,padx=0,pady=50,)

div=tk.Button(root,text="Division",font=my_font,background='black',foreground='white',command=divs)
div.grid(column=3,row=3,sticky=tk.W,padx=20,pady=50,)

mod=tk.Button(root,text="Modulus",font=my_font,background='black',foreground='white',command=modl)
mod.grid(column=4,row=3,sticky=tk.W,padx=0,pady=50,)

label=tk.Label(root,text='RESULT',background='black',foreground='white',font=my_font)
label.grid(column=0,row=5,sticky=tk.W,padx=20,pady=20)

result=tk.Label(root,text='',background='black',foreground='white',font=my_font)
result.grid(column=1,row=5,sticky=tk.W,padx=20,pady=20,columnspan=3)

root.config(bg='black')
root.mainloop()#without this will close