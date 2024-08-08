from tkinter import *


def open_mf():
    win = Tk()
    win.geometry('1000x600')
    win.title('HOSPITAL MANAGEMENT')
    win.attributes('-fullscreen', True)

    # Sliding text
    txt = 'HOSPITAL MANAGEMENT'
    count = 0
    display_text = ''
    label = Label(win, text=display_text, fg='black', font=('Helvetica', 30))
    label.grid(row=0, column=0, columnspan=3, pady=20)

    def slider():
        nonlocal count, display_text
        if count >= len(txt):
            count = 0
            display_text = ''
        else:
            display_text += txt[count]
            count += 1
        label.config(text=display_text)
        label.after(100, slider)  # Call the slider function every 100 milliseconds


    slider()

    # Adding buttons
    register = Button(win, width=40, text='REGISTER PATIENT NAME',
                      font=('arial', 20, 'bold'))
    register.grid(row=1, column=0, padx=20, pady=20)

    appointment = Button(
        win, width=40, text='APPLY FOR APPOINTMENT', font=('arial', 20, 'bold'))
    appointment.grid(row=2, column=0, padx=20, pady=20)

    search = Button(win, width=40, text='SEARCH FOR APPOINTMENTS',
                    font=('arial', 20, 'bold'))
    search.grid(row=3, column=0, padx=20, pady=20)

    quit_button = Button(win, width=40, text='QUIT', font=(
        'arial', 20, 'bold'), command=win.destroy)
    quit_button.grid(row=4, column=0, padx=20, pady=20)

    win.mainloop()
    