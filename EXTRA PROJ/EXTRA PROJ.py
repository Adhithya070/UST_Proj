import tkinter as tk
from tkinter import ttk
import pymongo as mo
global mycl
global dblist
from tkinter import messagebox

mycl=mo.MongoClient("mongodb://localhost:27017/")
dblist=mycl.list_database_names()

def getdet():
    d = mycl['MBCETDATABASE']['EMPLOYEE']
    x = d.find({}, {'_id': 0, 'EmpID': 1})
    j = []
    a=int(i.get())
    for z in x: j.append(z['EmpID'])
    if a in j:
        q = {'EmpID': a}
        c = d.find(q, {'_id': 0, 'EmpID':0})
        for m in c: k=m
        nam.config(text=k['EmpName'])
        dep.config(text=k['Dept'])
        ema.config(text=k['Email'])
    else:
        messagebox.showwarning('not found', "EmpID not found!")

root = tk.Tk()
root.geometry("1000x500")
root.title("empdetails.exe")
root.resizable(False, False)
root.config(bg='black')

my_font = ('Times New Roman', 20, 'bold')

head=tk.Label(root, text="Employee Details", font=('Times New Roman', 25, 'bold','underline'), foreground='white', background='black')
head.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20, columnspan=2)

id = ttk.Label(root, text="Enter EmpID", font=my_font, foreground='white', background='black')
id.grid(column=0, row=1, sticky=tk.W, padx=20, pady=20)

i = tk.Entry(root, background='black', foreground='white', font=my_font)
i.grid(column=1, row=1, sticky=tk.W, padx=20, pady=20,)

b1 = tk.Button(root, text='Get Details', width=20, bg='black', font=my_font, fg='white',command=getdet)
b1.grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)

name = ttk.Label(root, text="NAME", font=my_font, foreground='white', background='black')
name.grid(column=0, row=3, sticky=tk.W, padx=20, pady=20)

nam= ttk.Label(root, text="", font=my_font, foreground='white', background='black')
nam.grid(column=1, row=3, sticky=tk.W, padx=20, pady=20)

dept = ttk.Label(root, text="DEPARTMENT", font=my_font, foreground='white', background='black')
dept.grid(column=0, row=4, sticky=tk.W, padx=20, pady=20)

dep = ttk.Label(root, text="", font=my_font, foreground='white', background='black')
dep.grid(column=1, row=4, sticky=tk.W, padx=20, pady=20)

email = ttk.Label(root, text="EMAIL", font=my_font, foreground='white', background='black')
email.grid(column=0, row=5, sticky=tk.W, padx=20, pady=20)

ema = ttk.Label(root, text="", font=my_font, foreground='white', background='black')
ema.grid(column=1, row=5, sticky=tk.W, padx=20, pady=20)

root.mainloop()