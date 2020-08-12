from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()

GUI.title('ชื่อ')
GUI.geometry('400x300')

FONT=('TH SarabunPSK',15)

############################################
def add1():
	messagebox.showinfo('การบวก','a + b = ?')
def add2():
	messagebox.showinfo('การลบ','a - b = ?')
def add3():
	messagebox.showinfo('การคูณ','a x b = ?')
def add4():
	messagebox.showinfo('การหาร','a / b = ?')
##################################################
def plus():
	ta = valuel.get()
	sa = valuel2.get()
	res = ta + sa 
	r.set(f'ผลบวก = {res:,d}')
def min():
	a = valuel3.get()
	b = valuel4.get()
	res2 = a - b 
	r3.set(f'ผลต่าง = {res2:,d}')
def x():
	a2 = valuel5.get()
	b2 = valuel6.get()
	res3 = a2 * b2 
	r4.set(f'ผลคูณ = {res3:,d}')
def h():
	a3 = val.get()
	b3 = valuel8.get()
	res4 = a3 / b3 
	r5.set(f'ผลหาร = {res4:,.2f}')
def cir():
	R = valuel9.get()
	pt = 3.14*(R**2)
	r2.set(f'พื้นที่วงกลม= {pt:,.2f}')

####################################
Tap = ttk.Notebook(GUI)

f1 = Frame(Tap)
f2 = Frame(Tap)
f3 = Frame(Tap)
f4 = Frame(Tap)
f5 = Frame(Tap)

Tap.pack(fill=BOTH,expand=1)
Tap.add(f1,text='บวก')
Tap.add(f3,text='ลบ')
Tap.add(f4,text='คูณ')
Tap.add(f5,text='หาร')
Tap.add(f2,text='พื้นที่วงกลม')
###################################
def gui2():
	GUI2 = Toplevel()
	GUI2.title('note')
	GUI2.geometry('400x400')

	L1=Label(GUI2,text='ดีจ้า',font=FONT)
	L1.pack()

	notes=StringVar()

	E = Entry(GUI2,textvariable=notes,font=FONT,width=50)
	E.pack()


	GUI.mainloop()

####################################
menubar =Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='note',command=gui2)
file.add_command(label='close',command=GUI.quit)
menubar.add_cascade(label='File',menu=file)

cal = Menu(menubar,tearoff=0)
cal.add_command(label='บวก',command=add1)
cal.add_command(label='ลบ',command=add2)
cal.add_command(label='คูณ',command=add3)
cal.add_command(label='หาร',command=add4)
menubar.add_cascade(label='คำแนะนำ',menu=cal)
###################บวก#########################
valuel = IntVar()
valuel2 = IntVar()
r =IntVar()
r.set('---------ผลลัพธ์---------')

l = Label(f1,text='a',font=FONT)
l.pack()

E1 = ttk.Entry(f1,textvariable=valuel,font=FONT)
E1.pack(pady=10)

l = Label(f1,text='b',font=FONT)
l.pack()

E2 = ttk.Entry(f1,textvariable=valuel2,font=FONT)
E2.pack(pady=10)

B1=ttk.Button(f1,text='บวก',command=plus)
B1.pack(pady=10)

Lr = Label(f1,textvariabl=r,foreground='red',font=FONT)
Lr.pack(pady=20)
###################ลบ#########################
valuel3 = IntVar()
valuel4 = IntVar()
r3 =IntVar()
r3.set('---------ผลลัพธ์---------')

l = Label(f3,text='a',font=FONT)
l.pack()

E1 = ttk.Entry(f3,textvariable=valuel3,font=FONT)
E1.pack(pady=10)

l = Label(f3,text='b',font=FONT)
l.pack()

E2 = ttk.Entry(f3,textvariable=valuel4,font=FONT)
E2.pack(pady=10)

B1=ttk.Button(f3,text='ลบ',command=min)
B1.pack(pady=10)

Lr = Label(f3,textvariabl=r3,foreground='red',font=FONT)
Lr.pack(pady=20)
###################คูณ#########################
valuel5 = IntVar()
valuel6 = IntVar()
r4 =IntVar()
r4.set('---------ผลลัพธ์---------')

l = Label(f4,text='a',font=FONT)
l.pack()

E1 = ttk.Entry(f4,textvariable=valuel5,font=FONT)
E1.pack(pady=10)

l = Label(f4,text='b',font=FONT)
l.pack()

E2 = ttk.Entry(f4,textvariable=valuel6,font=FONT)
E2.pack(pady=10)

B1=ttk.Button(f4,text='คูณ',command=x)
B1.pack(pady=10)

Lr = Label(f4,textvariabl=r4,foreground='red',font=FONT)
Lr.pack(pady=20)
###################หาร#########################
val = DoubleVar()
valuel8 = DoubleVar()
r5 =DoubleVar()
r5.set('---------ผลลัพธ์---------')

l = Label(f5,text='a',font=FONT)
l.pack()

E1 = ttk.Entry(f5,textvariable=val,font=FONT)
E1.pack(pady=10)

l = Label(f5,text='b',font=FONT)
l.pack()

E2 = ttk.Entry(f5,textvariable=valuel8,font=FONT)
E2.pack(pady=10)

B1=ttk.Button(f5,text='หาร',command=h)
B1.pack(pady=10)

Lr = Label(f5,textvariabl=r5,foreground='red',font=FONT)
Lr.pack(pady=20)
##################พท.วงกลม#######################
valuel9 = DoubleVar()
r2 =DoubleVar()
r2.set('---------ผลลัพธ์---------')

l = Label(f2,text='รัศมี',font=FONT)
l.pack(pady=10)

E3 = ttk.Entry(f2,textvariable=valuel9,font=FONT)
E3.pack(anchor=S)

B2=ttk.Button(f2,text='กดสิ',command=cir)
B2.pack(pady=20)

Lr2 = Label(f2,textvariabl=r2,foreground='red',font=FONT)
Lr2.pack()
##############################################

GUI.mainloop()
