#login frame
from tkinter import *
from tkinter import messagebox
import database as db
import hashlib
import mainframe as mf
#1st window(login)
log=Tk()
log.geometry('720x800')


#window title
log.title('HOSPITAL MANAGEMENT') 

#window label


#Title
tusername=Label(log,text='username')
tusername.grid(row=2, column=1, pady=40)
tpassword=Label(log,text='password')
tpassword.grid(row=3, column=1, pady=50)

# ENTRY (for user to input into)
# for username
username = Entry(log, bg='yellow', fg='navy', font=('arial', 10, 'bold') ,width=40)
username.grid(row=2, column=2, pady=40)

password = Entry(log, bg='yellow', fg='navy', font=('arial', 10, 'bold'), width=40)
password.grid(row=3, column=2, pady=50)


user=[]
passw=[]
def get():
    user_input=username.get()
    passw_input=password.get()
    #hashing passw to hash value

    hashed_passw=hashlib.md5(passw_input.encode()).hexdigest()

    stored_user='hi'
    stored_passw = '202cb962ac59075b964b07152d234b70'

    if user_input==stored_user and hashed_passw==stored_passw:
        messagebox.showinfo('!alert!','login successful')
        log.destroy()
        mf.open_mf()
    else:
        messagebox.showerror('!alert!','login failed')
        log.destroy()
    
    

# BUTTONS
but1 = Button(log, text='login', height=3, width=30, command=lambda:{get()})
but1.place(x=250, y=600)

log.mainloop()