from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI CLOCK")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        title=Label(self.root, text="Welcome", font=("times new roman",50,"bold"),bg="#04444a",fg="white")
        title.pack(fill="x",pady=10)

        self.lbl=Label(self.root,bg="white",width=380,height=300,bd=10)
        self.lbl.pack(pady=55)
         #self.clock_img()
        self.working()


    def clock_img(self,hr,min_,sec_):
        clock = Image.new("RGB", (400, 400), (25, 26, 25))
        draw = ImageDraw.Draw(clock)

        #----for clock image
        bg=Image.open("w2.jpg")   # w1.JPG also use
        bg=bg.resize((300,300),Image.ANTIALIAS) #'Image.ANTIALIAS' image clearing bagde na aena mate used thai che
        clock.paste(bg,(50,50))   # x thi 50 space lese and  y thi 50 space lese

        # formula for Rotate the clock

        # end_x=center_x-line_length * math.sin(angle_in_radiasion)
        # end_y=center_y+line_length * math.cos(angle_in_radiasion)



        #-----hour line image
        origin=200,200
        draw.line((origin,200+40*sin(radians(hr)),200-40*cos(radians(hr))), fill="green", width=4) #240

        # -----Minute line image
        draw.line((origin,200+60*sin(radians(min_)),200-60*cos(radians(min_))), fill="red", width=4) #260

        # -----second line image
        draw.line((origin,200+70*sin(radians(sec_)),200-70*cos(radians(sec_))), fill="orange", width=3) #270
        draw.ellipse((195,195,210,210),fill="black")

        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
         #print(h,m,s)

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
         #print(hr,min_,sec_)
        self.clock_img(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)

        self.lbl.after(200,self.working)


root=Tk()
obj=Clock(root)
root.mainloop()