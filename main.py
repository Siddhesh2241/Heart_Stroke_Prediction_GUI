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
roots.resizable(True, True)
roots.configure(bg = background)




# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# icon 1
image_icon = PhotoImage(file = "Images\icon.png")
roots.iconphoto(False, image_icon)

## header section 2
logo = PhotoImage(file = "Images\header.png")
myimage = Label(image = logo, bg = background)
myimage.place(x=0,y=0)

##<<<<<< frame 3 >>>>>>>
Heading_entry = Frame(roots,width=800,height=190, bg = "#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text="Registration No",font="arial 13",bg="#df2d4b",fg =framefg).place(x=10,y=0)
Label(Heading_entry,text="Date",font="arial 13",bg="#df2d4b",fg =framefg).place(x=400,y=0)

Label(Heading_entry,text="Patient Name",font="arial 13",bg="#df2d4b",fg =framefg).place(x=10,y=90)
Label(Heading_entry,text="Birth Year",font="arial 13",bg="#df2d4b",fg =framefg).place(x=400,y=90)

Entry_image = PhotoImage(file = "Images\Rounded Rectangle 1.png")
Entry_image2 = PhotoImage(file = "Images\Rounded Rectangle 2.png")

Label(Heading_entry,image = Entry_image,bg = "#df2d4b").place(x=10,y=30)
Label(Heading_entry,image = Entry_image,bg = "#df2d4b").place(x=400,y=30)

Label(Heading_entry,image = Entry_image2,bg = "#df2d4b").place(x=10,y=120)
Label(Heading_entry,image = Entry_image2,bg = "#df2d4b").place(x=400,y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry,font="arial 15",textvariable=Registration,width=10,bg="#0e5363",fg="White",bd=0)
reg_entry.place(x=30,y=45)


Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_enrty = Entry(Heading_entry,font="arial 15",textvariable=Date,width=10,bg="#0e5363",fg="White",bd=0)
date_enrty.place(x=420,y=45)
Date.set(d1)


Name = StringVar()
name_entry = Entry(Heading_entry,font="arial 15",textvariable=Name,width=20,bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB = IntVar()
DOB_entry = Entry(Heading_entry,font="arial 15",textvariable=DOB,width=10,bg="#ededed",fg="#222222",bd=0)
DOB_entry.place(x=420,y=130)

#####################Body Section 4####################

Detail_entry = Frame(roots,width=490,height=260, bg = "#dbe0e3")
Detail_entry.place(x=30,y=450)

###################radio buttons####################
Label(Detail_entry,text="sex: ",font="arial 13",bg=framebg,fg =framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs: ",font="arial 13",bg=framebg,fg =framefg).place(x=180,y=10)
Label(Detail_entry,text="Exercise: ",font="arial 9",bg=framebg,fg =framefg).place(x=335,y=10)

def selection():
   if gen.get() == 1:
       Gender = 1
       return(Gender)
   
   elif gen.get() == 2:
       Gender = 0
       return(Gender)
   else:
       print("Gender")
   

def selection2():
    
   if fbs.get() == 1:
       Fbs = 1
       return(Fbs)
   
   elif fbs.get() == 2:
       Fbs = 0
       return(Fbs)
   else:
       print("Fbs")

def selection3():
   
   if Exercise.get() == 1:
       Exang = 1
       return(Exang)
   
   elif Exercise.get() == 2:
       Exang = 0
       return(Exang)
   else:
       print("Exang")


gen = IntVar()
R1 = Radiobutton(Detail_entry, text="Male", variable=gen, value=1,command=selection)
R2 = Radiobutton(Detail_entry,text="Female", variable=gen, value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)



fbs = IntVar()
R3 = Radiobutton(Detail_entry, text="True", variable=fbs, value=1,command=selection)
R4 = Radiobutton(Detail_entry,text="False", variable=fbs, value=2,command=selection)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

Exercise = IntVar()
R5 = Radiobutton(Detail_entry, text="Yes", variable=Exercise , value=1,command=selection)
R6 = Radiobutton(Detail_entry,text="No", variable=Exercise , value=2,command=selection)
R5.place(x=387,y=10)
R6.place(x=430,y=10)

###################Combobox####################
Label(Detail_entry,text="Chest pain: ",font="arial 9",bg=framebg,fg =framefg).place(x=10,y=50)
Label(Detail_entry,text="Rest ECG Result: ",font="arial 9",bg=framebg,fg =framefg).place(x=10,y=90)
Label(Detail_entry,text="slope: ",font="arial 13",bg=framebg,fg =framefg).place(x=10,y=130)
Label(Detail_entry,text="No of vessels: ",font="arial 9",bg=framebg,fg =framefg).place(x=10,y=170)
Label(Detail_entry,text="Thalassemia : ",font="arial 9",bg=framebg,fg =framefg).place(x=10,y=210)



def selection4():
   
   input1 = cp_combobox.get()
   if input1 == '0=typical angina':
       cp = 0
       return(cp)
   elif input1 == '1=atypica angina':
       cp = 1
       return(cp)
   elif input1 == '2=non-anginal pain':
       cp = 2
       return(cp)
   elif input1 == '3=asymptomacit':
       cp = 3
       return(cp)
   else:
         print("Excersie")


def selection5():
   
   input1 = slope_combobox.get()
   if input1 == '0=upsloping':
       
       return(0)
   elif input1 == '1=Flat':
       
       return(1)
   elif input1 == '2=downsloping':
       
       return(2)
   else:
         print("Excersie")



cp_combobox = Combobox(Detail_entry,values=['0=typical angina','1=atypica angina','2=non-anginal pain','3=asymptomacit'],font="arial 12",state='r',width=14)
restecg_combobox = Combobox(Detail_entry,values=['0','1','2'],font="arial 12",state='r',width=11)
slope_combobox = Combobox(Detail_entry,values=['0 = upsloping','1 = Flat','2 = downsloping'],font="arial 12",state='r',width=12)
ca_combobox = Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state='r',width=14)
thal_combobox = Combobox(Detail_entry,values=['0','1','2','3'],font="arial 12",state='r',width=14)

cp_combobox.place(x=80,y=50)
restecg_combobox.place(x=120,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=100,y=170)
thal_combobox.place(x=100,y=210)




###################Data Entry Box####################


Label(Detail_entry,text="Smoking",font="arial 9",width=10,bg="#dbe0e3",fg="Black").place(x=250,y=50)
Label(Detail_entry,text="Resting BP",font="arial 9",width=10,bg=framebg,fg=framefg).place(x=250,y=90)
Label(Detail_entry,text="Cholestrol",font="arial 9",width=10,bg=framebg,fg=framefg).place(x=250,y=130)
Label(Detail_entry,text="Max Heart Rate",font="arial 9",width=12,bg=framebg,fg=framefg).place(x=260,y=170)
Label(Detail_entry,text="oldpeak",font="arial 9",width=10,bg=framebg,fg=framefg).place(x=250,y=210)


trestbps = StringVar()
chol= StringVar()
thalanch= StringVar()
oldepeak= StringVar()


trestbps_entry = Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry = Entry(Detail_entry,textvariable=chol,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalanch_entry = Entry(Detail_entry,textvariable=thalanch,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldepeak_entry = Entry(Detail_entry,textvariable=oldepeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)


trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalanch_entry.place(x=350,y=170)
oldepeak_entry.place(x=320,y=210)







roots.mainloop()

