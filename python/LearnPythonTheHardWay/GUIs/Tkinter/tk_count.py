'''
Created on 2012-11-19

@author: Administrator
'''

from tkinter import *
main_window = Tk()  # a basic window hierarchy created by the program - main_window is the top-level window widget. 

count_label = Label(main_window, text = "Count: 0")
count_label.grid(row =0, column = 1) # this is the widget placement command, which is accomplished by the 'grid' command
count_value = 0

def increment_count():
    global count_value, count_label
    count_value = count_value + 1
    count_label.configure(text = "Count: " + str(count_value))  # the use of widget attributes, to set and modify the appearance and behavior of widgets

incr_button = Button(main_window, command = increment_count, text = "Increment")
incr_button.grid(row = 0, column = 0)
quit_button = Button(main_window, text = "Quit", command = main_window.destroy) # when clicked, the button should close the main window
quit_button.grid(row = 1, column = 0)
mainloop()
