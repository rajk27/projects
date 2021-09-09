from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
import random
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "project"
    )
mycursor = mydb.cursor()

root = Tk()
root.title("LOGIN")
w_width = root.winfo_screenwidth()
w_height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w_width,w_height))

top_frame=Frame(root,height=100,bg="gray85",width=w_width,bd=5)
top_frame.pack(side="top",fill="both")

lb=Label(top_frame,text="LOGIN",font=("arial",30,"bold"),fg="black",bg="gray85")
lb.pack(side="top",anchor="center")

login_frame = Frame(root,height=470,width=450,bg="gray85")
login_frame.place(x=550,y=180)

###===========LOGIN INFO===========###
uname = StringVar()
password=StringVar()

lb = Label(login_frame,text="Username",font=("impact",18),bg="gray85")
lb.place(x=50,y=70)
u_entry=Entry(login_frame,width="20",textvariable = uname,relief="ridge",font=("arial",15,"bold"))
u_entry.place(x=170,y=70)

lb = Label(login_frame,text="Password",font=("impact",18),bg="gray85")
lb.place(x=50,y=150)
p_entry=Entry(login_frame,show="*",width="20",textvariable=password,relief="ridge",font=("arial",15,"bold"))
p_entry.place(x=170,y=150)
###===========LOGIN INFO===========###

def student_list():
    wind = Tk()
    w_width = wind.winfo_screenwidth()
    w_height = wind.winfo_screenheight()
    wind.geometry("%dx%d+0+0"%(w_width,w_height))
    wind.title("STUDENTS")

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students WHERE Roll_no LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind)

    wrapper2 = LabelFrame(wind,text = "Search",height="100")
    wrapper1 = LabelFrame(wind,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="30")
    trv.pack()

    #trv.bind("<Double-1>",enter_result_4)
    
    trv.column("1", width = 100, anchor ='c')
    trv.column("2", width = 150, anchor ='sw')
    trv.column("3", width = 100, anchor ='c')
    trv.column("4", width = 200, anchor ='c')
    trv.column("5", width = 100, anchor ='c')
    trv.column("6", width = 100, anchor ='c')
    trv.column("7", width = 100, anchor ='c')
    trv.column("8", width = 100, anchor ='c')
    trv.column("9", width = 100, anchor ='c')
            
    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="Email")
    trv.heading("5", text ="Username")
    trv.heading("6", text ="Password")
    trv.heading("7", text ="Course")
    trv.heading("8", text ="Branch")
    trv.heading("9", text ="Semester")
                
    query ="select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

    ###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

def view_result_1():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,URN,btac_101,btam_101,btcs_101,btcs_102,btme_101,btme_102,mst1_btac_101,mst1_btam_101,mst1_btcs_101,mst1_btme_102,mst2_btac_101,mst2_btam_101,mst2_btcs_101,mst2_btme_102,mst3_btac_101,mst3_btam_101,mst3_btcs_101,mst3_btme_102,sgpa from sem_1 WHERE URN LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,URN,btac_101,btam_101,btcs_101,btcs_102,btme_101,btme_102,mst1_btac_101,mst1_btam_101,mst1_btcs_101,mst1_btme_102,mst2_btac_101,mst2_btam_101,mst2_btcs_101,mst2_btme_102,mst3_btac_101,mst3_btam_101,mst3_btcs_101,mst3_btme_102,sgpa from sem_1"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')


    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTAC-18101")
    trv.heading("5", text ="BTAM-18101")
    trv.heading("6", text ="BTCS-18101")
    trv.heading("7", text ="BTCS-18102")
    trv.heading("8", text ="BTME-18101")
    trv.heading("9", text ="BTME-18102")
    trv.heading("10", text ="MST-1_BTAC-101")
    trv.heading("11", text ="MST-1_BTAM-101")
    trv.heading("12", text ="MST-1_BTCS-101")
    trv.heading("13", text ="MST-1_BTME-102")
    trv.heading("14", text ="MST-2_BTAC-101")
    trv.heading("15", text ="MST-2_BTAM-101")
    trv.heading("16", text ="MST-2_BTCS-101")
    trv.heading("17", text ="MST-2_BTME-102")
    trv.heading("18", text ="MST-3_BTAC-101")
    trv.heading("19", text ="MST-3_BTAM-101")
    trv.heading("20", text ="MST-3_BTCS-101")
    trv.heading("21", text ="MST-3_BTME-102")
    trv.heading("22", text ="SGPA")

    query ="select ID,Name,URN,btac_101,btam_101,btcs_101,btcs_102,btme_101,btme_102,mst1_btac_101,mst1_btam_101,mst1_btcs_101,mst1_btme_102,mst2_btac_101,mst2_btam_101,mst2_btcs_101,mst2_btme_102,mst3_btac_101,mst3_btam_101,mst3_btcs_101,mst3_btme_102,sgpa from sem_1"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

#================================================================================================================================================#

def view_result_2():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,name,rollno,,btph_101,btee_101,amcs_101,btph_102,btee_102,btme_101,mst1_btph_101,mst1_btee_101,mst1_amcs_101,mst1_btme_101,mst2_btph_101,mst2_btee_101,mst2_amcs_101,mst2_btme_101,mst3_btph_101,mst3_btee_101,mst3_amcs_101,mst3_btme_101,sgpa from sem_2 WHERE rollno LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,name,rollno,,btph_101,btee_101,amcs_101,btph_102,btee_102,btme_101,mst1_btph_101,mst1_btee_101,mst1_amcs_101,mst1_btme_101,mst2_btph_101,mst2_btee_101,mst2_amcs_101,mst2_btme_101,mst3_btph_101,mst3_btee_101,mst3_amcs_101,mst3_btme_101,sgpa from sem_2"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTPH-18101")
    trv.heading("5", text ="BTEE-18101")
    trv.heading("6", text ="AMCS-18101")
    trv.heading("7", text ="BTPH-18102")
    trv.heading("8", text ="BTEE-18102")
    trv.heading("9", text ="BTME-18101")
    trv.heading("10", text ="MST-1_BTPH-101")
    trv.heading("11", text ="MST-1_BTEE-101")
    trv.heading("12", text ="MST-1_AMCS-101")
    trv.heading("13", text ="MST-1_BTME-101")
    trv.heading("14", text ="MST-2_BTPH-101")
    trv.heading("15", text ="MST-2_BTEE-101")
    trv.heading("16", text ="MST-2_AMCS-101")
    trv.heading("17", text ="MST-2_BTME-101")
    trv.heading("18", text ="MST-3_BTPH-101")
    trv.heading("19", text ="MST-3_BTEE-101")
    trv.heading("20", text ="MST-3_AMCS-101")
    trv.heading("21", text ="MST-3_BTME-101")
    trv.heading("22", text ="SGPA")

    query ="select ID,name,rollno,btph_101,btee_101,amcs_101,btph_102,btee_102,btme_101,mst1_btph_101,mst1_btee_101,mst1_amcs_101,mst1_btme_101,mst2_btph_101,mst2_btee_101,mst2_amcs_101,mst2_btme_101,mst3_btph_101,mst3_btee_101,mst3_amcs_101,mst3_btme_101,sgpa from sem_2"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

#================================================================================================================================================#

def view_result_3():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,name,rollno,btcs_301,btcs_302,btcs_303,amcs_301,hsmc_301,btcs_304,btcs_305,btcs_306,btcs_307,mst1_btcs_301,mst1_btcs_302,mst1_btcs_303,mst1_amcs_301,mst1_hsmc_301,mst2_btcs_301,mst2_btcs_302,mst2_btcs_303,mst2_amcs_301,mst2_hsmc_301,mst3_btcs_301,mst3_btcs_302,mst3_btcs_303,mst3_amcs_301,mst3_hsmc_301,sgpa from sem_3 WHERE rollno LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,name,rollno,btcs_301,btcs_302,btcs_303,amcs_301,hsmc_301,btcs_304,btcs_305,btcs_306,btcs_307,mst1_btcs_301,mst1_btcs_302,mst1_btcs_303,mst1_amcs_301,mst1_hsmc_301,mst2_btcs_301,mst2_btcs_302,mst2_btcs_303,mst2_amcs_301,mst2_hsmc_301,mst3_btcs_301,mst3_btcs_302,mst3_btcs_303,mst3_amcs_301,mst3_hsmc_301,sgpa from sem_3"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')
    trv.column("28", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18301")
    trv.heading("5", text ="BTCS-18302")
    trv.heading("6", text ="BTCS-18303")
    trv.heading("7", text ="AMCS-18301")
    trv.heading("8", text ="HSMC-18301")
    trv.heading("9", text ="BTCS-18304")
    trv.heading("10", text ="BTCS-18305")
    trv.heading("11", text ="BTCS-18306")
    trv.heading("12", text ="BTCS-18307")
    trv.heading("13", text ="MST-1_BTCS-301")
    trv.heading("14", text ="MST-1_BTCS-302")
    trv.heading("15", text ="MST-1_BTCS-303")
    trv.heading("16", text ="MST-1_AMCS-301")
    trv.heading("17", text ="MST-1_HSMC-301")
    trv.heading("18", text ="MST-2_BTCS-301")
    trv.heading("19", text ="MST-2_BTCS-302")
    trv.heading("20", text ="MST-2_BTCS-303")
    trv.heading("21", text ="MST-2_AMCS-301")
    trv.heading("22", text ="MST-2_HSMC-301")
    trv.heading("23", text ="MST-3_BTCS-301")
    trv.heading("24", text ="MST-3_BTCS-302")
    trv.heading("25", text ="MST-3_BTCS-303")
    trv.heading("26", text ="MST-3_AMCS-301")
    trv.heading("27", text ="MST-3_HSMC-301")
    trv.heading("28", text ="SGPA")

    query ="select ID,name,rollno,btcs_301,btcs_302,btcs_303,amcs_301,hsmc_301,btcs_304,btcs_305,btcs_306,btcs_307,mst1_btcs_301,mst1_btcs_302,mst1_btcs_303,mst1_amcs_301,mst1_hsmc_301,mst2_btcs_301,mst2_btcs_302,mst2_btcs_303,mst2_amcs_301,mst2_hsmc_301,mst3_btcs_301,mst3_btcs_302,mst3_btcs_303,mst3_amcs_301,mst3_hsmc_301,sgpa from sem_3"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

#================================================================================================================================================#

def view_result_4():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,name,rollno,btcs_402,btcs_403,btcs_404,btam_401,bths_904,btcs_405,btcs_406,btcs_407,csmc,mst1_btcs_402,mst1_btcs_403,mst1_btcs_404,mst1_btam_401,mst1_bths_904,mst2_btcs_402,mst2_btcs_403,mst2_btcs_404,mst2_btam_401,mst2_bths_904,mst3_btcs_402,mst3_btcs_403,mst3_btcs_404,mst3_btam_401,mst3_bths_904,sgpa from sem_4 WHERE rollno LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,name,rollno,btcs_402,btcs_403,btcs_404,btam_401,bths_904,btcs_405,btcs_406,btcs_407,csmc,mst1_btcs_402,mst1_btcs_403,mst1_btcs_404,mst1_btam_401,mst1_bths_904,mst2_btcs_402,mst2_btcs_403,mst2_btcs_404,mst2_btam_401,mst2_bths_904,mst3_btcs_402,mst3_btcs_403,mst3_btcs_404,mst3_btam_401,mst3_bths_904,sgpa from sem_4"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')
    trv.column("28", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18402")
    trv.heading("5", text ="BTCS-18403")
    trv.heading("6", text ="BTCS-18404")
    trv.heading("7", text ="BTAM-18401")
    trv.heading("8", text ="BTHS-18904")
    trv.heading("9", text ="BTCS-18505")
    trv.heading("10", text ="BTCS-18506")
    trv.heading("11", text ="BTCS-18507")
    trv.heading("12", text ="CSMC")
    trv.heading("13", text ="MST-1_BTCS-402")
    trv.heading("14", text ="MST-1_BTCS-403")
    trv.heading("15", text ="MST-1_BTCS-404")
    trv.heading("16", text ="MST-1_BTAM-401")
    trv.heading("17", text ="MST-1_BTHS-904")
    trv.heading("18", text ="MST-2_BTCS-402")
    trv.heading("19", text ="MST-2_BTCS-403")
    trv.heading("20", text ="MST-2_BTCS-404")
    trv.heading("21", text ="MST-2_BTAM-401")
    trv.heading("22", text ="MST-2_BTHS-904")
    trv.heading("23", text ="MST-3_BTCS-402")
    trv.heading("24", text ="MST-3_BTCS-403")
    trv.heading("25", text ="MST-3_BTCS-404")
    trv.heading("26", text ="MST-3_BTAM-401")
    trv.heading("27", text ="MST-3_BTHS-904")
    trv.heading("28", text ="SGPA")

    query ="select ID,name,rollno,btcs_402,btcs_403,btcs_404,btam_401,bths_904,btcs_405,btcs_406,btcs_407,csmc,mst1_btcs_402,mst1_btcs_403,mst1_btcs_404,mst1_btam_401,mst1_bths_904,mst2_btcs_402,mst2_btcs_403,mst2_btcs_404,mst2_btam_401,mst2_bths_904,mst3_btcs_402,mst3_btcs_403,mst3_btcs_404,mst3_btam_401,mst3_bths_904,sgpa from sem_4"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#


#=============================================VIEW RESULT=============================================#

def view_result_5():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,name,rollno,branch,email,contact,sem,btcs_501,btcs_502,btcs_503,btcs_504,bths_905,btcs_505,btcs_506,btcs_507,csmc,mst1_btcs_501,mst1_btcs_502,mst1_btcs_503,mst1_btcs_504,mst1_bths_905,mst2_btcs_501,mst2_btcs_502,mst2_btcs_503,mst2_btcs_504,mst2_bths_905,mst3_btcs_501,mst3_btcs_502,mst3_btcs_503,mst3_btcs_504,mst3_bths_905,sgpa from sem_5 WHERE rollno LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,name,rollno,branch,email,contact,sem,btcs_501,btcs_502,btcs_503,btcs_504,bths_905,btcs_505,btcs_506,btcs_507,csmc,mst1_btcs_501,mst1_btcs_502,mst1_btcs_503,mst1_btcs_504,mst1_bths_905,mst2_btcs_501,mst2_btcs_502,mst2_btcs_503,mst2_btcs_504,mst2_bths_905,mst3_btcs_501,mst3_btcs_502,mst3_btcs_503,mst3_btcs_504,mst3_bths_905,sgpa from sem_5"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')
    trv.column("28", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18501")
    trv.heading("5", text ="BTCS-18502")
    trv.heading("6", text ="BTCS-18503")
    trv.heading("7", text ="BTCS-18504")
    trv.heading("8", text ="BTCS-18505")
    trv.heading("9", text ="BTCS-18506")
    trv.heading("10", text ="BTCS-18507")
    trv.heading("11", text ="BTCS-18508")
    trv.heading("12", text ="BTHS-18905")
    trv.heading("13", text ="MST-1_BTCS-502")
    trv.heading("14", text ="MST-1_BTCS-503")
    trv.heading("15", text ="MST-1_BTCS-504")
    trv.heading("16", text ="MST-1_BTCS-501")
    trv.heading("17", text ="MST-1_BTHS-905")
    trv.heading("18", text ="MST-2_BTCS-502")
    trv.heading("19", text ="MST-2_BTCS-503")
    trv.heading("20", text ="MST-2_BTCS-504")
    trv.heading("21", text ="MST-2_BTCS-501")
    trv.heading("22", text ="MST-2_BTHS-905")
    trv.heading("23", text ="MST-3_BTCS-502")
    trv.heading("24", text ="MST-3_BTCS-503")
    trv.heading("25", text ="MST-3_BTCS-504")
    trv.heading("26", text ="MST-3_BTCS-501")
    trv.heading("27", text ="MST-3_BTHS-905")
    trv.heading("28", text ="SGPA")

    query ="select ID,Name,URN,btcs_501,btcs_502,btcs_503,btcs_504,btcs_505,btcs_506,btcs_507,btcs_508,bths_905,mst1_btcs_502,mst1_btcs_503,mst1_btcs_504,mst1_btcs_501,mst1_bths_905,mst2_btcs_502,mst2_btcs_503,mst2_btcs_504,mst2_btcs_501,mst2_bths_905,mst3_btcs_502,mst3_btcs_503,mst3_btcs_504,mst3_btcs_501,mst3_bths_905,sgpa from sem_5"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)
###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

def view_result_6():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,URN,btcs_601,btcs_602,btcs_603,btcs_604,btcs_605,btcs_965,btcs_966,btcs_994,mst1_btcs_601,mst1_btcs_602,mst1_btcs_965,mst1_btcs_966,mst1_btcs_994,mst2_btcs_601,mst2_btcs_602,mst2_btcs_965,mst2_btcs_966,mst2_btcs_994,mst3_btcs_601,mst3_btcs_602,mst3_btcs_965,mst3_btcs_966,mst3_btcs_994,sgpa from sem_6 WHERE URN LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,URN,btcs_601,btcs_602,btcs_603,btcs_604,btcs_605,btcs_965,btcs_966,btcs_994,mst1_btcs_601,mst1_btcs_602,mst1_btcs_965,mst1_btcs_966,mst1_btcs_994,mst2_btcs_601,mst2_btcs_602,mst2_btcs_965,mst2_btcs_966,mst2_btcs_994,mst3_btcs_601,mst3_btcs_602,mst3_btcs_965,mst3_btcs_966,mst3_btcs_994,sgpa from sem_6"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18601")
    trv.heading("5", text ="BTCS-18602")
    trv.heading("6", text ="BTCS-18603")
    trv.heading("7", text ="BTCS-18604")
    trv.heading("8", text ="BTCS-18905")
    trv.heading("9", text ="BTCS-18965")
    trv.heading("10", text ="BTCS-18966")
    trv.heading("11", text ="BTCS-18994")
    trv.heading("12", text ="MST-1_BTCS-601")
    trv.heading("13", text ="MST-1_BTCS-602")
    trv.heading("14", text ="MST-1_BTCS-965")
    trv.heading("15", text ="MST-1_BTCS-966")
    trv.heading("16", text ="MST-1_BTCS-994")
    trv.heading("17", text ="MST-2_BTCS-601")
    trv.heading("18", text ="MST-2_BTCS-602")
    trv.heading("19", text ="MST-2_BTCS-965")
    trv.heading("20", text ="MST-2_BTCS-966")
    trv.heading("21", text ="MST-2_BTCS-994")
    trv.heading("22", text ="MST-3_BTCS-601")
    trv.heading("23", text ="MST-3_BTCS-602")
    trv.heading("24", text ="MST-3_BTCS-965")
    trv.heading("25", text ="MST-3_BTCS-966")
    trv.heading("26", text ="MST-3_BTCS-994")
    trv.heading("27", text ="SGPA")

    query ="select ID,Name,URN,btcs_601,btcs_602,btcs_603,btcs_604,btcs_605,btcs_965,btcs_966,btcs_994,mst1_btcs_601,mst1_btcs_602,mst1_btcs_965,mst1_btcs_966,mst1_btcs_994,mst2_btcs_601,mst2_btcs_602,mst2_btcs_965,mst2_btcs_966,mst2_btcs_994,mst3_btcs_601,mst3_btcs_602,mst3_btcs_965,mst3_btcs_966,mst3_btcs_994,sgpa from sem_6"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

def view_result_7():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,URN,btcs_701,btcs_702,btcs_703,btcs_704,btcs_705,btcs_706,btcs_707,btcs_708,btcs_709,mst1_btcs_701,mst1_btcs_702,mst1_btcs_703,mst1_btcs_704,mst1_btcs_705,mst2_btcs_701,mst2_btcs_702,mst2_btcs_703,mst2_btcs_704,mst2_btcs_705,mst3_btcs_701,mst3_btcs_702,mst3_btcs_703,mst3_btcs_704,mst3_btcs_705,sgpa from sem_7 WHERE URN LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,URN,btcs_701,btcs_702,btcs_703,btcs_704,btcs_705,btcs_706,btcs_707,btcs_708,btcs_709,mst1_btcs_701,mst1_btcs_702,mst1_btcs_703,mst1_btcs_704,mst1_btcs_705,mst2_btcs_701,mst2_btcs_702,mst2_btcs_703,mst2_btcs_704,mst2_btcs_705,mst3_btcs_701,mst3_btcs_702,mst3_btcs_703,mst3_btcs_704,mst3_btcs_705,sgpa from sem_7"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')
    trv.column("28", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18701")
    trv.heading("5", text ="BTCS-18702")
    trv.heading("6", text ="BTCS-18703")
    trv.heading("7", text ="BTCS-18704")
    trv.heading("8", text ="BTCS-18705")
    trv.heading("9", text ="BTCS-18706")
    trv.heading("10", text ="BTCS-18707")
    trv.heading("11", text ="BTCS-18708")
    trv.heading("12", text ="BTCS-18705")
    trv.heading("13", text ="MST-1_BTCS-701")
    trv.heading("14", text ="MST-1_BTCS-702")
    trv.heading("15", text ="MST-1_BTCS-703")
    trv.heading("16", text ="MST-1_BTCS-704")
    trv.heading("17", text ="MST-1_BTCS-705")
    trv.heading("18", text ="MST-2_BTCS-701")
    trv.heading("19", text ="MST-2_BTCS-702")
    trv.heading("20", text ="MST-2_BTCS-703")
    trv.heading("21", text ="MST-2_BTCS-704")
    trv.heading("22", text ="MST-2_BTCS-705")
    trv.heading("23", text ="MST-3_BTCS-701")
    trv.heading("24", text ="MST-3_BTCS-702")
    trv.heading("25", text ="MST-3_BTCS-703")
    trv.heading("26", text ="MST-3_BTCS-704")
    trv.heading("27", text ="MST-3_BTCS-705")
    trv.heading("28", text ="SGPA")

    query ="select ID,Name,URN,btcs_701,btcs_702,btcs_703,btcs_704,btcs_705,btcs_706,btcs_707,btcs_708,btcs_709,mst1_btcs_701,mst1_btcs_702,mst1_btcs_703,mst1_btcs_704,mst1_btcs_705,mst2_btcs_701,mst2_btcs_702,mst2_btcs_703,mst2_btcs_704,mst2_btcs_705,mst3_btcs_701,mst3_btcs_702,mst3_btcs_703,mst3_btcs_704,mst3_btcs_705,sgpa from sem_7"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

    ###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)

#================================================================================================================================================#

def view_result_8():
    wind_result = Tk()
    r_width = wind_result.winfo_screenwidth()
    r_height = wind_result.winfo_screenheight()
    wind_result.title("Result Window")
    wind_result.geometry("%dx%d+0+0" % (r_width,r_height))

    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,URN,btcs_801,btcs_802,btcs_803,btcs_804,btcs_805,btcs_806,btcs_807,btcs_808,mst1_btcs_801,mst1_btcs_802,mst1_btcs_803,mst1_btcs_804,mst1_btcs_805,mst2_btcs_801,mst2_btcs_802,mst2_btcs_803,mst2_btcs_804,mst2_btcs_805,mst3_btcs_801,mst3_btcs_802,mst3_btcs_803,mst3_btcs_804,mst3_btcs_805,sgpa from sem_8 WHERE URN LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,URN,btcs_801,btcs_802,btcs_803,btcs_804,btcs_805,btcs_806,btcs_807,btcs_808,mst1_btcs_801,mst1_btcs_802,mst1_btcs_803,mst1_btcs_804,mst1_btcs_805,mst2_btcs_801,mst2_btcs_802,mst2_btcs_803,mst2_btcs_804,mst2_btcs_805,mst3_btcs_801,mst3_btcs_802,mst3_btcs_803,mst3_btcs_804,mst3_btcs_805,sgpa from sem_8"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_result)

    wrapper2 = LabelFrame(wind_result,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_result,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 50, anchor ='c')
    trv.column("2", width = 100, anchor ='sw')
    trv.column("3", width = 80, anchor ='c')
    trv.column("4", width = 80, anchor ='c')
    trv.column("5", width = 80, anchor ='c')
    trv.column("6", width = 80, anchor ='c')
    trv.column("7", width = 80, anchor ='c')
    trv.column("8", width = 80, anchor ='c')
    trv.column("9", width = 80, anchor ='c')
    trv.column("10", width = 80, anchor ='c')
    trv.column("11", width = 80, anchor ='c')
    trv.column("12", width = 80, anchor ='c')
    trv.column("13", width = 80, anchor ='c')
    trv.column("14", width = 80, anchor ='c')
    trv.column("15", width = 80, anchor ='c')
    trv.column("16", width = 80, anchor ='c')
    trv.column("17", width = 80, anchor ='c')
    trv.column("18", width = 80, anchor ='c')
    trv.column("19", width = 80, anchor ='c')
    trv.column("20", width = 80, anchor ='c')
    trv.column("21", width = 80, anchor ='c')
    trv.column("22", width = 80, anchor ='c')
    trv.column("23", width = 80, anchor ='c')
    trv.column("24", width = 80, anchor ='c')
    trv.column("25", width = 80, anchor ='c')
    trv.column("26", width = 80, anchor ='c')
    trv.column("27", width = 80, anchor ='c')

    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="BTCS-18801")
    trv.heading("5", text ="BTCS-18802")
    trv.heading("6", text ="BTCS-18803")
    trv.heading("7", text ="BTCS-18804")
    trv.heading("8", text ="BTCS-18805")
    trv.heading("9", text ="BTCS-18806")
    trv.heading("10", text ="BTCS-18807")
    trv.heading("11", text ="BTCS-18808")
    trv.heading("12", text ="MST-1_BTCS-801")
    trv.heading("13", text ="MST-1_BTCS-802")
    trv.heading("14", text ="MST-1_BTCS-803")
    trv.heading("15", text ="MST-1_BTCS-804")
    trv.heading("16", text ="MST-1_BTCS-805")
    trv.heading("17", text ="MST-2_BTCS-801")
    trv.heading("18", text ="MST-2_BTCS-802")
    trv.heading("19", text ="MST-2_BTCS-803")
    trv.heading("20", text ="MST-2_BTCS-804")
    trv.heading("21", text ="MST-2_BTCS-805")
    trv.heading("22", text ="MST-3_BTCS-801")
    trv.heading("23", text ="MST-3_BTCS-802")
    trv.heading("24", text ="MST-3_BTCS-803")
    trv.heading("25", text ="MST-3_BTCS-804")
    trv.heading("26", text ="MST-3_BTCS-805")
    trv.heading("27", text ="SGPA")

    query ="select ID,Name,URN,btcs_801,btcs_802,btcs_803,btcs_804,btcs_805,btcs_806,btcs_807,btcs_808,mst1_btcs_801,mst1_btcs_802,mst1_btcs_803,mst1_btcs_804,mst1_btcs_805,mst2_btcs_801,mst2_btcs_802,mst2_btcs_803,mst2_btcs_804,mst2_btcs_805,mst3_btcs_801,mst3_btcs_802,mst3_btcs_803,mst3_btcs_804,mst3_btcs_805,sgpa from sem_8"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

    ###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)
#============================================VIEW RESULT========================
    
#============================================ENTER RESULT 1=================================#
def enter_result_1():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0" % (w3_w, w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3 = Frame(wind3, height=200, bg="wheat3", width=w_width, bd=5)
    top_frame3.pack(side="top", fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btac_101 = StringVar(wind3)
    btam_101 = StringVar(wind3)
    btcs_101 = StringVar(wind3)
    btcs_102 = StringVar(wind3)
    btme_101 = StringVar(wind3)
    btme_102 = StringVar(wind3)

    mst11 = StringVar(wind3)
    mst12 = StringVar(wind3)
    mst13 = StringVar(wind3)
    mst14 = StringVar(wind3)

    mst21 = StringVar(wind3)
    mst22 = StringVar(wind3)
    mst23 = StringVar(wind3)
    mst24 = StringVar(wind3)

    mst31 = StringVar(wind3)
    mst32 = StringVar(wind3)
    mst33 = StringVar(wind3)
    mst34 = StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3 = Label(top_frame3, text="ENTER DETAILS", font=("impact", 30, "italic"), fg="gray26",bg="wheat3")
    lb3.pack(side="top", anchor="center", ipadx="5")

    bottom_frame3 = Frame(wind3, width=w3_w, height=w3_h, bg="wheat1", bd=5)
    bottom_frame3.pack(side="left")

    lb4 = Label(bottom_frame3, text="Personal Info.", font=("arial", 15, "bold"), fg="black",bg="white")
    lb4.place(x=105, y=20)

    lb4 = Label(bottom_frame3, text="Name", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=10, y=70)
    en4 = Entry(bottom_frame3, width="20", textvariable=name3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=70)

    lb4 = Label(bottom_frame3, text="Roll No.", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=10, y=120)
    en4 = Entry(bottom_frame3, width="20", textvariable=roll3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=120)

###For Storing Result###

    lb4 = Label(bottom_frame3, text="THEORY", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=20)

    lb4 = Label(bottom_frame3, text="BTAC-101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=btac_101, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=70)

    lb4 = Label(bottom_frame3, text="BTAM-101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=btam_101, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_101, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=170)

    lb4 = Label(bottom_frame3, text="PRACTICALS", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=220)

    lb4 = Label(bottom_frame3, text="BTME-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=btme_101, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=270)

    lb4 = Label(bottom_frame3, text="BTCS-18102", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=320)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_102, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=320)

    lb4 = Label(bottom_frame3, text="BTME-18102", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=430, y=370)
    en4 = Entry(bottom_frame3, width="5", textvariable=btme_102, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=370)

###====MST-I====###

    lb4 = Label(bottom_frame3, text="MST-I", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=780, y=20)

    lb4 = Label(bottom_frame3, text="BTAC-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=700, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst11, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=70)

    lb4 = Label(bottom_frame3, text="BTAM-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=700, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst12, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=700, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst13, relief="ridge", font=("arial", 15),
    bg="gray99")
    en4.place(x=860, y=170)

    lb4 = Label(bottom_frame3, text="BTME-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=700, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst14, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=220)

###====MST-II====###

    lb4 = Label(bottom_frame3, text="MST-II", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1050, y=20)

    lb4 = Label(bottom_frame3, text="BTAC-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=970, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst21, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=70)

    lb4 = Label(bottom_frame3, text="BTAM-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=970, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst22, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=970, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst23, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=170)

    lb4 = Label(bottom_frame3, text="BTME-18102", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=970, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst24, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=220)

###====MST-III====###

    lb4 = Label(bottom_frame3, text="MST-III", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1320, y=20)

    lb4 = Label(bottom_frame3, text="BTAC-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=1240, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst31, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=70)

    lb4 = Label(bottom_frame3, text="BTAM-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=1240, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst32, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18101", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=1240, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst33, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=170)

    lb4 = Label(bottom_frame3, text="BTME-18102", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=1240, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst34, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=220)

    ###====SGPA====###

    lb4 = Label(bottom_frame3, text="SGPA", font=("arial", 15, "bold"), fg="black", bg="wheat1")
    lb4.place(x=595, y=530)
    en4 = Entry(bottom_frame3, width="10", textvariable=sgpa, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=675, y=530)

    ###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btac_101.get()
            x2 = btam_101.get()
            x3 = btcs_102.get()
            x4 = btcs_101.get()
            x5 = btme_102.get()
            x6 = btme_101.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()

            x7 = sgpa.get()

            sql = "INSERT INTO sem_1 (Name,URN,btac_101,btam_101,btcs_101,btcs_102,btme_101,btme_102,mst1_btac_101,mst1_btam_101,mst1_btcs_101,mst1_btme_102,mst2_btac_101,mst2_btam_101,mst2_btcs_101,mst2_btme_102,mst3_btac_101,mst3_btam_101,mst3_btcs_101,mst3_btme_102,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3, r3,x1, x2,x4, x3, x6,x5, m1, m2, m3, m4, s1, s2, s3, s4, t1, t2, t3, t4,x7)
            mycursor.execute(sql, val)
            mydb.commit()
            mb.showinfo("SAVED", "Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
        ###---End of save_result function---###

    btn3 = Button(bottom_frame3, text="Save", font=("arial", 30, "bold"), fg="white", bg="gray30",activebackground="gray90", command=save_result)
    btn3.place(x=680, y=650)
#============================================ENTER RESULT 1=================================#
        
#============================================ENTER RESULT 2=================================#

def enter_result_2():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0"%(w3_w,w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3=Frame(wind3,height=200,bg="wheat3",width=w_width,bd=5)
    top_frame3.pack(side="top",fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    amcs_101 = StringVar(wind3)
    btph_101 = StringVar(wind3)
    btph_102 = StringVar(wind3)
    btme_101 = StringVar(wind3)
    btee_101 = StringVar(wind3)
    btee_102 = StringVar(wind3)

    mst11 =StringVar(wind3)
    mst12 =StringVar(wind3)
    mst13 =StringVar(wind3)
    mst14 =StringVar(wind3)

    mst21 =StringVar(wind3)
    mst22 =StringVar(wind3)
    mst23 =StringVar(wind3)
    mst24 =StringVar(wind3)

    mst31 =StringVar(wind3)
    mst32 =StringVar(wind3)
    mst33 =StringVar(wind3)
    mst34 =StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3=Label(top_frame3,text="ENTER DETAILS",font=("impact",30,"italic"),fg="gray26",bg="wheat3")
    lb3.pack(side="top",anchor="center",ipadx="5")

    bottom_frame3=Frame(wind3,width=w3_w,height=w3_h,bg="wheat1",bd=5)
    bottom_frame3.pack(side="left")

    lb4=Label(bottom_frame3,text="Personal Info.",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=105,y=20)

    lb4=Label(bottom_frame3,text="Name",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=10,y=70)
    en4=Entry(bottom_frame3,width="20",textvariable=name3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=120,y=70)

    lb4=Label(bottom_frame3,text="Roll No.",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=10,y=120)
    en4=Entry(bottom_frame3,width="20",textvariable=roll3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=120,y=120)

###For Storing Result###

    lb4=Label(bottom_frame3,text="THEORY",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=480,y=20)

    lb4=Label(bottom_frame3,text="BTPH-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=btph_101,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=70)

    lb4=Label(bottom_frame3,text="BTEE-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=btee_101,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=120)

    lb4=Label(bottom_frame3,text="AMCS-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=amcs_101,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=170)

    lb4=Label(bottom_frame3,text="PRACTICALS",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=480,y=220)

    lb4=Label(bottom_frame3,text="BTPH-18102",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=270)
    en4=Entry(bottom_frame3,width="5",textvariable=btph_102,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=270)

    lb4=Label(bottom_frame3,text="BTEE-18102",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=320)
    en4=Entry(bottom_frame3,width="5",textvariable=btee_102,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=320)

    lb4=Label(bottom_frame3,text="BTME-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=430,y=370)
    en4=Entry(bottom_frame3,width="5",textvariable=btme_101,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=370)

###====MST-I====###

    lb4=Label(bottom_frame3,text="MST-I",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=780,y=20)

    lb4=Label(bottom_frame3,text="BTPH-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=700,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst11,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=70)

    lb4=Label(bottom_frame3,text="BTEE-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=700,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst12,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=120)

    lb4=Label(bottom_frame3,text="AMCS-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=700,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst13,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=170)

    lb4=Label(bottom_frame3,text="BTME-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=700,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst14,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=220)

###====MST-II====###

    lb4=Label(bottom_frame3,text="MST-II",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1050,y=20)

    lb4=Label(bottom_frame3,text="BTPH-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=970,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst21,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=70)

    lb4=Label(bottom_frame3,text="BTEE-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=970,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst22,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=120)

    lb4=Label(bottom_frame3,text="AMCS-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=970,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst23,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=170)

    lb4=Label(bottom_frame3,text="BTME-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=970,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst24,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=220)

###====MST-III====###

    lb4=Label(bottom_frame3,text="MST-III",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1320,y=20)

    lb4=Label(bottom_frame3,text="BTPH-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=1240,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst31,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=70)

    lb4=Label(bottom_frame3,text="BTEE-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=1240,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst32,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=120)

    lb4=Label(bottom_frame3,text="AMCS-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=1240,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst33,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=170)

    lb4=Label(bottom_frame3,text="BTME-18101",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=1240,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst34,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=220)

###====SGPA====###

    lb4=Label(bottom_frame3,text="SGPA",font=("arial",15,"bold"),fg="black",bg="wheat1")
    lb4.place(x=595,y=530)
    en4=Entry(bottom_frame3,width="10",textvariable=sgpa,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=675,y=530)

###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = amcs_101.get()
            x2 = btph_101.get()
            x3 = btph_102.get()
            x4 = btee_101.get()
            x5 = btee_102.get()
            x6 = btme_101.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()

            x7 = sgpa.get()

            sql = "INSERT INTO sem_2 (name,rollno,,btph_101,btee_101,amcs_101,btph_102,btee_102,btme_101,mst1_btph_101,mst1_btee_101,mst1_amcs_101,mst1_btme_101,mst2_btph_101,mst2_btee_101,mst2_amcs_101,mst2_btme_101,mst3_btph_101,mst3_btee_101,mst3_amcs_101,mst3_btme_101,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3,r3,x2,x4,x1,x3,x5,x6,m1,m2,m3,m4,s1,s2,s3,s4,t1,t2,t3,t4,x7)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount,"Record inserted")
            mb.showinfo("SAVED","Result saved successfully.")

        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
        ###---End of save_result function---###

    btn3=Button(bottom_frame3,text="Save",font=("arial",30,"bold"),fg="white",bg="gray30",activebackground="gray90",command=save_result)
    btn3.place(x=680,y=650)

#============================================ENTER RESULT 2=================================#
                    
#============================================ENTER RESULT 3=================================#

def enter_result_3():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0"%(w3_w,w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3=Frame(wind3,height=200,bg="gainsboro",width=w_width,bd=5)
    top_frame3.pack(side="top",fill="both")

    name3 = StringVar(wind3)
    roll3 = StringVar(wind3)
  
    amcs_301 = StringVar(wind3)
    btcs_301 = StringVar(wind3)
    btcs_302 = StringVar(wind3)
    btcs_303 = StringVar(wind3)
    btcs_301 = StringVar(wind3)
    btcs_304 = StringVar(wind3)
    btcs_305 = StringVar(wind3)
    btcs_306 = StringVar(wind3)
    btcs_307 = StringVar(wind3)
    hsmc_301 = StringVar(wind3)

    mst11 =StringVar(wind3)
    mst12 =StringVar(wind3)
    mst13 =StringVar(wind3)
    mst14 =StringVar(wind3)
    mst15 =StringVar(wind3)

    mst21 =StringVar(wind3)
    mst22 =StringVar(wind3)
    mst23 =StringVar(wind3)
    mst24 =StringVar(wind3)
    mst25 =StringVar(wind3)

    mst31 =StringVar(wind3)
    mst32 =StringVar(wind3)
    mst33 =StringVar(wind3)
    mst34 =StringVar(wind3)
    mst35 =StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3=Label(top_frame3,text="ENTER DETAILS",font=("impact",30,"italic"),fg="gray26",bg="gainsboro")
    lb3.pack(side="top",anchor="center",ipadx="5")

    bottom_frame3=Frame(wind3,width=w3_w,height=w3_h,bg="azure",bd=5)
    bottom_frame3.pack(side="left")

    lb4=Label(bottom_frame3,text="Personal Info.",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=105,y=20)

    lb4=Label(bottom_frame3,text="Name",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=70)
    en4=Entry(bottom_frame3,width="20",textvariable=name3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=120,y=70)

    lb4=Label(bottom_frame3,text="Roll No.",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=120)
    en4=Entry(bottom_frame3,width="20",textvariable=roll3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=120,y=120)

###For Storing Result###

    lb4=Label(bottom_frame3,text="THEORY",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=480,y=20)

    lb4=Label(bottom_frame3,text="BTCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_301,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=70)

    lb4=Label(bottom_frame3,text="BTCS-18302",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_302,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=120)

    lb4=Label(bottom_frame3,text="BTCS-18303",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_303,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=170)

    lb4=Label(bottom_frame3,text="AMCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=amcs_301,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=220)

    lb4=Label(bottom_frame3,text="HSMC-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=270)
    en4=Entry(bottom_frame3,width="5",textvariable=hsmc_301,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=270)

    lb4=Label(bottom_frame3,text="PRACTICALS",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=480,y=320)

    lb4=Label(bottom_frame3,text="BTCS-18304",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=370)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_304,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=370)

    lb4=Label(bottom_frame3,text="BTCS-18305",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=420)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_305,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=420)

    lb4=Label(bottom_frame3,text="BTCS-18306",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=470)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_306,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=470)

    lb4=Label(bottom_frame3,text="BTCS-18307",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=430,y=520)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_307,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=590,y=520)

    ###====MST-I====###

    lb4=Label(bottom_frame3,text="MST-I",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=780,y=20)

    lb4=Label(bottom_frame3,text="BTCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=700,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst11,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=70)

    lb4=Label(bottom_frame3,text="BTCS-18302",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=700,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst12,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=120)

    lb4=Label(bottom_frame3,text="BTCS-18303",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=700,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst13,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=170)

    lb4=Label(bottom_frame3,text="AMCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=700,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst14,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=220)

    lb4=Label(bottom_frame3,text="HSMC-18302",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=700,y=270)
    en4=Entry(bottom_frame3,width="5",textvariable=mst15,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=860,y=270)

    ###====MST-II====###

    lb4=Label(bottom_frame3,text="MST-II",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1050,y=20)

    lb4=Label(bottom_frame3,text="BTCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst21,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=70)

    lb4=Label(bottom_frame3,text="BTCS-18302",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst22,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=120)

    lb4=Label(bottom_frame3,text="BTCS-18303",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst23,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=170)

    lb4=Label(bottom_frame3,text="AMCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst24,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=220)

    lb4=Label(bottom_frame3,text="HSMC-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=270)
    en4=Entry(bottom_frame3,width="5",textvariable=mst25,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=270)

    ###====MST-III====###

    lb4=Label(bottom_frame3,text="MST-III",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1320,y=20)

    lb4=Label(bottom_frame3,text="BTCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=70)
    en4=Entry(bottom_frame3,width="5",textvariable=mst31,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=70)

    lb4=Label(bottom_frame3,text="BTCS-18302",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=120)
    en4=Entry(bottom_frame3,width="5",textvariable=mst32,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=120)

    lb4=Label(bottom_frame3,text="BTCS-18303",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=170)
    en4=Entry(bottom_frame3,width="5",textvariable=mst33,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=170)

    lb4=Label(bottom_frame3,text="AMCS-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=220)
    en4=Entry(bottom_frame3,width="5",textvariable=mst34,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=220)

    lb4=Label(bottom_frame3,text="HSMC-18301",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=270)
    en4=Entry(bottom_frame3,width="5",textvariable=mst35,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=270)

    ###====SGPA====###

    lb4=Label(bottom_frame3,text="SGPA",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=800,y=530)
    en4=Entry(bottom_frame3,width="10",textvariable=sgpa,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=880,y=530)

    ###----window for saving result---###

    def save_result():

        n3 = name3.get()
        r3 = roll3.get()                       

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = amcs_301.get()
            x2 = btcs_302.get()
            x3 = btcs_303.get()
            x4 = btcs_304.get()
            x5 = btcs_305.get()
            x6 = btcs_306.get()
            x7 = btcs_307.get()
            x8 = hsmc_301.get()
            x10 = btcs_301.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x9 = sgpa.get()

            sql = "INSERT INTO sem_3 (name,rollno,btcs_301,btcs_302,btcs_303,amcs_301,hsmc_301,btcs_304,btcs_305,btcs_306,btcs_307,mst1_btcs_301,mst1_btcs_302,mst1_btcs_303,mst1_amcs_301,mst1_hsmc_301,mst2_btcs_301,mst2_btcs_302,mst2_btcs_303,mst2_amcs_301,mst2_hsmc_301,mst3_btcs_301,mst3_btcs_302,mst3_btcs_303,mst3_amcs_301,mst3_hsmc_301,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3,r3,x10,x2,x3,x1,x8,x4,x5,x6,x7,m1,m2,m3,m4,m5,s1,s2,s3,s4,s5,t1,t2,t3,t4,t5,x9)
            mycursor.execute(sql, val)
            mydb.commit()
            mb.showinfo("SAVED","Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
###---End of save_result function---###

    btn3=Button(bottom_frame3,text="Save",font=("arial",30,"bold"),fg="white",bg="gray30",activebackground="gray90",command=save_result)
    btn3.place(x=680,y=650)
    
#============================================ENTER RESULT 3=================================#

#============================================ENTER RESULT 4=================================#
def enter_result_4():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0"%(w3_w,w3_h))
    wind3.title("ENTER DETAILS")
    
    top_frame3=Frame(wind3,height=150,bg="powder blue",width=w_width,bd=5)
    top_frame3.pack(side="top",fill="both")

    
    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btam_401 = StringVar(wind3)
    btcs_402 = StringVar(wind3)
    btcs_403 = StringVar(wind3)
    btcs_404 = StringVar(wind3)
    btcs_405 = StringVar(wind3)
    btcs_406 = StringVar(wind3)
    btcs_407 = StringVar(wind3)
    bths_904 = StringVar(wind3)
    csmc = StringVar(wind3)

    mst11 =StringVar(wind3)
    mst12 =StringVar(wind3)
    mst13 =StringVar(wind3)
    mst14 =StringVar(wind3)
    mst15 =StringVar(wind3)

    mst21 =StringVar(wind3)
    mst22 =StringVar(wind3)
    mst23 =StringVar(wind3)
    mst24 =StringVar(wind3)
    mst25 =StringVar(wind3)

    mst31 =StringVar(wind3)
    mst32 =StringVar(wind3)
    mst33 =StringVar(wind3)
    mst34 =StringVar(wind3)
    mst35 =StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3=Label(top_frame3,text="ENTER DETAILS",font=("impact",26,"italic"),fg="gray26",bg="powder blue")
    lb3.pack(side="top",anchor="center",ipadx="5")

    bottom_frame3=Frame(wind3,width=w3_w,height=w3_h,bg="lavender",bd=5)
    bottom_frame3.pack(side="left")

    '''lb4=Label(bottom_frame3,text="Personal Info.",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=105,y=5)'''

    lb4=Label(bottom_frame3,text="Name",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=330)
    en4=Entry(bottom_frame3,width="20",textvariable=name3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=330)

    lb4=Label(bottom_frame3,text="Roll No.",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=550,y=330)
    en4=Entry(bottom_frame3,width="10",textvariable=roll3,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=710,y=330)
###For Storing Result###

    lb4=Label(bottom_frame3,text="THEORY",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1320,y=5)

    lb4=Label(bottom_frame3,text="BTCS-18402",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=55)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_402,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=55)

    lb4=Label(bottom_frame3,text="BTCS-18403",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=105)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_403,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=105)

    lb4=Label(bottom_frame3,text="BTCS-18404",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=155)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_404,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=155)

    lb4=Label(bottom_frame3,text="BTAM-18401",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=205)
    en4=Entry(bottom_frame3,width="5",textvariable=btam_401,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=205)

    lb4=Label(bottom_frame3,text="BTHS-18904",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1240,y=255)
    en4=Entry(bottom_frame3,width="5",textvariable=bths_904,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1400,y=255)

    lb4=Label(bottom_frame3,text="PRACTICALS",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=1050,y=5)

    lb4=Label(bottom_frame3,text="BTCS-18405",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=55)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_405,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=55)

    lb4=Label(bottom_frame3,text="BTCS-18406",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=105)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_406,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=105)

    lb4=Label(bottom_frame3,text="BTCS-18407",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=155)
    en4=Entry(bottom_frame3,width="5",textvariable=btcs_407,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=155)

    lb4=Label(bottom_frame3,text="CSMC",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=970,y=205)
    en4=Entry(bottom_frame3,width="5",textvariable=csmc,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=1130,y=205)

    ###====MST-I====###

    lb4=Label(bottom_frame3,text="MST-I",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=105,y=5)

    lb4=Label(bottom_frame3,text="BTCS-18402",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=55)
    en4=Entry(bottom_frame3,width="5",textvariable=mst11,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=170,y=55)

    lb4=Label(bottom_frame3,text="BTCS-18403",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=105)
    en4=Entry(bottom_frame3,width="5",textvariable=mst12,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=170,y=105)

    lb4=Label(bottom_frame3,text="BTCS-18404",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=155)
    en4=Entry(bottom_frame3,width="5",textvariable=mst13,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=170,y=155)

    lb4=Label(bottom_frame3,text="BTAM-18401",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=205)
    en4=Entry(bottom_frame3,width="5",textvariable=mst14,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=170,y=205)

    lb4=Label(bottom_frame3,text="BTHS-18904",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=10,y=255)
    en4=Entry(bottom_frame3,width="5",textvariable=mst15,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=170,y=255)

                    ###====MST-II====###

    lb4=Label(bottom_frame3,text="MST-II",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=375,y=5)

    lb4=Label(bottom_frame3,text="BTCS-18402",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=325,y=55)
    en4=Entry(bottom_frame3,width="5",textvariable=mst21,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=485,y=55)

    lb4=Label(bottom_frame3,text="BTCS-18403",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=325,y=105)
    en4=Entry(bottom_frame3,width="5",textvariable=mst22,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=485,y=105)

    lb4=Label(bottom_frame3,text="BTCS-18404",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=325,y=155)
    en4=Entry(bottom_frame3,width="5",textvariable=mst23,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=485,y=155)

    lb4=Label(bottom_frame3,text="BTAM-18401",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=325,y=205)
    en4=Entry(bottom_frame3,width="5",textvariable=mst24,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=485,y=205)

    lb4=Label(bottom_frame3,text="BTHS-18904",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=325,y=255)
    en4=Entry(bottom_frame3,width="5",textvariable=mst25,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=485,y=255)

    ###====MST-III====###

    lb4=Label(bottom_frame3,text="MST-III",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=645,y=5)

    lb4=Label(bottom_frame3,text="BTCS-18402",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=595,y=55)
    en4=Entry(bottom_frame3,width="5",textvariable=mst31,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=755,y=55)

    lb4=Label(bottom_frame3,text="BTCS-18403",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=595,y=105)
    en4=Entry(bottom_frame3,width="5",textvariable=mst32,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=755,y=105)

    lb4=Label(bottom_frame3,text="BTCS-18404",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=595,y=155)
    en4=Entry(bottom_frame3,width="5",textvariable=mst33,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=755,y=155)

    lb4=Label(bottom_frame3,text="BTAM-18401",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=595,y=205)
    en4=Entry(bottom_frame3,width="5",textvariable=mst34,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=755,y=205)

    lb4=Label(bottom_frame3,text="BTHS-18904",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=595,y=255)
    en4=Entry(bottom_frame3,width="5",textvariable=mst35,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=755,y=255)

    ###====SGPA====###

    lb4=Label(bottom_frame3,text="SGPA",font=("arial",15,"bold"),fg="black",bg="white")
    lb4.place(x=140,y=330)
    en4=Entry(bottom_frame3,width="10",textvariable=sgpa,relief="ridge",font=("arial",15),bg="gray99")
    en4.place(x=300,y=330)

    ###----window for saving result---###

    def save_result():

        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btam_401.get()
            x2 = btcs_402.get()
            x3 = btcs_403.get()
            x4 = btcs_404.get()
            x5 = btcs_405.get()
            x6 = btcs_406.get()
            x7 = btcs_407.get()
            x8 = bths_904.get()
            x10 = csmc.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x9 = sgpa.get()
            sql = "INSERT INTO sem_4 (name,rollno,btcs_402,btcs_403,btcs_404,btam_401,bths_904,btcs_405,btcs_406,btcs_407,csmc,mst1_btcs_402,mst1_btcs_403,mst1_btcs_404,mst1_btam_401,mst1_bths_904,mst2_btcs_402,mst2_btcs_403,mst2_btcs_404,mst2_btam_401,mst2_bths_904,mst3_btcs_402,mst3_btcs_403,mst3_btcs_404,mst3_btam_401,mst3_bths_904,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3,r3,x2,x3,x4,x1,x8,x5,x6,x7,x10,m1,m2,m3,m4,m5,s1,s2,s3,s4,s5,t1,t2,t3,t4,t5,x9)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount,"Record inserted")
            mb.showinfo("SAVED","Result saved successfully.")
        
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
                    

                        ###---End of save_result function---###

    btn3=Button(bottom_frame3,text="Save",font=("times new roman",26,"bold"),fg="white",bg="gray30",activebackground="gray90",command=save_result)
    btn3.place(x=600,y=385)
#=========================================ENTER RESULT 4=======================#
    
#=========================================ENTER RESULT 5=======================#
def enter_result_5():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0" % (w3_w, w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3 = Frame(wind3, height=150, bg="powder blue", width=w_width, bd=5)
    top_frame3.pack(side="top", fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btcs_501 = StringVar(wind3)
    btcs_502 = StringVar(wind3)
    btcs_503 = StringVar(wind3)
    btcs_504 = StringVar(wind3)
    btcs_505 = StringVar(wind3)
    btcs_506 = StringVar(wind3)
    btcs_507 = StringVar(wind3)
    btcs_508 = StringVar(wind3)
    bths_905 = StringVar(wind3)

    mst11 = StringVar(wind3)
    mst12 = StringVar(wind3)
    mst13 = StringVar(wind3)
    mst14 = StringVar(wind3)
    mst15 = StringVar(wind3)

    mst21 = StringVar(wind3)
    mst22 = StringVar(wind3)
    mst23 = StringVar(wind3)
    mst24 = StringVar(wind3)
    mst25 = StringVar(wind3)

    mst31 = StringVar(wind3)
    mst32 = StringVar(wind3)
    mst33 = StringVar(wind3)
    mst34 = StringVar(wind3)
    mst35 = StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3 = Label(top_frame3, text="ENTER DETAILS", font=("impact", 26, "italic"), fg="gray26",bg="powder blue")
    lb3.pack(side="top", anchor="center", ipadx="5")

    bottom_frame3 = Frame(wind3, width=w3_w, height=w3_h, bg="lavender", bd=5)
    bottom_frame3.pack(side="left")

    lb4 = Label(bottom_frame3, text="Personal Info.", font=("arial", 15, "bold"), fg="black",bg="white")
    lb4.place(x=105, y=20)

    lb4 = Label(bottom_frame3, text="Name", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=70)
    en4 = Entry(bottom_frame3, width="20", textvariable=name3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=70)

    lb4 = Label(bottom_frame3, text="Roll No.", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=120)
    en4 = Entry(bottom_frame3, width="20", textvariable=roll3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=120)

###For Storing Result###

    lb4 = Label(bottom_frame3, text="THEORY", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18502", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_502, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18503", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_503, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18504", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_504, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18501", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_501, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18905", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=bths_905, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=270)

    lb4 = Label(bottom_frame3, text="PRACTICALS", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=320)

    lb4 = Label(bottom_frame3, text="BTCS-18505", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=370)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_505, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=370)

    lb4 = Label(bottom_frame3, text="BTCS-18506", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=420)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_506, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=420)

    lb4 = Label(bottom_frame3, text="BTCS-18507", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=470)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_507, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=470)

    lb4 = Label(bottom_frame3, text="BTCS-508", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=520)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_508, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=520)

    ###====MST-I====###

    lb4 = Label(bottom_frame3, text="MST-I", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=780, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18502", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst11, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18503", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst12, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18504", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst13, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18501", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst14, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18905", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst15, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=270)

    ###====MST-II====###

    lb4 = Label(bottom_frame3, text="MST-II", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1050, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18502", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst21, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18503", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst22, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18504", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst23, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18501", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst24, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18905", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst25, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=270)

    ###====MST-III====###

    lb4 = Label(bottom_frame3, text="MST-III", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1320, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18502", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst31, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18503", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst32, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18504", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst33, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18501", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst34, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18905", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst35, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=270)

    ###====SGPA====###

    lb4 = Label(bottom_frame3, text="SGPA", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=800, y=530)
    en4 = Entry(bottom_frame3, width="10", textvariable=sgpa, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=880, y=530)

###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btcs_501.get()
            x2 = btcs_502.get()
            x3 = btcs_503.get()
            x4 = btcs_504.get()
            x5 = btcs_505.get()
            x6 = btcs_506.get()
            x7 = btcs_507.get()
            x8 = btcs_508.get()
            x9 = bths_905.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x10 = sgpa.get()

            sql = "INSERT INTO sem_5 (Name,URN,btcs_501,btcs_502,btcs_503,btcs_504,btcs_505,btcs_506,btcs_507,btcs_508,bths_905,mst1_btcs_502,mst1_btcs_503,mst1_btcs_504,mst1_btcs_501,mst1_bths_905,mst2_btcs_502,mst2_btcs_503,mst2_btcs_504,mst2_btcs_501,mst2_bths_905,mst3_btcs_502,mst3_btcs_503,mst3_btcs_504,mst3_btcs_501,mst3_bths_905,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)"
            val = (n3,r3,x1,x2,x3,x4,x5,x6,x7,x8,x9, m1, m2, m3, m4, m5, s1, s2, s3,s4, s5, t1, t2, t3, t4, t5, x10)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Record inserted")
            mb.showinfo("SAVED", "Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
        ###---End of save_result function---###

    btn3 = Button(bottom_frame3, text="Save", font=("arial", 30, "bold"), fg="white", bg="gray30",activebackground="gray90", command=save_result)
    btn3.place(x=680, y=650)


#=========================================ENTER RESULT 5=======================#
    
#=========================================ENTER RESULT 6=======================#
def enter_result_6():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0" % (w3_w, w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3 = Frame(wind3, height=200, bg="powder blue", width=w_width, bd=5)
    top_frame3.pack(side="top", fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btcs_601 = StringVar(wind3)
    btcs_602 = StringVar(wind3)
    btcs_603 = StringVar(wind3)#Practical
    btcs_604 = StringVar(wind3)#Practical
    btcs_605 = StringVar(wind3)#Practical
    btcs_965 = StringVar(wind3)
    btcs_966 = StringVar(wind3)
    btcs_994 = StringVar(wind3)

    mst11 = StringVar(wind3)
    mst12 = StringVar(wind3)
    mst13 = StringVar(wind3)
    mst14 = StringVar(wind3)
    mst15 = StringVar(wind3)

    mst21 = StringVar(wind3)
    mst22 = StringVar(wind3)
    mst23 = StringVar(wind3)
    mst24 = StringVar(wind3)
    mst25 = StringVar(wind3)

    mst31 = StringVar(wind3)
    mst32 = StringVar(wind3)
    mst33 = StringVar(wind3)
    mst34 = StringVar(wind3)
    mst35 = StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3 = Label(top_frame3, text="ENTER DETAILS", font=("impact", 30, "italic"), fg="gray26",bg="powder blue")
    lb3.pack(side="top", anchor="center", ipadx="5")

    bottom_frame3 = Frame(wind3, width=w3_w, height=w3_h, bg="lavender", bd=5)
    bottom_frame3.pack(side="left")

    lb4 = Label(bottom_frame3, text="Personal Info.", font=("arial", 15, "bold"), fg="black",bg="white")
    lb4.place(x=105, y=20)

    lb4 = Label(bottom_frame3, text="Name", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=70)
    en4 = Entry(bottom_frame3, width="20", textvariable=name3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=70)

    lb4 = Label(bottom_frame3, text="Roll No.", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=120)
    en4 = Entry(bottom_frame3, width="20", textvariable=roll3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=120)

###For Storing Result###

    lb4 = Label(bottom_frame3, text="THEORY", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18601", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_601, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18602", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_602, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18965", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_965, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18966", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_966, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18994", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_994, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=270)
    
    lb4 = Label(bottom_frame3, text="PRACTICALS", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=370)

    lb4 = Label(bottom_frame3, text="BTCS-18603", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=420)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_603, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=3420)

    lb4 = Label(bottom_frame3, text="BTCS-18604", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=470)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_604, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=470)

    lb4 = Label(bottom_frame3, text="BTCS-18605", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=520)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_605, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=520)



###====MST-I====###

    lb4 = Label(bottom_frame3, text="MST-I", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=780, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18601", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst11, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18602", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst12, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18965", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst13, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=170)

    lb4 = Label(bottom_frame3, text="BTAM-18966", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst14, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18994", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst15, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=270)

###====MST-II====###

    lb4 = Label(bottom_frame3, text="MST-II", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1050, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18601", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst21, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18602", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst22, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18965", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst23, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=170)

    lb4 = Label(bottom_frame3, text="BTAM-18966", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst24, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18994", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst25, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=270)

###====MST-III====###

    lb4 = Label(bottom_frame3, text="MST-III", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1320, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18601", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst31, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18602", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst32, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18965", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst33, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=170)

    lb4 = Label(bottom_frame3, text="BTAM-18966", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst34, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=220)

    lb4 = Label(bottom_frame3, text="BTHS-18994", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst35, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=270)

    ###====SGPA====###

    lb4 = Label(bottom_frame3, text="SGPA", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=800, y=530)
    en4 = Entry(bottom_frame3, width="10", textvariable=sgpa, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=880, y=530)

    ###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btcs_601.get()
            x2 = btcs_602.get()
            x3 = btcs_603.get()
            x4 = btcs_604.get()
            x5 = btcs_605.get()
            x6 = btcs_965.get()
            x7 = btcs_966.get()
            x8 = bths_994.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x9 = sgpa.get()

            sql = "INSERT INTO sem_6 (Name,URN,btcs_601,btcs_602,btcs_603,btcs_604,btcs_605,btcs_965,btcs_966,btcs_994,mst1_btcs_601,mst1_btcs_602,mst1_btcs_965,mst1_btcs_966,mst1_btcs_994,mst2_btcs_601,mst2_btcs_602,mst2_btcs_965,mst2_btcs_966,mst2_btcs_994,mst3_btcs_601,mst3_btcs_602,mst3_btcs_965,mst3_btcs_966,mst3_btcs_994,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3, r3,x1,x2, x3, x4,x5, x6, x7,x8, m1, m2, m3, m4, m5, s1, s2, s3,s4, s5, t1, t2, t3, t4, t5, x9)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Record inserted")
            mb.showinfo("SAVED", "Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
    ###---End of save_result function---###

    btn3 = Button(bottom_frame3, text="Save", font=("arial", 30, "bold"), fg="white", bg="gray30",activebackground="gray90", command=save_result)
    btn3.place(x=680, y=650)

#=========================================ENTER RESULT 6=======================#
    
#=========================================ENTER RESULT 7=======================#
def enter_result_7():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0" % (w3_w, w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3 = Frame(wind3, height=200, bg="powder blue", width=w_width, bd=5)
    top_frame3.pack(side="top", fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btcs_701 = StringVar(wind3)
    btcs_702 = StringVar(wind3)
    btcs_703 = StringVar(wind3)
    btcs_704 = StringVar(wind3)
    btcs_705 = StringVar(wind3)
    btcs_706 = StringVar(wind3)
    btcs_707 = StringVar(wind3)
    btcs_708 = StringVar(wind3)
    btcs_709 = StringVar(wind3)

    mst11 = StringVar(wind3)
    mst12 = StringVar(wind3)
    mst13 = StringVar(wind3)
    mst14 = StringVar(wind3)
    mst15 = StringVar(wind3)

    mst21 = StringVar(wind3)
    mst22 = StringVar(wind3)
    mst23 = StringVar(wind3)
    mst24 = StringVar(wind3)
    mst25 = StringVar(wind3)

    mst31 = StringVar(wind3)
    mst32 = StringVar(wind3)
    mst33 = StringVar(wind3)
    mst34 = StringVar(wind3)
    mst35 = StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3 = Label(top_frame3, text="ENTER DETAILS", font=("impact", 30, "italic"), fg="gray26",bg="powder blue")
    lb3.pack(side="top", anchor="center", ipadx="5")

    bottom_frame3 = Frame(wind3, width=w3_w, height=w3_h, bg="lavender", bd=5)
    bottom_frame3.pack(side="left")

    lb4 = Label(bottom_frame3, text="Personal Info.", font=("arial", 15, "bold"), fg="black",bg="white")
    lb4.place(x=105, y=20)

    lb4 = Label(bottom_frame3, text="Name", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=70)
    en4 = Entry(bottom_frame3, width="20", textvariable=name3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=70)

    lb4 = Label(bottom_frame3, text="Roll No.", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=120)
    en4 = Entry(bottom_frame3, width="20", textvariable=roll3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=120)

    ###For Storing Result###

    lb4 = Label(bottom_frame3, text="THEORY", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18701", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_701, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18702", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_702, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18703", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_703, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18704", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_704, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18705", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_705, relief="ridge", font=("arial", 15),
                bg="gray99")
    en4.place(x=590, y=270)

    lb4 = Label(bottom_frame3, text="PRACTICALS", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=320)

    lb4 = Label(bottom_frame3, text="BTCS-18706", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=370)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_706, relief="ridge", font=("arial", 15),
                bg="gray99")
    en4.place(x=590, y=370)

    lb4 = Label(bottom_frame3, text="BTCS-18707", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=420)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_707, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=420)

    lb4 = Label(bottom_frame3, text="BTCS-18708", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=470)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_708, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=470)

    lb4 = Label(bottom_frame3, text="BTCS_18709", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=520)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_709, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=520)

    ###====MST-I====###

    lb4 = Label(bottom_frame3, text="MST-I", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=780, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18701", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst11, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18702", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst12, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18703", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst13, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18704", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst14, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18705", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst15, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=270)

    ###====MST-II====###

    lb4 = Label(bottom_frame3, text="MST-II", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1050, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18701", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst21, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18702", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst22, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18703", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst23, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18704", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst24, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18705", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst25, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=270)

    ###====MST-III====###

    lb4 = Label(bottom_frame3, text="MST-III", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1320, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18701", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst31, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18702", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst32, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18703", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst33, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18704", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst34, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18705", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst35, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=270)

    ###====SGPA====###

    lb4 = Label(bottom_frame3, text="SGPA", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=800, y=530)
    en4 = Entry(bottom_frame3, width="10", textvariable=sgpa, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=880, y=530)

    ###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btcs_701.get()
            x2 = btcs_702.get()
            x3 = btcs_703.get()
            x4 = btcs_704.get()
            x5 = btcs_705.get()
            x6 = btcs_706.get()
            x7 = btcs_707.get()
            x8 = bths_708.get()
            x10 = btcs_709.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x9 = sgpa.get()

            sql = "INSERT INTO sem_7 (Name,URN,btcs_701,btcs_702,btcs_703,btcs_704,btcs_705,btcs_706,btcs_707,btcs_708,btcs_709,mst1_btcs_701,mst1_btcs_702,mst1_btcs_703,mst1_btcs_704,mst1_btcs_705,mst2_btcs_701,mst2_btcs_702,mst2_btcs_703,mst2_btcs_704,mst2_btcs_705,mst3_btcs_701,mst3_btcs_702,mst3_btcs_703,mst3_btcs_704,mst3_btcs_705,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3, r3, x1,x2,x3,x4,x5,x6, x7,x8, x10, m1, m2, m3, m4, m5, s1, s2, s3,s4, s5, t1, t2, t3, t4, t5, x9)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "Record inserted")
            mb.showinfo("SAVED", "Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
        ###---End of save_result function---###

    btn3 = Button(bottom_frame3, text="Save", font=("arial", 30, "bold"), fg="white", bg="gray30",activebackground="gray90", command=save_result)
    btn3.place(x=680, y=650)
    
    
#=========================================ENTER RESULT 7=======================#
    
#=========================================ENTER RESULT 8=======================#
def enter_result_8():
    wind3 = Tk()
    w3_w = wind3.winfo_screenwidth()
    w3_h = wind3.winfo_screenheight()
    wind3.geometry("%dx%d+0+0" % (w3_w, w3_h))
    wind3.title("ENTER DETAILS")

    top_frame3 = Frame(wind3, height=200, bg="powder blue", width=w_width, bd=5)
    top_frame3.pack(side="top", fill="both")

    name3 = StringVar(wind3)
    roll3 = IntVar(wind3)

    btcs_801 = StringVar(wind3)
    btcs_802 = StringVar(wind3)
    btcs_803 = StringVar(wind3)
    btcs_804 = StringVar(wind3)
    btcs_805 = StringVar(wind3)
    btcs_806 = StringVar(wind3)
    btcs_807 = StringVar(wind3)
    btcs_808 = StringVar(wind3)

    mst11 = StringVar(wind3)
    mst12 = StringVar(wind3)
    mst13 = StringVar(wind3)
    mst14 = StringVar(wind3)
    mst15 = StringVar(wind3)

    mst21 = StringVar(wind3)
    mst22 = StringVar(wind3)
    mst23 = StringVar(wind3)
    mst24 = StringVar(wind3)
    mst25 = StringVar(wind3)

    mst31 = StringVar(wind3)
    mst32 = StringVar(wind3)
    mst33 = StringVar(wind3)
    mst34 = StringVar(wind3)
    mst35 = StringVar(wind3)

    sgpa = StringVar(wind3)

    lb3 = Label(top_frame3, text="ENTER DETAILS", font=("impact", 30, "italic"), fg="gray26",bg="powder blue")
    lb3.pack(side="top", anchor="center", ipadx="5")

    bottom_frame3 = Frame(wind3, width=w3_w, height=w3_h, bg="lavender", bd=5)
    bottom_frame3.pack(side="left")

    lb4 = Label(bottom_frame3, text="Personal Info.", font=("arial", 15, "bold"), fg="black",bg="white")
    lb4.place(x=105, y=20)

    lb4 = Label(bottom_frame3, text="Name", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=70)
    en4 = Entry(bottom_frame3, width="20", textvariable=name3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=70)

    lb4 = Label(bottom_frame3, text="Roll No.", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=10, y=120)
    en4 = Entry(bottom_frame3, width="20", textvariable=roll3, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=120, y=120)

    ###For Storing Result###

    lb4 = Label(bottom_frame3, text="THEORY", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18801", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_801, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18802", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_802, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18803", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_803, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18804", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_804, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18805", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_805, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=270)

    lb4 = Label(bottom_frame3, text="PRACTICALS", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=480, y=320)

    lb4 = Label(bottom_frame3, text="BTCS-18806", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=370)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_806, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=370)

    lb4 = Label(bottom_frame3, text="BTCS-18807", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=420)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_807, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=420)

    lb4 = Label(bottom_frame3, text="BTCS-18808", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=430, y=470)
    en4 = Entry(bottom_frame3, width="5", textvariable=btcs_808, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=590, y=470)


    ###====MST-I====###

    lb4 = Label(bottom_frame3, text="MST-I", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=780, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18801", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst11, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18802", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst12, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18803", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst13, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18804", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst14, relief="ridge", font=("arial", 15),
                bg="gray99")
    en4.place(x=860, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18805", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=700, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst15, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=860, y=270)

    ###====MST-II====###

    lb4 = Label(bottom_frame3, text="MST-II", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1050, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18801", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst21, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18802", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst22, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18803", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst23, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18804", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst24, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18805", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=970, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst25, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1130, y=270)

    ###====MST-III====###

    lb4 = Label(bottom_frame3, text="MST-III", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1320, y=20)

    lb4 = Label(bottom_frame3, text="BTCS-18801", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=70)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst31, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=70)

    lb4 = Label(bottom_frame3, text="BTCS-18802", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=120)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst32, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=120)

    lb4 = Label(bottom_frame3, text="BTCS-18803", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=170)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst33, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=170)

    lb4 = Label(bottom_frame3, text="BTCS-18804", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=220)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst34, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=220)

    lb4 = Label(bottom_frame3, text="BTCS-18805", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=1240, y=270)
    en4 = Entry(bottom_frame3, width="5", textvariable=mst35, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=1400, y=270)

    ###====SGPA====###

    lb4 = Label(bottom_frame3, text="SGPA", font=("arial", 15, "bold"), fg="black", bg="white")
    lb4.place(x=800, y=530)
    en4 = Entry(bottom_frame3, width="10", textvariable=sgpa, relief="ridge", font=("arial", 15),bg="gray99")
    en4.place(x=880, y=530)

    ###----window for saving result---###

    def save_result():
        n3 = name3.get()
        r3 = roll3.get()

        sql="select count(*) from  students where Name=%s and Roll_no=%s"
        mycursor.execute(sql,(n3,r3))
        count=mycursor.fetchone()
        if(count[0]==1):
            x1 = btcs_801.get()
            x2 = btcs_802.get()
            x3 = btcs_803.get()
            x4 = btcs_804.get()
            x5 = btcs_805.get()
            x6 = btcs_806.get()
            x7 = btcs_807.get()
            x8 = btcs_808.get()

            m1 = mst11.get()
            m2 = mst12.get()
            m3 = mst13.get()
            m4 = mst14.get()
            m5 = mst15.get()

            s1 = mst21.get()
            s2 = mst22.get()
            s3 = mst23.get()
            s4 = mst24.get()
            s5 = mst25.get()

            t1 = mst31.get()
            t2 = mst32.get()
            t3 = mst33.get()
            t4 = mst34.get()
            t5 = mst35.get()

            x9 = sgpa.get()

            sql = "INSERT INTO sem_8 (Name,URN,btcs_801,btcs_802,btcs_803,btcs_804,btcs_805,btcs_806,btcs_807,btcs_808,mst1_btcs_801,mst1_btcs_802,mst1_btcs_803,mst1_btcs_804,mst1_btcs_805,mst2_btcs_801,mst2_btcs_802,mst2_btcs_803,mst2_btcs_804,mst2_btcs_805,mst3_btcs_801,mst3_btcs_802,mst3_btcs_803,mst3_btcs_804,mst3_btcs_805,sgpa) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (n3, r3,x1,x2,x3,x4,x5,x6,x7,x8, m1, m2, m3, m4, m5, s1, s2, s3,s4, s5, t1, t2, t3, t4, t5, x9)
            mycursor.execute(sql, val)
            mydb.commit()
            mb.showinfo("SAVED", "Result saved successfully.")
        else:
            mb.showerror("Error",'Invalid Student Name or Roll Number.')
    ###---End of save_result function---###

    btn3 = Button(bottom_frame3, text="Save", font=("arial", 30, "bold"), fg="white", bg="gray30",activebackground="gray90", command=save_result)
    btn3.place(x=680, y=650)

    
#=========================================ENTER RESULT 8=======================#

#==================================ADMIN BUTTON==============================#

def login_admin():
    un = uname.get()
    ps = password.get()
    if(un == 'admin' and ps == '@dmin'):
        u_entry.delete(0,"end")
        p_entry.delete(0,"end")
        wind_admin = Tk()
        wind_admin.title("MENU")
        w_width = wind_admin.winfo_screenwidth()
        w_height = wind_admin.winfo_screenheight()
        wind_admin.geometry("%dx%d+0+0" % (w_width,w_height))

        main_frame = Frame(wind_admin, height = w_height, width = w_width, bg = "gray10")
        main_frame.pack()

        btn_frame = Frame(main_frame, height=650,width=550,bg="gray90")
        btn_frame.place(x=500,y=100)

        def add_instructor():
            wind_inst = Tk()
            wind_inst.title("Add Instructors")
            w_width= wind_inst.winfo_screenwidth()
            w_height = wind_inst.winfo_screenheight()
            wind_inst.geometry("%dx%d+0+0" % (w_width,w_height))
            main_frame = Frame(wind_inst,height=w_height,width=w_width,bg="gray20")
            main_frame.pack()

            instructor_frame = Frame(main_frame,height=810,width=660,bg="gray90")
            instructor_frame.place(x=400,y=10)

            lb = Label(instructor_frame,text="Instuctor's Info.",font=("times new roman",30,"bold"),bg="gray90")
            lb.place(x=170,y=10)

            fullname = StringVar(wind_inst)
            email = StringVar(wind_inst)
            user = StringVar(wind_inst)
            pword = StringVar(wind_inst)
            course = StringVar(wind_inst)
            branch = StringVar(wind_inst)
            des = StringVar(wind_inst)

            lb = Label(instructor_frame,text="Full Name",font=("impact",18),bg="gray90")
            lb.place(x=50,y=90)
            fn_entry=Entry(instructor_frame,width="20",textvariable = fullname,bd=6,relief="ridge",font=("arial",15,"bold"))
            fn_entry.place(x=180,y=90)

            lb = Label(instructor_frame,text="E-mail",font=("impact",18),bg="gray90")
            lb.place(x=50,y=160)
            e_entry=Entry(instructor_frame,width="20",textvariable = email,bd=6,relief="ridge",font=("arial",15,"bold"))
            e_entry.place(x=180,y=160)

            lb = Label(instructor_frame,text="Username",font=("impact",18),bg="gray90")
            lb.place(x=50,y=230)
            un_entry=Entry(instructor_frame,width="20",textvariable=user,bd=6,relief="ridge",font=("arial",15,"bold"))
            un_entry.place(x=180,y=230)

            lb = Label(instructor_frame,text="Password",font=("impact",18),bg="gray90")
            lb.place(x=50,y=300)
            ps_entry=Entry(instructor_frame,width="20",textvariable=pword,bd=6,relief="ridge",font=("arial",15,"bold"))
            ps_entry.place(x=180,y=300)

            lb = Label(instructor_frame,text="Course",font=("impact",18),bg="gray90")
            lb.place(x=50,y=370)
            #c_entry=Entry(instructor_frame,width="20",textvariable=course,bd=6,relief="ridge",font=("arial",15,"bold"))
            c_combo = ttk.Combobox(instructor_frame,textvariable = course,font=("arial",15,"bold"),width=20)#,state="readonly")
            c_combo['values'] = ('B.Tech.','B.Sc.','M.Tech.','M.Sc.','Diploma')
            c_combo.place(x=180,y=370)
            c_combo.current()

            lb = Label(instructor_frame,text="Branch",font=("impact",18),bg="gray90")
            lb.place(x=50,y=440)
            #br_entry=Entry(instructor_frame,width="20",textvariable=branch,bd=6,relief="ridge",font=("arial",15,"bold"))
            c_value = course.get()
            br_combo = ttk.Combobox(instructor_frame,textvariable = branch,font=("arial",15,"bold"),width=20)
            br_combo['values'] = ('CSE','IT','ME','ECE','Biotech','Chemical','Civil','Agriculture','Thermal','Production','Chemistry','Physics')
            
            '''if(c_value == 'B.Tech.'):
                br_combo['values'] = ('CSE','IT','ME','ECE','Biotech','Chemical','Civil')
            elif(c_value == 'B.Sc.'):
                br_combo['values'] = ('Agriculture')
            elif(c_value == 'M.Tech.'):
                br_combo['values'] = ('CSE','ECE','Chemical','Thermal','Production')
            elif(c_value == 'M.Sc.'):
                br_combo['values'] = ('Chemistry','Physics')
            else:
                br_combo['values'] = ('CSE','ME','ECE')'''

            br_combo.place(x=180,y=440)
            br_combo.current()
            
            lb = Label(instructor_frame,text="Designation",font=("impact",18),bg="gray90")
            lb.place(x=50,y=510)
            des_entry=Entry(instructor_frame,width="20",textvariable=des,bd=6,relief="ridge",font=("arial",15,"bold"))
            des_entry.place(x=180,y=510)

            def get_pass():
                ps_entry.delete(0,"end")
                p = str()
                characters = "abcdefeghijklmnopqrstuvwxyz0123456789@#$%&"
                for i in range(0,8):
                    p = p + random.choice(characters)
                ps_entry.insert(0,p)

            btn = Button(instructor_frame,text="Get Password",font=("times new roman",15,"bold"),fg="black",bg="gray99",activebackground="gray90",command=get_pass)
            btn.place(x=480,y=300)

###==========ADD BUTTON===========###
            def add_instructor():

                fn = fullname.get()
                em = email.get()
                us = user.get()
                pw = pword.get()
                c = course.get()
                b = branch.get()
                desg = des.get()
                
                un = uname.get()
                ps = password.get()
                sql = "INSERT INTO instructors (Full_Name,Email,Username,Password,Course,Branch,Designation) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                val = (fn,em,us,pw,c,b,desg)
                mycursor.execute(sql, val)
                mydb.commit()

                fn_entry.delete(0,"end")
                e_entry.delete(0,"end")
                un_entry.delete(0,"end")
                ps_entry.delete(0,"end")
                c_combo.delete(0,"end")
                br_combo.delete(0,"end")
                des_entry.delete(0,"end")

            btn = Button(instructor_frame,text="ADD",font=("times new roman",25,"bold"),fg="black",bg="gray99",activebackground="gray90",command=add_instructor)
            btn.place(x=280,y=670)
            
        btn = Button(btn_frame,text="Add Instructors",font=("times new roman",30,"bold","italic"),fg="black",bg="light sky blue",activebackground="deep sky blue",command=add_instructor)
        btn.place(x=125,y=100)
#========================================ADD STUDENTS=========================#
        def add_students():
            stud_wind = Tk()
            stud_wind.title("Student Details")
            w_width = stud_wind.winfo_screenwidth()
            w_height = stud_wind.winfo_screenheight()
            stud_wind.geometry("%dx%d+0+0" % (w_width,w_height))

            main_frame = Frame(stud_wind,height=w_height,width=w_width,bg="gray20")
            main_frame.pack()

            stud_frame = Frame(main_frame,height=810,width=660,bg="gray90")
            stud_frame.place(x=400,y=10)

            lb = Label(stud_frame,text="Student's Info.",font=("times new roman",30,"bold"),bg="gray90")
            lb.place(x=170,y=10)

            nm = StringVar(stud_wind)
            rn = StringVar(stud_wind)
            email = StringVar(stud_wind)
            user = StringVar(stud_wind)
            pword = StringVar(stud_wind)
            course = StringVar(stud_wind)
            branch = StringVar(stud_wind)
            sem = StringVar(stud_wind)

            lb = Label(stud_frame,text="Full Name",font=("impact",18),bg="gray90")
            lb.place(x=80,y=90)
            fn_entry=Entry(stud_frame,width="20",textvariable = nm,bd=6,relief="ridge",font=("arial",15,"bold"))
            fn_entry.place(x=210,y=90)

            lb = Label(stud_frame,text="Roll No.",font=("impact",18),bg="gray90")
            lb.place(x=80,y=160)
            rn_entry=Entry(stud_frame,width="20",textvariable=rn,bd=6,relief="ridge",font=("arial",15,"bold"))
            rn_entry.place(x=210,y=160)

            lb = Label(stud_frame,text="E-mail",font=("impact",18),bg="gray90")
            lb.place(x=80,y=230)
            e_entry=Entry(stud_frame,width="20",textvariable = email,bd=6,relief="ridge",font=("arial",15,"bold"))
            e_entry.place(x=210,y=230)

            lb = Label(stud_frame,text="Username",font=("impact",18),bg="gray90")
            lb.place(x=80,y=300)
            un_entry=Entry(stud_frame,width="20",textvariable=user,bd=6,relief="ridge",font=("arial",15,"bold"))
            un_entry.place(x=210,y=300)

            lb = Label(stud_frame,text="Password",font=("impact",18),bg="gray90")
            lb.place(x=80,y=370)
            ps_entry=Entry(stud_frame,width="20",textvariable=pword,bd=6,relief="ridge",font=("arial",15,"bold"))
            ps_entry.place(x=210,y=370)

            lb = Label(stud_frame,text="Course",font=("impact",18),bg="gray90")
            lb.place(x=80,y=440)
            #c_entry=Entry(instructor_frame,width="20",textvariable=course,bd=6,relief="ridge",font=("arial",15,"bold"))
            c_combo = ttk.Combobox(stud_frame,textvariable = course,font=("arial",15,"bold"),width=20) #,state = "readonly")
            c_combo['values'] = ('B.Tech.','B.Sc.','M.Tech.','M.Sc.','Diploma')
            c_combo.place(x=210,y=440)
            c_combo.current()

            lb = Label(stud_frame,text="Branch",font=("impact",18),bg="gray90")
            lb.place(x=80,y=510)
            #br_entry=Entry(instructor_frame,width="20",textvariable=branch,bd=6,relief="ridge",font=("arial",15,"bold"))
            c_value = course.get()
            br_combo = ttk.Combobox(stud_frame,textvariable = branch,font=("arial",15,"bold"),width=20)
            br_combo['values'] = ('CSE','IT','ME','ECE','Biotech','Chemical','Civil','Agriculture','Thermal','Production','Chemistry','Physics')
            
            '''if(c_value == 'B.Tech.'):
                br_combo['values'] = ('CSE','IT','ME','ECE','Biotech','Chemical','Civil')
            elif(c_value == 'B.Sc.'):
                br_combo['values'] = ('Agriculture')
            elif(c_value == 'M.Tech.'):
                br_combo['values'] = ('CSE','ECE','Chemical','Thermal','Production')
            elif(c_value == 'M.Sc.'):
                br_combo['values'] = ('Chemistry','Physics')
            else:
                br_combo['values'] = ('CSE','ME','ECE')'''

            br_combo.place(x=210,y=510)
            br_combo.current()

            lb = Label(stud_frame,text="Semester",font=("impact",18),bg="gray90")
            lb.place(x=80,y=580)
            sem_combo = ttk.Combobox(stud_frame,textvariable = sem,font=("arial",15,"bold"),width=20)
            sem_combo['values'] = ('1','2','3','4','5','6','7','8')
            sem_combo.place(x=210,y=580)
            sem_combo.current()
            
            
            def add_stu():
                name = nm.get()
                roll = rn.get()
                em = email.get()
                un = user.get()
                pw = pword.get()
                c = course.get()
                br = branch.get()
                s = sem.get()
                
                print("Name: ",name)
                sql = "INSERT INTO students (Name,Roll_no,Email,Username,Password,Course,Branch,Semester) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (name,roll,em,un,pw,c,br,s)
                mycursor.execute(sql, val)
                mydb.commit()
                print(mycursor.rowcount,"Record inserted")

                fn_entry.delete(0,"end")
                rn_entry.delete(0,"end")
                e_entry.delete(0,"end")
                un_entry.delete(0,"end")
                ps_entry.delete(0,"end")
                c_combo.delete(0,"end")
                br_combo.delete(0,"end")
                sem_combo.delete(0,"end")
                
            btn = Button(stud_frame,text="ADD",font=("times new roman",25,"bold"),fg="black",bg="gray99",activebackground="gray90",command=add_stu)
            btn.place(x=280,y=670)

        btn = Button(btn_frame,text="Add Students",font=("times new roman",30,"bold","italic"),fg="black",bg="light sky blue",activebackground="deep sky blue",command = add_students)
        btn.place(x=145,y=270)

        btn = Button(btn_frame,text="View Result",font=("times new roman",30,"bold","italic"),fg="black",bg="light sky blue",activebackground="deep sky blue",command=view_res)
        btn.place(x=155,y=440)
    else:
        mb.showerror("Error",'invalid username or password')
            
btn=Button(login_frame,text="Login as Admin",font=("arial",15),fg="black",bg="gray90",activebackground="gray85",command=login_admin,width=20)
btn.place(x=105,y=210)
#==================================ADMIN BUTTON==============================#

#==================================HOD BUTTON================================#

def students():
    wind_list = Tk()
    r_width = wind_list.winfo_screenwidth()
    r_height = wind_list.winfo_screenheight()
    wind_list.title("Result Window")
    wind_list.geometry("%dx%d+0+0" % (r_width,r_height))
    
    def update(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert("","end",values = i)

    def search():
        q2 = q.get()
        query = "select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students WHERE Roll_no LIKE '%"+q2+"%'"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    def clear():
        query = "select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students"
        mycursor.execute(query)
        rows = mycursor.fetchall()
        update(rows)

    q = StringVar(wind_list)

    wrapper2 = LabelFrame(wind_list,text = "Search",height="100")
    wrapper1 = LabelFrame(wind_list,text = "Students")

    wrapper2.pack(fill=X,padx=20,pady=20)
    wrapper1.pack(fill="both",expand="yes",padx=20,pady=20)

    trv = ttk.Treeview(wrapper1,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="30")
    trv.pack()

    trv.column("1", width = 100, anchor ='c')
    trv.column("2", width = 150, anchor ='sw')
    trv.column("3", width = 100, anchor ='c')
    trv.column("4", width = 200, anchor ='c')
    trv.column("5", width = 100, anchor ='c')
    trv.column("6", width = 100, anchor ='c')
    trv.column("7", width = 100, anchor ='c')
    trv.column("8", width = 100, anchor ='c')
    trv.column("9", width = 100, anchor ='c')
            
    trv.heading("1", text ="S.No.")
    trv.heading("2", text ="Name")
    trv.heading("3", text ="Roll No.")
    trv.heading("4", text ="Email")
    trv.heading("5", text ="Username")
    trv.heading("6", text ="Password")
    trv.heading("7", text ="Course")
    trv.heading("8", text ="Branch")
    trv.heading("9", text ="Semester")
                
    query ="select ID,Name,Roll_no,Email,Username,Password,Course,Branch,Semester from students"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    update(rows)

    treeXScroll = ttk.Scrollbar(wrapper1, orient=HORIZONTAL)
    treeXScroll.pack(side=BOTTOM,expand="yes",fill=X)
    treeXScroll.configure(command=trv.xview)
    trv.configure(xscrollcommand=treeXScroll.set)

    ###Search Section

    lbl = Label(wrapper2,text = "Search",font=("times new roman",16,"bold"))
    ent = Entry(wrapper2,textvariable=q,font=("times new roman",12))
    btn = Button(wrapper2,text = "Search",command = search,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")
    cbtn = Button(wrapper2,text = "Clear",command = clear,font=("times new roman",13,"bold"),fg="white",bg="gray22",activebackground="gray80")

    lbl.place(x=550,y=25)
    ent.place(x=640,y=27)
    btn.place(x=830,y=23)
    cbtn.place(x=920,y=23)


def view_res():
    wind_stu = Tk()
    wind_stu.title("VIEW Result")
    w_width = wind_stu.winfo_screenwidth()
    w_height = wind_stu.winfo_screenheight()
    wind_stu.geometry("%dx%d+0+0" % (w_width,w_height))

    main_frame = Frame(wind_stu,height=w_height,width=w_width,bg="gray20")
    main_frame.pack()

    stu_frame = Frame(main_frame,height=810,width=660,bg="gray90")
    stu_frame.place(x=410,y=10)

    lb = Label(stu_frame,text="SELECT SEMESTER:",font=("times new roman",30,"bold"),bg="gray90")
    lb.place(x=150,y=10)

    btn1 = Button(stu_frame,text="Sem 1",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_1)
    btn1.place(x=250,y=90)

    btn2 = Button(stu_frame,text="Sem 2",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_2)
    btn2.place(x=250,y=175)

    btn3 = Button(stu_frame,text="Sem 3",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_3)
    btn3.place(x=250,y=260)

    btn4 = Button(stu_frame,text="Sem 4",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_4)
    btn4.place(x=250,y=345)

    btn5 = Button(stu_frame,text="Sem 5",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_5)
    btn5.place(x=250,y=430)

    btn6 = Button(stu_frame,text="Sem 6",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_6)
    btn6.place(x=250,y=515)

    btn7 = Button(stu_frame,text="Sem 7",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_7)
    btn7.place(x=250,y=600)

    btn8 = Button(stu_frame,text="Sem 8",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_8)
    btn8.place(x=250,y=685)

def login_hod():
    un = uname.get()
    pw = password.get()
    sql="select count(*) from instructors where Username=%s and Password=%s and Designation = 'HOD'"
    try:
        mycursor.execute(sql,(un,pw))
        count=mycursor.fetchone()
        if(count[0]==1):
            print("you are successfully logged-in")
            #root.withdraw()
            u_entry.delete(0,"end")
            p_entry.delete(0,"end")
            wind_hod = Tk()
            wind_hod.title("Student's Details")
            w_width = wind_hod.winfo_screenwidth()
            w_height = wind_hod.winfo_screenheight()
            wind_hod.geometry("%dx%d+0+0" % (w_width,w_height))

            main_frame = Frame(wind_hod, height = w_height, width = w_width, bg = "gray10")
            main_frame.pack()

            btn_frame = Frame(main_frame, height=500,width=480,bg="gray90")
            btn_frame.place(x=500,y=160)

            btn = Button(btn_frame,text="View Students",font=("times new roman",30,"bold","italic"),fg="black",bg="light sky blue",activebackground="deep sky blue",command=students)
            btn.place(x=125,y=120)

            btn = Button(btn_frame,text=" View Result ",font=("times new roman",30,"bold","italic"),fg="black",bg="light sky blue",activebackground="deep sky blue",command=view_res)
            btn.place(x=125,y=310)

            
        else:
            mb.showerror("Error",'Invalid username or password')
            
    except (mysql.connector.Error) as e:
        print(e)
        
btn=Button(login_frame,text="Login as HOD",font=("arial",15),fg="black",bg="gray90",activebackground="gray85",command=login_hod,width=20)
btn.place(x=105,y=270)
#==================================HOD BUTTON================================#

#==================================INSTRUCTOR BUTTON=========================#

def login_inst():
    un = uname.get()
    pw = password.get()
    sql="select count(*) from instructors where Username=%s and Password=%s and Designation = 'Professor'"
    try:
        mycursor.execute(sql,(un,pw))
        count=mycursor.fetchone()
        if(count[0]==1):
            print("you are successfully logged-in")
            #root.withdraw()
            u_entry.delete(0,"end")
            p_entry.delete(0,"end")
            wind_inst = Tk()
            wind_inst.title("ADD/VIEW Result")
            w_width = wind_inst.winfo_screenwidth()
            w_height = wind_inst.winfo_screenheight()
            wind_inst.geometry("%dx%d+0+0" % (w_width,w_height))

            frm = Frame(wind_inst,height=w_height,width=w_width,bg="gray10")
            frm.pack(side="top")

            left_frame = Frame(frm,height=800,width=600,bg="gray90")
            left_frame.place(x=100,y=20)

            right_frame = Frame(frm,height=800,width=600,bg="gray90")
            right_frame.place(x=800,y=20)

            lb1 = Label(left_frame,text="ENTER RESULT FOR:",font=("arial",30,"italic"),bg="black",fg="white")
            lb1.place(x=85,y=5)

            btn1 = Button(left_frame,text="Sem 1",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_1)
            btn1.place(x=240,y=90)

            btn2 = Button(left_frame,text="Sem 2",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_2)
            btn2.place(x=240,y=175)

            btn3 = Button(left_frame,text="Sem 3",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_3)
            btn3.place(x=240,y=260)

            btn4 = Button(left_frame,text="Sem 4",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_4)
            btn4.place(x=240,y=345)

            btn5 = Button(left_frame,text="Sem 5",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_5)
            btn5.place(x=240,y=430)

            btn6 = Button(left_frame,text="Sem 6",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_6)
            btn6.place(x=240,y=515)

            btn7 = Button(left_frame,text="Sem 7",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_7)
            btn7.place(x=240,y=600)

            btn8 = Button(left_frame,text="Sem 8",bg="ivory4",activebackground="ivory2",font = ("arial",20,"bold italic"),command=enter_result_8)
            btn8.place(x=240,y=685)



            lb2 = Label(right_frame,text="VIEW RESULT FOR:",font=("arial",30,"italic"),bg="black",fg="white")
            lb2.place(x=100,y=5)

            btn1 = Button(right_frame,text="Sem 1",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_1)
            btn1.place(x=240,y=90)

            btn2 = Button(right_frame,text="Sem 2",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_2)
            btn2.place(x=240,y=175)

            btn3 = Button(right_frame,text="Sem 3",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_3)
            btn3.place(x=240,y=260)

            btn4 = Button(right_frame,text="Sem 4",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_4)
            btn4.place(x=240,y=345)

            btn5 = Button(right_frame,text="Sem 5",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_5)
            btn5.place(x=240,y=430)

            btn6 = Button(right_frame,text="Sem 6",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_6)
            btn6.place(x=240,y=515)

            btn7 = Button(right_frame,text="Sem 7",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_7)
            btn7.place(x=240,y=600)

            btn8 = Button(right_frame,text="Sem 8",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_8)
            btn8.place(x=240,y=685)
                
        else:
            mb.showerror("Error",'Invalid username or password')
            
    except (mysql.connector.Error) as e:
        print(e)
        
btn=Button(login_frame,text="Login as Instructor",font=("arial",15),fg="black",bg="gray90",activebackground="gray85",command=login_inst,width=20)
btn.place(x=105,y=330)
#==================================INSTRUCTOR BUTTON=========================#

#==================================STUDENT BUTTON=========================#

def login_stu():
    un = uname.get()
    pw = password.get()
    sql="select count(*) from students where Username=%s and Password=%s"
    try:
        mycursor.execute(sql,(un,pw))
        count=mycursor.fetchone()
        if(count[0]==1):
            print("you are successfully logged-in")
            u_entry.delete(0,"end")
            p_entry.delete(0,"end")
            wind_stu = Tk()
            wind_stu.title("VIEW Result")
            w_width = wind_stu.winfo_screenwidth()
            w_height = wind_stu.winfo_screenheight()
            wind_stu.geometry("%dx%d+0+0" % (w_width,w_height))

            main_frame = Frame(wind_stu,height=w_height,width=w_width,bg="gray20")
            main_frame.pack()

            stu_frame = Frame(main_frame,height=810,width=660,bg="gray90")
            stu_frame.place(x=410,y=10)

            lb = Label(stu_frame,text="SELECT SEMESTER:",font=("times new roman",30,"bold"),bg="gray90")
            lb.place(x=150,y=10)

            btn1 = Button(stu_frame,text="Sem 1",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_1)
            btn1.place(x=250,y=90)

            btn2 = Button(stu_frame,text="Sem 2",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_2)
            btn2.place(x=250,y=175)

            btn3 = Button(stu_frame,text="Sem 3",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_3)
            btn3.place(x=250,y=260)

            btn4 = Button(stu_frame,text="Sem 4",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_4)
            btn4.place(x=250,y=345)

            btn5 = Button(stu_frame,text="Sem 5",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_5)
            btn5.place(x=250,y=430)

            btn6 = Button(stu_frame,text="Sem 6",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_6)
            btn6.place(x=250,y=515)

            btn7 = Button(stu_frame,text="Sem 7",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_7)
            btn7.place(x=250,y=600)

            btn8 = Button(stu_frame,text="Sem 8",bg="DarkOrange1",activebackground="OrangeRed2",font = ("arial",20,"bold italic"),command=view_result_8)
            btn8.place(x=250,y=685)

        else:
            mb.showerror("Error",'Invalid username or password')
            
    except (mysql.connector.Error) as e:
        print(e)

btn=Button(login_frame,text="Login as Student",font=("arial",15),fg="black",bg="gray90",activebackground="gray85",command=login_stu,width=20)
btn.place(x=105,y=390)
#==================================STUDENT BUTTON=========================#
