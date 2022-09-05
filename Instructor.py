# import tkinter,ttk,Scorollbar and ,messagaebox
# imoprt sqlite3 database
from tkinter import *
from tkinter import ttk, Scrollbar
from tkinter import messagebox
import sqlite3

# create class
class Insdetails:
    def instructorPage(self):
        global ins
        ins = Toplevel()
        ins.title('DanceFeet Instructor')
        ins.geometry('1000x600')
        ins.resizable(False, False)
        ins.config(background='#ADDFFF')
        InstructorForm.register(ins)


class InstructorForm:

    def register(self):
        # connect database
        try:
            con = sqlite3.connect("Database.db")
            cursor = con.cursor()
        except ConnectionError as e:
            print(e)

        # set data function
        def setData(event):
            selected = ins_records.focus()
            chosenData = ins_records.item(selected)
            global chosenRow
            chosenRow = chosenData["values"]
            self.INSID.set(chosenRow[0])
            self.INSNAME.set(chosenRow[1])
            self.GENDER.set(chosenRow[2])
            self.CONTACT.set(chosenRow[3])
            self.STYLE.set(chosenRow[4])
            self.RATE.set(chosenRow[5])
            self.AVAILABILITY.set(chosenRow[6])
         # add data for Instructor database
        def addInstructor():
            try:
                cursor.execute("INSERT INTO instructor VALUES (?,?,?,?,?,?,?)",
                               (self.INSID.get(), self.INSNAME.get(), self.GENDER.get(), self.CONTACT.get(),
                                self.STYLE.get(), self.RATE.get(), self.AVAILABILITY.get()))

                con.commit()
                resetForm()
                viewInstructors()
            except sqlite3.IntegrityError as e:
                messagebox.showerror("Error!", "Cannot Insert Duplicate Entries")
         # reset Instructor form
        def resetForm():
            self.INSID.set(0)
            self.INSNAME.set(" ")
            self.GENDER.set(" ")
            self.CONTACT.set(" ")
            self.STYLE.set(" ")
            self.RATE.set(0.0)
            self.AVAILABILITY.set(" ")

         # view instructor database
        def viewInstructors():
            cursor.execute("SELECT * FROM instructor")
            results = cursor.fetchall()

            ins_records.delete(*ins_records.get_children())
            for row in results:
                ins_records.insert("", END, values=row)

        # delete Instructor recodes
        def dltInstructor():
            print(type(chosenRow[0]))
            cursor.execute("DELETE FROM instructor WHERE InstructorID = ?", (chosenRow[0],))
            con.commit()
            resetForm()
            viewInstructors()

        # update Instructor details
        def editInstructor():
            cursor.execute(
                "UPDATE instructor SET name=?, Gender=?, Contact=?, dancestyle=?, Hourlyrate=?, availability=? WHERE InstructorID = ?",
                (self.INSNAME.get(), self.GENDER.get(), self.CONTACT.get(), self.STYLE.get(), self.RATE.get(),
                 self.AVAILABILITY.get(), self.INSID.get()))
            con.commit()
            resetForm()
            viewInstructors()

        # ----------- create frames ----------------
        Left = Frame(ins, bd=3, relief=RIDGE)
        Left.place(x=5, y=5, width=300, height=590)

        Right = Frame(ins, relief=RIDGE)
        Right.place(x=300, y=5, width=700, height=590)
        righttitle = Frame(Right, relief=RIDGE, padx=10, pady=10)
        righttitle.grid(row=0, column=0)
        rigthTop = Frame(Right, bd=3, relief=RIDGE, padx=10, pady=10)
        rigthTop.grid(row=1, column=0)

        # ================================================
        self.INSID = IntVar()
        self.INSNAME = StringVar()
        self.STYLE = StringVar()
        self.GENDER = StringVar()
        self.CONTACT = StringVar()
        self.RATE = DoubleVar()
        self.AVAILABILITY = StringVar()

        # -------------- Student Table view ---------------
        InsID = Label(Left, text="Instructor ID").grid(row=1, column=0, pady=10, sticky=W)
        name = Label(Left, text="Name").grid(row=3, column=0, pady=10, sticky=W)
        gender = Label(Left, text="Gender").grid(row=5, column=0, pady=10, sticky=W)
        contact = Label(Left, text="Contact Num").grid(row=7, column=0, pady=10, sticky=W)
        dancing_style = Label(Left, text="Dance Style").grid(row=9, column=0, pady=10, sticky=W)
        rate = Label(Left, text="Hurley Rate").grid(row=11, column=0, pady=10, sticky=W)
        availability = Label(Left, text="Availability").grid(row=13, column=0, pady=10, sticky=W)

        stuID_entry = Entry(Left, width=30, textvariable=self.INSID, bd=3).grid(row=1, column=1, pady=10, sticky=W)
        first_name_entry = Entry(Left, width=30, textvariable=self.INSNAME, bd=3).grid(row=3, column=1, pady=10,
                                                                                       sticky=W)
        gender_entry = ttk.Combobox(Left, textvariable=self.GENDER, width=27, state="readonly")
        gender_entry.grid(row=5, column=1, pady=10, sticky=W)
        gender_entry['values'] = ('male', 'female')
        contact_entry = Entry(Left, width=30, textvariable=self.CONTACT, bd=3).grid(row=7, column=1, pady=10, sticky=W)
        dancing_style_entry = ttk.Combobox(Left, textvariable=self.STYLE, width=27, state="readonly")
        dancing_style_entry.grid(row=9, column=1, pady=10, sticky=W)
        dancing_style_entry['values'] = ('Waltz', 'Jive', 'ChaCha', 'Samba')
        rate_entry = Entry(Left, width=30, textvariable=self.RATE, bd=3).grid(row=11, column=1, pady=10, sticky=W)
        availability_entry = ttk.Combobox(Left, textvariable=self.AVAILABILITY, width=27, state="readonly")
        availability_entry.grid(row=13, column=1, pady=10, sticky=W)
        availability_entry['values'] = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

        Left_btn = Button(righttitle, width=10, text="SUBMIT", command=addInstructor, relief=RIDGE).grid(row=0,
                                                                                                         column=0)
        Left_btn2 = Button(righttitle, width=10, text="RESET", command=resetForm, relief=RIDGE).grid(row=0, column=1)
        Left_btn3 = Button(righttitle, width=10, text="READ", command=viewInstructors, relief=RIDGE).grid(row=0,
                                                                                                          column=2)
        Left_btn4 = Button(righttitle, width=10, text="DELETE", command=dltInstructor, relief=RIDGE).grid(row=0,
                                                                                                          column=3)
        Left_btn5 = Button(righttitle, width=10, text="UPDATE", command=editInstructor, relief=RIDGE).grid(row=0,
                                                                                                           column=4)

        # ------------------------------------------------
        scroll_y = Scrollbar(rigthTop, orient=VERTICAL)
        ins_records = ttk.Treeview(rigthTop, height=15, columns=("insID", "Name", "gender",
                                                                 "contact", "style", "rate", "available"),
                                   yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        ins_records.heading('insID', text='InstructorID')
        ins_records.heading('Name', text='Name')
        ins_records.heading('gender', text='Gender')
        ins_records.heading('contact', text='Contact')
        ins_records.heading('style', text='Style')
        ins_records.heading('rate', text='Rate')
        ins_records.heading('available', text='Availability')

        ins_records['show'] = 'headings'
        ins_records.column('insID', width=80)
        ins_records.column('Name', width=90)
        ins_records.column('gender', width=70)
        ins_records.column('contact', width=70)
        ins_records.column('style', width=80)
        ins_records.column('rate', width=70)
        ins_records.column('available', width=70)

        ins_records.pack(fill=BOTH, expand=1)
        ins_records.bind('<ButtonRelease-1>', setData)
