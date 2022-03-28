import tkinter as tk
from tkinter import ttk
import datetime as dt
from tkinter.messagebox import *

root = tk.Tk()
root.geometry("429x100")
root.resizable(False,False)
root.title("days by date calculator")
root.config(bg = "white")

#dates 
date = dt.date.today()
current_day = f"{date:%d}"
current_month = f"{date:%B}"
current_year = f"{date:%Y}"

#combobox value 
day_cb = ttk.Combobox(root,textvariable = current_day, values=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),state="readonly")
month_cb = ttk.Combobox(root, textvariable = current_month, values=("January", "February","March","April","May","June","July","August","September","Oktober","November","December"),state="readonly")
year_cb = ttk.Combobox(root, textvariable= current_year,values=("2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030"),state="readonly")

selected_day = tk.IntVar(value = current_day)
selected_month = tk.StringVar(value = current_month)
selected_year = tk.IntVar(value = current_year)

#combobox placement
day_cb.grid(column = 1, row = 2)
month_cb.grid(column= 2, row = 2)
year_cb.grid(column=  3, row= 2)

label = tk.Label(text="Please select a date:")
label.grid(column=  2, row= 1)

def calculator():
    day = int(selected_day.get())
    month = str(selected_month.get())
    year = int(selected_year.get())
    global number, textInfo
    dayPicked = int(day)
    monthPicked = month
    yearPicked = int(year)
    monthNumber = int(dt.datetime.strptime(monthPicked, "%B").month)
    today = date
    datePicked = dt.date(yearPicked, monthNumber, dayPicked)
    difference = datePicked - today
    number = difference.days
    if number > 0:
        if number == 1:
            textInfo = "This is " + str(number) + " day in the future"
        else:
            textInfo = "This is " + str(number) + " days in the future"
    elif number < 0:
        if -number == 1:
            textInfo = "This was " + str(-number) + " day ago"
        else:
            textInfo = "This was " + str(-number) + " days ago"
    else:
        textInfo = "This is today"
        
GoButton = tk.Button(
    root,
    text="Go",
    bg="blue",
    fg="white",
    activebackground="green",
    command=lambda:[calculator(),showinfo(title="tijdverschil",message=textInfo)])
GoButton.grid(column=  2, row= 4)

root.mainloop()