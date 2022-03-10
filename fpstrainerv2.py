import tkinter as tk
import time 
import random
from tkinter import Entry, Place, messagebox, Label, Button
from turtle import update

root = tk.Tk()
root.title("FPS Training V1")
root.geometry("700x700")
root.config(bg = "grey")

#global variables
timer = 20
points = 0
pointsV2 = 0
listRandom = 0 
a = False

my_box = Entry(root)
my_box.insert(0, str(timer))
my_box.place(rely = 0.1 , relx = 0.4)

#List
buttonBind = ["<w>", "<s>", "<a>", "<d>", "<space>", "<Button>", "<Double-Button>", "<Triple-Button>"]
buttonList = ["W", "S", "A", "D", "Space", "One click", "Double Click", "Triple Click"]


#Label posities
x=random.randint(0,385) 
y=random.randint(75,450)

#List with randomchoice
buttonsBindRandom = random.choice(buttonBind)
buttonsRandom = random.choice(buttonList) 


#list tegelijkertijd binden
listRandomV2 = random.randint(0,2)
listRandom = random.randint(0,7)
buttonBind[listRandom]
buttonList[listRandom]

def startprogramma():
    global timer
    startButton.destroy()
    timer = int(my_box.get())
    my_box.destroy()
    keyGame.place(x=random.randint(0,385), y=random.randint(75,450))
    createKeyBind()
    countdown()
    pointslabel.place(x=600)
    
    #bug: key unbind niet
def createKeyBind():
    global buttonsBindRandom, buttonBind, buttonList, listRandom
    print(buttonBind[listRandom])
    root.bind(buttonBind[listRandom], keybind)
    print(buttonBind)
    
    
def keybind(event):
    global buttonsRandom, buttonBind, listRandom
    root.unbind(buttonBind[listRandom])
    listRandom = random.randint(0,7)
    keyGame.place(x=random.randint(0,385), y=random.randint(75,450))
    keyGame.configure(text= "Press: " + (buttonList[listRandom]))
    createKeyBind()
    pointStack()
  
def pointStack():
    global points, buttonBind, listRandom
    print(buttonBind[listRandom])
    if buttonBind[listRandom] == "<Button>" or buttonBind[listRandom] == "<Double-Button>" or buttonBind[listRandom] == "<Triple-Button>":
        points = points +2
        print("+2")
    else:
        print("+1")
        points = points +1      
    pointslabel.configure(text= str(points) + " Points")         
    
def countdown():
    global timer,a
    if a == False:
        startButton.destroy()
        a = True
    timerlabel.place(anchor="nw")
    timerlabel.configure(text ="Time remaining: " + str(timer))
    if timer > 0:
        timer -= 1      
        root.after(1000, countdown)
    else:
        messageBox()
        
def messageBox():
    if timer == 0:
            scoreBox = messagebox.showinfo(title="Game Ended!", message= "Total Points: " + str(points))
            restartButton = messagebox.askretrycancel(title="Game ended!", message= "Do you want to retry?")
            if restartButton:
                gameReset()
            else: 
                root.destroy() 
                       
def gameReset():
    global timer, points
    timer = 20 
    points = 0
    keyGame.pack
    countdown()
    
keyGame = tk.Label(
    text= "Press: " + str(buttonList[listRandom]),
    fg= "white",
    bg= "black",
    font=("arial", 20, "bold"),
    relief="solid",
    activebackground="red",
)
          
startButton = tk.Button(
    root, 
    text= "START TRAINING", 
    fg = "white",
    bg= "Black",
    font=("arial", 20, "bold"),
    relief="solid",
    activebackground="red",
    command = startprogramma
)
startButton.pack(ipadx = 75,ipady = 50, side = "top", expand = True)

timerlabel = tk.Label(
    root,
    text="Time Left:",
    padx="15",
    font= ("Calibri", 15, "bold"),
    bg="grey",
    fg="black"
)

pointslabel = tk.Label(
    root,
    text="0 Points",
    font= ("Calibri", 15, "bold"),
    padx="5",
    bg= "grey",
    fg="black",
)

root.mainloop()
