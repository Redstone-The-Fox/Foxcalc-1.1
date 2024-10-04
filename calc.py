#!/usr/bin/env python

from sys import set_int_max_str_digits
import tkinter as tk
from tkinter import ttk
from math import *
import math

set_int_max_str_digits(100000)

root = tk.Tk()

root.title("FoxCalc 1.1")
root.geometry('400x500')
root.resizable(False, False)

calcu = ""

def go():
    global calcu
    #print(f"[Log]: Button = Clicked")
    try:
        exec(f'print("Your answer is: ", end=""); print({calcu})')
    except Exception:
        print('Invalid Operation')

def ac():
    global calcu
    #print(f"[Log]: Button AC Clicked")
    calcu = ''
    calculation.config(text=calcu)

def button_clicked(clicked: any) -> None:
    global calcu
    #print(f"[Log]: Button {clicked} Clicked")
    calcu = calcu + str(clicked)
    calculation.config(text=calcu)

wlc = tk.Label(root, text='FoxCalc 1.1', font=('Helvetica', 24))
wlc.pack()
wlc.place(x=0, y=125)

btn1 = tk.Button(root, text='1', command=lambda: button_clicked(1), width=2, height=1)
btn1.pack()
btn1.place(x=0, y=0)

btn2 = tk.Button(root, text='2', command=lambda: button_clicked(2), width=2, height=1)
btn2.pack()
btn2.place(x=45, y=0)

btn3 = tk.Button(root, text='3', command=lambda: button_clicked(3), width=2, height=1)
btn3.pack()
btn3.place(x=90, y=0)

btn4 = tk.Button(root, text='4', command=lambda: button_clicked(4), width=2, height=1)
btn4.pack()
btn4.place(x=135, y=0)

btn5 = tk.Button(root, text='5', command=lambda: button_clicked(5), width=2, height=1)
btn5.pack()
btn5.place(x=0, y=40)

btn6 = tk.Button(root, text='6', command=lambda: button_clicked(6), width=2, height=1)
btn6.pack()
btn6.place(x=45, y=40)

btn7 = tk.Button(root, text='7', command=lambda: button_clicked(7), width=2, height=1)
btn7.pack()
btn7.place(x=90, y=40)

btn8 = tk.Button(root, text='8', command=lambda: button_clicked(8), width=2, height=1)
btn8.pack()
btn8.place(x=135, y=40)

btn9 = tk.Button(root, text='9', command=lambda: button_clicked(9), width=2, height=1)
btn9.pack()
btn9.place(x=0, y=80)

btn0 = tk.Button(root, text='0', command=lambda: button_clicked(0), width=2, height=1)
btn0.pack()
btn0.place(x=45, y=80)

btnPLUS = tk.Button(root, text='+', command=lambda: button_clicked(" + "), width=4, height=2)
btnPLUS.pack()
btnPLUS.place(x=0, y=420)

btnSUBT = tk.Button(root, text='-', command=lambda: button_clicked(" - "), width=4, height=2)
btnSUBT.pack()
btnSUBT.place(x=60, y=420)

btnMUL = tk.Button(root, text='*', command=lambda: button_clicked(" * "), width=4, height=2)
btnMUL.pack()
btnMUL.place(x=120, y=420)

btnDIV = tk.Button(root, text='/', command=lambda: button_clicked(" / "), width=4, height=2)
btnDIV.pack()
btnDIV.place(x=180, y=420)

btnLPAR = tk.Button(root, text='(', command=lambda: button_clicked("("), width=4, height=2)
btnLPAR.pack()
btnLPAR.place(x=0, y=365)

btnRPAR = tk.Button(root, text=')', command=lambda: button_clicked(")"), width=4, height=2)
btnRPAR.pack()
btnRPAR.place(x=60, y=365)

btnPOWER = tk.Button(root, text='^', command=lambda: button_clicked(" ** "), width=4, height=2)
btnPOWER.pack()
btnPOWER.place(x=120, y=365)

btnSQRT = tk.Button(root, text='√', command=lambda: button_clicked("sqrt("), width=4, height=2)
btnSQRT.pack()
btnSQRT.place(x=180, y=365)

btnSIN = tk.Button(root, text='sin()', command=lambda: button_clicked("sin("), width=2, height=1)
btnSIN.pack()
btnSIN.place(x=0, y=330)

btnTAN = tk.Button(root, text='tan()', command=lambda: button_clicked("tan("), width=2, height=1)
btnTAN.pack()
btnTAN.place(x=45, y=330)

btnCOS = tk.Button(root, text='cos()', command=lambda: button_clicked("cos("), width=2, height=1)
btnCOS.pack()
btnCOS.place(x=90, y=330)

btnSH = tk.Button(root, text='sinh()', command=lambda: button_clicked("sinh("), width=2, height=1)
btnSH.pack()
btnSH.place(x=135, y=330)

btnTH = tk.Button(root, text='tanh()', command=lambda: button_clicked("tanh("), width=2, height=1)
btnTH.pack()
btnTH.place(x=180, y=330)

btnCH = tk.Button(root, text='cosh()', command=lambda: button_clicked("cosh("), width=2, height=1)
btnCH.pack()
btnCH.place(x=225, y=330)

btnDECI = tk.Button(root, text='.', command=lambda: button_clicked("."), width=4, height=2)
btnDECI.pack()
btnDECI.place(x=240, y=365)

btnPI = tk.Button(root, text='π', command=lambda: button_clicked("math.pi"), width=4, height=2)
btnPI.pack()
btnPI.place(x=240, y=365)

btnGO = tk.Button(root, text='=', command=lambda: go(), width=4, height=2)
btnGO.pack()
btnGO.place(x=240, y=420)

btnAC = tk.Button(root, text='AC', command=lambda: ac(), width=4, height=2)
btnAC.pack()
btnAC.place(x=300, y=420)

calculation = tk.Label(root, text=calcu)
calculation.pack()
calculation.place(x=0, y=475)

root.mainloop()