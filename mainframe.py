from tkinter import *

def open_mf():
    win = Tk()
    win.geometry('1000x600')
    win.title('HOTEL MANAGEMENT')
    win.attributes('-fullscreen',True)  #to make win fullscreen
    '''win.attributes('-bottommost',True)'''

    
    # Sliding text
    txt = 'HOSPITAL MANAGEMENT'
    count = 0
    display_text = ''
    label = Label(win, text=display_text, fg='black', font=('Helvetica', 30))
    label.grid(row=2, column=2, pady=100)


    def slider():
        nonlocal count, display_text
        if count >= len(txt):
            count = 0
            display_text = ''
        else:
            display_text += txt[count]
            count += 1
        label.config(text=display_text)
        label.after(100, slider)  # Call the slider function every 500 milliseconds


    slider()



    #adding labels
    register=Button(win,width=40,text='REGISTER PATIENT NAME',font=('arial',20,'bold'))
    register.grid(row=2,column=2,pady=100)
    
    appointment = Button(win,width=40, text='APPLY FOR APPOINTMENT',font=('arial', 20, 'bold'))
    appointment.grid(row=2, column=2, pady=150)
    
    search=Button(win,width=40,text='SEARCH FOR APPOINTMENTS',font=('arial', 20, 'bold'))
    
    
    quit=Button(win,width=40,text='QUIT',font=('arial', 20, 'bold'))
    
    
    
    win.mainloop()
