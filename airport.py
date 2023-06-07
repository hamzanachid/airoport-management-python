from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import  pymysql
import datetime
# --------------- creation window principale------------------------
root=tk.ThemedTk()
root.geometry("750x500+300+100")
root.resizable(0,0)
root.set_theme('elegance')
root.title("AOT AIRPORT")
root.iconbitmap("iconapp.ico")

















# --------------------------conction to mysql
conn=pymysql.connect(host='localhost',user='root',password='HN2002hn')
cur=conn.cursor()
sql = '''use aot;'''
cur.execute(sql)
frame_pricipale =Frame(root,width=750,height=500,bg='grey60')
frame_pricipale.place(x=0,y=0)
title=Label(frame_pricipale,text='AOT AIRPORT',font=('Times', 20, 'bold'),bg='grey60',fg='#1A2E35')
title.place(x=280,y=20)
def tim(dat):
    l=dat.split('-')
    if len(l)!=3:
        return False
    if len(str(l[0])) !=4 or len(str(l[1])) not in (1,2) or len(str(len(l[2]))) not in (1,2) or int(l[1])>12 or int(l[2])>31:
        return False
    return True


def timetcheck(l):
    if len(list(map(str, filter(lambda x: x in (':'), l)))) != 2:
        return False
    if int(l.split(':')[0]) > 23 or int(l.split(':')[1]) > 60 or int(l.split(':')[2]) > 60:
        return False

    return True

def MONTH_YEARcheck(l):
    if len(list(map(str, filter(lambda x: x in ('-'), l)))) != 1:
        return False
    if int(l.split('-')[1]) > 12:
        return False

    return True
# -------------------------------avoin interface-----------------------
# DaunPenh
# DokChampa
# Estrangelo Edessa
# Euphemia
# Gautami
# Roman
# Script
def avoin():
    avoin=Toplevel()
    avoin.geometry('1030x590+200+70')
    avoin.resizable(0,0)
    # -------------------------------------creation first_frame
    first_frame=Frame(avoin,width=1100,height=200,bg='#1A2E35')
    first_frame.place(x=0,y=0)
    labl_title = Label(first_frame, text='AIRPLANE SPACE', font=('Times', 17, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    labl_title.place(x=400, y=-5)







    # -------------------------------------add new airplane
    labl_title = Label(first_frame, text='add or delete an airplane', font=('Times', 12, 'bold'), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=35, y=32)
    # -------------------------------------entry numav
    input_NUMAV = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_NUMAV.place(x=10, y=60)
    input_NUMAV.insert(0, "id-airplane")

    def on_enter(event):
        input_NUMAV.config(state=NORMAL)
        if input_NUMAV.get() == 'id-airplane':
            input_NUMAV.delete(0, END)

    input_NUMAV.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMAV.get() == '':
            input_NUMAV.insert(0, "id-airplane")

    input_NUMAV.bind("<FocusOut>", on_leave)
    # ----------------------------------------------entry airplane-type
    input_TYPAV = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_TYPAV.place(x=130, y=60)
    input_TYPAV.insert(0, "airplane-type")

    def on_enter(event):
        input_TYPAV.config(state=NORMAL)
        if input_TYPAV.get() == 'airplane-type':
            input_TYPAV.delete(0, END)

    input_TYPAV.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_TYPAV.get() == '':
            input_TYPAV.insert(0, "airplane-type")

    input_TYPAV.bind("<FocusOut>", on_leave)
    # ------------------------------- entry launch-date
    input_dtms = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_dtms.place(x=65, y=100)
    input_dtms.insert(0, "launch-date")

    def on_enter(event):
        input_dtms.config(state=NORMAL)
        if input_dtms.get() == 'launch-date':
            input_dtms.delete(0, END)

    input_dtms.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_dtms.get() == '':
            input_dtms.insert(0, "launch-date")

    input_dtms.bind("<FocusOut>", on_leave)

    # -------------------------------------------fonction add new airplane
    def add():
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        if input_NUMAV.get() == 'id-airplane' or input_dtms.get() == 'launch-date' or input_TYPAV.get() == 'airplane-type' or \
                input_NUMAV.get() == '' or input_dtms.get() == '' or input_TYPAV.get() == '':
            tiir.place_forget()
            tiir2.place_forget()
            tiir3.place_forget()
            tiir4.place_forget()
            tiir1.place(x=50, y=180)
        elif tim(input_dtms.get()) == False:
            tiir.place_forget()
            tiir2.place_forget()
            tiir3.place_forget()
            tiir1.place_forget()
            tiir4.place(x=70, y=180)
        elif int(input_NUMAV.get()) in l:
            tiir1.place_forget()
            tiir2.place_forget()
            tiir4.place_forget()
            tiir3.place_forget()
            tiir.place(x=50, y=180)
        else:
            tiir1.place_forget()
            tiir.place_forget()
            tiir3.place_forget()
            tiir2.place_forget()
            sql = 'insert into avoin values({},%s,%s)'.format(input_NUMAV.get())
            cur.execute(sql, (input_TYPAV.get(), input_dtms.get()))
            conn.commit()
            val = (input_NUMAV.get(), input_TYPAV.get(), input_dtms.get())
            tree.insert(parent='', index=val[0], iid=val[0], text='', values=val)
            tiir.place_forget()
            tiir1.place_forget()

    btnadd = Button(first_frame, text='add', font=('Times', 13, 'bold'), borderwidth=0, width=10, background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35', command=add)
    btnadd.place(x=15, y=140)

    # ----------------------------------delete fonction
    def dele():
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        if input_NUMAV.get() == 'id-airplane' or input_NUMAV.get() == '':
            tiir.place_forget()
            tiir1.place_forget()
            tiir2.place_forget()
            tiir3.place(x=70,y=180)
        elif int(input_NUMAV.get()) not in l:
            tiir.place_forget()
            tiir1.place_forget()
            tiir3.place_forget()
            tiir2.place(x=70,y=180)
        else:
            tiir1.place_forget()
            tiir.place_forget()
            tiir3.place_forget()
            tiir2.place_forget()
            tree.delete(input_NUMAV.get())
            cur.execute('SET FOREIGN_KEY_CHECKS=0;')
            cur.execute('delete from avoin where NUMAV={}'.format(input_NUMAV.get()))
            cur.execute('delete from revision where NUMAV={}'.format(input_NUMAV.get()))
            cur.execute('delete from avoin_vol where NUMAV={}'.format(input_NUMAV.get()))
            cur.execute('delete from avoin_nonnav where NUMAV={}'.format(input_NUMAV.get()))
            conn.commit()
    btndel = Button(first_frame, text='delete', font=('Times', 13, 'bold'), borderwidth=0, width=10, background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35',command=dele)
    btndel.place(x=135, y=140)
    tiir = Label(first_frame, text='id already exist', font=('Times', 10), bg='#1A2E35', fg='#5AE4A8')

    tiir1 = Label(first_frame, text='one of the  flieds is empty', font=('Times', 10), bg='#1A2E35', fg='#5AE4A8')











    # -----------------------------------------------search for an airplane by id
    labl_title = Label(first_frame, text='search for an airplane by id', font=('Times', 12, 'bold'), bg='#1A2E35',
                       fg='#D8D8D8')
    labl_title.place(x=295, y=32)
    input_NUMAVs = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_NUMAVs.place(x=285, y=60)
    input_NUMAVs.insert(0, "id-airplane")

    def on_enter(event):
        input_NUMAVs.config(state=NORMAL)
        if input_NUMAVs.get() == 'id-airplane':
            input_NUMAVs.delete(0, END)

    input_NUMAVs.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMAVs.get() == '':
            input_NUMAVs.insert(0, "id-airplane")

    input_NUMAVs.bind("<FocusOut>", on_leave)
    out_type = Entry(first_frame, bg='grey60', font=('Times', 15), fg='#1A2E35', borderwidth=0, width=11)
    out_type.place(x=285, y=105)
    out_type.insert(0, "airplane-type")
    out_type.config(state=DISABLED)
    out_NHLR = Entry(first_frame, bg='grey60', font=('Times', 15), fg='#1A2E35', borderwidth=0, width=10)
    out_NHLR.place(x=407, y=105)
    out_NHLR.insert(0, 'NHOLR')
    out_NHLR.config(state=DISABLED)
    out_dtms = Entry(first_frame, bg='grey60', font=('Times', 15), fg='#1A2E35', borderwidth=0, width=10)
    out_dtms.place(x=345, y=140)
    out_dtms.insert(0, ' launch-date')
    out_dtms.config(state=DISABLED)

    def ser():
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        if input_NUMAVs.get() == 'id-airplane' or input_NUMAVs.get() == '':
            tiir3.place(x=370, y=180)
            tiir2.place_forget()
        elif int(input_NUMAVs.get()) not in l:
            tiir3.place_forget()
            tiir2.place(x=370, y=180)
        else:
            tiir2.place_forget()
            tiir3.place_forget()
            sql = 'select * from avoin where NUMAV={}'.format(input_NUMAVs.get())
            cur.execute(sql)
            ser = cur.fetchall()
            out_type.config(state=NORMAL)
            out_type.delete(0, END)
            out_type.insert(0, ser[0][1])
            out_type.config(state=DISABLED)
            out_dtms.config(state=NORMAL)
            out_dtms.delete(0, END)
            out_dtms.insert(0, ser[0][2])
            out_dtms.config(state=DISABLED)
            sql = '''Select SUM(DURVOL) from avoin_vol inner join vol on vol.NUMVOL = avoin_vol.NUMVOL  where  avoin_vol.NUMAV={} and datevol>(select DATEREV FROM revision where REVISION.NUMAV={} order by DATEREV desc limit 1)'''.format(
                input_NUMAVs.get(), input_NUMAVs.get())
            cur.execute(sql)
            ser = cur.fetchall()
            print(ser)
            if ser[0][0] == None:
                out_NHLR.config(state=NORMAL)
                out_NHLR.delete(0, END)
                out_NHLR.insert(0, 0)
                out_NHLR.config(state=DISABLED)
            else:
                out_NHLR.config(state=NORMAL)
                out_NHLR.delete(0, END)
                out_NHLR.insert(0, ser[0][0])
                out_NHLR.config(state=DISABLED)

    tiir2 = Label(first_frame, text='id does not  exist', font=('Times', 10), bg='#1A2E35', fg='#5AE4A8')
    tiir3 = Label(first_frame, text='the field is empty', font=('Times', 10), bg='#1A2E35', fg='#5AE4A8')
    tiir4 = Label(first_frame, text='the input is not in dateformat ', font=('Times', 10), bg='#1A2E35', fg='#5AE4A8')
    btnser = Button(first_frame, text='search by id', font=('Times', 13, 'bold'),
                    borderwidth=0, width=10, background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35', command=ser)
    btnser.place(x=405, y=58)












    labl_title = Label(first_frame, text='search', font=('Times', 12, 'bold'), bg='#1A2E35',
                       fg='#D8D8D8')
    labl_title.place(x=575, y=33)
    input_typavs = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_typavs.place(x=540, y=60)
    input_typavs.insert(0, "airplane-type")

    def on_enter(event):
        input_typavs.config(state=NORMAL)
        if input_typavs.get() == 'airplane-type':
            input_typavs.delete(0, END)

    input_typavs.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_typavs.get() == '':
            input_typavs.insert(0, "airplane-type")

    input_typavs.bind("<FocusOut>", on_leave)
    def sert():
        search = Toplevel(avoin)
        search.geometry('300x250+329+120')
        search.resizable(0, 0)
        frame = Frame(search, width=300, height=250)
        frame.place(x=0, y=0)
        tree = ttk.Treeview(frame, height=12)
        tree['columns'] = ('id_airplane', 'airplane-type', 'commissioning-date')

        tree.column('#0', width=0, stretch=NO)
        tree.column('id_airplane', anchor=CENTER, width=80)
        tree.column('airplane-type', anchor=CENTER, width=90)
        tree.column('commissioning-date', anchor=CENTER, width=130)

        tree.heading('#0', anchor=CENTER, text='')
        tree.heading('id_airplane', anchor=CENTER, text='id_airplane')
        tree.heading('airplane-type', anchor=CENTER, text='airplane-type')
        tree.heading('commissioning-date', anchor=CENTER, text='commissioning-date')
        tree.place(x=0, y=0)
        sql = 'select * from avoin where TYPAV=%s'
        cur.execute(sql, (input_typavs.get()))
        rs = cur.fetchall()
        for i in rs:
            tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)

    #   ================================  BUTTON CHERCHER
    btnser = Button(first_frame, text='search by type', font=('Times', 13, 'bold'), borderwidth=0, width=11,
                    background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35', command=sert)
    btnser.place(x=544, y=100)









    labl_title = Label(first_frame, text='search for flight ', font=('Times', 12, 'bold'), bg='#1A2E35',
                       fg='#D8D8D8')
    labl_title.place(x=685, y=30)
    labl_title = Label(first_frame, text='search for technicien ', font=('Times', 12, 'bold'), bg='#1A2E35',
                       fg='#D8D8D8')
    labl_title.place(x=855, y=30)





    # ------------------------------
    def searchnav():
        try:
            search = Toplevel(avoin)
            search.geometry('200x250+750+120')
            search.resizable(0, 0)
            frame = Frame(search, width=300, height=250)
            frame.place(x=0, y=0)
            tree = ttk.Treeview(frame, height=12)
            tree['columns'] = ('id_tich', 'name_tich' )

            tree.column('#0', width=0, stretch=NO)
            tree.column('id_tich', anchor=CENTER, width=100)
            tree.column('name_tich', anchor=CENTER, width=100)

            tree.heading('#0', anchor=CENTER, text='')
            tree.heading('id_tich', anchor=CENTER, text='id_tich')
            tree.heading('name_tich', anchor=CENTER, text='name_tich')
            tree.place(x=0,y=0)
            sql='''select avoin_nonnav.NUMNONNAV,concat(NOM_NONNAV,'_',PRENOM_NONNAV )   from avoin_nonnav inner join nonnavig on avoin_nonnav.NUMNONNAV=nonnavig.NUMNONNAV where NUMAV={}'''.format(input_typa.get())
            cur.execute(sql)
            rs2=cur.fetchall()
            j=0
            for i in rs2:
                j+=1
                tree.insert(parent='', index=j, iid=j, text='', values=i)
        except:
            pass
    input_typa = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_typa.place(x=860, y=60)
    input_typa.insert(0, "airplane-id")

    def on_enter(event):
        input_typa.config(state=NORMAL)
        if input_typa.get() == 'airplane-id':
            input_typa.delete(0, END)

    input_typa.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_typa.get() == '':
            input_typa.insert(0, "airplane-id")

    input_typa.bind("<FocusOut>", on_leave)
    btnser = Button(first_frame, text='search by id', font=('Times', 13, 'bold'), borderwidth=0, width=11,
                    background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35',command=searchnav )
    btnser.place(x=865, y=100)
    # ------------------------------











    input_NUMAVa = Entry(first_frame, bg='grey60', font=('Times', 16, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_NUMAVa.place(x=680, y=60)
    input_NUMAVa.insert(0, "id-airplane")

    def on_enter(event):
        input_NUMAVa.config(state=NORMAL)
        if input_NUMAVa.get() == 'id-airplane':
            input_NUMAVa.delete(0, END)

    input_NUMAVa.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMAVa.get() == '':
            input_NUMAVa.insert(0, "id-airplane")

    input_NUMAVa.bind("<FocusOut>", on_leave)

    def servol():
        try:
            search = Toplevel(avoin)
            search.geometry('660x262+329+120')
            search.resizable(0, 0)
            frame = Frame(search, width=700, height=262)
            frame.place(x=0, y=0)
            tree = ttk.Treeview(frame, height=12)
            tree['columns'] = ('id_airplane', 'id-flight', 'depart-city','arrival-city','depart-hour','duration-flitgh','flight-date')

            tree.column('#0', width=0, stretch=NO)
            tree.column('id_airplane', anchor=CENTER, width=80)
            tree.column('id-flight', anchor=CENTER, width=80)
            tree.column('depart-city', anchor=CENTER, width=80)
            tree.column('arrival-city', anchor=CENTER, width=80)
            tree.column('depart-hour', anchor=CENTER, width=80)
            tree.column('duration-flitgh', anchor=CENTER, width=80)
            tree.column('flight-date', anchor=CENTER, width=180)

            tree.heading('#0', anchor=CENTER, text='')
            tree.heading('id_airplane', anchor=CENTER, text='id_airplane')
            tree.heading('id-flight', anchor=CENTER, text='id-flight')
            tree.heading('depart-city', anchor=CENTER, text='depart-city')
            tree.heading('arrival-city', anchor=CENTER, text='arrival-city')
            tree.heading('depart-hour', anchor=CENTER, text='depart-hour')
            tree.heading('duration-flitgh', anchor=CENTER, text='duration-flitgh')
            tree.heading('flight-date', anchor=CENTER, text='flight-date')
            tree.place(x=0, y=0)
            sql = '''select avoin.NUMAV,vol.NUMVOL,VILDEP,VILARR,HDEP,DURVOL,datevol from avoin inner join avoin_vol on avoin.NUMAV=avoin_vol.NUMAV
                    inner join vol on vol.NUMVOL=avoin_vol.NUMVOL where avoin.NUMAV={} '''.format(input_NUMAVa.get())
            cur.execute(sql)
            rs = cur.fetchall()
            j=0
            for i in rs:
                j+=1
                tree.insert(parent='', index=j, iid=j, text='', values=i)
        except:
            pass
    btnser = Button(first_frame, text='search', font=('Times', 13, 'bold'), borderwidth=0, width=11,
                    background='#5AE4A8',
                    activebackground='#5AE4A8', fg='#1A2E35', activeforeground='#1A2E35', command=servol)
    btnser.place(x=680, y=100)








    # ------------------------------table avoin
    second_frame = Frame(avoin, width=300, height=500, bg='#1A2E35')
    second_frame.place(x=0, y=400)
    av_table = Label(second_frame, text='AIRPLANE TABLE', font=('Times', 12, 'bold'), bg='#1A2E35', fg='#D8D8D8')
    av_table.place(x=65, y=0)
    tree = ttk.Treeview(second_frame, height=7)
    tree['columns'] = ('id_airplane', 'airplane-type', 'launch-date' )

    tree.column('#0', width=0, stretch=NO)
    tree.column('id_airplane', anchor=CENTER, width=70)
    tree.column('airplane-type', anchor=CENTER, width=100)
    tree.column('launch-date', anchor=CENTER, width=130)
    tree.heading('#0', anchor=CENTER, text='')
    tree.heading('id_airplane', anchor=CENTER, text='id_airplane')
    tree.heading('airplane-type', anchor=CENTER, text='airplane-type')
    tree.heading('launch-date', anchor=CENTER, text='launch-date')
    tree.place(x=0, y=30)








    sql = 'select * from avoin  '
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)







    # ------------------------- review table
    third_frame = Frame(avoin, width=800, height=300, bg='#1A2E35')
    third_frame.place(x=300, y=400)
    rev_table = Label(third_frame, text='REVIEW TABLE', font=('Times', 12, 'bold'), bg='#1A2E35', fg='#D8D8D8')
    rev_table.place(x=300, y=0)
    tree2 = ttk.Treeview(third_frame, height=7)
    tree2['columns'] = ('id-review', 'anomaly' ,'repairs','organs','review-date','id-airplane')
    tree2.column('#0', width=0, stretch=NO)
    tree2.column('id-review', anchor=CENTER, width=70)
    tree2.column('anomaly', anchor=CENTER, width=160)
    tree2.column('organs', anchor=CENTER, width=160)
    tree2.column('repairs', anchor=CENTER, width=160)
    tree2.column('review-date', anchor=CENTER, width=115)
    tree2.column('id-airplane', anchor=CENTER, width=64)

    tree2.heading('id-review', anchor=CENTER, text='id-review')
    tree2.heading('anomaly', anchor=CENTER, text='anomaly')
    tree2.heading('organs', anchor=CENTER, text='organs')
    tree2.heading('repairs', anchor=CENTER, text='repairs')
    tree2.heading('review-date', anchor=CENTER, text='review-date')
    tree2.heading('id-airplane', anchor=CENTER, text='id-airplane')
    tree2.place(x=0, y=30)
    sql = 'select * from revision '
    cur.execute(sql)
    rs1 = cur.fetchall()
    for i in rs1:
        tree2.insert(parent='', index=i[0], iid=i[0], text='', values=i)




    #-----------------------------------------------------------------------------------------------
    four_frame = Frame(avoin, width=1100, height=200, bg='#5AE4A8')
    four_frame.place(x=0, y=200)
    labl_title = Label(four_frame, text='REVIEW SPACE', font=('Times', 17, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=385, y=0)
    labl_title = Label(four_frame, text='add a review for an airplane', font=('Times', 13, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=50, y=25)
    labl_title = Label(four_frame, text='search for review\n of an airplane', font=('Times', 13, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=395, y=40)
    input_idair = Entry(four_frame, bg='grey60', font=('Times', 16,'bold'), fg='#1A2E35', borderwidth=0, width=12)
    input_idair.place(x=20, y=50)
    input_idair.insert(0, "id_airplane")

    def on_enter(event):
        input_idair.config(state=NORMAL)
        if input_idair.get() == 'id_airplane':
            input_idair.delete(0, END)

    input_idair.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_idair.get() == '':
            input_idair.insert(0, "id_airplane")

    input_idair.bind("<FocusOut>", on_leave)


    input_org = Entry(four_frame, bg='grey60', font=('Times', 16,'bold'), fg='#1A2E35', borderwidth=0, width=12)
    input_org.place(x=160, y=90)
    input_org.insert(0, "organs")

    def on_enter(event):
        input_org.config(state=NORMAL)
        if input_org.get() == 'organs':
            input_org.delete(0, END)

    input_org.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_org.get() == '':
            input_org.insert(0, "organs")

    input_org.bind("<FocusOut>", on_leave)

    input_an = Entry(four_frame,  bg='grey60', font=('Times', 16,'bold'), fg='#1A2E35', borderwidth=0, width=12)
    input_an.place(x=20, y=90)
    input_an.insert(0, "Anomaly")

    def on_enter(event):
        input_an.config(state=NORMAL)
        if input_an.get() == 'Anomaly':
            input_an.delete(0, END)

    input_an.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_an.get() == '':
            input_an.insert(0, "Anomaly")

    input_an.bind("<FocusOut>", on_leave)

    input_rep = Entry(four_frame,  bg='grey60', font=('Times', 16,'bold'), fg='#1A2E35', borderwidth=0, width=12)
    input_rep.place(x=160, y=50)
    input_rep.insert(0, "repairs")

    def on_enter(event):
        input_rep.config(state=NORMAL)
        if input_rep.get() == 'repairs':
            input_rep.delete(0, END)

    input_rep.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_rep.get() == '':
            input_rep.insert(0, "repairs")

    input_rep.bind("<FocusOut>", on_leave)

    def addr():
        if input_an.get() == 'Anomaly' or input_rep.get() == 'repairs' or input_idair.get() == 'id_airplane' or input_org.get() == 'organs':
            error9.place(x=95,y=170)
            error10.place_forget()
            error8.place_forget()
            return
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        if int(input_idair.get()) not in l:
            error8.place(x=95,y=170)
            error9.place_forget()
            error10.place_forget()
            return
        sql = '''select NUMVOL from avoin_vol where NUMAV={} '''.format(input_idair.get())
        cur.execute(sql)
        rev = cur.fetchall()
        if rev==():
            error10.place(x=95,y=170)
            error9.place_forget()
            error8.place_forget()
        else:
            error10.place_forget()
            error9.place_forget()
            error8.place_forget()
            sql = 'select NUMREV from revision order by  NUMREV desc limit 1'
            cur.execute(sql)
            nbrrev = cur.fetchall()
            sql = 'insert into revision values({},%s,%s,%s,now(),{})'.format(nbrrev[0][0] + 1, input_idair.get())
            cur.execute(sql, (input_an.get(), input_rep.get(), input_org.get()))
            val=(nbrrev[0][0] + 1,input_an.get(), input_rep.get(), input_org.get(),datetime.datetime.now(),input_idair.get())
            tree2.insert(parent='', index=val[0], iid=val[0], text='', values=val)
            conn.commit()

    btn = Button(four_frame, text='add a review ', font=(6), borderwidth=0, width=12, background='#1A2E35',
                 fg='#D8D8D8', activeforeground='#D8D8D8', activebackground='#1A2E35', command=addr)
    btn.place(x=105, y=130)


    input_idaire = Entry(four_frame, bg='grey60', font=('Times', 16), fg='#1A2E35', borderwidth=0, width=9)
    input_idaire.place(x=406, y=90)
    input_idaire.insert(0, "id_airplane")

    def on_enter(event):
        input_idaire.config(state=NORMAL)
        if input_idaire.get() == 'id_airplane':
            input_idaire.delete(0, END)

    input_idaire.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_idaire.get() == '':
            input_idaire.insert(0, "id_airplane")

    input_idaire.bind("<FocusOut>", on_leave)

    def airrev():
        if (input_idaire.get()) == 'id_airplane' or input_idaire.get() == '':
            pass
        else:
            rev = Toplevel(third_frame)
            rev.geometry("700x261+400+300")
            rev.resizable(0, 0)
            trr = ttk.Treeview(rev, height=12)
            trr['columns'] = ('id-review', 'anomaly', 'repairs', 'organs', 'review-date','NBDVAR')

            trr.column('#0', width=0, stretch=NO)
            trr.column('id-review', anchor=CENTER, width=80)
            trr.column('anomaly', anchor=CENTER, width=130)
            trr.column('repairs', anchor=CENTER, width=130)
            trr.column('organs', anchor=CENTER, width=130)
            trr.column('review-date', anchor=CENTER, width=130)
            trr.column('NBDVAR', anchor=CENTER, width=130)

            trr.heading('#0', anchor=CENTER, text='')
            trr.heading('id-review', anchor=CENTER, text='id-review')
            trr.heading('anomaly', anchor=CENTER, text='anomaly')
            trr.heading('repairs', anchor=CENTER, text='repairs')
            trr.heading('organs', anchor=CENTER, text='organs')
            trr.heading('review-date', anchor=CENTER, text='review-date')
            trr.heading('NBDVAR', anchor=CENTER, text='NBDVAR')
            trr.place(x=0, y=0)
            sql = 'select * from revision where NUMAV={}'.format(input_idaire.get())
            cur.execute(sql)
            revi = cur.fetchall()
            for i in revi:
                sql='''Select SUM(DURVOL) from avoin_vol inner join vol on vol.NUMVOL = avoin_vol.NUMVOL  where  avoin_vol.NUMAV={} and datevol <(select DATEREV FROM revision where revision.NUMREV={})'''.format(input_idaire.get(),i[0])
                cur.execute(sql)
                re=cur.fetchall()
                print(re[0][0])
                if re[0][0]==None:
                    val=(i[0],i[1],i[2],i[3],i[4] ,0 )
                else:
                    val = (i[0], i[1], i[2], i[3], i[4], re[0])
                trr.insert(parent='', index=i[0], iid=i[0], text='', values=val)

    error8 = Label(four_frame, text='id-airplane does not exist!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error9 = Label(four_frame, text='one of the fields is empty!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error10 = Label(four_frame, text='you can  not add review without flight', font=('Times', 9), bg='#5AE4A8',
                    fg='#1A2E35')
    btn = Button(four_frame, text='airplane review', font=(6), borderwidth=0, width=12,background='#1A2E35',
                 fg='#D8D8D8', activeforeground='#D8D8D8', activebackground='#1A2E35',  command=airrev)
    btn.place(x=400, y=130)

    def ser1():
        serc = Toplevel(third_frame)
        serc.geometry("240x261+850+394")
        trees = ttk.Treeview(serc, height=12)
        trees['columns'] = ('id_airplane', 'review-date')

        trees.column('#0', width=0, stretch=NO)
        trees.column('id_airplane', anchor=CENTER, width=120)
        trees.column('review-date', anchor=CENTER, width=120)

        trees.heading('#0', anchor=CENTER, text='')
        trees.heading('id_airplane', anchor=CENTER, text='id_airplane')
        trees.heading('review-date', anchor=CENTER, text='review-date')
        trees.place(x=0, y=0)
        sql = '''select NUMAV , max(daterev) from revision group by NUMAV having datediff(curdate(),max(daterev))>180'''
        cur.execute(sql)
        rs2 = cur.fetchall()
        i = 0
        for j in rs2:
            i += 1
            trees.insert(parent='', index=i, iid=i, text='', values=j)

    labl_title = Label(four_frame, text='airplane who didnt do any\nreview in the last 6 month', font=('Times', 13, 'bold'),
                       bg='#5AE4A8',
                       fg='#1A2E35')
    labl_title.place(x=570, y=60)
    btn1 = Button(four_frame, text='search', font=(6), borderwidth=0,
                  width=21, background='#1A2E35',
                 fg='#D8D8D8', activeforeground='#D8D8D8', activebackground='#1A2E35', command=ser1)
    btn1.place(x=570, y=105)
    def de():
        serc = Toplevel(third_frame)
        serc.geometry("240x261+850+394")
        trees = ttk.Treeview(serc, height=12)
        trees['columns'] = ('id_airplane', 'num_of_vol')

        trees.column('#0', width=0, stretch=NO)
        trees.column('id_airplane', anchor=CENTER, width=120)
        trees.column('num_of_vol', anchor=CENTER, width=120)

        trees.heading('#0', anchor=CENTER, text='')
        trees.heading('id_airplane', anchor=CENTER, text='id_airplane')
        trees.heading('num_of_vol', anchor=CENTER, text='num_of_vol')
        trees.place(x=0, y=0)
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        for i in l:
            sql = '''Select SUM(DURVOL) from avoin_vol inner join vol on vol.NUMVOL = avoin_vol.NUMVOL  where  avoin_vol.NUMAV={} and datevol>(select DATEREV FROM revision where REVISION.NUMAV={} order by DATEREV desc limit 1)'''.format(
                 i, i)
            cur.execute(sql)
            ser = cur.fetchall()
            if ser[0][0]==None  :
                pass
            elif ser[0][0]>1000:
                trees.insert(parent='', index=i, iid=i, text='', values=(i, ser[0][0]))

    labl_title = Label(four_frame, text='airplanes that surpassed\n 1000h without review ',
                       font=('Times', 13, 'bold'),
                       bg='#5AE4A8',
                       fg='#1A2E35')
    labl_title.place(x=800, y=60)
    btn1 = Button(four_frame, text='search', font=(6), borderwidth=0,
                  width=21, background='#1A2E35',
                  fg='#D8D8D8', activeforeground='#D8D8D8', activebackground='#1A2E35', command=de)
    btn1.place(x=800, y=105)
img1=ImageTk.PhotoImage(file='avav.png')
btnavoin=Button(frame_pricipale,image=img1 , borderwidth=0,bg='grey60',activebackground='grey60', width=150 ,command=avoin)
btnavoin.place(x=20,y=150)
av=Label(frame_pricipale,text='Airplane',font=('Times', 20, 'bold'),bg='grey60',fg='#1A2E35')
av.place(x=40,y=290)




















# -----------------------------------------------
def vol():
    vol = Toplevel()
    vol.geometry('1050x620+200+70')
    vol.resizable(0, 0)
    # ---------------creation first_frame---------
    first_frame = Frame(vol, width=1250, height=200, bg='#1A2E35')
    first_frame.place(x=0, y=0)
    labl_title = Label(first_frame, text='FLIGHT SPACE', font=('Times', 17), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=420, y=3)
    # ------------------LABEL---------------------
    labl_title = Label(first_frame, text='           add a flight', font=('Times', 12), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=20, y=40)

    # --------------------------------------ENTRY NUMAV
    input_NUMVOLS = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_NUMVOLS.place(x=15, y=70)
    input_NUMVOLS.insert(0, "      id")

    def on_enter(event,  ):
        input_NUMVOLS.config(state=NORMAL)
        if input_NUMVOLS.get() == '      id':
            input_NUMVOLS.delete(0, END)

    input_NUMVOLS.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOLS.get() == '':
            input_NUMVOLS.insert(0, "      id")

    input_NUMVOLS.bind("<FocusOut>", on_leave)
    # ------------------------------ENTRY  VILLE DE DEPART
    input_VILDEPS= Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_VILDEPS.place(x=105, y=70)
    input_VILDEPS.insert(0, "  depar city")

    def on_enter(event,  ):
        input_VILDEPS.config(state=NORMAL)
        if input_VILDEPS.get() == '  depar city':
            input_VILDEPS.delete(0, END)

    input_VILDEPS.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_VILDEPS.get() == '':
            input_VILDEPS.insert(0, "  depar city")

    input_VILDEPS.bind("<FocusOut>", on_leave)
    # ------------------------------------------VILLE D'ARRIVEE
    input_VILARRS = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_VILARRS.place(x=15, y=100)
    input_VILARRS.insert(0, "   arri city")

    def on_enter(event,  ):
        input_VILARRS.config(state=NORMAL)
        if input_VILARRS.get() == '   arri city':
            input_VILARRS.delete(0, END)

    input_VILARRS.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_VILARRS.get() == '':
            input_VILARRS.insert(0, "   arri city")

    input_VILARRS.bind("<FocusOut>", on_leave)
    # ------------------------------HEURE DE DEPART
    input_HDEPS = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_HDEPS.place(x=105, y=100)
    input_HDEPS.insert(0, " depar time")

    def on_enter(event,  ):
        input_HDEPS.config(state=NORMAL)
        if input_HDEPS.get() == ' depar time':
            input_HDEPS.delete(0, END)

    input_HDEPS.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_HDEPS.get() == '':
            input_HDEPS.insert(0, " depar time")

    input_HDEPS.bind("<FocusOut>", on_leave)
    # ------------------------------------DUREE DU VOL
    input_DURVOLS = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_DURVOLS.place(x=15, y=130)
    input_DURVOLS.insert(0, "  flight dur")

    def on_enter(event,  ):
        input_DURVOLS.config(state=NORMAL)
        if input_DURVOLS.get() == '  flight dur':
            input_DURVOLS.delete(0, END)

    input_DURVOLS.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_DURVOLS.get() == '':
            input_DURVOLS.insert(0, "  flight dur")

    input_DURVOLS.bind("<FocusOut>", on_leave)
    # ----------------------------BOUTTON AJOUTER
    def addvol():
        sql='select NUMVOL from vol'
        cur.execute(sql)
        ids=cur.fetchall()
        l=[]
        for i in ids:
            l.append(i[0])
        if  input_NUMVOLS.get()=='      id'   or input_DURVOLS.get()=='  flight dur' or input_HDEPS.get()==' depar time' or input_VILARRS=='   arri city' or input_VILDEPS.get()=='  depar city' or input_NUMVOLS.get()==''   or input_DURVOLS.get()=='' or input_HDEPS.get()=='' or input_VILARRS=='' or input_VILDEPS.get()=='' :
             error2.place(x=30, y=160)
             error1.place_forget()
             error3.place_forget()
             error4.place_forget()
        elif int(input_NUMVOLS.get()) in l:
             error1.place(x=50, y=160)
             error2.place_forget()
             error3.place_forget()
             error4.place_forget()
        elif timetcheck(input_HDEPS.get())==False:
             error1.place_forget()
             error2.place_forget()
             error4.place_forget()
             error3.place(x=10, y=160)
        else  :
            error1.place_forget()
            error2.place_forget()
            error3.place_forget()
            error4.place(x=30, y=160)
            sql='''insert into vol values({},%s,%s,%s,{})'''.format(input_NUMVOLS.get(),input_DURVOLS.get())
            cur.execute(sql,(input_VILDEPS.get(),input_VILARRS.get(),input_HDEPS.get()))
            conn.commit()
            val=(input_NUMVOLS.get(),input_VILDEPS.get(),input_VILARRS.get(),input_HDEPS.get(),input_DURVOLS.get())
            tree.insert(parent='', index=input_NUMVOLS.get(), iid=input_NUMVOLS.get(), text='', values=val)
    btnser = Button(first_frame, text='add', font=('Times', 10, 'bold'), borderwidth=0, width=11, background='#5ae4a8',
                    activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=addvol)
    btnser.place(x=105, y=130)
    error1 = Label(first_frame, text='id already existe!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')
    # error1.place(x=50, y=160)
    error2 = Label(first_frame, text='one of the fields is empty!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')
    # error2.place(x=30, y=160)
    error3 = Label(first_frame, text='you should enter a time(Hr:Min:Sc)!!', font=('Times',9), bg='#1A2E35', fg='#D8D8D8')
    # error3.place(x=10, y=160)
    error4 = Label(first_frame, text='your operation is done', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')
    # error4.place(x=30, y=160)
    # ------------------------------------LABEL---------------------
    labl_title = Label(first_frame, text='     delete/search a flight', font=('Times', 12), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=220, y=40)

    # -----------------------------NUM DU VOL
    input_NUMVOL2 = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_NUMVOL2.place(x=270, y=85)
    input_NUMVOL2.insert(0, "   id-vol")

    def on_enter(event,  ):
        input_NUMVOL2.config(state=NORMAL)
        if input_NUMVOL2.get() == '   id-vol':
            input_NUMVOL2.delete(0, END)

    input_NUMVOL2.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOL2.get() == '':
            input_NUMVOL2.insert(0, "   id-vol")

    input_NUMVOL2.bind("<FocusOut>", on_leave)
    # -----------------------------------BOUTTON SUPPRIMER
    def dele():
        sql = 'select NUMVOL from vol'
        cur.execute(sql)
        ids = cur.fetchall()
        l = []
        for i in ids:
            l.append(i[0])
        if   input_NUMVOL2.get()=='   id-vol' or input_NUMVOL2.get()==''  :
            error5.place(x=260, y=160)
            error6.place_forget()
            error7.place_forget()
        elif int(input_NUMVOL2.get()) not in l:
            error5.place_forget()
            error6.place_forget()
            error7.place(x=235,y=160)
        else:
            error6.place(x=235, y=160)
            error5.place_forget()
            error7.place_forget()
            sql = '''delete from avoin_vol where NUMVOL = {}'''.format(input_NUMVOL2.get())
            cur.execute(sql)
            sql = '''delete from escl_vol where NUMVOL = {}'''.format(input_NUMVOL2.get())
            cur.execute(sql)
            sql = '''delete from nav_vol where NUMVOL = {}'''.format(input_NUMVOL2.get())
            cur.execute(sql)
            sql='''delete from vol where NUMVOL = {}'''.format(input_NUMVOL2.get())
            cur.execute(sql)
            tree.delete(input_NUMVOL2.get())
            conn.commit()
    btnser = Button(first_frame, text='delete', font=('Times', 9, 'bold'), borderwidth=0, width=8, background='#5ae4a8',
                    activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=dele)
    btnser.place(x=230, y=130)
    def serr():
        try :
            error6.place(x=235, y=160)
            error5.place_forget()
            sql = '''select NUMVOL,VILDEP,VILARR ,DURVOL,
                         HDEP from vol where NUMVOL={}'''.format(input_NUMVOL2.get())
            cur.execute(sql)
            rs3=cur.fetchall()
            sear = Toplevel()
            sear.geometry('300x450+0+0')
            sear.resizable(0, 0)
            frameinfo = Frame(sear, width=300, height=450, bg='grey60')
            frameinfo.place(x=0, y=0)

            info = Label(frameinfo, text='flight', font=('Comic Sans MS', 15, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=105, y=0)
            info = Label(frameinfo, text='id_flight', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=95, y=50)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END, rs3[0][0])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=80)
            info = Label(frameinfo, text='depart-city', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=95, y=120)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][1])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=150)

            info = Label(frameinfo, text='arrival-city', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=95, y=190)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END, rs3[0][2])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=220)
            info = Label(frameinfo, text='depart-hour', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=95, y=260)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][4])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=290)

            info = Label(frameinfo, text='flight-duration', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=95, y=330)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][3])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=360)
        except:
            error5.place(x=260, y=160)
            error6.place_forget()
    # -------------------------------------BOUTTON SEARCH
    btnser = Button(first_frame, text='search', font=('Times', 9, 'bold'), borderwidth=0, width=8, background='#5ae4a8',
                    activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=serr)
    btnser.place(x=305, y=130)
    error5 = Label(first_frame, text='invalid input', font=('Times', 9), bg='#1A2E35',
                   fg='#D8D8D8')
    error6 = Label(first_frame, text='your operation is done', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')
    error7 = Label(first_frame, text='id does not existe!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    # ------------------------------------LABEL3---------------------
    labl_title = Label(first_frame, text='search flights with arrival & depart city', font=('Times', 12), bg='#1A2E35',
                       fg='#D8D8D8')
    labl_title.place(x=385, y=40)

    # -----------------------------------VILLE DE DEPART
    input_VILDEP = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_VILDEP.place(x=413, y=85)
    input_VILDEP.insert(0, "  depar city")
    def on_enter(event,  ):
        input_VILDEP.config(state=NORMAL)
        if input_VILDEP.get() == '  depar city':
            input_VILDEP.delete(0, END)

    input_VILDEP.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_VILDEP.get() == '':
            input_VILDEP.insert(0, "  depar city")

    input_VILDEP.bind("<FocusOut>", on_leave)
    # ------------------------------------------VILLE D'ARRIVEE
    input_VILARR = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    input_VILARR.place(x=500, y=85)
    input_VILARR.insert(0, "   arri city")
    def on_enter(event,  ):
        input_VILARR.config(state=NORMAL)
        if input_VILARR.get() == '   arri city':
            input_VILARR.delete(0, END)

    input_VILARR.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_VILARR.get() == '':
            input_VILARR.insert(0, "   arri city")

    input_VILARR.bind("<FocusOut>", on_leave)
    # -------------------------------------BOUTTON SEARCH
    def serv():
        top = Toplevel()
        top.geometry("275x200")
        top.resizable(0, 0)
        sql = '''select NUMVOL,HDEP,DURVOL from vol where VILDEP=%s AND VILARR=%s'''
        cur.execute(sql, (input_VILDEP.get(), input_VILARR.get()))
        rs4 = cur.fetchall()
        this_frame = Frame(top, width=275, height=200, bg='white')
        this_frame.place(x=0, y=0)

        trees = ttk.Treeview(this_frame, height=10)
        trees['columns'] = ('ID-FLIGHT', 'DEPART-HOUR', 'FLIGHT-DURATION')

        trees.column('#0', width=0, stretch=NO)
        trees.column('ID-FLIGHT', anchor=CENTER, width=70)
        trees.column('DEPART-HOUR', anchor=CENTER, width=100)
        trees.column('FLIGHT-DURATION', anchor=CENTER, width=105)

        trees.heading('#0', anchor=CENTER, text='')
        trees.heading('ID-FLIGHT', anchor=CENTER, text='ID-FLIGHT')
        trees.heading('DEPART-HOUR', anchor=CENTER, text='DEPART-HOUR')
        trees.heading('FLIGHT-DURATION', anchor=CENTER, text='FLIGHT-DURATION')
        trees.place(x=0, y=0)
        j=0
        for i in  rs4:
            j+=1
            trees.insert(parent='',text='',index=j,values=i,iid=j)

    # ------------------------------------------------
    btnser = Button(first_frame, text='search ', font=('Times', 9, 'bold'), borderwidth=0, width=10,
                    background='#5ae4a8', activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=serv)
    btnser.place(x=460, y=130)

    # ------------------------------------LABEL3---------------------
    labl_title = Label(first_frame, text='add  flight in a aiplane', font=('Times', 12), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=650, y=40)

    # -----------------------------NUM DU VOL
    input_NUMVOL4 = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_NUMVOL4.place(x=640, y=85)
    input_NUMVOL4.insert(0, "  id-flight")
    def on_enter(event,  ):
        input_NUMVOL4.config(state=NORMAL)
        if input_NUMVOL4.get() == '  id-flight':
            input_NUMVOL4.delete(0, END)

    input_NUMVOL4.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOL4.get() == '':
            input_NUMVOL4.insert(0, "  id-flight")

    input_NUMVOL4.bind("<FocusOut>", on_leave)
    # -----------------------------NUM DE L'AVION
    input_NUMVOL5 = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    input_NUMVOL5.place(x=715, y=85)
    input_NUMVOL5.insert(0, "id-airplane")

    def on_enter(event,  ):
        input_NUMVOL5.config(state=NORMAL)
        if input_NUMVOL5.get() == 'id-airplane':
            input_NUMVOL5.delete(0, END)

    input_NUMVOL5.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOL5.get() == '':
            input_NUMVOL5.insert(0, "id-airplane")

    input_NUMVOL5.bind("<FocusOut>", on_leave)
    # -------------------------------------BOUTTON ADD--------------------------------------
    def addfliair():
        if input_NUMVOL5.get()=='id-airplane'  or input_NUMVOL4.get()=='  id-flight' or input_NUMVOL5.get()==''   or input_NUMVOL4.get()=='' :
            error013.place(x=640,y=160)
            error014.place_forget()
            error12.place_forget()
            error00.place_forget()
            error016.place_forget()
            return
        sql = 'select NUMVOL from vol'
        cur.execute(sql)
        id1 = cur.fetchall()
        l1 = []
        for i in id1:
            l1.append(i[0])
        sql = 'select NUMAV from avoin'
        cur.execute(sql)
        id2 = cur.fetchall()
        l2 = []
        for i in id2:
            l2.append(i[0])
        sql = '''Select SUM(DURVOL) from avoin_vol inner join vol on vol.NUMVOL = avoin_vol.NUMVOL  where  avoin_vol.NUMAV={} and datevol>(select DATEREV FROM revision where REVISION.NUMAV={} order by DATEREV desc limit 1)'''.format(
            input_NUMVOL5.get(), input_NUMVOL5.get())
        cur.execute(sql)
        ser = cur.fetchall()
        l = ser[0][0]
        if l == None:
            l = 0
        if int(input_NUMVOL5.get()) not in l2 :
            error014.place(x=640,y=160)
            error016.place_forget()
            error013.place_forget()
            error012.place_forget()
            error00.place_forget()
        elif int(input_NUMVOL4.get()) not in l1 :
            error012.place(x=640, y=160)
            error014.place_forget()
            error016.place_forget()
            error013.place_forget()
            error00.place_forget()
        elif  l >=1000:
          error014.place_forget()
          error013.place_forget()
          error012.place_forget()
          error00.place_forget()

          error016.place(x=640, y=160)
        else:
            error00.place(x=640, y=160)
            error013.place_forget()
            error016.place_forget()
            error012.place_forget()
            error014.place_forget()
            sql='''insert into avoin_vol values({},{},now()) '''.format(input_NUMVOL4.get(),input_NUMVOL5.get())
            cur.execute(sql)
            conn.commit()

    error012 = Label(first_frame, text='id-flight does not exist!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    error013= Label(first_frame, text='one of the fields is empty!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    error014 = Label(first_frame, text='id-air does not exist!!', font=('Times', 9), bg='#1A2E35',
                    fg='#D8D8D8')
    error00 = Label(first_frame, text='your operation is done', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    error016 = Label(first_frame, text='a review is required', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')
    btnser = Button(first_frame, text='Add', font=('Times', 9, 'bold'), borderwidth=0, width=11, background='#5ae4a8',
                    activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=addfliair)
    btnser.place(x=670, y=130)

    # ------------------------------------LABEL7---------------------
    labl_title = Label(first_frame, text='add  navigant in a flight', font=('Times', 12), bg='#1A2E35', fg='#D8D8D8')
    labl_title.place(x=840, y=40)

    # -----------------------------NUM DU VOL
    input_NUMVOL0 = Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_NUMVOL0.place(x=832, y=85)
    input_NUMVOL0.insert(0, "  id-flight")
    def on_enter(event,  ):
        input_NUMVOL0.config(state=NORMAL)
        if input_NUMVOL0.get() == '  id-flight':
            input_NUMVOL0.delete(0, END)

    input_NUMVOL0.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOL0.get() == '':
            input_NUMVOL0.insert(0, "  id-flight")

    input_NUMVOL0.bind("<FocusOut>", on_leave)
    # -----------------------------NUM DE L'AVION
    input_NUMNAV= Entry(first_frame, bg='#9A9A9A', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    input_NUMNAV.place(x=912, y=85)
    input_NUMNAV.insert(0, "id-navig")
    def on_enter(event,  ):
        input_NUMNAV.config(state=NORMAL)
        if input_NUMNAV.get() == 'id-navig':
            input_NUMNAV.delete(0, END)

    input_NUMNAV.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMNAV.get() == '':
            input_NUMNAV.insert(0, "id-navig")

    input_NUMNAV.bind("<FocusOut>", on_leave)
    # -------------------------------------BOUTTON ADD NAVIGANT--------------------------------------
    def addnavtoflight():
        sql = 'select NUMVOL from vol'
        cur.execute(sql)
        id1 = cur.fetchall()
        l1 = []
        for i in id1:
            l1.append(i[0])
        sql = 'select NUMNAV from navig'
        cur.execute(sql)
        id2 = cur.fetchall()
        l2 = []
        for i in id2:
            l2.append(i[0])
        if   input_NUMVOL0.get()=='' or input_NUMVOL0.get()== '  id-flight' or input_NUMNAV.get()=='id-navig' or input_NUMNAV.get()=='':
            error9.place(x=840, y=160)
            error8.place_forget()
            error10.place_forget()
            error11.place_forget()
        elif int(input_NUMVOL0.get()) not in l1:
            error8.place(x=840, y=160)
            error9.place_forget()
            error10.place_forget()
            error11.place_forget()
        elif int(input_NUMNAV.get())  not in l2:
            error10.place(x=840, y=160)
            error9.place_forget()
            error8.place_forget()
            error11.place_forget()
        else:
            error11.place(x=840, y=160)
            error10.place_forget()
            error9.place_forget()
            error8.place_forget()
            sql='''insert into nav_vol values({},{})'''.format(input_NUMVOL0.get(),input_NUMNAV.get())
            cur.execute(sql)
            conn.commit()

    btnser = Button(first_frame, text='Add', font=('Times', 9, 'bold'), borderwidth=0, width=11, background='#5ae4a8',
                    activebackground='dark slate grey', fg='#1A2E35', activeforeground='#D8D8D8',command=addnavtoflight)
    btnser.place(x=860, y=130)
    error8 = Label(first_frame, text='id-flight does not exist!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    error9 = Label(first_frame, text='one of the fields is empty!!', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    error10 = Label(first_frame, text='id-pers does not exist!!', font=('Times', 9), bg='#1A2E35',
                   fg='#D8D8D8')

    error11 = Label(first_frame, text='your operation is done', font=('Times', 10), bg='#1A2E35', fg='#D8D8D8')

    # ----------------------------------------ESPACE  ESCALE-----------------------------------------
    frame2 = Frame(vol, width=1250, height=200, bg='#5AE4A8')
    frame2.place(x=0, y=200)
    labl_title = Label(frame2, text='STOPOVER SPACE', font=('Times', 16), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=420, y=10)

    # ---------------------------------------LABEL4---------------------------
    labl_title = Label(frame2, text='          add a stopover', font=('Times', 12), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=20, y=40)

    # --------------------------------------------------ID ESCALE------------------------------
    input_NUMesc = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_NUMesc.place(x=15, y=70)
    input_NUMesc.insert(0, "stopover num")
    def on_enter(event ):
        input_NUMesc.config(state=NORMAL)
        if input_NUMesc.get() == 'stopover num':
            input_NUMesc.delete(0, END)

    input_NUMesc.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMesc.get() == '':
            input_NUMesc.insert(0, "stopover num")

    input_NUMesc.bind("<FocusOut>", on_leave)
    # ------------------------------------VILLE D'ESCALE------------------------------------------
    input_city1 = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_city1.place(x=115, y=70)
    input_city1.insert(0, "   city stop")
    def on_enter(event ):
        input_city1.config(state=NORMAL)
        if input_city1.get() == '   city stop':
            input_city1.delete(0, END)

    input_city1.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_city1.get() == '':
            input_city1.insert(0, "   city stop")

    input_city1.bind("<FocusOut>", on_leave)
    # --------------------------------------------HEURE DE L'ESCALE----------------------------
    input_time1 = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_time1.place(x=15, y=100)
    input_time1.insert(0, "stopover time")
    def on_enter(event ):
        input_time1.config(state=NORMAL)
        if input_time1.get() == 'stopover time':
            input_time1.delete(0, END)

    input_time1.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_time1.get() == '':
            input_time1.insert(0, "stopover time")

    input_time1.bind("<FocusOut>", on_leave)
    # ------------------------------------DUREE D'ESCALE-------------------------------
    input_duresc = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    input_duresc.place(x=115, y=100)
    input_duresc.insert(0, " stpover dur")
    def on_enter(event ):
        input_duresc.config(state=NORMAL)
        if input_duresc.get() == ' stpover dur':
            input_duresc.delete(0, END)

    input_duresc.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_duresc.get() == '':
            input_duresc.insert(0, " stpover dur")

    input_duresc.bind("<FocusOut>", on_leave)
    # ------------------------------------BOUTTON AJOUTER ESCALE---------------------------------
    def addesc():
        sql='''select NUMESCL from escale'''
        cur.execute(sql)
        rs1=cur.fetchall()
        l=[]
        for i in rs1:
            l.append(i[0])
        if input_NUMesc.get()=='stopover num' or input_duresc.get()==' stpover dur' or input_city1.get()=='   city stop' or input_time1.get() =='stopover time':
            error13.place(x=45,y=170)
            error12.place_forget()
            error15.place_forget()
        elif  int(input_NUMesc.get()) in l  :
            error12.place(x=45, y=170)
            error13.place_forget()
            error15.place_forget()
        else:
            error15.place(x=45, y=170)
            error13.place_forget()
            error12.place_forget()
            sql='''insert into escale values({},%s,%s ,{})'''.format(input_NUMesc.get(),input_duresc.get())
            cur.execute(sql,( input_city1.get(),input_time1.get() ))
            conn.commit()
            val=(input_NUMesc.get(),input_city1.get(),input_time1.get(),input_duresc.get())
            trees.insert(parent='', index=input_NUMesc.get(), iid=input_NUMesc.get(), text='', values=val)

    error12 = Label(frame2, text='id-already existe !!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error13 = Label(frame2 , text='one of the fields is empty!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error15 = Label(frame2, text='your operation is done', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    btnser = Button(frame2, text='add', font=('Times', 10, 'bold'), borderwidth=0, width=10, background='#1A2E35',
                    activebackground='#1A2E35', fg='#D8D8D8', activeforeground='#D8D8D8',command=addesc)
    btnser.place(x=70, y=140)

    # ---------------------------------------LABEL5---------------------------
    labl_title = Label(frame2, text='delete a stopover', font=('Times', 12), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=255, y=40)

    # -----------------------------NUM DU ESCALE------------------------------------
    input_escdel = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_escdel.place(x=270, y=70)
    input_escdel.insert(0, "  id-stopo")
    def on_enter(event ):
        input_escdel.config(state=NORMAL)
        if input_escdel.get() == '  id-stopo':
            input_escdel.delete(0, END)

    input_escdel.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_escdel.get() == '':
            input_escdel.insert(0, "  id-stopo")

    input_escdel.bind("<FocusOut>", on_leave)
    # ------------------------------------BOUTTON SUPPRILMER
    def delee():
        sql = '''select NUMESCL from escale'''
        cur.execute(sql)
        rs1 = cur.fetchall()
        l = []
        for i in rs1:
            l.append(i[0])
        if input_escdel.get()== '  id-stopo':
            error17.place(x=250 ,y= 130 )
            error18.place_forget()
            error19.place_forget()
        elif   int(input_escdel.get()) not in l:
            error19.place(x=250, y=130)
            error18.place_forget()
            error17.place_forget()
        else:
            error18.place(x=250, y=130)
            error19.place_forget()
            error17.place_forget()
            sql = '''delete from escl_vol where NUMESCL = {}'''.format(input_escdel.get())
            cur.execute(sql)
            sql='''delete from escale where NUMESCL = {}'''.format(input_escdel.get())
            cur.execute(sql)
            trees.delete(input_escdel.get())
            conn.commit()

    error19 = Label(frame2, text='id does not   existe !!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error17 = Label(frame2, text='the field  is empty!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    error18 = Label(frame2, text='your operation is done', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')

    btnser = Button(frame2, text='delete', font=('Times', 10, 'bold'), borderwidth=0, width=10, background='#1A2E35',
                    activebackground='#1A2E35', fg='#D8D8D8', activeforeground='#D8D8D8',command=delee)
    btnser.place(x=265, y=100)

    # ---------------------------------------LABEL5---------------------------
    labl_title = Label(frame2, text='search flights passing by stopover', font=('Times', 12), bg='#5AE4A8',
                       fg='#1A2E35')
    labl_title.place(x=380, y=40)

    # -----------------------------NUM DU VOL------------------------------------
    input_escd = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_escd.place(x=440, y=70)
    input_escd.insert(0, "  id-stopo")
    def on_enter(event ):
        input_escd.config(state=NORMAL)
        if input_escd.get() == '  id-stopo':
            input_escd.delete(0, END)

    input_escd.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_escd.get() == '':
            input_escd.insert(0, "  id-stopo")

    input_escd.bind("<FocusOut>", on_leave)
    # ---------------------------------------------------------------------------

    def servol():
        if input_escd.get() == '  id-stopo' or input_escd.get() == '':
            error20.place(x=420, y=130)
        else:
            top = Toplevel()
            top.geometry("540x200")
            top.resizable(0, 0)
            sql='''select  NUMVOL,escale.NUMESCL,VILESC,DURESC,HARRESC,NOOD from   escl_vol 
                   inner join escale	on escale.NUMESCL=escl_vol.NUMESCL  
                   where escale.NUMESCL={}'''.format(input_escd.get())
            cur.execute(sql)
            rse=cur.fetchall()
            this_frame = Frame(top, width=540, height=200, bg='white')
            this_frame.place(x=0, y=0)

            trs = ttk.Treeview(this_frame, height=10)
            trs['columns'] = ('ID-FLIGHT','id_ESCL','VILESC','HARRESC','DURESC','NOOD')

            trs.column('#0', width=0, stretch=NO)
            trs.column('ID-FLIGHT', anchor=CENTER, width=70)
            trs.column('id_ESCL', anchor=CENTER, width=70)
            trs.column('VILESC', anchor=CENTER, width=100)
            trs.column('HARRESC', anchor=CENTER, width=100)
            trs.column('DURESC', anchor=CENTER, width=100)
            trs.column('NOOD', anchor=CENTER, width=100)

            trs.heading('#0', anchor=CENTER, text='')
            trs.heading('ID-FLIGHT', anchor=CENTER, text='ID-FLIGHT')
            trs.heading('id_ESCL', anchor=CENTER, text='id_ESCL')
            trs.heading('VILESC', anchor=CENTER, text='VILESC')
            trs.heading('HARRESC', anchor=CENTER, text='HARRESC')
            trs.heading('DURESC', anchor=CENTER, text='DURESC')
            trs.heading('NOOD', anchor=CENTER, text='NOOD')
            trs.place(x=0, y=0)
            j=0
            for i in rse:
                trs.insert(parent='',text='',iid=j,index=j,values=i)
                j+=1

    error20 = Label(frame2, text='the field  is empty!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    btnser = Button(frame2, text='search', font=('Times', 10, 'bold'), borderwidth=0, width=11, background='#1A2E35',
                    activebackground='#1A2E35', fg='#D8D8D8', activeforeground='#D8D8D8', command=servol)
    btnser.place(x=430, y=100)

    this_frame = Frame(vol, width=590, height=500, bg='white')
    this_frame.place(x=590, y=400)

    trees = ttk.Treeview(this_frame, height=10)
    trees['columns'] = ('id_ESCL', 'VILESC', 'HARRESC', 'DURESC' )

    trees.column('#0', width=0, stretch=NO)
    trees.column('id_ESCL', anchor=CENTER, width=70)
    trees.column('VILESC', anchor=CENTER, width=130)
    trees.column('HARRESC', anchor=CENTER, width=130)
    trees.column('DURESC', anchor=CENTER, width=130)

    trees.heading('#0', anchor=CENTER, text='')
    trees.heading('id_ESCL', anchor=CENTER, text='id_ESCL')
    trees.heading('VILESC', anchor=CENTER, text='VILESC')
    trees.heading('HARRESC', anchor=CENTER, text='HARRESC')
    trees.heading('DURESC', anchor=CENTER, text='DURESC')
    trees.place(x=0, y=0)
    sql = 'USE aot;'
    cur.execute(sql)
    sql = 'select * from escale'
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        trees.insert(parent='', index=i[0], iid=i[0], text='', values=i)



    second_frame = Frame(vol, width=590, height=500, bg='white')
    second_frame.place(x=0, y=400)

    tree = ttk.Treeview(second_frame, height=10)
    tree['columns'] = ('id_flght', 'flight-des', 'flight-arr', 'flight-dir', 'flight-hr')

    tree.column('#0', width=0, stretch=NO)
    tree.column('id_flght', anchor=CENTER, width=70)
    tree.column('flight-des', anchor=CENTER, width=130)
    tree.column('flight-arr', anchor=CENTER, width=130)
    tree.column('flight-dir', anchor=CENTER, width=130)
    tree.column('flight-hr', anchor=CENTER, width=130)

    tree.heading('#0', anchor=CENTER, text='')
    tree.heading('id_flght', anchor=CENTER, text='id_flght')
    tree.heading('flight-des', anchor=CENTER, text='flight-des')
    tree.heading('flight-arr', anchor=CENTER, text='flight-arr')
    tree.heading('flight-dir', anchor=CENTER, text='flight-dir')
    tree.heading('flight-hr', anchor=CENTER, text='flight-hr')
    tree.place(x=0, y=0)
    sql = 'select * from vol'
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        tree.insert(parent='', index=i[0], iid=i[0], text='', values=i)

    # ------------------------------------BOUTTON CHERCHER LES ESCALES D'UNE AVION


    # ---------------------------------------LABEL6---------------------------
    labl_title = Label(frame2, text='search stopover for a flight ', font=('Times', 12), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=600, y=40)

    # -----------------------------NUM DU ESCALE------------------------------------
    input_NUMVOL60 = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_NUMVOL60.place(x=650, y=70)
    input_NUMVOL60.insert(0, " id-flight")
    def on_enter(event ):
        input_NUMVOL60.config(state=NORMAL)
        if input_NUMVOL60.get() == ' id-flight':
            input_NUMVOL60.delete(0, END)

    input_NUMVOL60.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMVOL60.get() == '':
            input_NUMVOL60.insert(0, " id-flight")

    input_NUMVOL60.bind("<FocusOut>", on_leave)
    def servol():
        if input_NUMVOL60.get()==' id-flight':
            error20.place(x=630, y=125)
        else:
            top = Toplevel()
            top.geometry("540x200")
            top.resizable(0, 0)
            sql='''select  NUMVOL,escale.NUMESCL,VILESC,DURESC,HARRESC,NOOD from   escl_vol 
                   inner join escale	on escale.NUMESCL=escl_vol.NUMESCL  
                   where NUMVOL={}'''.format(input_NUMVOL60.get())
            cur.execute(sql)
            rse=cur.fetchall()
            this_frame = Frame(top, width=540, height=200, bg='white')
            this_frame.place(x=0, y=0)

            trs = ttk.Treeview(this_frame, height=10)
            trs['columns'] = ('ID-FLIGHT','id_ESCL','VILESC','HARRESC','DURESC','NOOD')

            trs.column('#0', width=0, stretch=NO)
            trs.column('ID-FLIGHT', anchor=CENTER, width=70)
            trs.column('id_ESCL', anchor=CENTER, width=70)
            trs.column('VILESC', anchor=CENTER, width=100)
            trs.column('HARRESC', anchor=CENTER, width=100)
            trs.column('DURESC', anchor=CENTER, width=100)
            trs.column('NOOD', anchor=CENTER, width=100)

            trs.heading('#0', anchor=CENTER, text='')
            trs.heading('ID-FLIGHT', anchor=CENTER, text='ID-FLIGHT')
            trs.heading('id_ESCL', anchor=CENTER, text='id_ESCL')
            trs.heading('VILESC', anchor=CENTER, text='VILESC')
            trs.heading('HARRESC', anchor=CENTER, text='HARRESC')
            trs.heading('DURESC', anchor=CENTER, text='DURESC')
            trs.heading('NOOD', anchor=CENTER, text='NOOD')
            trs.place(x=0, y=0)
            j=0
            for i in rse:
                trs.insert(parent='',text='',iid=j,index=j,values=i)
                j+=1


    # ------------------------------------BOUTTON CHERCHER LES ESCALES D'UNE AVION
    btnser = Button(frame2, text='search-stopfli', font=('Times', 10, 'bold'), borderwidth=0, width=11,
                    background='#1A2E35', activebackground='#1A2E35', fg='#D8D8D8', activeforeground='#D8D8D8',command=servol)
    btnser.place(x=640, y=100)
    # ------------------------------------LABEL7---------------------
    labl_title = Label(frame2, text='add  stopover in a flight', font=('Times', 12), bg='#5AE4A8', fg='#1A2E35')
    labl_title.place(x=820, y=32)

    # -----------------------------NUM DU VOL
    input_NUMvl = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    input_NUMvl.place(x=820, y=70)
    input_NUMvl.insert(0, "  id-stop")
    def on_enter(event ):
        input_NUMvl.config(state=NORMAL)
        if input_NUMvl.get() == '  id-stop':
            input_NUMvl.delete(0, END)

    input_NUMvl.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMvl.get() == '':
            input_NUMvl.insert(0, "  id-stop")

    input_NUMvl.bind("<FocusOut>", on_leave)
    # -----------------------------NUM DE L'AVION
    input_NUMfl = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    input_NUMfl.place(x=900, y=70)
    input_NUMfl.insert(0, "id-flight")
    def on_enter(event ):
        input_NUMfl.config(state=NORMAL)
        if input_NUMfl.get() == 'id-flight':
            input_NUMfl.delete(0, END)

    input_NUMfl.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_NUMfl.get() == '':
            input_NUMfl.insert(0, "id-flight")

    input_NUMfl.bind("<FocusOut>", on_leave)
    input_nood = Entry(frame2, bg='grey60', font=('Times', 12, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    input_nood.place(x=860, y=105)
    input_nood.insert(0, "NOOD")
    def on_enter(event ):
        input_nood.config(state=NORMAL)
        if input_nood.get() == 'NOOD':
            input_nood.delete(0, END)

    input_nood.bind("<Button-1>", on_enter)

    def on_leave(event):
        if input_nood.get() == '':
            input_nood.insert(0, "NOOD")

    input_nood.bind("<FocusOut>", on_leave)
    # -------------------------------------BOUTTON ADD NAVIGANT--------------------------------------
    def addesctoflight():
        sql = 'select NUMVOL from vol'
        cur.execute(sql)
        id1 = cur.fetchall()
        l1 = []
        for i in id1:
            l1.append(i[0])
        sql = '''select NUMESCL from escale'''
        cur.execute(sql)
        rs1 = cur.fetchall()
        l = []
        for i in rs1:
            l.append(i[0])


        sql = '''select * from escl_vol'''
        cur.execute(sql)
        rs1 = cur.fetchall()
        if input_nood.get()=='NOOD' or input_NUMfl.get()=='id-flight' or input_NUMvl.get()=='  id-stop' or input_nood.get()=='' or input_NUMfl.get()=='' or input_NUMvl.get()=='':
             error21.place(x=830,y=170)
             error22.place_forget()
             error23.place_forget()
             error24.place_forget()
             error25.place_forget()
        elif  int(input_NUMfl.get()) not in l1 :
             error23.place(x=830,y=170)
             error21.place_forget()
             error22.place_forget()
             error24.place_forget()
             error25.place_forget()
        elif int(input_NUMvl.get()) not in l :
            error22.place(x=830, y=170)
            error21.place_forget()
            error23.place_forget()
            error24.place_forget()
            error25.place_forget()
        elif (int(input_NUMfl.get()),int(input_NUMvl.get()) , int(input_nood.get()))  in rs1:
            error25.place(x=830, y=170)
            error21.place_forget()
            error23.place_forget()
            error24.place_forget()
            error22.place_forget()
        else:
            error24.place(x=830, y=170)
            error21.place_forget()
            error23.place_forget()
            error22.place_forget()
            error25.place_forget()
            sql = '''insert into escl_vol values({},{},{})'''.format(input_NUMfl.get(), input_NUMvl.get(),input_nood.get())
            cur.execute(sql)
            conn.commit()

    error21 = Label(frame2, text='one of the fields  is empty!!', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    error22 = Label(frame2, text='id-stop does not existe ', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    error23 = Label(frame2, text='id-flight does not existe ', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    error24 = Label(frame2, text='your operation is done ', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    error25 = Label(frame2, text='already exist', font=('Times', 10), bg='#5AE4A8', fg='#1A2E35')
    btnser = Button(frame2, text='Add', font=('Times', 9, 'bold'), borderwidth=0, width=11, background='#1A2E35',
                    activebackground='#1A2E35', fg='#D8D8D8', activeforeground='#D8D8D8',
                    command=addesctoflight)
    btnser.place(x=850, y=140)
img2=ImageTk.PhotoImage(file='direct-flight.png')
btnvol=Button(frame_pricipale,image=img2 , borderwidth=0,bg='grey60',activebackground='grey60', width=150,command=vol   )
btnvol.place(x=300,y=150)
volt=Label(frame_pricipale,text='Flying',font=('Times', 20, 'bold'),bg='grey60',fg='#1A2E35')
volt.place(x=340,y=290)
# -----------------------------------------
def emol():
    plot = Toplevel()
    plot.geometry("1270x600+100+20")
    plot.resizable(0, 0)
    frame1 = Frame(plot, width=625, height=370, bg='#5AE4A8')
    frame1.place(x=0, y=0)
    im1 = PhotoImage(file='add-user.png')
    im2 = PhotoImage(file='update11.png')
    im3 = PhotoImage(file='magnifying-glass.png')
    im4 = PhotoImage(file='people.png')
    im5 = PhotoImage(file='remove-user.png')
    im6 = PhotoImage(file='click.png')
    im7 = PhotoImage(file='add-button (1).png')
    def addnav():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if en1.get() == '       NBR' or en2.get() == '  fname' or en3.get() == ' Sname' or en4.get() == 'phone-number' or en5.get() == ' city' or en6.get() == ' distrinct' or en7.get() == ' zip-code' or en8.get() == ' salaire' or en9.get() == ' COMS-DATE':
            error1.place(x=70,y=120)
            error2.place_forget()
            error3.place_forget()
            error4.place_forget()
        elif int(en1.get()) in l:
            error2.place(x=70, y=120)
            error1.place_forget()
            error3.place_forget()
            error4.place_forget()
        else:
            error3.place(x=70, y=120)
            error2.place_forget()
            error1.place_forget()
            error4.place_forget()
            sql='''insert into navig values({},%s,%s,{},%s,%s,%s,{},%s)'''.format(en1.get(),en4.get(),en8.get())
            cur.execute(sql,(en3.get(),en2.get(),en5.get(),en6.get(),en7.get(),en9.get()))
            val=(en1.get(),en2.get(),en3.get(),en4.get(),en5.get(),en6.get(),en7.get(),en8.get(),en9.get())
            trees.insert(parent='',text='',iid=en1.get(),index=en1.get(),values=val)
            conn.commit()
    btnpil1 = Button(frame1, image=im1, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=addnav)
    btnpil1.place(x=260, y=120)

    def updav():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs=cur.fetchall()
        l=[]
        for i in rs:
            l.append(i[0])
        if en1.get()=='       NBR' or en2.get()=='  fname' or en3.get()==' Sname' or en4.get()=='phone-number' or en5.get()==' city' or en6.get()==' distrinct' or en7.get()==' zip-code' or en8.get()==' salaire' or en9.get()==' COMS-DATE' :
            error1.place(x=70, y=120)
            error2.place_forget()
            error3.place_forget()
            error4.place_forget()
        elif   int(en1.get()) not in l :
            error4.place(x=70, y=120)
            error2.place_forget()
            error1.place_forget()
            error3.place_forget()
        else:
            error3.place(x=70, y=120)
            error2.place_forget()
            error1.place_forget()
            error4.place_forget()
            sql='''update navig set NOM_NAV=%s,PRENOM_NAV=%s,TEL_NAV={},VIL_NAV=%s,QRT_NAV=%s,CDP_NAV=%s,SAL_NAV={},DATEMB_NAV=%s where NUMNAV={}'''.format(en4.get(),en8.get(),en1.get())
            cur.execute(sql,(en3.get(),en2.get(),en5.get(),en6.get(),en7.get(),en9.get()))
            val = (en1.get(), en3.get(), en2.get(), en4.get(), en5.get(), en6.get(), en7.get(), en8.get(), en9.get())
            trees.item(en1.get(), text='', values=val)
            conn.commit()
    error1 = Label(frame1, text='one of the fields is empty!!', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error2 = Label(frame1, text='id already existe', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error3 = Label(frame1, text='your opearation is done', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error4 = Label(frame1, text='id does not existe', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    btnpil2 = Button(frame1, image=im2, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=updav )
    btnpil2.place(x=320, y=120)
    def sernb():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ens1.get()==' MONTH' or ens3.get()=='NBR':
            error5.place(x=85, y=255)
            error6.place_forget()
            error7.place_forget()
            error8.place_forget()
        elif int(ens3.get()) not in l:
            error8.place(x=85, y=255)
            error6.place_forget()
            error7.place_forget()
            error5.place_forget()
        elif   MONTH_YEARcheck(ens1.get())==False:
            error6.place(x=85, y=255)
            error5.place_forget()
            error7.place_forget()
            error8.place_forget()
        else:
            error7.place(x=85, y=255)
            error6.place_forget()
            error5.place_forget()
            error8.place_forget()
            dat=''.join(ens1.get().split('-'))
            sql='''select SUM(DURVOL)  from navig inner join nav_vol on navig.NUMNAV=nav_vol.NUMNAV
                   inner join vol on vol.NUMVOL=nav_vol.NUMVOL inner join avoin_vol on
                   avoin_vol.NUMVOL=vol.NUMVOL where navig.NUMNAV={} and extract( YEAR_MONTH  from datevol)= %s '''.format(ens3.get())
            cur.execute(sql,dat)
            rs=cur.fetchall()
            if rs[0][0]==None:
                ens0.config(state=NORMAL)
                ens0.delete(0,END)
                ens0.insert(0,0)
                ens0.config(state=DISABLED)
            else:
                ens0.config(state=NORMAL)
                ens0.delete(0, END)
                ens0.insert(0, rs[0][0])
                ens0.config(state=DISABLED)
    btnpil3 = Button(frame1, image=im3, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=sernb)
    btnpil3.place(x=240, y=200)
    error5 = Label(frame1, text='one of the fields is empty!!', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error6 = Label(frame1, text='not in date format', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error7 = Label(frame1, text='your opearation is done', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error8 = Label(frame1, text='id does not existe', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    def searchinfo():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ens4.get()=="   NBR" :
            error9.place(x=435, y=230)
            error11.place_forget()
            error12.place_forget()

        elif int(ens4.get()) not in l :
            error12.place(x=435, y=230)
            error9.place_forget()
            error11.place_forget()

        else:
            error11.place(x=435, y=230)
            error9.place_forget()
            error12.place_forget()
            sear=Toplevel()
            sear.geometry('300x450+0+0')
            sear.resizable(0, 0)
            frameinfo = Frame(sear, width=300, height=450, bg='grey60')
            frameinfo.place(x=0, y=0)
            sql='''select concat(NOM_NAV,'-',PRENOM_NAV),TEL_NAV,concat(VIL_NAV,'-',QRT_NAV,'-',CDP_NAV),SAL_NAV,
                 DATEMB_NAV from navig where NUMNAV={}'''.format(ens4.get())
            cur.execute(sql)
            rs3=cur.fetchall()
            info = Label(frameinfo, text='information', font=('Comic Sans MS', 15, 'bold'), bg='grey60',
                            fg='#1A2E35')
            info.place(x=80,y=0)
            info = Label(frameinfo, text='FULL_NAME', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=50)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END,rs3[0][0])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=80)
            info = Label(frameinfo, text='PHONE_NAME', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=120)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][1])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=150)

            info = Label(frameinfo, text='Adress', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=190)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END, rs3[0][2])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=220)
            info = Label(frameinfo, text='Salaire', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=260)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][3])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=290)

            info = Label(frameinfo, text='DATEMB_NAV', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=330)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][4])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=360)


    btnpil3 = Button(frame1, image=im4, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=searchinfo)
    btnpil3.place(x=465, y=197)
    def dele():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ens4.get() == "   NBR":
            error9.place(x=435, y=230)
            error11.place_forget()
            error12.place_forget()

        elif int(ens4.get()) not in l:
            error12.place(x=435, y=230)
            error9.place_forget()
            error11.place_forget()

        else:
            error11.place(x=435, y=230)
            error9.place_forget()
            error12.place_forget()
            sql='''delete from nav_vol where NUMNAV={}'''.format(ens4.get())
            cur.execute(sql)
            sql='''delete from navig where NUMNAV={}'''.format(ens4.get())
            cur.execute(sql)
            conn.commit()
            trees.delete(ens4.get())
    btnpil3 = Button(frame1, image=im5, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=dele)
    btnpil3.place(x=515, y=197)
    error9 = Label(frame1, text='the field is empty!!', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error11 = Label(frame1, text='your opearation is done', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error12 = Label(frame1, text='id does not existe', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    def pers():
        sql = '''select * from vol'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ens5.get() == 'flight-nbr':
            error13.place(x=110, y=330)
            error14.place_forget()
            error15.place_forget()
        elif int(ens5.get()) not in l:
            error15.place(x=110, y=330)
            error14.place_forget()
            error13.place_forget()
        else:
            error14.place(x=90, y=330)
            error13.place_forget()
            error15.place_forget()
            pers=Toplevel()
            pers.geometry('250x340')
            pers.resizable(0,0)
            tree3=ttk.Treeview(pers,height=16)
            tree3['columns']=('NBR','FNAME','SNAME')

            tree3.column('#0', width=0, stretch=NO)
            tree3.column('NBR', anchor=CENTER, width=60)
            tree3.column('FNAME', anchor=CENTER, width=95)
            tree3.column('SNAME', anchor=CENTER, width=95)

            tree3.heading('#0', text='', anchor=CENTER)
            tree3.heading('NBR', text='NBR', anchor=CENTER)
            tree3.heading('FNAME', text='FNAME', anchor=CENTER)
            tree3.heading('SNAME', text='SNAME', anchor=CENTER)
            tree3.place(x=0,y=0)

            sql='''select  navig.NUMNAV,NOM_NAV,PRENOM_NAV from navig inner join nav_vol on nav_vol.NUMNAV=navig.NUMNAV where NUMVOL={}'''.format(ens5.get())
            cur.execute(sql)
            rs4=cur.fetchall()
            j=0
            for i in rs4:
                j+=1
                tree3.insert(parent='', text='', iid=j, index=j, values=i)
    btnpil3 = Button(frame1, image=im6, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=pers)
    btnpil3.place(x=200, y=310)
    def sear():
        sql = '''select * from navig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ens8.get() == 'nbr_per':
            error13.place(x=400, y=330)
            error14.place_forget()
            error15.place_forget()
        elif  int(ens8.get() ) not in l:
            error15.place(x=400, y=330)
            error14.place_forget()
            error13.place_forget()
        else    :
            error14.place(x=400, y=330)
            error13.place_forget()
            error15.place_forget()
            sql = '''select SUM(DURVOL)  from navig inner join nav_vol on navig.NUMNAV=nav_vol.NUMNAV
            inner join vol on vol.NUMVOL=nav_vol.NUMVOL inner join avoin_vol on
            avoin_vol.NUMVOL=vol.NUMVOL where navig.NUMNAV={}'''.format(
                ens8.get())
            cur.execute(sql)
            rs = cur.fetchall()
            if rs[0][0]==None:
                ens6.config(state=NORMAL)
                ens6.delete(0, END)
                ens6.insert(0, 0)
                ens6.config(state=DISABLED)
            else:
                ens6.config(state=NORMAL)
                ens6.delete(0,END)
                ens6.insert(0, rs[0][0])
                ens6.config(state=DISABLED)
    error13 = Label(frame1, text='the field is empty!!', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error14 = Label(frame1, text='your opearation is done', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    error15 = Label(frame1, text='id does not existe', font=('Times', 10, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    btnpil3 = Button(frame1, image=im6, borderwidth=0, bg='#5AE4A8', activebackground='#5AE4A8', width=70,command=sear)
    btnpil3.place(x=480, y=280)

    title = Label(frame1, text='personal space', font=('Times', 20, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=225, y=10)
    title = Label(frame1, text='add or update a personal info', font=('Times', 11, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=210, y=55)

    # --------------------------------------------
    en1 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=9)
    en1.place(x=0, y=90)
    en1.insert(0, "       NBR")

    def on_enter(event):
        en1.config(state=NORMAL)
        if en1.get() == '       NBR':
            en1.delete(0, END)

    en1.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en1.get() == '':
            en1.insert(0, "       NBR")

    en1.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en2 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=8)
    en2.place(x=66, y=90)
    en2.insert(0, "  fname")

    def on_enter(event):
        en2.config(state=NORMAL)
        if en2.get() == '  fname':
            en2.delete(0, END)

    en2.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en2.get() == '':
            en2.insert(0, "  fname")

    en2.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en3 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=8)
    en3.place(x=125, y=90)
    en3.insert(0, " Sname")

    def on_enter(event):
        en3.config(state=NORMAL)
        if en3.get() == ' Sname':
            en3.delete(0, END)

    en3.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en3.get() == '':
            en3.insert(0, " Sname")

    en3.bind("<FocusOut>", on_leave)
    # -------------------------------------------
    en4 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=12)
    en4.place(x=184, y=90)
    en4.insert(0, "phone-number")

    def on_enter(event):
        en4.config(state=NORMAL)
        if en4.get() == 'phone-number':
            en4.delete(0, END)

    en4.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en4.get() == '':
            en4.insert(0, "phone-number")

    en4.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en5 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=8)
    en5.place(x=271, y=90)
    en5.insert(0, " city")

    def on_enter(event):
        en5.config(state=NORMAL)
        if en5.get() == ' city':
            en5.delete(0, END)

    en5.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en5.get() == '':
            en5.insert(0, " city")

    en5.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en6 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=9)
    en6.place(x=330, y=90)
    en6.insert(0, " distrinct")

    def on_enter(event):
        en6.config(state=NORMAL)
        if en6.get() == ' distrinct':
            en6.delete(0, END)

    en6.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en6.get() == '':
            en6.insert(0, " distrinct")

    en6.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en7 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=10)
    en7.place(x=396, y=90)
    en7.insert(0, " zip-code")

    def on_enter(event):
        en7.config(state=NORMAL)
        if en7.get() == ' zip-code':
            en7.delete(0, END)

    en7.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en7.get() == '':
            en7.insert(0, " zip-code")

    en7.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en8 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=9)
    en8.place(x=469, y=90)
    en8.insert(0, " salaire")

    def on_enter(event):
        en8.config(state=NORMAL)
        if en8.get() == ' salaire':
            en8.delete(0, END)

    en8.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en8.get() == '':
            en8.insert(0, " salaire")

    en8.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    en9 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=12)
    en9.place(x=535, y=90)
    en9.insert(0, " COMS-DATE")

    def on_enter(event):
        en9.config(state=NORMAL)
        if en9.get() == ' COMS-DATE':
            en9.delete(0, END)

    en9.bind("<Button-1>", on_enter)

    def on_leave(event):
        if en9.get() == '':
            en9.insert(0, " COMS-DATE")

    en9.bind("<FocusOut>", on_leave)
    # --------------------------------------------

    title = Label(frame1, text='number of flight hours', font=('Times', 11, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=100, y=170)

    ens1 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=11)
    ens1.place(x=100, y=205)
    ens1.insert(0, " MONTH")

    def on_enter(event):
        ens1.config(state=NORMAL)
        if ens1.get() == ' MONTH':
            ens1.delete(0, END)

    ens1.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ens1.get() == '':
            ens1.insert(0, " MONTH")

    ens1.bind("<FocusOut>", on_leave)
    # ---------------------------------------------------------
    ens3 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=10)
    ens3.place(x=180, y=205)
    ens3.insert(0, "NBR")

    def on_enter(event):
        ens3.config(state=NORMAL)
        if ens3.get() == 'NBR':
            ens3.delete(0, END)

    ens3.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ens3.get() == '':
            ens3.insert(0, "NBR")

    ens3.bind("<FocusOut>", on_leave)
    ens0 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=17)
    ens0.place(x=115, y=235)
    ens0.config(state=DISABLED)
    frame2=Frame(plot, width=700, height=400 )
    frame2.place(x=625,y=0)
    trees = ttk.Treeview(frame2, height=21)
    trees['columns'] = ('NBR', 'FNAME', 'SNAME', 'PHONE_NBR', 'CITY', 'DISTRICT', 'ZIP_CODE', 'SALARY', 'COMS_DATE')

    trees.column('#0', width=0, stretch=NO)
    trees.column('NBR', anchor=CENTER, width=60)
    trees.column('FNAME', anchor=CENTER, width=70)
    trees.column('SNAME', anchor=CENTER, width=70)
    trees.column('PHONE_NBR', anchor=CENTER, width=90)
    trees.column('COMS_DATE', anchor=CENTER, width=90)
    trees.column('CITY', anchor=CENTER, width=80)
    trees.column('DISTRICT', anchor=CENTER, width=65)
    trees.column('ZIP_CODE', anchor=CENTER, width=60)
    trees.column('SALARY', anchor=CENTER, width=60)

    trees.heading('#0', text='', anchor = CENTER)
    trees.heading('NBR', text='NBR', anchor=CENTER)
    trees.heading('FNAME', text='FNAME', anchor=CENTER)
    trees.heading('SNAME', text='SNAME', anchor=CENTER)
    trees.heading('PHONE_NBR', text='PHONE_NBR', anchor=CENTER)
    trees.heading('COMS_DATE', text='COMS_DATE', anchor=CENTER)
    trees.heading('CITY', text='CITY', anchor=CENTER)
    trees.heading('DISTRICT', text='DISTRICT', anchor=CENTER)
    trees.heading('ZIP_CODE', text='ZIP_CODE', anchor=CENTER)
    trees.heading('SALARY', text='SALARY', anchor=CENTER)
    trees.place(x=0, y=0)
    sql ="""select * from navig"""
    cur.execute(sql)
    rs=cur.fetchall()
    for i in rs :
            trees.insert(parent='',text='',iid=i[0],index=i[0],values=i)

    frame3 = Frame(plot, width=700, height=300)
    frame3.place(x=625, y=350)
    trees2 = ttk.Treeview(frame3, height=12)
    trees2['columns'] = ('NBR', 'FNAME', 'SNAME', 'PHONE_NBR', 'CITY', 'DISTRICT', 'ZIP_CODE', 'SALARY', 'COMS_DATE')

    trees2.column('#0', width=0, stretch=NO)
    trees2.column('NBR', anchor=CENTER, width=60)
    trees2.column('SNAME', anchor=CENTER, width=70)
    trees2.column('FNAME', anchor=CENTER, width=70)
    trees2.column('PHONE_NBR', anchor=CENTER, width=90)
    trees2.column('COMS_DATE', anchor=CENTER, width=90)
    trees2.column('CITY', anchor=CENTER, width=80)
    trees2.column('DISTRICT', anchor=CENTER, width=65)
    trees2.column('ZIP_CODE', anchor=CENTER, width=60)
    trees2.column('SALARY', anchor=CENTER, width=60)

    trees2.heading('#0', text='', anchor=CENTER)
    trees2.heading('NBR', text='NBR', anchor=CENTER)
    trees2.heading('SNAME', text='FNAME', anchor=CENTER)
    trees2.heading('FNAME', text='SNAME', anchor=CENTER)
    trees2.heading('PHONE_NBR', text='PHONE_NBR', anchor=CENTER)
    trees2.heading('COMS_DATE', text='COMS_DATE', anchor=CENTER)
    trees2.heading('CITY', text='CITY', anchor=CENTER)
    trees2.heading('DISTRICT', text='DISTRICT', anchor=CENTER)
    trees2.heading('ZIP_CODE', text='ZIP_CODE', anchor=CENTER)
    trees2.heading('SALARY', text='SALARY', anchor=CENTER)
    trees2.place(x=0, y=0)

    title = Label(frame1, text='search or delete a personnel', font=('Times', 11, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=385, y=170)

    sql = """select * from nonnavig"""
    cur.execute(sql)
    rs = cur.fetchall()
    for i in rs:
        trees2.insert(parent='', text='', iid=i[0], index=i[0], values=i)

    ens4 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=11)
    ens4.place(x=395, y=205)
    ens4.insert(0, "   NBR")

    def on_enter(event):
        ens4.config(state=NORMAL)
        if ens4.get() == '   NBR':
            ens4.delete(0, END)

    ens4.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ens4.get() == '':
            ens4.insert(0, "    NBR")

    ens4.bind("<FocusOut>", on_leave)
    # ---------------------------------------------------------
    title = Label(frame1, text='personal in flight', font=('Times', 11, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=105, y=280)
    ens5 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=11)
    ens5.place(x=125, y=315)
    ens5.insert(0, "flight-nbr")

    def on_enter(event):
        ens5.config(state=NORMAL)
        if ens5.get() == 'flight-nbr':
            ens5.delete(0, END)

    ens5.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ens5.get() == '':
            ens5.insert(0, "flight-nbr")

    ens5.bind("<FocusOut>", on_leave)

    title = Label(frame1, text='total flight time', font=('Times', 11, 'bold'), bg='#5AE4A8', fg='#1A2E35')
    title.place(x=400, y=255)
    ens8 = Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=11)
    ens8.place(x=410, y=290)
    ens8.insert(0, "nbr_per")

    def on_enter(event):
        ens8.config(state=NORMAL)
        if ens8.get() == 'nbr_per':
            ens8.delete(0, END)

    ens8.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ens8.get() == '':
            ens8.insert(0, "nbr_per")

    ens8.bind("<FocusOut>", on_leave)
    ens6= Entry(frame1, bg='#1A2E35', font=('Times', 10, 'bold'), fg='grey99', borderwidth=0, width=10)
    ens6.place(x=415, y=315)
    ens6.config(state=DISABLED)
    # ---------------------------------------------------------
    frame4=Frame(plot, width=625, height=260,bg='#1A2E35' )
    frame4.place(x=0,y=350)
    title = Label(frame4, text='technician space', font=('Times', 20, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    title.place(x=225, y=10)
    title = Label(frame4, text='add or update a technician info', font=('Times', 11, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    title.place(x=210, y=55)

    def addnonnav():
        sql = '''select * from nonnavig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if enn1.get() == '       NBR' or enn2.get() == '  fname' or enn3.get() == ' Sname' or enn4.get() == 'phone-number' or enn5.get() == ' city' or enn6.get() == ' distrinct' or enn7.get() == ' zip-code' or enn8.get() == ' salaire' or enn9.get() == ' COMS-DATE':
            error01.place(x=70, y=120)
            error02.place_forget()
            error03.place_forget()
            error04.place_forget()
        elif int(enn1.get()) in l:
            error02.place(x=70, y=120)
            error01.place_forget()
            error03.place_forget()
            error04.place_forget()
        else:
            error03.place(x=70, y=120)
            error02.place_forget()
            error01.place_forget()
            error04.place_forget()
            sql='''insert into nonnavig values({},%s,%s,{},%s,%s,%s,{},%s)'''.format(enn1.get(),enn4.get(),enn8.get())
            cur.execute(sql,(enn3.get(),enn2.get(),enn5.get(),enn6.get(),enn7.get(),enn9.get()))
            val=(enn1.get(),enn3.get(),enn2.get(),enn4.get(),enn5.get(),enn6.get(),enn7.get(),enn8.get(),enn9.get())
            trees2.insert(parent='',text='',iid=enn1.get(),index=enn1.get(),values=val)
            conn.commit()
    btnpil1 = Button(frame4, image=im1, borderwidth=0, bg='#1A2E35', activebackground='#1A2E35', width=70,command=addnonnav )
    btnpil1.place(x=260, y=120)

    def updnonnav():
        sql = '''select * from nonnavig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if enn1.get() == '       NBR' or enn2.get() == '  fname' or enn3.get() == ' Sname' or enn4.get() == 'phone-number' or enn5.get() == ' city' or enn6.get() == ' distrinct' or enn7.get() == ' zip-code' or enn8.get() == ' salaire' or enn9.get() == ' COMS-DATE':
            error01.place(x=70, y=120)
            error02.place_forget()
            error03.place_forget()
            error04.place_forget()
        elif int(enn1.get()) not in l:
            error04.place(x=70, y=120)
            error02.place_forget()
            error01.place_forget()
            error03.place_forget()
        else:
            error03.place(x=70, y=120)
            error02.place_forget()
            error01.place_forget()
            error04.place_forget()
            sql = '''update nonnavig set NOM_NONNAV=%s,PRENOM_NONNAV=%s,TEL_NONNAV={},VIL_NONNAV=%s,QRT_NONNAV=%s,CDP_NONNAV=%s,SAL_NONNAV={},DATEMB_NONNAV=%s where NUMNONNAV={}'''.format(
                enn4.get(), enn8.get(), enn1.get())
            cur.execute(sql, (enn2.get(), enn3.get(), enn5.get(), enn6.get(), enn7.get(), enn9.get()))
            val = (enn1.get(), enn2.get(), enn3.get(), enn4.get(), enn5.get(), enn6.get(), enn7.get(), enn8.get(), enn9.get())
            trees2.item(enn1.get(), text='', values=val)
            conn.commit()
    error01 = Label(frame4, text='one of the fields is empty!!', font=('Times', 10, 'bold'),bg='#1A2E35', fg='#5AE4A8')
    error02 = Label(frame4, text='id already existe', font=('Times', 10, 'bold'),bg='#1A2E35', fg='#5AE4A8')
    error03 = Label(frame4, text='your opearation is done', font=('Times', 10, 'bold'),bg='#1A2E35', fg='#5AE4A8')
    error04 = Label(frame4, text='id does not existe', font=('Times', 10, 'bold'),bg='#1A2E35', fg='#5AE4A8')
    btnpil2 = Button(frame4, image=im2, borderwidth=0, bg='#1A2E35', activebackground='#1A2E35', width=70,command=updnonnav )
    btnpil2.place(x=320, y=120)
    # --------------------------------------------
    enn1 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    enn1.place(x=0, y=90)
    enn1.insert(0, "       NBR")

    def on_enter(event):
        enn1.config(state=NORMAL)
        if enn1.get() == '       NBR':
            enn1.delete(0, END)

    enn1.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn1.get() == '':
            enn1.insert(0, "       NBR")

    enn1.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn2 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    enn2.place(x=66, y=90)
    enn2.insert(0, "  fname")

    def on_enter(event):
        enn2.config(state=NORMAL)
        if enn2.get() == '  fname':
            enn2.delete(0, END)

    enn2.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn2.get() == '':
            enn2.insert(0, "  fname")

    enn2.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn3 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    enn3.place(x=125, y=90)
    enn3.insert(0, " Sname")

    def on_enter(event):
        enn3.config(state=NORMAL)
        if enn3.get() == ' Sname':
            enn3.delete(0, END)

    enn3.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn3.get() == '':
            enn3.insert(0, " Sname")

    enn3.bind("<FocusOut>", on_leave)
    # -------------------------------------------
    enn4 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=12)
    enn4.place(x=184, y=90)
    enn4.insert(0, "phone-number")

    def on_enter(event):
        enn4.config(state=NORMAL)
        if enn4.get() == 'phone-number':
            enn4.delete(0, END)

    enn4.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn4.get() == '':
            enn4.insert(0, "phone-number")

    enn4.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn5 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=8)
    enn5.place(x=271, y=90)
    enn5.insert(0, " city")

    def on_enter(event):
        enn5.config(state=NORMAL)
        if enn5.get() == ' city':
            enn5.delete(0, END)

    enn5.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn5.get() == '':
            enn5.insert(0, " city")

    enn5.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn6 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    enn6.place(x=330, y=90)
    enn6.insert(0, " distrinct")

    def on_enter(event):
        enn6.config(state=NORMAL)
        if enn6.get() == ' distrinct':
            enn6.delete(0, END)

    enn6.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn6.get() == '':
            enn6.insert(0, " distrinct")

    enn6.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn7 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=10)
    enn7.place(x=396, y=90)
    enn7.insert(0, " zip-code")

    def on_enter(event):
        enn7.config(state=NORMAL)
        if enn7.get() == ' zip-code':
            enn7.delete(0, END)

    enn7.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn7.get() == '':
            enn7.insert(0, " zip-code")

    enn7.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn8 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=9)
    enn8.place(x=469, y=90)
    enn8.insert(0, " salaire")

    def on_enter(event):
        enn8.config(state=NORMAL)
        if enn8.get() == ' salaire':
            enn8.delete(0, END)

    enn8.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn8.get() == '':
            enn8.insert(0, " salaire")

    enn8.bind("<FocusOut>", on_leave)
    # --------------------------------------------
    enn9 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=12)
    enn9.place(x=535, y=90)
    enn9.insert(0, " COMS-DATE")

    def on_enter(event):
        enn9.config(state=NORMAL)
        if enn9.get() == ' COMS-DATE':
            enn9.delete(0, END)

    enn9.bind("<Button-1>", on_enter)

    def on_leave(event):
        if enn9.get() == '':
            enn9.insert(0, " COMS-DATE")

    enn9.bind("<FocusOut>", on_leave)
    # -----------------------------------------------hajar
    title = Label(frame4, text='search or delete a personnel', font=('Times', 11, 'bold'),  bg='#1A2E35', fg='#5AE4A8')
    title.place(x=385, y=150)

    ensn4 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    ensn4.place(x=385, y=190)
    ensn4.insert(0, "   NBR")

    def on_enter(event):
        ensn4.config(state=NORMAL)
        if ensn4.get() == '   NBR':
            ensn4.delete(0, END)

    ensn4.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ensn4.get() == '':
            ensn4.insert(0, "    NBR")

    ensn4.bind("<FocusOut>", on_leave)
    def searchinfoa():
        sql = '''select * from nonnavig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ensn4.get() == "   NBR":
            error09.place(x=435, y=230)
            error011.place_forget()
            error012.place_forget()

        elif int(ensn4.get()) not in l:
            error012.place(x=435, y=230)
            error09.place_forget()
            error011.place_forget()
        else:
            error011.place(x=435, y=230)
            error09.place_forget()
            error012.place_forget()
            sear=Toplevel()
            sear.geometry('300x450+0+0')
            sear.resizable(0, 0)
            frameinfo = Frame(sear, width=300, height=450, bg='grey60')
            frameinfo.place(x=0, y=0)
            sql='''select concat(NOM_NONNAV,'-',PRENOM_NONNAV),TEL_NONNAV,concat(VIL_NONNAV,'-',QRT_NONNAV,'-',CDP_NONNAV),SAL_NONNAV,
                 DATEMB_NONNAV from nonnavig where NUMNONNAV={}'''.format(ensn4.get())
            cur.execute(sql)
            rs3=cur.fetchall()
            info = Label(frameinfo, text='information', font=('Comic Sans MS', 15, 'bold'), bg='grey60',
                            fg='#1A2E35')
            info.place(x=80,y=0)
            info = Label(frameinfo, text='FULL_NAME', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=50)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END,rs3[0][0])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=80)
            info = Label(frameinfo, text='PHONE_NAME', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=120)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][1])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=150)

            info = Label(frameinfo, text='Adress', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=190)
            nameemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            nameemp.insert(END, rs3[0][2])
            nameemp.config(state=DISABLED)
            nameemp.place(x=40, y=220)
            info = Label(frameinfo, text='Salaire', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=260)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][3])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=290)

            info = Label(frameinfo, text='DATEMB_NAV', font=('Comic Sans MS', 11, 'bold'), bg='grey60',
                         fg='#1A2E35')
            info.place(x=80, y=330)
            phoneemp = Entry(frameinfo, font=('Comic Sans MS', 12, 'bold'), bg='grey60', fg='#1A2E35', borderwidth=0)
            phoneemp.insert(END, rs3[0][4])
            phoneemp.config(state=DISABLED)
            phoneemp.place(x=40, y=360)
    def dele():
        sql = '''select * from nonnavig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        if ensn4.get() == "   NBR":
            error09.place(x=435, y=230)
            error011.place_forget()
            error012.place_forget()

        elif int(ensn4.get()) not in l:
            error012.place(x=435, y=230)
            error09.place_forget()
            error011.place_forget()
        else:
            error011.place(x=435, y=230)
            error09.place_forget()
            error012.place_forget()
            sql='''delete from avoin_nonnav where NUMNONNAV={}'''.format(ensn4.get())
            cur.execute(sql)
            sql='''delete from nonnavig where NUMNONNAV={}'''.format(ensn4.get())
            cur.execute(sql)
            conn.commit()
            trees2.delete(ensn4.get())
    btnpil3 = Button(frame4, image=im5, borderwidth=0, bg='#1A2E35', activebackground='#1A2E35', width=70, command=dele)
    btnpil3.place(x=515, y=182)
    btnpil3 = Button(frame4, image=im4, borderwidth=0, bg='#1A2E35', activebackground='#1A2E35', width=70,
                     command=searchinfoa)
    btnpil3.place(x=465, y=182)
    error09 = Label(frame4, text='the field is empty!!', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    error011 = Label(frame4, text='your opearation is done', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    error012 = Label(frame4, text='id does not existe', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')

    def persn():
        sql = '''select * from nonnavig'''
        cur.execute(sql)
        rs = cur.fetchall()
        l = []
        for i in rs:
            l.append(i[0])
        sql = '''select * from avoin'''
        cur.execute(sql)
        rs = cur.fetchall()
        l1 = []
        for i in rs:
            l1.append(i[0])
        if ensn7.get()=='id-airplane' or ensn8.get()=='id-tech' :
            error09.place(x=40, y=220)
            error011.place_forget()
            error012.place_forget()
            error013.place_forget()
        elif  int(ensn8.get()) not in l:
            error013.place(x=40, y=220)
            error011.place_forget()
            error09.place_forget()
            error012.place_forget()
        elif  int(ensn7.get()) not in l1:
            error012.place(x=40, y=220)
            error011.place_forget()
            error09.place_forget()
            error013.place_forget()
        else:
            error011.place(x=40, y=220)
            error012.place_forget()
            error09.place_forget()
            error013.place_forget()
            sql='''insert into avoin_nonnav values({},{})'''.format(ensn8.get(),ensn7.get())
            cur.execute(sql)
            conn.commit()
    error09 = Label(frame4, text='one of the fields is empty!!', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    error011 = Label(frame4, text='your opearation is done', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    error012 = Label(frame4, text='id-airplane does not existe', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    error013 = Label(frame4, text='id-tech does not existe', font=('Times', 10, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    btnpiln3 = Button(frame4, image=im6, borderwidth=0, bg='#1A2E35', activebackground='#1A2E35', width=70,command=persn  )
    btnpiln3.place(x=180, y=190)

    # --------------------------------------
    title = Label(frame4, text='add tich to airplane', font=('Times', 11, 'bold'), bg='#1A2E35', fg='#5AE4A8')
    title.place(x=50, y=155)
    ensn7 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    ensn7.place(x=30, y=190)
    ensn7.insert(0, "id-airplane")

    def on_enter(event):
        ensn7.config(state=NORMAL)
        if ensn7.get() == 'id-airplane':
            ensn7.delete(0, END)

    ensn7.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ensn7.get() == '':
            ensn7.insert(0, "id-airplane")

    ensn7.bind("<FocusOut>", on_leave)

    ensn8 = Entry(frame4, bg='grey60', font=('Times', 10, 'bold'), fg='#1A2E35', borderwidth=0, width=11)
    ensn8.place(x=111, y=190)
    ensn8.insert(0, "id-tech")

    def on_enter(event):
        ensn8.config(state=NORMAL)
        if ensn8.get() == 'id-tech':
            ensn8.delete(0, END)

    ensn8.bind("<Button-1>", on_enter)

    def on_leave(event):
        if ensn7.get() == '':
            ensn7.insert(0, "id-tech")

    ensn7.bind("<FocusOut>", on_leave)
    plot.mainloop()
img3=ImageTk.PhotoImage(file='pilot.png')
btnpil=Button(frame_pricipale,image=img3 , borderwidth=0,bg='grey60',activebackground='grey60', width=150,command=emol)
btnpil.place(x=580,y=150)
pilt=Label(frame_pricipale,text='Employe',font=('Times', 20, 'bold'),bg='grey60',fg='#1A2E35')
pilt.place(x=600,y=290)
root.mainloop()


SELECT  * FROM TABLE WHERE NOM=? ;