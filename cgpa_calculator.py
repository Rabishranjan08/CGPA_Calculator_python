# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 22:59:06 2018

@author: dell
"""

import sqlite3
from tkinter import *
from tkinter import messagebox


db=sqlite3.connect("calculator.db")

c=db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS demo20(firstname,lastname,registration,tgpa_1,tgpa_2,cgpa_1,rem)')
print("table has been created")
def fun():

    d=c.execute("SELECT * FROM demo20")
    data = d.fetchall()
    print(data)
    history = Tk()
    history.title('History')

    lstbox = Listbox(history, width=80, height=20)
    lstbox.pack()

    for i in range(len(data)):
        a = data[i]

        lstbox.insert(END, i+1)
        lstbox.insert(END, 'First Name :: ' + a[0])
        lstbox.insert(END, 'Last Name  :: ' + a[1])
        lstbox.insert(END, 'Reg No.    :: ' + a[2])
        lstbox.insert(END, 'TGPA 1     :: ' + a[3])
        lstbox.insert(END, 'TGPA 2     :: ' + a[4])
        lstbox.insert(END, 'CGPA       :: ' + a[5])
        lstbox.insert(END, 'Remarks    :: ' + a[6])
        lstbox.insert(END, '\n\n')


def convert(v = 'A'):
    if v == 'O' or v == 'o':
        v = 10
    elif v == 'A' or v == 'a':
        v = 9
    elif v=='B' or v=='b':
        v = 8
    elif v=='C' or v=='c':
        v=7
    elif v=='D' or v=='d':
        v=6
    else:
        v=5
        
    return v


"""function to calculate the tgpa"""

def calculator():
    global sg1,sg2,sg3,sg4,sg5,sg6
    sg1 = s1.get()
    sg2 = s2.get()
    sg3 = s3.get()
    sg4 = s4.get()
    sg5 = s5.get()
    sg6 = s6.get()
    
    sg1= convert(sg1)
    sg2= convert(sg2)
    sg3= convert(sg3)
    sg4= convert(sg4)
    sg5= convert(sg5)
    sg6= convert(sg6)
     
def caltgpa_1():
    calculator()
    cd1=int(c1.get())
    cd2=int(c2.get())
    cd3=int(c3.get())
    cd4=int(c4.get())
    cd5=int(c5.get())
    cd6=int(c6.get())
    global tgpa_1
    if((sg1)!="") and ((sg2)!="") and ((sg3)!="") and ((sg4)!="") and ((sg5)!="") and ((sg6)!="") and ((cd1)!="") and ((cd2)!="") and ((cd3)!="") and ((cd4)!="") and ((cd5)!="") and ((cd6)!=""):
        tgpa_1=((sg1*cd1)+(sg2*cd2)+(sg3*cd3)+(sg4*cd4)+(sg5*cd5)+(sg6*cd6))/(cd1+cd2+cd3+cd4+cd5+cd6)
        l.insert(END,tgpa_1)
    else :
        messagebox.showinfo("Warning", "please fill all the entries")
def calculator1():
    global sg7,sg8,sg9,sg10,sg11,sg12
    sg7 = n1.get()
    sg8 = n2.get()
    sg9 = n3.get()
    sg10 = n4.get()
    sg11 = n5.get()
    sg12 = n6.get()
    
    sg7= convert(sg7)
    sg8= convert(sg8)
    sg9= convert(sg9)
    sg10= convert(sg10)
    sg11= convert(sg11)
    sg12= convert(sg12)
    
def caltgpa_2():
    calculator1()
    cd7=int(d1.get())
    cd8=int(d2.get())
    cd9=int(d3.get())
    cd10=int(d4.get())
    cd11=int(d5.get())
    cd12=int(d6.get())
    global tgpa_2
    if(str(n1.get())!="") and (str(n2.get())!="") and (str(n3.get())!="") and (str(n4.get())!="") and (str(n5.get())!="") and (str(n6.get())!="") and (str(d1.get())!="") and (str(d2.get())!="") and (str(d3.get())!="") and (str(d4.get())!="") and (str(d5.get())!="") and (str(d6.get())!=""):
        tgpa_2=((sg7*cd7)+(sg8*cd8)+(sg9*cd9)+(sg10*cd10)+(sg11*cd11)+(sg12*cd12))/(cd7+cd8+cd9+cd10+cd11+cd12)
        l_1.insert(END,tgpa_2)
    else :
        messagebox.showinfo("Warning", "please fill all the entries")


def calcgpa_1():
    global cgpa_1
    cgpa_1=(tgpa_1+tgpa_2)/2
    l_2.insert(END,cgpa_1)

    global rem
    if (str(cgpa_1) == "10"):
        rem = "O"
    elif (str(cgpa_1) >= "9"or str(cgpa_1)<"10"):
        rem = "A+"
    elif (str(cgpa_1) >= "8" or str(cgpa_1)<"9"):
        rem = "A"
    elif (str(cgpa_1) >= "7"or str(cgpa_1)<"8"):
        rem = "B"
    elif (str(cgpa_1) >= "6" or str(cgpa_1)<"7"):
        rem = "c"
    elif (str(cgpa_1) >= "5" or str(cgpa_1)<"6"):
        rem = "D"
    else:
        rem = "F"


    print('data to insert', e1.get(), e2.get(), e3.get())
    c.execute("INSERT INTO demo20 VALUES(?,?,?,?,?,?,?)", (e1.get(), e2.get(), e3.get(), str(tgpa_1), str(tgpa_2), str(cgpa_1), str(rem)))
    db.commit()


def rem_1():
    l_3.insert(END,rem)
    
        
class ABC:
    def __init__(self):
        window = Tk()
        window.title('KNOW YOUR CGPA')

        frame0 = Frame(window)
        frame0.pack()
        Label(frame0, text='CGPA CALCULATOR', bg='black', fg='white',font=('bold',20),padx=154).pack()

        frame1 = Frame(window, bd=4, relief=RAISED, bg='lightgrey',padx=78)
        frame1.pack()
        global e1,e2,e3
        Label(frame1, text='DETAILS:-', justify=LEFT,fg="white",bg='black',font=('bold',15)).grid(row=1, column=1, sticky=W)
        Label(frame1, text='First Name:', justify=LEFT, bg='lightgrey').grid(row=2, column=1, sticky=W)
        e1=Entry(frame1)
        e1.grid(row=2, column=2, sticky=W)

        Label(frame1, text='Last Name:', justify=LEFT, bg='lightgrey').grid(row=2, column=3, sticky=E)
        e2=Entry(frame1)
        e2.grid(row=2, column=4, sticky=E)
        Label(frame1, text='Regestration no.:', justify=LEFT, bg='lightgrey').grid(row=3, column=1, sticky=W)
        e3=Entry(frame1)
        e3.grid(row=3, column=2,sticky=W)

        frame2 = Frame(window, bd=4, relief=RAISED, bg='grey',padx=20)
        frame2.pack()
       







        Label(frame2, text='SEMESTER 1:-', bg='black', fg='white',font=('bold',15),justify=LEFT).grid(row=4, column=1,sticky=E)
        Label(frame2,text="GRADES",bd=1,fg="white",bg="black").grid(row=5,column=3)
        Label(frame2,text="Subject 1",justify=LEFT,fg="black",bg="grey").grid(row=6,column=1)
        Label(frame2,text="Subject 2",justify=LEFT,fg="black",bg="grey").grid(row=7,column=1)
        Label(frame2,text="Subject 3",justify=LEFT,fg="black",bg="grey").grid(row=8,column=1)
        Label(frame2,text="Subject 4",justify=LEFT,fg="black",bg="grey").grid(row=9,column=1)
        Label(frame2,text="Subject 5",justify=LEFT,fg="black",bg="grey").grid(row=10,column=1)
        Label(frame2,text="Subject 6",justify=LEFT,fg="black",bg="grey").grid(row=11,column=1)
        global s1,s2,s3,s4,s5,s6
        s1=Entry(frame2)
        s1.grid(row=6,column=3)
        s2=Entry(frame2)
        s2.grid(row=7,column=3)
        s3=Entry(frame2)
        s3.grid(row=8,column=3)
        s4=Entry(frame2)
        s4.grid(row=9,column=3)
        s5=Entry(frame2)
        s5.grid(row=10,column=3)
        s6=Entry(frame2)
        s6.grid(row=11,column=3)


        Label(frame2,text="CREDIT",bd=1,fg="white",bg="black").grid(row=5,column=4)
        global c1,c2,c3,c4,c5,c6
        c1=Entry(frame2)
        c1.grid(row=6,column=4)
        c2=Entry(frame2)
        c2.grid(row=7,column=4)
        c3=Entry(frame2)
        c3.grid(row=8,column=4)
        c4=Entry(frame2)
        c4.grid(row=9,column=4)
        c5=Entry(frame2)
        c5.grid(row=10,column=4)
        c6=Entry(frame2)
        c6.grid(row=11,column=4)

        Label(frame2,text='TGPA',fg='white',bg='black',font=('bold',11)).grid(row=9,column=17)
        global l
        l=Listbox(frame2,height=1,width=15)
        l.grid(row=9,column=18)

        b1=Button(frame2,text="CALCULATE TGPA",bg="black",fg="white",command=caltgpa_1)
        b1.grid(row=15,columnspan=2)

        frame3 = Frame(window, bd=4, relief=RAISED, bg='grey',padx=20)
        frame3.pack()

       
        Label(frame3, text='SEMESTER 2:-', bg='black', fg='white',font=('bold',15),justify=LEFT).grid(row=17, column=1,sticky=E)
        Label(frame3,text="GRADES",bd=1,fg="white",bg="black").grid(row=18,column=3)
        Label(frame3,text="Subject 1",justify=LEFT,fg="black",bg="grey").grid(row=19,column=1)
        Label(frame3,text="Subject 2",justify=LEFT,fg="black",bg="grey").grid(row=20,column=1)
        Label(frame3,text="Subject 3",justify=LEFT,fg="black",bg="grey").grid(row=21,column=1)
        Label(frame3,text="Subject 4",justify=LEFT,fg="black",bg="grey").grid(row=22,column=1)
        Label(frame3,text="Subject 5",justify=LEFT,fg="black",bg="grey").grid(row=23,column=1)
        Label(frame3,text="Subject 6",justify=LEFT,fg="black",bg="grey").grid(row=24,column=1)
        global n1,n2,n3,n4,n5,n6
        n1=Entry(frame3)
        n1.grid(row=19,column=3)
        n2=Entry(frame3)
        n2.grid(row=20,column=3)
        n3=Entry(frame3)
        n3.grid(row=21,column=3)
        n4=Entry(frame3)
        n4.grid(row=22,column=3)
        n5=Entry(frame3)
        n5.grid(row=23,column=3)
        n6=Entry(frame3)
        n6.grid(row=24,column=3)
        
        Label(frame3,text="CREDIT",bd=1,fg="white",bg="black").grid(row=18,column=4)
        global d1,d2,d3,d4,d5,d6
        d1=Entry(frame3)
        d1.grid(row=19,column=4)
        d2=Entry(frame3)
        d2.grid(row=20,column=4)
        d3=Entry(frame3)
        d3.grid(row=21,column=4)
        d4=Entry(frame3)
        d4.grid(row=22,column=4)
        d5=Entry(frame3)
        d5.grid(row=23,column=4)
        d6=Entry(frame3)
        d6.grid(row=24,column=4)

        Label(frame3,text='TGPA',fg='white',bg='black',font=('bold',11)).grid(row=22,column=17)
        global l_1
        l_1=Listbox(frame3,height=1,width=15)
        l_1.grid(row=22,column=18)

        b2=Button(frame3,text="CALCULATE TGPA",bg="black",fg="white",command=caltgpa_2)
        b2.grid(row=29,columnspan=2)


        frame4 = Frame(window, bd=4, relief=RAISED, bg='lightgrey',padx=196)
        frame4.pack()
        b3=Button(frame4,text='CGPA',fg='white',bg='black',font=('bold',11),padx=15,command=calcgpa_1).grid(row=35,column=3)
        b4=Button(frame4,text='REMARKS',fg='white',bg='black',font=('bold',11),command=rem_1).grid(row=38,column=3)
        b5=Button(frame4,text="HISTORY",fg='white',bg='black',font=('bold',11),command=fun)
        b5.grid(row=39,column=4)
        global l_2
        l_2=Listbox(frame4,height=1,width=15)
        l_2.grid(row=35,column=4)
        global l_3
        l_3=Listbox(frame4,height=1,width=15)
        l_3.grid(row=38,column=4)



        window.mainloop()


ABC()
