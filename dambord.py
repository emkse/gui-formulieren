import tkinter as tk

root = tk.Tk()
root.geometry("800x800")
root.title("Dambord")
bord = tk.Frame(root)

# r = rijen, c = kolommen
waarde = False
for r in range(10):
    if waarde == True:
        waarde = False
    else:
        waarde = True
    for c in range(10):
        if waarde == True:
            colour = "black"
            waarde = False
        else: 
            colour = "white"
            waarde = True
        tile = tk.Label(bord, bg = colour, padx = 30, pady = 20)
        tile.grid(row = r, column = c)
bord.pack(expand = True)

root.mainloop()