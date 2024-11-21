from tkinter import*
def append_number(num):
    global x
    if lab0['text'] == '0':
        lab0['text'] = str(num)
    else:
        lab0['text'] += str(num)

def clear_display():
    global x
    x = 0
    lab0['text'] = '0'

def set_operator(op):
    global x, operator
    x = int(lab0['text'])
    operator = op
    lab0['text'] = '0'

def calculate():
    global x, operator
    if operator:
        y = int(lab0['text'])
        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        elif operator == '÷':
            result = x / y if y != 0 else "Error"
        else:
            result = "Error"
        lab0['text'] = str(result)
        operator = None
root = Tk()
root.title('計算機')
root.geometry('500x500+100+50')
x=0
operator = None
lab0=Label(root,width=25,height=2,
           bg='#ccddef',
           text=str(x),
           justify=CENTER,
           font="Arial 20 bold")
lab0.pack()
btn0=Button(root,
            text="0",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(0))
btn0.place(x=150,y=400)
btnC=Button(root,
            text="C",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=clear_display)
btnC.place(x=50,y=400)
btn11=Button(root,
            text="=",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=calculate)
btn11.place(x=250,y=400)
btn12=Button(root,
            text="+",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: set_operator('+'))
btn12.place(x=350,y=400)
btn1=Button(root,
            text="1",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(1))
btn1.place(x=50,y=300)
btn2=Button(root,
            text="2",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(2))
btn2.place(x=150,y=300)
btn3=Button(root,
            text="3",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(3))
btn3.place(x=250,y=300)
btn13=Button(root,
            text="-",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: set_operator('-'))
btn13.place(x=350,y=300)
btn4=Button(root,
            text="4",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(4))
btn4.place(x=50,y=200)
btn5=Button(root,
            text="5",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(5))
btn5.place(x=150,y=200)
btn6=Button(root,
            text="6",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(6))
btn6.place(x=250,y=200)
btn14=Button(root,
            text="*",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: set_operator('*'))
btn14.place(x=350,y=200)
btn7=Button(root,
            text="7",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(7))
btn7.place(x=50,y=100)
btn8=Button(root,
            text="8",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(8))
btn8.place(x=150,y=100)
btn9=Button(root,
            text="9",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: append_number(9))
btn9.place(x=250,y=100)
btn15=Button(root,
            text="÷",
            font="Arial 20 bold",
            width=5,
            height=2,
            command=lambda: set_operator('÷'))
btn15.place(x=350,y=100)
root.mainloop()