'''
Created on 2012-11-18

@author: Administrator
'''
from tkinter import *
import sys 

if __name__ == '__main__':
    win = Tk()
    button = Button(win, text = "Goodbye", command = sys.exit)
    button.pack()
    mainloop()