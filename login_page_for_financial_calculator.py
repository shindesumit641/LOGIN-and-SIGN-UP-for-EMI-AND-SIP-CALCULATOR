# _____________________________LOGIN PAGE________________________

from tkinter import *
from tkinter import messagebox
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.root.geometry("1350x700+0+0")

        #-----------ALl VARIABLE------------
        self.username_var=StringVar()
        self.password_var=StringVar()
        self.email_var=StringVar()
        self.phone_var=StringVar()


        Out_side_frame = Frame(self.root, bd=5, relief=GROOVE, bg="blue")
        Out_side_frame.place(x=0, y=0, width=1350, height=700)

        Out_side_in_frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Out_side_in_frame.place(x=75, y=75, width=1350 - 150, height=700 - 150)

        F = Frame(self.root, bd=15, relief=GROOVE, bg="#1affff")
        F.place(x=350, y=150, width=750, height=350)

        # assining variable
        self.user = StringVar()
        self.password = StringVar()

        title_for_login = Label(self.root, text="LOGIN SYSTEM", font=("times new roman", 30, "bold"), bg="white",
                                fg="#ff6600").grid(row=0, column=1, padx=600, pady=90)

        userlabel = Label(F, text="UserName ", font=("times new roman", 20, "bold"), bg="#1affff", fg="#1a1aff").grid(row=1,
                                                                                                                 column=0,
                                                                                                                 padx=50,
                                                                                                                 pady=50)
        user_text = Entry(F, bd=7, relief=GROOVE, textvariable=self.username_var, width=30, font=("arial 15 bold"))
        user_text.grid(row=1, column=1)

        passwordlabel = Label(F, text="Password ", font=("times new roman", 20, "bold"), bg="#1affff", fg="#1a1aff").grid(
            row=2, column=0, padx=50, pady=0)
        password_text = Entry(F, bd=7, relief=GROOVE, show="*", textvariable=self.password_var, width=30,
                              font=("arial 15 bold"))
        password_text.grid(row=2, column=1)

        Button_Login = Button(F, text="Login", font="arial 15 bold", bd=7, bg="white", fg="blue", width=10,
                              command=self.Check_login)
        Button_Login.place(x=100, y=250)
        Button_Reset = Button(F, text="Reset", font="arial 15 bold", bd=7, bg="white", fg="blue", width=10,
                              command=self.reset)
        Button_Reset.place(x=300, y=250)
        Button_Exit = Button(F, text="Exit", font="arial 15 bold", bd=7, bg="white", fg="blue", width=10,
                             command=self.exit_fun)
        Button_Exit.place(x=500, y=250)

        Button_SignUp = Button(self.root, text="Sign Up", font="arial 15 bold", bd=7, bg="#ff6600", fg="white", width=10,
                               activebackground="blue", command=self.sign_up)
        Button_SignUp.place(x=665, y=550)

    def Check_login(self):
        login=False
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute('select Username , Password from login')

        for email,password in cur:
            if(email==self.username_var.get() and password==self.password_var.get()):
                self.logfun()
                login=True
                break

        if(login==False):
            messagebox.showinfo('InCorrect Login','YOU HAVE ENTER WRONG USERNAME OR PASSWORD \n Please Check Once Again!!! ')


        con.commit()
        con.close()



    def sip(self):

        # _________________SIP CALCULATOR__________________________

        top2 = Toplevel()
        # title of the window
        top2.title("SIP CALCULATOR")
        # geometry of the window
        top2.geometry("1350x700+0+0")

        F1 = Frame(top2, bd=10, relief=GROOVE)
        F1.place(x=200, y=50, width=950, height=600)

        title = Label(F1, text="SIP CALCULATOR", font=("time new roman", 30, "bold"), fg="blue").grid(row=0, column=1)

        e1 = IntVar()
        e2 = IntVar()
        e3 = IntVar()

        L1 = Label(F1, text="SIP AMOUNT ", font=("time new roman", 20, "bold")).grid(row=1, column=0, pady=20)
        e1 = Entry(F1, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        e1.grid(row=1, column=1, padx=20, pady=20)

        L2 = Label(F1, text="NUMBER OF YEARS ", font=("time new roman", 20, "bold")).grid(row=2, column=0, pady=20)
        e2 = Entry(F1, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        e2.grid(row=2, column=1, padx=20, pady=20)

        L3 = Label(F1, text=" RETURNS ", font=("time new roman", 20, "bold")).grid(row=3, column=0, pady=20)
        e3 = Entry(F1, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        e3.grid(row=3, column=1, padx=20, pady=20)
        L4 = Label(F1, text=" % ", font=("time new roman", 20, "bold")).grid(row=3, column=2, padx=0, pady=20)


         # noinspection PyMethodParameters
        def Sip_calculator():
            # principal amount
            investment = int(e1.get())

            print(e1.get())
            print(e2.get())
            print(e3.get())

            # Rate of Return
            annualRate = int(e3.get())
            monthlyRate = annualRate / 12 / 100  # Rate of interest

            # Time period
            years = int(e2.get())
            months = years * 12

            # Future Value of the amount invested per month
            futureValue = int(investment * (pow(1 + float(monthlyRate), int(months)) - 1) / monthlyRate)

            print(futureValue)

            Future_value = Label(F1, text=futureValue, font=("time new roman", 50, "bold"), bg="blue", fg="white",
                                 width=10, bd=7).grid(row=10, column=1, padx=0, pady=40)

        submit = Button(F1, text=" CALCULATE ", font="arial 15 bold", bg="blue", fg="white", command=Sip_calculator,bd=7, width=10).grid(row=4, column=1, padx=0, pady=20)


    def emi(self):
         # _____________________EMI CALCULATOR_____________________

        top = Toplevel()
        # title of the window
        top.title("EMI CALCULATOR")
        # geometry of the window
        top.geometry("1350x700+0+0")

        F2 = Frame(top, bd=10, relief=GROOVE)
        F2.place(x=200, y=50, width=950, height=600)

        title = Label(F2, text="EMI CALCULATOR", font=("time new roman", 30, "bold"), fg="blue").grid(row=0, column=1)

        E1 = IntVar()
        E2 = IntVar()
        E3 = IntVar()

        L1 = Label(F2, text="PRINCIPLE AMOUNT", font=("time new roman", 20, "bold")).grid(row=1, column=0, pady=20)
        E1 = Entry(F2, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        E1.grid(row=1, column=1, padx=20, pady=20)

        L2 = Label(F2, text="NUMBER OF YEARS ", font=("time new roman", 20, "bold")).grid(row=2, column=0, pady=20)
        E2 = Entry(F2, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        E2.grid(row=2, column=1, padx=20, pady=20)

        L3 = Label(F2, text=" RATE ", font=("time new roman", 20, "bold")).grid(row=3, column=0, pady=20)
        E3 = Entry(F2, bd=7, relief=GROOVE, width=25, font=("arial 15 bold"))
        E3.grid(row=3, column=1, padx=20, pady=20)
        L4 = Label(F2, text=" % ", font=("time new roman", 20, "bold")).grid(row=3, column=2, padx=0, pady=20)

        def EMI_calculator():

            Principal = int(E1.get())
            Rate = int(E3.get())
            MonthlyRate = Rate / (12 * 100)
            Years = int(E2.get())
            Months = Years * 12

            EMI = round((Principal * MonthlyRate * (1 + MonthlyRate) ** Months) / ((1 + MonthlyRate) ** Months - 1))

            TotalInterest = (EMI * Months) - Principal

            TotalPayment = int(Principal) + int(TotalInterest)

            print("EMI To paid :", EMI)
            print("Total Interest to be Paid :", TotalInterest)
            print("Total Payment to be Done :", TotalPayment)

            EMI_Value = Label(F2, text="EMI  " + str(EMI), font=("time new roman", 30, "bold"), fg="red").grid(row=9,
                                                                                                               column=0,
                                                                                                               padx=0,
                                                                                                               pady=20)
            Interest_Value = Label(F2, text=" INTEREST AMOUNT " + str(TotalInterest), font=("time new roman", 30, "bold"),
                                   bg="blue", fg="white").grid(row=9, column=1, padx=0, pady=20)
            Payment_Value = Label(F2, text=" TOTAL PAYMENT " + str(TotalPayment), font=("time new roman", 30, "bold"),
                                  bg="blue", fg="white").grid(row=10, column=1, padx=0, pady=10)

        submit1 = Button(F2, text=" CALCULATE ", font="arial 15 bold", bg="blue", fg="white", command=EMI_calculator, bd=7,
                         width=10).grid(row=4, column=1, padx=0, pady=20)

    def logfun(self):
        print(self.user.get(), self.password.get())
        display = messagebox.showinfo("Info", "Welcome " + self.username_var.get())



        top1 = Toplevel()
        top1.title("Choose the Option")
        top1.geometry("1350x700+0+0")

        Option_frame = Frame(top1, bd=5, relief=GROOVE, bg="blue")
        Option_frame.place(x=0, y=0, width=1350, height=700)

        Out_side_in_frame1 = Frame(Option_frame, bd=5, relief=GROOVE, bg="white")
        Out_side_in_frame1.place(x=50, y=50, width=1350 - 100, height=700 - 100)

        Option_label = Label(Out_side_in_frame1, text=" Choose The Option? ", font=("times new roman", 30, "bold"),
                             bg="white", fg="blue")
        Option_label.place(x=500, y=50)

        Emi_button = Button(Out_side_in_frame1, text=" EMI CALCULATION ", bd=10, font=("times new roman", 30, "bold"),
                            bg="blue", fg="white", width=10, activebackground="orange",command=self.emi)
        Emi_button.place(x=425, y=200, width=500, height=100)

        sip_button = Button(Out_side_in_frame1, text=" SIP CALCULATION ", bd=10, font=("times new roman", 30, "bold"),
                            bg="blue", fg="white", width=10, activebackground="orange", command=self.sip)
        sip_button.place(x=425, y=400, width=500, height=100)
        return

    def reset(self):

        self.user.set("")
        self.password.set("")
        self.username_var.set("")
        self.password_var.set("")
        self.email_var.set("")
        self.phone_var.set("")

    def exit_fun(self):
        option = messagebox.askyesno("Exit", "Do you really want to exit?")

        if option == 1:
            self.root.destroy()
        else:
            return

    def sign_up(self):

        top3=Toplevel()
        top3.title("Sign Up")
        top3.geometry("1350x700+0+0")

        Sign_up_frame = Frame(top3, bd=5, relief=GROOVE, bg="#ff6600")
        Sign_up_frame.place(x=0, y=0, width=1350, height=700)

        Sign_up_in_frame = Frame(Sign_up_frame, bd=5, relief=GROOVE, bg="white")
        Sign_up_in_frame.place(x=50, y=50, width=1350 - 100, height=700 - 100)

        Sign_up_inside_in_frame = Frame(Sign_up_frame, bd=5, relief=GROOVE, bg="#ff6600")
        Sign_up_inside_in_frame.place(x=200, y=125, width=1350 - 400, height=700 - 250)

        title_label = Label(Sign_up_in_frame, text=" Sign In ", font=("times new roman", 30, "bold"), bg="white",
                            fg="#ff0000")
        title_label.place(x=550 + 50, y=5)

        Username_label = Label(Sign_up_inside_in_frame, text=" Username ", font=("times new roman", 25, "bold"),
                               bg="#ff6600", fg="white")
        Username_label.place(x=200, y=20)
        username_text = Entry(Sign_up_inside_in_frame, bd=7,textvariable=self.username_var, relief=GROOVE, width=25, font=("arial 15 bold"))
        username_text.place(x=400, y=20)

        Password_label = Label(Sign_up_inside_in_frame, text=" Password", font=("times new roman", 25, "bold"),
                               bg="#ff6600", fg="white")
        Password_label.place(x=200, y=90)
        Password_text = Entry(Sign_up_inside_in_frame, bd=7,textvariable=self.password_var, relief=GROOVE, show="*", width=25, font=("arial 15 bold"))
        Password_text.place(x=400, y=90)

        Email_label = Label(Sign_up_inside_in_frame, text=" Email ", font=("times new roman", 25, "bold"), bg="#ff6600",
                            fg="white")
        Email_label.place(x=200, y=90 + 70)
        Email_text = Entry(Sign_up_inside_in_frame, bd=7,textvariable=self.email_var, relief=GROOVE, width=25, font=("arial 15 bold"))
        Email_text.place(x=400, y=90 + 70)

        Phone_label = Label(Sign_up_inside_in_frame, text=" Phone no ", font=("times new roman", 25, "bold"),
                            bg="#ff6600", fg="white")
        Phone_label.place(x=200, y=160 + 70)
        Phone_text = Entry(Sign_up_inside_in_frame, bd=7,textvariable=self.phone_var, relief=GROOVE, width=25, font=("arial 15 bold"))
        Phone_text.place(x=400, y=160 + 70)



        Submit = Button(Sign_up_inside_in_frame, text=" Submit ", bd=7, font=("times new roman", 25, "bold"),
                        bg="white", fg="#ff0000",command=self.Enter_data)
        Submit.place(x=450, y=330)


    def Enter_data(self):
        con=pymysql.connect(host="localhost",user="root",password="Sumit@123",database="stm")
        cur=con.cursor()
        cur.execute('insert into login values(%s,%s,%s,%s)',(self.username_var.get(),
                                                             self.password_var.get(),
                                                             self.email_var.get(),
                                                             self.phone_var.get()
                                                            ))

        con.commit()
        con.close()
        self.reset()

root = Tk()
ob = Login(root)
root.mainloop()
  
