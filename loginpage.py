from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import pymysql
# -------------------------------
# creation des tables
conn=pymysql.connect(host='localhost',user='root',password='HN2002hn')
cur=conn.cursor()
try :
    sql='''use aot;'''
    cur.execute(sql)
except :
    sql='create database aot;'
    cur.execute(sql)
    sql='use airpl;'
    cur.execute(sql)
    sql='''create table avoin(
        NUMAV int primary key,
        TYPAV varchar(20) not null,
        DATMS date not null);'''
    cur.execute(sql)
    sql='''create table revision( 
        NUMREV int primary key,
        anom varchar(20)  ,
        rep varchar(20),
        org varchar(20),
        DATEREV date not null,
        NUMAV int ,
        foreign key (NUMAV) references avoin(NUMAV)
        );'''
    cur.execute(sql)
    sql='''create table vol(
        NUMVOL int primary key,
        VILDEP varchar(20) not null,
        VILARR varchar(20) not null,
        HDEP time not null,
        DURVOL int not null);'''
    cur.execute(sql)
    sql='''create table avoin_vol(
        NUMVOL int ,
        foreign key (NUMVOL) references vol(NUMVOL),
        NUMAV int ,
        foreign key (NUMAV) references avoin(NUMAV),
        datevol date not null);'''
    cur.execute(sql)
    sql='''create table navig(
        NUMNAV int primary key,
        NOM_NAV varchar(20) not null,
        PRENOM_NAV varchar(20) not null,
        TEL_NAV bigint not null,
        VIL_NAV varchar(20) ,
        QRT_NAV varchar(20),
        CDP_NAV varchar(20),
        SAL_NAV float ,
        DATEMB_NAV date);'''
    cur.execute(sql)
    sql='''create table nonnavig(
        NUMNONNAV int primary key,
        NOM_NONNAV varchar(20) not null,
        PRENOM_NONNAV varchar(20) not null,
        TEL_NONNAV bigint not null,
        VIL_NONNAV varchar(20) ,
        QRT_NONNAV varchar(20),
        CDP_NONNAV varchar(20),
        SAL_NONNAV float ,
        DATEMB_NONNAV date);'''
    cur.execute(sql)
    sql='''create table nav_vol(
        NUMVOL int,
        foreign key (NUMVOL) references vol(NUMVOL),
        NUMNAV int,
        foreign key (NUMNAV) references navig(NUMNAV))'''
    cur.execute(sql)
    sql='''create table avoin_nonnav(
        NUMNONNAV  int,
        foreign key (NUMNONNAV) references nonnavig(NUMNONNAV),
        NUMAV  int,
        foreign key (NUMAV) references avoin(NUMAV))'''
    cur.execute(sql)
    sql='''create table escale(
        NUMESCL int primary key,
        VILESC varchar(20) not null,
        HARRESC time not null,
        DURESC int not null);'''
    cur.execute(sql)
    sql='''create table escl_vol(
        NUMVOL int,
        foreign key (NUMVOL) references vol(NUMVOL),
        NUMESCL  int,
        foreign key (NUMESCL) references escale(NUMESCL),
        NOOD int not null);'''
    cur.execute(sql)
    sql='''create table users(
        id int primary key,username varchar(20),email longtext,pasword varchar(20))'''
    cur.execute(sql)
    sql='''INSERT into users 
    values
    (1,"hamza-nachid","hamzanachid82@gmail.com","HN2002hn"),
    (2,"hajar-aloua","hajaraloua83@gmail.com","wjah13"),
    (3,"chaimaa-ari","chaimaaari84@gmail.com","ariari") '''
    cur.execute(sql)
    conn.commit()
# -------------------------------
root=tk.ThemedTk()
root.geometry("798x500")
root.resizable(0,0)
root.title("AOT AIRPORT")
root.iconbitmap("iconapp.ico")
# ---------------------------------
framer=Frame(root,height=520,width=450 )
framer.place(x=-2,y=-2)
imagelogo=ImageTk.PhotoImage(file='test143.jpg')
lb1=Label(framer,image=imagelogo,bg='white')
lb1.place(x=0,y=0)
framel=Frame(root,height=520,width=400,bg='white')
framel.place(x=448,y=0)
wl=Label(framel,text='Welcome to our company',font=('Comic Sans MS', 20, 'bold'),bg='white',fg='MistyRose4')
wl.place(x=10,y=20)
wle=Label(framel,text='Welcome Back',font=('Comic Sans MS', 10, 'bold'),bg='white',fg='MistyRose4')
wle.place(x=15,y=90)
wle=Label(framel,text='Please Login to your account',font=('Comic Sans MS', 10, 'bold'),bg='white',fg='MistyRose4')
wle.place(x=15,y=110)
# ------------------------------------------
imagu=ImageTk.PhotoImage(file='userlog.png')
lb1=Label(framel,image=imagu,bg='white')
lb1.place(x=10,y=182)
usere = Entry(framel, bg='#1A2E35', font=('Comic Sans MS', 15, 'bold'),fg='white', borderwidth=0, width=23)
usere.place(x=55, y=185)
# -----------------------------------------------
imagelog=ImageTk.PhotoImage(file='mail.png')
lb1=Label(framel,image=imagelog,bg='white')
lb1.place(x=10,y=252)
emailen = Entry(framel, bg='#1A2E35', font=('Comic Sans MS', 15, 'bold'),fg='white', borderwidth=0, width=23)
emailen.place(x=55, y=255)
imagelogs=ImageTk.PhotoImage(file='padlock1.png')
lb1=Label(framel,image=imagelogs,bg='white')
lb1.place(x=10,y=320)
passwe = Entry(framel , bg='#1A2E35', font=('Comic Sans MS', 15, 'bold'),fg='white', borderwidth=0, width=23)
passwe.place(x=55, y=325)
def login():
    sql='''select username,email,pasword from users '''
    cur.execute(sql)
    users=cur.fetchall()
    if (usere.get(),emailen.get(),passwe.get()) in users:
        root.destroy()
        import airport
    elif usere.get()=='UserName':
        messagebox.showerror('ERROR','the user name is empty')
    elif emailen.get()=='Email':
        messagebox.showerror('ERROR','the email is empty')
    elif passwe.get()=='Password':
        messagebox.showerror('ERROR','the Password is empty')
    else:
        messagebox.showerror('ERROR', 'the information incorrect')
lbrlog = Button(framel, text='Login', font=('Comic Sans MS', 14, 'bold'), bg='grey60', fg='white',
                activeforeground='white', activebackground='azure3', borderwidth=1, width=15,command=login )
lbrlog.place(x=95, y=400)
usere.insert(0,"UserName")
def on_enter(event):
    usere.config(state=NORMAL)
    if usere.get()=='UserName':
         usere.delete(0,END)
usere.bind("<Button-1>",on_enter)
def on_leave(event):
    if usere.get()=='':
        usere.insert(0, "UserName")
usere.bind("<FocusOut>",on_leave)
emailen.insert(0,"Email")
def on_enter(event):
    emailen.config(state=NORMAL)
    if emailen.get()=='Email':
         emailen.delete(0,END)
emailen.bind("<Button-1>",on_enter)
def on_leave(event):
    if emailen.get()=='':
        emailen.insert(0, "Email")
emailen.bind("<FocusOut>",on_leave)
passwe.insert(0,"Password")
def on_enter(event):
    passwe.config(state=NORMAL)
    if passwe.get()=='Password':
         passwe.delete(0,END)
passwe.bind("<Button-1>",on_enter)
def on_leave(event):
    if passwe.get()=='':
        passwe.insert(0, "Password")
passwe.bind("<FocusOut>",on_leave)
root.mainloop()