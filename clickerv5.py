<<<<<<< HEAD
from ssl import Options
import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("400x400")
root.config(bg = "grey")
count = 0 
countLabel = tk.Label(root,text = count)
countCheck = ""
BoxState = "disabled"

def autoClick():
    global countCheck
    checkBox = AutoclickBox.get()
    if checkBox == 1:
        if countCheck == "Up":
            UpB()
        elif countCheck == "Down":
            DownB()
        root.after(100,autoClick)


def XorDivide(event):    
    global count, countCheck
    if countCheck == "Multiply":
        count *= 3
    elif countCheck == "Divide":
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
    countCheck = "Multiply"
    Autoclick.configure(state = "normal")
def UpB(event):
    Up()    

def Down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Divide"
    Autoclick.configure(state = "normal")
def DownB(event):
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
    command=autoClick,
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

=======
from ssl import Options
import tkinter as tk

root = tk.Tk()
root.title("Clicker")
root.geometry("400x400")
root.config(bg = "grey")
count = 0 
countLabel = tk.Label(root,text = count)
countCheck = ""
BoxState = "disabled"

def autoClick():
    global countCheck
    checkBox = AutoclickBox.get()
    if checkBox == 1:
        if countCheck == "Up":
            UpB()
        elif countCheck == "Down":
            DownB()
        root.after(100,autoClick)


def XorDivide(event):    
    global count, countCheck
    if countCheck == "Multiply":
        count *= 3
    elif countCheck == "Divide":
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
    countCheck = "Multiply"
    Autoclick.configure(state = "normal")
def UpB(event):
    Up()    

def Down():
    global count, countCheck
    count -= 1
    countLabel.configure(text = count)
    colourChanges("")
    countCheck = "Divide"
    Autoclick.configure(state = "normal")
def DownB(event):
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
    command=autoClick,
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

>>>>>>> 15c22d11bf6cd2dbbf9f94ee62df95fc56e4df80
root.mainloop()