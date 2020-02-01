# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 02:12:50 2020

@author: Azhan
"""
from tkinter import *
 
expression = "" 

def press(num): 
     
    global expression  
    expression = expression + str(num)  
    equation.set(expression) 
 
def equalpress(): 
     
    try: 

        global expression 
        total = str(eval(expression)) 
        equation.set(total) 
        expression = ""
    
    except:
         
        equation.set(" error ") 
        expression = "" 
 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 

# Driver code 
if __name__ == "__main__": 
 
    window = Tk()  
    window.configure(background="light green") 
    window.title("Simple Calculator")   
    window.geometry("430x263") 
 
    equation = StringVar() 
 
    expression_field = Entry(window, textvariable=equation) 

    expression_field.grid(columnspan=180, ipadx=140,ipady=10) 

    equation.set('enter your expression')  
    
    button1 = Button(window, text=' 1 ', fg='black', bg='red', 
                    command=lambda: press(1), height=3, width=14) 
    button1.grid(row=4, column=0) 

    button2 = Button(window, text=' 2 ', fg='black', bg='yellow', 
                    command=lambda: press(2), height=3, width=14) 
    button2.grid(row=4, column=1) 

    button3 = Button(window, text=' 3 ', fg='black', bg='pink', 
                    command=lambda: press(3), height=3, width=14) 
    button3.grid(row=4, column=2) 

    button4 = Button(window, text=' 4 ', fg='black', bg='red', 
                    command=lambda: press(4), height=3, width=14) 
    button4.grid(row=5, column=0) 

    button5 = Button(window, text=' 5 ', fg='black', bg='yellow', 
                    command=lambda: press(5), height=3, width=14) 
    button5.grid(row=5, column=1) 

    button6 = Button(window, text=' 6 ', fg='black', bg='pink', 
                    command=lambda: press(6), height=3, width=14) 
    button6.grid(row=5, column=2) 

    button7 = Button(window, text=' 7 ', fg='black', bg='red', 
                    command=lambda: press(7), height=3, width=14) 
    button7.grid(row=6, column=0) 

    button8 = Button(window, text=' 8 ', fg='black', bg='yellow', 
                    command=lambda: press(8), height=3, width=14) 
    button8.grid(row=6, column=1) 

    button9 = Button(window, text=' 9 ', fg='black', bg='pink', 
                    command=lambda: press(9), height=3, width=14) 
    button9.grid(row=6, column=2) 

    button0 = Button(window, text=' 0 ', fg='black', bg='red', 
                    command=lambda: press(0), height=3, width=14) 
    button0.grid(row=7, column=0) 

    plus = Button(window, text=' + ', fg='black', bg='orange', 
                command=lambda: press("+"), height=3, width=14) 
    plus.grid(row=4, column=3) 

    minus = Button(window, text=' - ', fg='black', bg='orange', 
                command=lambda: press("-"), height=3, width=14) 
    minus.grid(row=5, column=3) 

    multiply = Button(window, text=' * ', fg='black', bg='orange', 
                    command=lambda: press("*"), height=3, width=14) 
    multiply.grid(row=6, column=3) 

    divide = Button(window, text=' / ', fg='black', bg='orange', 
                    command=lambda: press("/"), height=3, width=14) 
    divide.grid(row=7, column=3) 

    equal = Button(window, text=' = ', fg='black', bg='orange', 
                command=equalpress, height=3, width=14) 
    equal.grid(row=7, column=2) 

    clear = Button(window, text='Clear', fg='black', bg='white', 
                command=clear, height=3, width=14) 
    clear.grid(row=7, column='1') 

    # start of the window 
    window.mainloop() 
