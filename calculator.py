import tkinter as tk

# Button click function
def click(value):
    entry.insert(tk.END, value)

# Calculate function
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Clear function
def clear():
    entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, font=("Arial", 20), bd=5)
entry.grid(row=0, column=0, columnspan=4)

# Row 1
btn7 = tk.Button(root, text="7", width=5, height=2, command=lambda: click("7"))
btn7.grid(row=1, column=0)

btn8 = tk.Button(root, text="8", width=5, height=2, command=lambda: click("8"))
btn8.grid(row=1, column=1)

btn9 = tk.Button(root, text="9", width=5, height=2, command=lambda: click("9"))
btn9.grid(row=1, column=2)

btndiv = tk.Button(root, text="/", width=5, height=2, command=lambda: click("/"))
btndiv.grid(row=1, column=3)

# Row 2
btn4 = tk.Button(root, text="4", width=5, height=2, command=lambda: click("4"))
btn4.grid(row=2, column=0)

btn5 = tk.Button(root, text="5", width=5, height=2, command=lambda: click("5"))
btn5.grid(row=2, column=1)

btn6 = tk.Button(root, text="6", width=5, height=2, command=lambda: click("6"))
btn6.grid(row=2, column=2)

btnmul = tk.Button(root, text="*", width=5, height=2, command=lambda: click("*"))
btnmul.grid(row=2, column=3)

# Row 3
btn1 = tk.Button(root, text="1", width=5, height=2, command=lambda: click("1"))
btn1.grid(row=3, column=0)

btn2 = tk.Button(root, text="2", width=5, height=2, command=lambda: click("2"))
btn2.grid(row=3, column=1)

btn3 = tk.Button(root, text="3", width=5, height=2, command=lambda: click("3"))
btn3.grid(row=3, column=2)

btnsub = tk.Button(root, text="-", width=5, height=2, command=lambda: click("-"))
btnsub.grid(row=3, column=3)

# Row 4
btn0 = tk.Button(root, text="0", width=5, height=2, command=lambda: click("0"))
btn0.grid(row=4, column=0)

btndot = tk.Button(root, text=".", width=5, height=2, command=lambda: click("."))
btndot.grid(row=4, column=1)

btnequal = tk.Button(root, text="=", width=5, height=2, command=calculate)
btnequal.grid(row=4, column=2)

btnadd = tk.Button(root, text="+", width=5, height=2, command=lambda: click("+"))
btnadd.grid(row=4, column=3)

# Clear button
btnclear = tk.Button(root, text="Clear", width=22, height=2, command=clear)
btnclear.grid(row=5, column=0, columnspan=4)

root.mainloop()