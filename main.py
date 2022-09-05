# import tkinter , Admin_view python file and Instructor_view file
from tkinter import *
from Admin_view import Admin
from Instructor_view import Instructor

# define window
window = Tk()
window.title('DanceFeet Managment')
window.geometry('1000x600')
window.resizable(False, False)
window.config(background='#e9ecef')


# create a class as a login
class Login:

    def logPage(self):
        # define a function for a open admin view
        def AdminPage():
            nextAdmin = Admin
            nextAdmin.adminPage(window)

        # define a function for a open instructor view
        def instPage():
            nextInstructor = Instructor
            nextInstructor.instPage(window)

        # __ Login Frame __
        Frame_login = Frame(window, width=400, height=400, bg='#ADDFFF', bd=3)
        Frame_login.place(x=100, y=125)
        #  __ Title & Sub title __
        title = Label(Frame_login, text="Login here", font=("Bauhaus 93", 20), fg="#0000A5", bg='#ADDFFF'). \
            place(x=50, y=30)
        subtitle = Label(Frame_login, text="Dancefeet Login Area", font=("Goudy old style", 12), fg="#1d1d1d",
                         bg='#ADDFFF').place(x=50, y=70)

        # __ create button __

        admin = Button(Frame_login, text="Login as a Admin", cursor="hand2", bd=3, width=20,
                       font=("Goudy old style", 12), fg="#1d1d1d", command=AdminPage).place(x=100, y=150)

        instructor = Button(Frame_login, text="Login as a Instructor", cursor="hand2", bd=3, width=20,
                            font=("Goudy old style", 12),
                            fg="#1d1d1d", command=instPage).place(x=100, y=250)

        # create LAbles

        self.dance_name = Label(window, text="Dancefeet", font=("ANDREIAN", 45, "bold"), fg="#151B54").place(
            x=550, y=100)
        self.acd_name = Label(window, text="Academy ", font=("ANDREIAN", 45, "bold"), fg="#151B54").place(
            x=650, y=250)
        self.sys_name = Label(window, text="System.", font=("ANDREIAN", 40, "bold"), fg="#151B54").place(
            x=750, y=400)


Login.logPage(window)

window.mainloop()
