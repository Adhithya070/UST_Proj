import tkinter as tk
import os.path
import csv
from tkinter import ttk
from tkinter import messagebox

def verf(event) :
    reverse.config(text='')
    if not event.char.isalnum():
        entry.delete(0, tk.END)
        entry.insert(0, entry.get()[::-1])

def pal() :
    given = entry.get()
    if len(given.strip())>0:
        result=given[::-1]
        reverse.config(text=result)
        data(priv.get())
    else:
        messagebox.showwarning('Empty','Given String is Empty')

def clear():
    entry.delete(0,tk.END)
    reverse.config(text='')

def data(user_type):
    if user_type==1:
        rev=entry.get()[::-1]
        if (entry.get()==rev):
            with open(txtf,'a',newline='') as fp:
                fp.write(entry.get()+'\n')
        else:
            with open(csvf,'a',newline='') as fp:
                writer=csv.writer(fp)
                writer.writerow([entry.get(),rev])
    elif (user_type==0):
        given = entry.get()
        if len(given.strip()) > 0:
            result = given[::-1]
            reverse.config(text=result)
            if (given.lower() == result.lower()):
                messagebox.showinfo('Palindrome', 'Is Palindrome')
            else:
                messagebox.showinfo('Not Palindrome', 'Is Not Palindrome')
        else:
            messagebox.showwarning('Empty', 'Inpur is Mandatory')

#<root>main window obj
root=tk.Tk()
root.geometry("600x400")
root.title("PALINDROME V2")
root.resizable(False,False)
root.config(bg='grey')

txtf='PalindromeText.txt'
csvf='ReversedTable.csv'

if not os.path.exists(txtf):
    with open(txtf,'w',newline='') as fp:
        fp.write('Palindrome List\n============\n')

if not os.path.exists(csvf):
    with open(csvf,'w',newline='') as fp:
        writer=csv.writer(fp)
        writer.writerow(['Given','Reversed'])

priv=tk.IntVar()
head=ttk.Label(root,text="Palindrome Check!",font=('Helvetica',20,'bold'))
head.grid(column=0,row=0,sticky=tk.W,padx=20,pady=20,columnspan=3)
head.config(foreground='white',background='black')

admin=ttk.Radiobutton(root,text="Administrator",variable=priv,value=1,command=clear,style="Black.TRadiobutton")
admin.grid(column=0,row=1,sticky=tk.W,padx=20,pady=50,columnspan=3)

user=ttk.Radiobutton(root,text="User",variable=priv,value=0,command=clear,style="Black.TRadiobutton")
user.grid(column=1,row=1,sticky=tk.W,padx=50,pady=50,columnspan=3)

given=ttk.Label(root,text="Given String",font=('Helvetica',10,'bold'))
given.grid(column=0,row=2,sticky=tk.W,padx=20,pady=20)
given.config(foreground='white',background='black')

entry=ttk.Entry(root)
entry.grid(column=1,row=2,sticky=tk.W,padx=20,pady=20)
entry.bind('<KeyRelease>',verf)
entry.config(background='black')

button = ttk.Button(root, text='Reverse',command=pal)
button.grid(column=2,row=2,sticky=tk.W,padx=20,pady=20)

result=ttk.Label(root,text='Reversed String')
result.grid(column=0,row=3,sticky=tk.W,padx=20,pady=20)
result.config(foreground='white',background='black',font=('Helvetica',10,'bold'))

reverse=ttk.Label(root,text='',font=('Helvetica',10,'bold'))
reverse.grid(column=1,row=3,sticky=tk.W,padx=20,pady=20,columnspan=3)

root.mainloop()