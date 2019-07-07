from tkinter import *
window=Tk()
window.title("Calculator")

def add(text):
    txt=nText.get()
    if txt=="Error":
        nText.set(text)
    else:
        nText.set(txt+text)

def delete():
    nText.set(nText.get()[:-1])

def reset():
    nText.set("")

def calculate():
    try:
        nText.set(eval(nText.get()))
    except:
        nText.set("ERROR")

nText=StringVar()
Entry(window,textvariable=nText, font=("Times 18")).grid(sticky="WE", column=1, columnspan=4)

Button(window,text="C",command=reset, font=("Times 18"),width=4).grid(row=1, column=1)
Button(window,text="X",command=delete, font=("Times 18"),width=4).grid(row=1, column=2)
Button(window,text="/",command=lambda:add("/"), font=("Times 18"),width=4).grid(row=1, column=3)
Button(window,text="*",command=lambda:add("*"), font=("Times 18"),width=4).grid(row=1, column=4)

Button(window,text="7",command=lambda:add("7"), font=("Times 18"),width=4).grid(row=2, column=1)
Button(window,text="8",command=lambda:add("8"), font=("Times 18"),width=4).grid(row=2, column=2)
Button(window,text="9",command=lambda:add("+"), font=("Times 18"),width=4).grid(row=2, column=3)
Button(window,text="+",command=lambda:add("+"), font=("Times 18"),width=4).grid(row=2, column=4)

Button(window,text="4",command=lambda:add("4"), font=("Times 18"),width=4).grid(row=3, column=1)
Button(window,text="5",command=lambda:add("5"), font=("Times 18"),width=4).grid(row=3, column=2)
Button(window,text="6",command=lambda:add("6"), font=("Times 18"),width=4).grid(row=3, column=3)
Button(window,text="-",command=lambda:add("-"), font=("Times 18"),width=4).grid(row=3, column=4)

Button(window,text="1",command=lambda:add("1"), font=("Times 18"),width=4).grid(row=4, column=1)
Button(window,text="2",command=lambda:add("2"), font=("Times 18"),width=4).grid(row=4, column=2)
Button(window,text="3",command=lambda:add("3"), font=("Times 18"),width=4).grid(row=4, column=3)
Button(window,text="=",command=calculate, font=("Times 18"),width=4).grid(sticky="NS", row=4, column=4,rowspan=2)

Button(window,text="0",command=lambda:add("0"), font=("Times 18"),width=4).grid(sticky="WE", row=5, column=1,columnspan=2)
Button(window,text=".",command=lambda:add("."), font=("Times 18"),width=4).grid( row=5, column=3)

window.mainloop() #this helps countinously show windows
