from tkinter import *
import calendar
#import ttkbootstrap as ttk

def show_calender():
    window2 = Tk()
    window2.title("Year")
    window.geometry("700x800")
    fetch_year = int(answer.get())
    calender_detail = calendar.calendar(fetch_year)
    cal_year = Label(window2, text = calender_detail, font = ("Consolas", 15))
    cal_year.grid(row = 5, column = 1)

    window2.mainloop()


window = Tk()
window.title("Calender")
window.geometry("500x500")
window.configure(background = "navy")

calender = Label(window, text = "Calender", bg = "pink", fg = "black", font = ("times", 126, "bold"))
year = Label(window, text = "Enter year:", bg = "purple", fg = "black", font = ("times", 30))
answer = Entry(window, bg = "white", fg = "black")
#button_style = ttk.Style().configure("custom.TButton", background = "pink")
show_calender = Button(window, text = "Show calender", command = show_calender)
exit = Button(window, text = "Exit", command = exit)

#grid fonction is used for placing the widgets(buttons, label..) at respective positions in a table like structure 
calender.grid(row = 1, column = 1)
year.grid(row = 2, column = 1)
answer.grid(row = 3, column = 1)
show_calender.grid(row = 4, column = 1)
exit.grid(row = 6, column = 1)



window.mainloop()