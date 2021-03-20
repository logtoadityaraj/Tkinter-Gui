
from tkinter import *
import math as m
from PIL import Image, ImageTk





root = Tk()

f1 = Frame(root)


root.geometry("1600x1200")
# photo = PhotoImage(file="image1.png")

# For Jpg Images

image = Image.open("C:/Users/DELL/pythonProject/image.png")
photo = ImageTk.PhotoImage(image)

label0 = Label(image=photo)
label0.grid(row=0,column = 0)

Label1 = Label(f1, text="Load lying perpendicular to the plane of Groove Joint", font="comicsansms 13 bold").grid(row=0, column=6)

#Text for our form
Force1 = Label(f1, text="Force  (KN)")
eccentricity1 = Label(f1, text="eccentricity  (mm)")
depth1 = Label(f1, text="depth  (mm)")
throat_thickness1 = Label(f1, text="throat thickness  (mm)")


#Pack text for our form
Force1.grid(row=1, column=5)
eccentricity1.grid(row=2, column=5)
depth1.grid(row=3, column=5)
throat_thickness1.grid(row=4, column=5)

# Tkinter variable for storing entries
Force1 = StringVar()
eccentricity1 = StringVar()
depth1 = StringVar()
throat_thickness1 = StringVar()



#Entries for our form
forceentry1 = Entry(f1, textvariable=Force1)
eccentricityentry1 = Entry(f1, textvariable=eccentricity1)
depthentry1 = Entry(f1, textvariable=depth1)
throat_thicknessentry1 = Entry(f1, textvariable=throat_thickness1)


# Packing the Entries
forceentry1.grid(row=1, column=6)
eccentricityentry1.grid(row=2, column=6)
depthentry1.grid(row=3, column=6)
throat_thicknessentry1.grid(row=4, column=6)


e1 = Entry(f1,width = 40)
e1.grid(row=7, column=6,padx = 20)



def checkSafety1():
    e1.delete(0, END)
    P1 = float(forceentry1.get())
    E1 = float(eccentricity1.get())
    d1 = float(depth1.get())
    te1 = float(throat_thickness1.get())

    q1 = (P1*10*10*10)/(d1 * E1)
    fb1 = (6*P1*10*10*10*E1)/(te1*d1*d1)
    fe1 = m.sqrt(3*q1*q1+fb1*fb1)
    Rw1 = 189.37

    sa1 = StringVar()
    sa1.set("fb = " + str(fb1))

    sb1 = StringVar()
    sb1.set("Rw = " + str(Rw1))



    if(fe1 <= Rw1):
        e1.insert(0,"Safe")
    else:
        e1.insert(0,"Unsafe")

    Label(f1, font="comicsansms 13 bold", textvariable=sa1).grid(row=2, column=7)
    Label(f1, font="comicsansms 13 bold", textvariable=sb1).grid(row=3, column=7)

#Button & packing it and assigning it a command
Button(f1,text="Check Safety", command=checkSafety1).grid(row=7, column=5)

f1.grid(row=0,column=3)


#########################################################################################################################################

f2 = Frame(root)

Label2 = Label(f2, text="Load lying perpendicular to the plane of Fillet Joint", font="comicsansms 13 bold").grid(row=0, column=6)
#0,6

#Text for our form
Force2 = Label(f2, text="Force  (KN)")
eccentricity2 = Label(f2, text="eccentricity  (mm)")
depth2 = Label(f2, text="depth  (mm)")
throat_thickness2 = Label(f2, text="throat thickness  (mm)")


#Pack text for our form
Force2.grid(row=1, column=5)
eccentricity2.grid(row=2, column=5)
depth2.grid(row=3, column=5)
throat_thickness2.grid(row=4, column=5)

# Tkinter variable for storing entries
Force2 = StringVar()
eccentricity2 = StringVar()
depth2 = StringVar()
throat_thickness2 = StringVar()



#Entries for our form
forceentry2 = Entry(f2, textvariable=Force2)
eccentricityentry2 = Entry(f2, textvariable=eccentricity2)
depthentry2= Entry(f2, textvariable=depth2)
throat_thicknessentry2 = Entry(f2, textvariable=throat_thickness2)


# Packing the Entries
forceentry2.grid(row=1, column=6)
eccentricityentry2.grid(row=2, column=6)
depthentry2.grid(row=3, column=6)
throat_thicknessentry2.grid(row=4, column=6)

e2 = Entry(f2,width = 40)
e2.grid(row=7, column=6,padx = 20)



def checkSafety2():
    e2.delete(0,END)
    P2 = float(forceentry2.get())
    E2 = float(eccentricity2.get())
    d2 = float(depth2.get())
    te2 = float(throat_thickness2.get())

    q2 = (P2*10*10*10)/(2* d2 * E2)
    fb2 = (3*P2*10*10*10*E2)/(te2*d2*d2)
    fe2 = m.sqrt(q2*q2+fb2*fb2)
    Rw2 = 189.37

    sa2 = StringVar()
    sa2.set("fb = " + str(fb2))

    sb2 = StringVar()
    sb2.set("Rw = " + str(Rw2))

# def find():
#     P2 = float(forceentry2.get())
#     E2 = float(eccentricity2.get())
#     d2 = float(depth2.get())
#
#     k = m.sqrt((1/189.37)*((P2*P2*10*10*10*10*10*10)/(1.414*d2*d2))*(1 + (36*E2*E2)/(d2*d2)))
#     print(k)
#     # throat_thickness2.insert(0,k)


    if(fe2 <= Rw2):
        e2.insert(0,"Safe")
    else:
        e2.insert(0,"Unsafe")
    print(fb2)
    Label(f2, font="comicsansms 13 bold", textvariable=sa2).grid(row=2, column=7)
    Label(f2, font="comicsansms 13 bold", textvariable=sb2).grid(row=3, column=7)

#Button & packing it and assigning it a command
Button(f2,text="Check Safety", command=checkSafety2).grid(row=7, column=5)

f2.grid(row=3,column=3)



root.mainloop()
