from ast import Lambda
from multiprocessing import Event
from ssl import Options
import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("400x400")
root.config(bg = "grey")
count = 0 
countLabel = tk.Label(root,text = count)
countChecker = " "
countCheck = " "
BoxState = "disabled"

def autoClick():
    print("test123")
    global countCheck
    checkBox = AutoclickBox.get()
    print(checkBox)
    if checkBox == 1:
        print(countCheck)
        if countCheck == "Up": 
            UpB()
            root.after(200, autoClick)
        elif countCheck == "Down":
            DownB()
        root.after(200,autoClick)
   

def XorDivide(event):    
    global count, countChecker
    if countChecker == "Multiply":
        count *= 3
    elif countChecker == "Divide":
        count /= 3
    countLabel.configure(text = count)
    

def backgroundcolorchange(event):
    root.configure(bg = "yellow")
    

def colourChanges(event):
    global count
    if count > 0:
        root.configure(bg = "green")
    elif count < 0:
        root.configure(bg = "red")
    else:
        root.configure(bg = "grey")
 
        
        
def Up():
    global count, countCheck
    count += 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Up"
    Autoclick.configure(state = "normal")
def UpB():
    Up()    

def Down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Down"
    Autoclick.configure(state = "normal")
def DownB():
    Down()


buttonUp = tk.Button(
    root,
    command = Up,
    text = "Up"    
)
buttonDown = tk.Button(
    root,
    command = Down,
    text = "Down"    
)

def SpaceB(event):
    XorDivide("")

buttonUp.pack(
ipadx = 55, 
side = "top",
expand = True
)

countLabel.pack(
    ipadx = 60,
    expand = True
)       

buttonDown.pack(
    ipadx = 45,
    side = "bottom",
    expand = True
)

AutoclickBox = tk.IntVar()
Autoclick = tk.Checkbutton(
    root,
    variable = AutoclickBox,
    command= autoClick,
    text="Autoclick",
    font= ('Calibri', 20, 'bold'),
    bg="white",
    state="disabled",
    onvalue = 1, 
    offvalue = 0,
)
Autoclick.pack()

countLabel.bind("<Enter>", backgroundcolorchange)
countLabel.bind("<Leave>", colourChanges)
root.bind("<Double-Button>", XorDivide)
root.bind("<space>", SpaceB)
root.bind("<Up>", UpB) and root.bind("<+>", UpB)
root.bind("<Down>", DownB) and root.bind ("-", DownB)

root.mainloop()