from tkinter import *
from PIL import ImageTk,Image
import os
from random import randrange
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

root = Tk()  
canvas = Canvas(root, width = 1000, height = 1000)  
canvas.pack()  
images =[] #we will append all images for current folder

# get all images with for loop
for x in range(6):
   val = str(x+1)#images start with 1 so we add +1
   name = val+'.png'#all images ends with *.png*
   images.append(PhotoImage(file=os.path.join(THIS_FOLDER, name)))

defaultImage =canvas.create_image(20, 20, anchor="nw", image=images[0]) 
text =Label(root)
text.configure(width=10,)
theVal = canvas.create_text(50,400, anchor="nw", text="Value is: 0")
def imageRandom():
    rnd =randrange(6)
    canvas.itemconfig(defaultImage, image=images[rnd])
    canvas.itemconfig(theVal, text="Value is:" + str(rnd+1))

btn = Button(root, text="To Dice", command=imageRandom)
btn.configure(width=10)

canvas.create_window(60,350, anchor="nw", window=btn)
root.mainloop()


