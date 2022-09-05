# import tkinter,ttk and sqlite3 database
from tkinter import *
from tkinter import ttk
import sqlite3

# creat class
class Instructor:
    def instPage(self):
        global instview
        instview = Toplevel()
        instview.title('DanceFeet Instructor View')
        instview.geometry('600x600')
        instview.resizable(False, False)
        instview.config(background='#e9ecef')
        InstructorForm.view(instview)


class InstructorForm:
    def view(self):
        # connect database
        try:
            con = sqlite3.connect("Database.db")
            cursor = con.cursor()
        except ConnectionError as e:
            print(e)

        # ----------- create frames ----------------
        Right = Frame(instview, relief=RIDGE)
        Right.place(x=30, y=5, width=700, height=590)

        rigthTop = Frame(Right, bd=3, relief=RIDGE)
        rigthTop.place(x=20, y=5)

        # ----------------Methods------------------------------
        def viewSession():
            cursor.execute("SELECT * FROM schedule")
            results = cursor.fetchall()

            sess_records.delete(*sess_records.get_children())
            for row in results:
                sess_records.insert("", END, values=row)

        # ------------------------------------------------
        title = Label(rigthTop, text="Current Sessions List", font=("Times New Roman", 16, "bold")).pack(fill=BOTH)
        scroll_y = Scrollbar(rigthTop, orient=VERTICAL)
        sess_records = ttk.Treeview(rigthTop, height=15, columns=("sessID", "stuName", "insName", "sessDay"),
                                    yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        sess_records.heading('sessID', text='SessionID')
        sess_records.heading('stuName', text='Student Name')
        sess_records.heading('insName', text='Instructor Name')
        sess_records.heading('sessDay', text='Session Day')

        sess_records['show'] = 'headings'

        sess_records.column('sessID', width=100)
        sess_records.column('stuName', width=150)
        sess_records.column('insName', width=150)
        sess_records.column('sessDay', width=100)

        sess_records.pack(fill=BOTH, expand=1)

        viewSession()
