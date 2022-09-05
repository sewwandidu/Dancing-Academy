# import tkinter massegebox,ttk,scrollbar and import sqliet3 database
from tkinter import *
from tkinter import ttk, Scrollbar
import sqlite3
from tkinter import messagebox


# create student class
class Student:
    def studentPage(self):
        global stu
        stu = Toplevel()
        stu.title('DanceFeet Student')
        stu.geometry('1300x600')
        stu.resizable(False, False)
        stu.config(background='#ADDFFF')
        StudentForm.register(stu)


class StudentForm:

    def register(self):

        # connect database
        try:
            con = sqlite3.connect("Database.db")
            cursor = con.cursor()
        except ConnectionError as e:
            print(e)

        # create set data for rows
        def setData(event):
            selected = stu_records.focus()
            chosenData = stu_records.item(selected)
            global chosenRow
            chosenRow = chosenData["values"]
            self.STUID.set(chosenRow[0])
            self.FIRSTNAME.set(chosenRow[1])
            self.SURNAME.set(chosenRow[2])
            self.MAIL.set(chosenRow[3])
            self.ADDRESS.set(chosenRow[4])
            self.GENDER.set(chosenRow[5])
            self.DOB.set(chosenRow[6])
            self.CONTACT.set(chosenRow[7])
            self.STYLE.set(chosenRow[8])
            self.RATE.set(chosenRow[9])
            self.AVAILABILITY.set(chosenRow[10])

        # create add student details for table
        def addStudent():
            try:
                cursor.execute("INSERT INTO student VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                               (self.STUID.get(), self.FIRSTNAME.get(), self.SURNAME.get(), self.MAIL.get(),
                                self.ADDRESS.get(), self.GENDER.get(), self.DOB.get(), self.CONTACT.get(),
                                self.STYLE.get(), self.RATE.get(), self.AVAILABILITY.get()))

                con.commit()
                resetForm()
                viewStudents()
            except sqlite3.IntegrityError as e:
                messagebox.showerror("Error!", "Cannot Insert Duplicate Entries")

        # create reset function
        def resetForm():
            self.STUID.set(0)
            self.FIRSTNAME.set(" ")
            self.SURNAME.set(" ")
            self.MAIL.set(" ")
            self.ADDRESS.set(" ")
            self.DOB.set(" ")
            self.STYLE.set(" ")
            self.GENDER.set(" ")
            self.CONTACT.set(" ")
            self.RATE.set(0.0)
            self.AVAILABILITY.set(" ")

        # create function for view student details
        def viewStudents():
            cursor.execute("SELECT * FROM student")
            results = cursor.fetchall()

            stu_records.delete(*stu_records.get_children())
            for row in results:
                stu_records.insert("", END, values=row)

        # create function for delete student details
        def dltStudents():
            cursor.execute("DELETE FROM student WHERE StudentID = ?", (chosenRow[0],))
            con.commit()
            resetForm()
            viewStudents()

         # create funtion for update student details
        def editStudent():
            cursor.execute(
                "UPDATE student SET firstname=?, surname=?, email=?, address=?, Gender=?, Dob=?, Contact=?, dancestyle=?, Hourlyrate=?, availability=?  WHERE StudentID = ?",
                (self.FIRSTNAME.get(), self.SURNAME.get(), self.MAIL.get(), self.ADDRESS.get(), self.GENDER.get(),
                 self.DOB.get(), self.CONTACT.get(),
                 self.STYLE.get(), self.RATE.get(), self.AVAILABILITY.get(), self.STUID.get()))
            con.commit()
            viewStudents()

        # ----------- create frames ----------------
        Left = Frame(stu, bd=3, relief=RIDGE)
        Left.place(x=5, y=5, width=500, height=590)

        Right = Frame(stu, relief=RIDGE)
        Right.place(x=300, y=5, width=1200, height=590)
        righttitle = Frame(Right, relief=RIDGE)
        righttitle.grid(row=1, column=0, padx=10, pady=10)
        rigthTop = Frame(Right, bd=3, relief=RIDGE)
        rigthTop.grid(row=3, column=0, padx=5, pady=10)

        # ================================================
        self.STUID = IntVar()
        self.FIRSTNAME = StringVar()
        self.SURNAME = StringVar()
        self.MAIL = StringVar()
        self.ADDRESS = StringVar()
        self.DOB = StringVar()
        self.STYLE = StringVar()
        self.GENDER = StringVar()
        self.CONTACT = StringVar()
        self.RATE = DoubleVar()
        self.AVAILABILITY = StringVar()

        # -------------- Student Table view ---------------
        StuID = Label(Left, text="Student ID").grid(row=0, column=0, pady=10, sticky=W)
        first_name = Label(Left, text="First Name").grid(row=1, column=0, pady=10, sticky=W)
        surname = Label(Left, text="Surname").grid(row=2, column=0, pady=10, sticky=W)
        email = Label(Left, text="Email").grid(row=3, column=0, pady=10, sticky=W)
        address = Label(Left, text="Address").grid(row=4, column=0, pady=10, sticky=W)
        gender = Label(Left, text="Gender").grid(row=5, column=0, pady=10, sticky=W)
        dob = Label(Left, text="Date of Birth").grid(row=6, column=0, pady=10, sticky=W)
        contact = Label(Left, text="Contact Num").grid(row=7, column=0, pady=10, sticky=W)
        dancing_style = Label(Left, text="Dance Style").grid(row=8, column=0, pady=10, sticky=W)
        rate = Label(Left, text="Hurley Rate").grid(row=9, column=0, pady=10, sticky=W)
        availability = Label(Left, text="Availability").grid(row=10, column=0, pady=10, sticky=W)
        # self.instructor = Label(self.Left, text="Instructor").place(x=5, y=430)

        stuID_entry = Entry(Left, width=30, textvariable=self.STUID, bd=3).grid(row=0, column=1, pady=10, sticky=W)
        first_name_entry = Entry(Left, width=30, textvariable=self.FIRSTNAME, bd=3).grid(row=1, column=1, pady=10,
                                                                                         sticky=W)
        surname_entry = Entry(Left, width=30, textvariable=self.SURNAME, bd=3).grid(row=2, column=1, pady=10, sticky=W)

        email_entry = Entry(Left, width=30, textvariable=self.MAIL, bd=3).grid(row=3, column=1, pady=10, sticky=W)
        address_entry = Entry(Left, width=30, textvariable=self.ADDRESS, bd=3).grid(row=4, column=1, pady=10, sticky=W)

        gender_entry = ttk.Combobox(Left, textvariable=self.GENDER, width=27, state="readonly")
        gender_entry.grid(row=5, column=1, pady=10, sticky=W)
        gender_entry['values'] = ('male', 'female')

        dob_entry = Entry(Left, width=30, textvariable=self.DOB, bd=3).grid(row=6, column=1, pady=10, sticky=W)
        contact_entry = Entry(Left, width=30, textvariable=self.CONTACT, bd=3).grid(row=7, column=1, pady=10, sticky=W)
        dancing_style_entry = ttk.Combobox(Left, width=27, textvariable=self.STYLE, state="readonly")
        dancing_style_entry.grid(row=8, column=1, pady=10, sticky=W)
        dancing_style_entry['values'] = ('Waltz', 'Jive', 'ChaCha', 'Samba')

        rate_entry = Entry(Left, width=30, textvariable=self.RATE, bd=3).grid(row=9, column=1, pady=10, sticky=W)
        availability_entry = ttk.Combobox(Left, textvariable=self.AVAILABILITY, width=27)
        availability_entry.grid(row=10, column=1, pady=10, sticky=W)
        availability_entry['values'] = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        # availability_entry = Entry(Left, width=30, textvariable=self.AVAILABILITY, bd=3).grid(row=10, column=1, pady=10,sticky=W)

        Left_btn1 = Button(righttitle, width=10, text="SUBMIT", command=addStudent, relief=RIDGE).grid(row=0, column=0)
        Left_btn2 = Button(righttitle, width=10, text="RESET", command=resetForm, relief=RIDGE).grid(row=0, column=1)
        Left_btn3 = Button(righttitle, width=10, text="READ", command=viewStudents, relief=RIDGE).grid(row=0, column=2)
        Left_btn4 = Button(righttitle, width=10, text="DELETE", command=dltStudents, relief=RIDGE).grid(row=0, column=3)
        Left_btn5 = Button(righttitle, width=10, text="UPDATE", command=editStudent, relief=RIDGE).grid(row=0, column=4)

        # ------------------------------------------------
        scroll_y = Scrollbar(rigthTop, orient=VERTICAL)
        stu_records = ttk.Treeview(rigthTop, height=20,
                                   columns=("stuID", "firstName", "surName", "mail", "address", "gender", "DOB",
                                            "Contact", "Style", "rate", "available"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        stu_records.heading('stuID', text='ID')
        stu_records.heading('firstName', text='First Name')
        stu_records.heading('surName', text='SurName')
        stu_records.heading('mail', text='Email')
        stu_records.heading('address', text='Address')
        stu_records.heading('gender', text='Gender')
        stu_records.heading('DOB', text='DOB')
        stu_records.heading('Contact', text='Contact')
        stu_records.heading('Style', text='Style')
        stu_records.heading('rate', text='Rate')
        stu_records.heading('available', text='Availability')

        stu_records['show'] = 'headings'

        stu_records.column('stuID', width=30)
        stu_records.column('firstName', width=80)
        stu_records.column('surName', width=100)
        stu_records.column('mail', width=150)
        stu_records.column('address', width=200)
        stu_records.column('gender', width=50)
        stu_records.column('DOB', width=70)
        stu_records.column('Contact', width=80)
        stu_records.column('Style', width=70)
        stu_records.column('rate', width=70)
        stu_records.column('available', width=70)

        stu_records.pack(fill=BOTH, expand=1)
        stu_records.bind('<ButtonRelease-1>', setData)


