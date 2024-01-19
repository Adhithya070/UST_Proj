#button = tk.Button(root, text='CHECK', width=25, command=pal(entry))
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
def rev():
    given=entry.get()
    if len(given.strip())>0:
        result=given[::-1]
        reverse.config(text=result)
        if(given.lower()==result.lower()):
            messagebox.showinfo('Palindrome','Is Palindrome')
        else:
            messagebox.showinfo('Not Palindrome', 'Is Not Palindrome')
    else:
        messagebox.showwarning('Empty','Input is Mandatory')
#<root>main window obj
root=tk.Tk()
root.geometry("700x700")#size window
root.title("PALINDROME V1")#window title
root.resizable(1,1)#no maximize button
root.config(bg='grey')

heading=ttk.Label(root,text="Palindrome Check",font=('Helvetica',20,'bold'))
heading.grid(column=0,row=0,sticky=tk.W,padx=20,pady=20,columnspan=3)
heading.config(foreground='white',background='black')

given=ttk.Label(root,text="Given String : ",font=('Helvetica',10,'bold'))
given.grid(column=0,row=2,sticky=tk.W,padx=20,pady=20)
given.config(foreground='white',background='black')

entry=ttk.Entry(root)
entry.grid(column=1,row=2,sticky=tk.W,padx=20,pady=20)
entry.config(foreground='black')

button = ttk.Button(root, text='Reverse',command=rev)
button.grid(column=2,row=2,sticky=tk.W,padx=20,pady=20)

result=ttk.Label(root,text='Reversed String')
result.grid(column=0,row=3,sticky=tk.W,padx=20,pady=20)

reverse=ttk.Label(root,text='',font=('Helvetica',10,'bold'))
reverse.grid(column=1,row=3,sticky=tk.W,padx=20,pady=20,columnspan=3)

root.mainloop()#without this will close
