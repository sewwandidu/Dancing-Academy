#import tkinter
#import Student file
#import Instructor file
#import Bokking file

from tkinter import *
from Student import Student
from Instructor import Insdetails
from Booking import Lesson

# crate a class
class Admin:
    def adminPage(self):
        global insadmin
        insadmin = Toplevel()
        insadmin.title('DanceFeet Admin View')
        insadmin.geometry('500x500')
        insadmin.resizable(False, False)
        insadmin.config(background='#ADDFFF')
        Ins_reg.ins_regpage(insadmin)


class Ins_reg:
    def ins_regpage(self):
        # student page get
        def studentPage():
            stu = Student
            stu.studentPage(insadmin)
        # Instructor page get
        def instructorPage():
            ins = Insdetails
            ins.instructorPage(insadmin)
        # lesson page get
        def lessonPage():
            book = Lesson
            book.lessonPage(insadmin)

        title = Label(insadmin, text="Admin Area", font=("Goudy old style", 12), fg="#1d1d1d", bg="#ADDFFF"
                      ).place(x=50, y=70)

        # ============================================================================================================================================================

        # __ Create Button __

        Stu_display = Button(insadmin, text="Display Student", cursor="hand2", bd=3, width=20, height=0,
                             font=("Goudy old style", 12), fg="#1d1d1d", bg='#00FFFF', command=studentPage).place(x=150,
                                                                                                                  y=150)

        Ins_display = Button(insadmin, text="Display Instructor", cursor="hand2", bd=3, width=20, height=0,
                             font=("Goudy old style", 12), fg="#1d1d1d", bg='#FFFF00', command=instructorPage).place(
            x=150, y=250)

        lesson_booking_display = Button(insadmin, text="Display lesson booking", cursor="hand2", bd=3, width=20,
                                        height=0,
                                        font=("Goudy old style", 12), fg="#1d1d1d", bg='#F433FF',
                                        command=lessonPage).place(x=150, y=350)

    # ------------------------------------------------------------------
