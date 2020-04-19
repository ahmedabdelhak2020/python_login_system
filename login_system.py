from tkinter import *
import tkinter.messagebox
from tkinter import ttk

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("restaurnat login system")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text= 'Restaurant Login', font=('arial',50,'bold'),bg='powder blue', fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)
        #===================================================================
        self.LonginFrame1 = LabelFrame(self.frame, width=1350, height=600,font=('arial',20,'bold'), relief='ridge', bg='cadet blue', bd=20)
        self.LonginFrame1.grid(row=1, column=0)

        self.LonginFrame2 = LabelFrame(self.frame, width=1350, height=600,font=('arial',20,'bold'), relief='ridge', bg='cadet blue', bd=20)
        self.LonginFrame2.grid(row=2, column=0)
        #===========================================Label and Enrtry==========================================
        self.lblUsername = Label(self.LonginFrame1, text='username',font=('arial',20,'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblUsername.grid(row=0, column=0)

        self.txtUsername = Entry(self.LonginFrame1, font=('arial',20,'bold'), textvariable= self.Username)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.LonginFrame1, text='password',font=('arial',20,'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)

        self.txtPassword = Entry(self.LonginFrame1, font=('arial',20,'bold'), show='*', textvariable= self.Password)
        self.txtPassword.grid(row=1, column=1)
        #===========================================Buttons===============================================
        self.btnLogin = Button(self.LonginFrame2, text='Login', width=17, font=('arial',20,'bold'), command = self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnReset = Button(self.LonginFrame2, text='Reset', width=17, font=('arial',20,'bold'), command = self.Rest)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = Button(self.LonginFrame2, text='Exit', width=17, font=('arial',20,'bold'), command = self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)
        self.master.mainloop()
        #===========================================Buttons===============================================
    def Login_System(self):
        U = (self.Username.get())
        P = (self.Password.get())
        if U == str(123456789)and str(987654321):
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
        else:
            tkinter.messagebox.askyesno("login system", "tool pad valid login detail")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    
    def Rest(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("login System", "Confirm if you want to exit")
        if self.iExit >0:
            self.master.destroy()
        else:
            command = self.new_window




    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("restaurnat")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master, bg='cadet blue')
        self.frame.pack()

if __name__ == "__main__":
    root = Tk()
    App_Function = Window1(root)
    