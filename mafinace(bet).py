from tkinter import *
from tkinter import ttk

Mafin = Tk()
Mafin.title('Mafinace')
Mafin.geometry('500x500')

###########################################33
tab = ttk.Notebook(Mafin)
tab.pack(fill=BOTH,expand=1)

F1 = Frame(tab)
F2 = Frame(tab)
F3 = Frame(tab)
F4 = Frame(tab)
F5 = Frame(tab)
F6 = Frame(tab)

tab.add(F1,text='รายรับรายจ่าย')
tab.add(F2,text='ค่าน้ำค่าไฟ')
tab.add(F3,text='เกณฑ์รายจ่าย')
tab.add(F4,text='แผนภูมิ')
tab.add(F5,text='ธนาคาร')
tab.add(F6,text='สถานการณ์การเงิน')

##################################################
#def save():


#####################F1##########################
income = Frame(F1)
expenses = Frame(F1)
excel = Frame(F1)

income.place(x=30,y=50)
expenses.place(x=300,y=50)
excel.place(x=230,y=300)

#################################
list1=StringVar()
category1=StringVar()
mon1=DoubleVar()

le1 = Label(income,text='รายกาาร')
le1.pack()
en1 = Entry(income,textvariable=list1)
en1.pack()
le2 = Label(income,text='ประเภท')
le2.pack()
en2 = Entry(income,textvariable=category1)
en2.pack()
le3 = Label(income,text='จำนวนเงิน')
le3.pack()
en3 = Entry(income,textvariable=mon1)
en3.pack()
save1 = Button(income,text='บันทึก')
save1.pack()

##################################
list2=StringVar()
category2=StringVar()
mon2=DoubleVar()

le21 = Label(expenses,text='รายกาาร')
le21.pack()
en21 = Entry(expenses,textvariable=list2)
en21.pack()
le22 = Label(expenses,text='ประเภท')
le22.pack()
en22 = Entry(expenses,textvariable=category2)
en22.pack()
le23 = Label(expenses,text='จำนวนเงิน')
le23.pack()
en23 = Entry(expenses,textvariable=mon2)
en23.pack()
save2 = Button(expenses,text='บันทึก')
save2.pack()

##############F2#################
tab1 = ttk.Notebook(F2)
tab1.pack(fill=BOTH,expand=1)

mitor = Frame(tab1)
mitor.pack()

tab1.add(mitor,text='กรอกค่าน้ำค่าไฟ')

date1=StringVar()
unit1=DoubleVar()

le1 = Label(mitor,text='ยูนิทน้ำ')
le1.pack()
le2 = Label(mitor,text='วันที่')
le2.pack()
en2 = Entry(mitor,textvariable=date1)
en2.pack()
le3 = Label(mitor,text='หน่วย')
le3.pack()
en3 = Entry(mitor,textvariable=unit1)
en3.pack()
save11 = Button(mitor,text='บันทึก')
save11.pack()

le21 = Label(mitor,text='ยูนิทไฟ')
le21.pack()
le22 = Label(mitor,text='วันที่')
le22.pack()
en22 = Entry(mitor,textvariable=date1)
en22.pack()
le32 = Label(mitor,text='หน่วย')
le32.pack()
en32 = Entry(mitor,textvariable=unit1)
en32.pack()
save12 = Button(mitor,text='บันทึก')
save12.pack()

Mafin.mainloop() 