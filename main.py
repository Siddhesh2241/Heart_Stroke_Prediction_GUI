from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

roots = Tk()
roots.title("Heart stroke prediction")
roots.geometry("1450x700+60+80")
roots.resizable(False, False)
roots.configure(bg = background)




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# icon 1
image_icon = PhotoImage(file = "Images\icon.png")
roots.iconphoto(False, image_icon)

## header section 2
logo = PhotoImage(file = "Images\header.png")
myimage = Label(image = logo, bg = background)
myimage.place(x=0,y=0)

##M<<<<<< frame 3 >>>>>>>
Heading_entry = Frame(roots,width=800,height=190, bg = "#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registration No",font="arial 13",bg="#df2d4b",fg =framefg).place(x=30,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg =framefg).place(x=430,y=0)

Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg =framefg).place(x=30,y=90)
Label(Heading_entry,text="Birth Year",font="arial 13",bg="#df2d4b",fg =framefg).place(x=430,y=90)

Entry_image = PhotoImage(file = "Images\Rounded Rectangle 1.png")
Entry_image2 = PhotoImage(file = "Images\Rounded Rectangle 2.png")

Label(Heading_entry,image = Entry_image,bg = "#df2d4b").place(x=20,y=30)
Label(Heading_entry,image = Entry_image,bg = "#df2d4b").place(x=430,y=30)

Label(Heading_entry,image = Entry_image2,bg = "#df2d4b").place(x=20,y=120)
Label(Heading_entry,image = Entry_image2,bg = "#df2d4b").place(x=430,y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry,font="arial 15",textvariable=Registration,width=30,bg="#0e5363",fg="White",bd=0)
reg_entry.place(x=30,y=45)


Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_enrty = Entry(Heading_entry,font="arial 15",textvariable=Date,width=15,bg="#0e5363",fg="White",bd=0)
date_enrty.place(x=500,y=45)
Date.set(d1)


Name = StringVar()
name_entry = Entry(Heading_entry,font="arial 20",textvariable=Name,width=20,bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB = IntVar()
DOB_entry = Entry(Heading_entry,font="arial 20",textvariable=DOB,width=20,bg="#ededed",fg="#222222",bd=0)
DOB_entry.place(x=450,y=130)

#####################Body Section 4####################

Detail_entry = Frame(roots,width=490,height=260, bg = "#dbe0e3")
Detail_entry.place(x=30,y=450)

###################radio buttons####################
Label(Detail_entry,text="sex: ",font="arial 13",bg=framebg,fg =framefg).place(x=10,y=10)













roots.mainloop()

