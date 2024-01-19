import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def actionbut():
    l2_val = largestTwo.get()
    l3_val = largestThree.get()

    if (not l3_val) and (not l2_val):
        b1.config(state='disabled')
        b2.config(state='disabled')
        e21.config(state='disabled')
        e22.config(state='disabled')
        e31.config(state='disabled')
        e32.config(state='disabled')
        e33.config(state='disabled')

    elif (l3_val) and (l2_val):
        b1.config(state='disabled')
        b2.config(state='disabled')
        e21.config(state='disabled')
        e22.config(state='disabled')
        e31.config(state='disabled')
        e32.config(state='disabled')
        e33.config(state='disabled')

    elif (not l3_val) and (l2_val):
        b1.config(state='normal')
        b2.config(state='normal')
        e21.config(state='normal')
        e22.config(state='normal')
        e31.config(state='disabled')
        e32.config(state='disabled')
        e33.config(state='disabled')

    elif (l3_val) and (not l2_val):
        b1.config(state='normal')
        b2.config(state='normal')
        e21.config(state='disabled')
        e22.config(state='disabled')
        e31.config(state='normal')
        e32.config(state='normal')
        e33.config(state='normal')

    else:
        b1.config(state='disabled')
        b2.config(state='disabled')
        e21.config(state='disabled')
        e22.config(state='disabled')
        e31.config(state='disabled')
        e32.config(state='disabled')
        e33.config(state='disabled')

def res():
    l2_val = largestTwo.get()
    l3_val = largestThree.get()
    if (l3_val) and (not l2_val):
        if (int(e31.get()) > int(e32.get()) and int(e31.get()) > int(e33.get())):
            e31.config(background='green')
            e32.config(background='red')
            e33.config(background='red')
            result.config(text=e31.get() + " is largest")
            messagebox.showinfo('largest', e31.get()+" is largest")
        elif (int(e33.get()) > int(e32.get()) and int(e33.get()) > int(e31.get())):
            e31.config(background='red')
            e32.config(background='red')
            e33.config(background='green')
            result.config(text=e33.get() + " is largest")
            messagebox.showinfo('largest', e33.get()+" is largest")
        else:
            e31.config(background='red')
            e32.config(background='green')
            e33.config(background='red')
            result.config(text=e32.get() + " is largest")
            messagebox.showinfo('largest', e32.get()+" is largest")
        e31.config(background='black')
        e32.config(background='black')
        e33.config(background='black')

    else:
        if (int(e21.get()) > int(e22.get())):
            e22.config(background='red')
            e21.config(background='green')
            result.config(text=e21.get() + " is largest")
            messagebox.showinfo('largest', e21.get()+" is largest")
        else:
            e21.config(background='red')
            e22.config(background='green')
            result.config(text=e22.get() + " is largest")
            messagebox.showinfo('largest', e22.get()+" is largest")
        e22.config(background='black')
        e21.config(background='black')

def rest():
    l2_val = largestTwo.get()
    l3_val = largestThree.get()
    result.config(text="")
    e31.delete(0,'end')
    e32.delete(0, 'end')
    e33.delete(0, 'end')
    e21.delete(0, 'end')
    e22.delete(0, 'end')

root = tk.Tk()
root.geometry("1000x500")
root.title("largestno.org")
root.resizable(False, False)
root.config(bg='black')

my_font = ('Times New Roman', 10, 'bold')

largestTwo = tk.BooleanVar()
largestTwo.set(False)
largestThree = tk.BooleanVar()
largestThree.set(False)

head=tk.Label(root, text="Largest Number", font=('Times New Roman', 20, 'bold','underline'), foreground='white', background='black')
head.grid(column=0, row=0, sticky=tk.W, padx=20, pady=20, columnspan=2)

l2b = ttk.Checkbutton(root, text='Largest among 2', command=actionbut, variable=largestTwo )
l2b.grid(column=0, row=1, sticky=tk.W, padx=20, pady=20, columnspan=2)

lab21 = ttk.Label(root, text="NUM 1", font=my_font, foreground='white', background='black')
lab21.grid(column=0, row=2, sticky=tk.W, padx=20, pady=20)

e21 = tk.Entry(root, background='black', foreground='white', font=my_font, state='disabled')
e21.grid(column=1, row=2, sticky=tk.W, padx=20, pady=20,)

lab22 = ttk.Label(root, text="NUM 2", font=my_font, foreground='white', background='black')
lab22.grid(column=0, row=3, sticky=tk.W, padx=20, pady=20)

e22 = tk.Entry(root, background='black', foreground='white', font=my_font, state='disabled')
e22.grid(column=1, row=3, sticky=tk.W, padx=20, pady=20,)

l3b = ttk.Checkbutton(root, text='Largest among 3', command=actionbut, variable=largestThree)
l3b.grid(column=2, row=1, sticky=tk.W, padx=20, pady=20, columnspan=2)

lab31 = ttk.Label(root, text="NUM 1", font=my_font, foreground='white', background='black')
lab31.grid(column=3, row=2, sticky=tk.W, padx=20, pady=20)

e31 = tk.Entry(root, background='black', foreground='white', font=my_font, state='disabled')
e31.grid(column=4, row=2, sticky=tk.W, padx=20, pady=20,)

lab32 = ttk.Label(root, text="NUM 2", font=my_font, foreground='white', background='black')
lab32.grid(column=3, row=3, sticky=tk.W, padx=20, pady=20)

e32 = tk.Entry(root, background='black', foreground='white', font=my_font, state='disabled')
e32.grid(column=4, row=3, sticky=tk.W, padx=20, pady=20,)

lab33 = ttk.Label(root, text="NUM 3", font=my_font, foreground='white', background='black')
lab33.grid(column=3, row=4, sticky=tk.W, padx=20, pady=20)

e33 = tk.Entry(root, background='black', foreground='white', font=my_font, state='disabled')
e33.grid(column=4, row=4, sticky=tk.W, padx=20, pady=20,)

b1 = tk.Button(root, text='Reset Values', width=20, bg='black', font=my_font, fg='white', state='disabled', command=rest)
b1.grid(column=0, row=5, sticky=tk.W, padx=20, pady=20)

b2 = tk.Button(root, text='Calculate', width=20, bg='black', font=my_font, fg='white', state='disabled', command=res)
b2.grid(column=1, row=5, sticky=tk.W, padx=20, pady=20)

result = ttk.Label(root, text="", font=my_font, foreground='white', background='black')
result.grid(column=3, row=6, sticky=tk.W, padx=20, pady=20)

root.mainloop()