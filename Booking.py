# import tkinter ttk and messagebox and Scrollbar
# import sqlite3 database
from tkinter import *
from tkinter import ttk, Scrollbar
import sqlite3


# crete a class
class Lesson:
    def lessonPage(self):
        global book
        book = Toplevel()
        book.title('lesson Sheduling')
        book.geometry('1000x600')
        book.resizable(False, False)
        book.config(background='#ADDFFF')
        BookingForm.register(book)


class BookingForm:
    def register(self):
        # connect database
        try:
            con = sqlite3.connect("Database.db")
            cursor = con.cursor()
        except ConnectionError as e:
            print(e)

        # view Instructor details
        def viewInstructors():
            cursor.execute("SELECT instructorID, name, Gender, dancestyle, Hourlyrate, availability FROM instructor")
            results = cursor.fetchall()

            ins_records.delete(*ins_records.get_children())
            for row in results:
                ins_records.insert("", END, values=row)

        # view Student details
        def viewStudents():
            cursor.execute("SELECT StudentID, firstname, Gender, dancestyle, Hourlyrate, availability FROM student")
            results = cursor.fetchall()

            stu_records.delete(*stu_records.get_children())
            for row in results:
                stu_records.insert("", END, values=row)

        # ----------- Functions ----------------
        def addSession():
            cursor.execute("INSERT INTO schedule VALUES (NULL,?,?,?)",
                           (self.STUNAME.get(), self.INSNAME.get(), self.SESSIONDAY.get()))
            con.commit()
            viewSession()


        # view settion table
        def viewSession():
            cursor.execute("SELECT * FROM schedule")
            results = cursor.fetchall()

            sess_records.delete(*sess_records.get_children())
            for row in results:
                sess_records.insert("", END, values=row)

        # Auto fill selected Student Name
        def setStuNames(event):
            selected1 = stu_records.focus()
            chosenData1 = stu_records.item(selected1)
            chosenRow = chosenData1["values"]
            self.STUNAME.set(chosenRow[1])

        # Auto fill selested Instructor Name And Available day
        def setInsDetails(event):
            selected2 = ins_records.focus()
            chosenData2 = ins_records.item(selected2)
            chosenRow2 = chosenData2["values"]
            self.INSNAME.set(chosenRow2[1])
            self.SESSIONDAY.set(chosenRow2[5])

        # reset Schedules form
        def resetForm():
            self.INSNAME.set(" ")
            self.STUNAME.set(" ")
            self.SESSIONDAY.set(" ")

        # ----------- create frames ----------------

        Left = Frame(book, bd=3, relief=RIDGE)
        Left.place(x=5, y=5, width=700, height=590)

        Right = Frame(book, relief=RIDGE)
        Right.place(x=300, y=3, width=700, height=590)
        righttitle = Frame(Left, relief=RIDGE)
        righttitle.grid(row=8, column=1)
        rigthTop = Frame(Right, bd=3, width=500, height=500, relief=RIDGE)
        rigthTop.place(x=50, y=5)
        rightMidd = Frame(Right, bd=3, width=500, height=500, relief=RIDGE)
        rightMidd.place(x=50, y=200)
        rightBottum = Frame(Right, bd=3, width=500, height=500, relief=RIDGE)
        rightBottum.place(x=50, y=395)

        # ================================================
        self.SESSID = IntVar()
        self.INSNAME = StringVar()
        self.STUNAME = StringVar()
        self.SESSIONDAY = StringVar()

        # -------------- Entry Form view ---------------
        InsID = Label(Left, text="Instructor Name").grid(row=1, column=0, pady=20, padx=10, sticky=W)
        name = Label(Left, text="Sudent Name").grid(row=3, column=0, pady=20, padx=10, sticky=W)
        availability = Label(Left, text="Availabal Day").grid(row=5, column=0, pady=20, padx=10, sticky=W)

        InsID_entry = Entry(Left, width=30, textvariable=self.INSNAME, bd=3, state="readonly").grid(row=1, column=1,
                                                                                                    pady=10, sticky=W)
        stu_name_entry = Entry(Left, width=30, textvariable=self.STUNAME, bd=3, state="readonly").grid(row=3, column=1,
                                                                                                       pady=10,
                                                                                                       sticky=W)
        sessionDay = Entry(Left, width=30, textvariable=self.SESSIONDAY, bd=3, state="readonly").grid(row=5, column=1,
                                                                                                      pady=10, sticky=W)

        Left_btn = Button(righttitle, width=20, text="ADD SESSION", command=addSession, relief=RIDGE, pady=10).grid(
            row=0, column=0)
        Left_btn2 = Button(righttitle, width=20, text="RESET FORM", command=resetForm, relief=RIDGE, pady=10).grid(
            row=1, column=0)
        Left_btn3 = Button(righttitle, width=20, text="VIEW SESSIONS", command=viewSession, relief=RIDGE, pady=10).grid(
            row=2, column=0)

        # ------------------------------------------------
        # Student Table View
        scroll_y = Scrollbar(rigthTop, orient=VERTICAL)
        stu_records = ttk.Treeview(rigthTop, height=8,
                                   columns=("stuID", "firstName", "gender",
                                            "style", "rate", "available"),
                                   yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        stu_records.heading('stuID', text='Student ID')
        stu_records.heading('firstName', text='First Name')
        stu_records.heading('gender', text='Gender')
        stu_records.heading('style', text='Style')
        stu_records.heading('rate', text='Rate')
        stu_records.heading('available', text='Availability')

        stu_records['show'] = 'headings'

        stu_records.column('stuID', width=90)
        stu_records.column('firstName', width=90)
        stu_records.column('gender', width=80)
        stu_records.column('style', width=90)
        stu_records.column('rate', width=90)
        stu_records.column('available', width=90)

        stu_records.pack(fill=BOTH, expand=1)
        stu_records.bind('<ButtonRelease-1>', setStuNames)

        # Instructor Table View
        scroll_y = Scrollbar(rightMidd, orient=VERTICAL)
        ins_records = ttk.Treeview(rightMidd, height=8, columns=("insID", "Name", "style",
                                                                 "gender", "rate", "available"),
                                   yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        ins_records.heading('insID', text='InstructorID')
        ins_records.heading('Name', text='Name')
        ins_records.heading('style', text='Style')
        ins_records.heading('gender', text='Gender')
        ins_records.heading('rate', text='Rate')
        ins_records.heading('available', text='Availability')

        ins_records['show'] = 'headings'
        ins_records.column('insID', width=80)
        ins_records.column('Name', width=90)
        ins_records.column('style', width=70)
        ins_records.column('gender', width=70)
        ins_records.column('rate', width=70)
        ins_records.column('available', width=70)

        ins_records.pack(fill=BOTH, expand=1)
        ins_records.bind('<ButtonRelease-1>', setInsDetails)

        # Session Table View
        scroll_y = Scrollbar(rightBottum, orient=VERTICAL)
        sess_records = ttk.Treeview(rightBottum, height=8, columns=("sessID", "stuName", "insName", "sessDay"),
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

        viewInstructors()
        viewStudents()
