from tkinter import *
import math as m
from PIL import Image, ImageTk



def show_frame(frame):
    frame.tkraise()

root0 = Tk()
root0.state('zoomed')
# root0.geometry("1200x1200")
root0.title("Aditya Raj | 18CE10003")

root = Frame(root0)

# For Jpg Images

image = Image.open("C:/Users/DELL/pythonProject/image.png")
photo = ImageTk.PhotoImage(image)

label0 = Label(root,image=photo)
label0.grid(row=0,column = 0)


f1 = Frame(root)


Label1 = Label(f1, text="Load lying perpendicular to the plane of Groove Joint", font="comicsansms 13 bold").grid(row=0, column=6,pady = 15)


#Text for our form
Force1 = Label(f1, text="Force  (P) KN")
eccentricity1 = Label(f1, text="eccentricity  (e)  mm")
depth1 = Label(f1, text="depth  (d)  mm")
FactorofSafety1 = Label(f1, text="Partial Factor of Safety  (γm0)")
Grade1 = Label(f1, text="yield stress of weld  (fy)  MPa")
throat_thickness1 = Label(f1, text="effective throat thickness  (te)  mm")


#Pack text for our form
Force1.grid(row=1, column=5)
eccentricity1.grid(row=2, column=5)
depth1.grid(row=3, column=5)
FactorofSafety1.grid(row=4, column=5)
Grade1.grid(row=5, column=5)
throat_thickness1.grid(row=6, column=5)


# Tkinter variable for storing entries
Force1 = StringVar()
eccentricity1 = StringVar()
depth1 = StringVar()
FactorofSafety1 = StringVar()
Grade1 = StringVar()
throat_thickness1 = StringVar()

#Entries for our form
forceentry1 = Entry(f1, textvariable=Force1,bd = 2)
eccentricityentry1 = Entry(f1, textvariable=eccentricity1,bd = 2)
depthentry1 = Entry(f1, textvariable=depth1,bd = 2)
FactorofSafetyentry1 = Entry(f1, textvariable=FactorofSafety1,bd = 2)
Gradeentry1 = Entry(f1, textvariable=Grade1,bd = 2)
throat_thicknessentry1 = Entry(f1, textvariable=throat_thickness1,bd = 2)


# Packing the Entries
forceentry1.grid(row=1, column=6,pady=2)
eccentricityentry1.grid(row=2, column=6,pady=2)
depthentry1.grid(row=3, column=6,pady=2)
FactorofSafetyentry1.grid(row=4, column=6,pady=2)
Gradeentry1.grid(row=5, column=6,pady=2)
throat_thicknessentry1.grid(row=6, column=6,pady=2)

e1 = Entry(f1,width = 40,bd=2)
e1.grid(row=7, column=6,padx = 20,pady=2)



def checkSafety1():

    e1.delete(0, END)
    P1 = float(forceentry1.get())
    E1 = float(eccentricity1.get())
    d1 = float(depth1.get())
    te1 = float(throat_thickness1.get())

    q1 = (P1*10*10*10)/(d1 * E1)
    fb1 = round((6*P1*10*10*10*E1)/(te1*d1*d1), 3)
    fe1 = m.sqrt(3*q1*q1+fb1*fb1)
    Rw1 = round((float(Gradeentry1.get()) / (float(FactorofSafetyentry1.get()))), 3)
    # print(Rw1)

    # print(Rw1)
    sa1 = StringVar()
    sa1.set("fb = " + str(fb1) + " MPa")

    sb1 = StringVar()
    sb1.set("Rw = " + str(Rw1) + " MPa")



    if(fe1 <= Rw1):
        e1.insert(0,"The joint is Safe")
    else:
        e1.insert(0,"The joint is Unsafe")

    Label(f1, font="comicsansms 13 bold", textvariable=sa1).grid(row=2, column=7)
    Label(f1, font="comicsansms 13 bold", textvariable=sb1).grid(row=3, column=7)

#Button & packing it and assigning it a command
Button(f1,text="Check Safety", command=checkSafety1).grid(row=7, column=5)

f1.grid(row=0,column=3)


#########################################################################################################################################

f2 = Frame(root)

Label2 = Label(f2, text="Load lying perpendicular to the plane of Fillet Joint", font="comicsansms 13 bold").grid(row=0, column=6,pady = 15)
#0,6

#Text for our form
Force2 = Label(f2, text="Force  (P)  KN")
eccentricity2 = Label(f2, text="eccentricity  (e)  mm")
depth2 = Label(f2, text="depth  (d)  mm")
FactorofSafety2 = Label(f2, text="Partial Factor of Safety  (γmw)")
Grade2 = Label(f2, text="ultimate stress of weld  (fu)  MPa")
throat_thickness2 = Label(f2, text="effective throat thickness  (te)  mm")


#Pack text for our form
Force2.grid(row=1, column=5)
eccentricity2.grid(row=2, column=5)
depth2.grid(row=3, column=5)
FactorofSafety2.grid(row=4,column=5)
Grade2.grid(row=5,column=5)
throat_thickness2.grid(row=6, column=5)


# Tkinter variable for storing entries
Force2 = StringVar()
eccentricity2 = StringVar()
depth2 = StringVar()
FactorofSafetyentry2 = StringVar()
Gradeentry2 = StringVar()


#Entries for our form
forceentry2 = Entry(f2, textvariable=Force2,bd = 2)
eccentricityentry2 = Entry(f2, textvariable=eccentricity2,bd = 2)
depthentry2= Entry(f2, textvariable=depth2,bd = 2)
FactorofSafetyentry2 = Entry(f2, textvariable=FactorofSafety2,bd = 2)
Gradeentry2 = Entry(f2, textvariable=Grade2,bd = 2)


# Packing the Entries
forceentry2.grid(row=1, column=6,pady=2)
eccentricityentry2.grid(row=2, column=6,pady=2)
depthentry2.grid(row=3, column=6,pady=2)
FactorofSafetyentry2.grid(row=4, column=6,pady=2)
Gradeentry2.grid(row=5, column=6,pady=2)


e2 = Entry(f2,width = 40,bd=2)
e2.grid(row=7, column=6,padx = 20,pady=2)

throat_thicknessentry2 = Entry(f2,bd = 2)
throat_thicknessentry2.grid(row=6, column=6,pady=2)

def checkSafety2():

    e2.delete(0,END)
    P2 = float(forceentry2.get())
    E2 = float(eccentricity2.get())
    d2 = float(depth2.get())
    te2 = float(throat_thicknessentry2.get())

    q2 = (P2*10*10*10)/(2* d2 * E2)
    fb2 = round((3*P2*10*10*10*E2)/(te2*d2*d2), 3)
    fe2 = m.sqrt(q2*q2+fb2*fb2)
    Rw2 = round((float(Gradeentry2.get()) / (1.73205080 * float(FactorofSafetyentry2.get()))), 3)


    sa2 = StringVar()
    sa2.set("fb = " + str(fb2) + " MPa")

    sb2 = StringVar()
    sb2.set("Rw = " + str(Rw2) + " MPa")

    if(fe2 <= Rw2):
        e2.insert(0,"The Joint is Safe")
    else:
        e2.insert(0,"The Joint is Unsafe")

    Label(f2, font="comicsansms 13 bold", textvariable=sa2).grid(row=2, column=7)
    Label(f2, font="comicsansms 13 bold", textvariable=sb2).grid(row=3, column=7)


def find():
    e2.delete(0,END)
    if(len(str(throat_thicknessentry2.get())) > 0):
        checkSafety2()
    else:

        P2 = float(forceentry2.get())
        E2 = float(eccentricity2.get())
        d2 = float(depth2.get())
        Rw2 = round((float(Gradeentry2.get()) / (1.73205080 * float(FactorofSafetyentry2.get()))), 3)

        k = round(m.sqrt((pow((3*P2*1000*E2)/(d2*d2),2) + pow((P2*1000)/(2*d2) ,2)) / (pow(Rw2,2))), 3)

        throat_thicknessentry2.insert(0,k)

        e2.insert(0, "The throat thickness should be greater than " + str(k) + "mm")


#Button & packing it and assigning it a command
Button(f2,text="Safety / Throat Thickness", command=find).grid(row=7, column=5)

f2.grid(row=3,column=3)

Label3 = Label(root, text="In Fillet Joint, if user wants to calculate : \n\n Just Safety : the throat thickness must be entered \n\n Throat thickness for safe joint : throat thickness entry should be left blank" , font="comicsansms 8 bold").grid(row=3, column =0)

root.pack()

root0.mainloop()
