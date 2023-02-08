from tkinter import *
from tkinter import messagebox

def info_erreur():
    messagebox.showinfo('Erreur_Fatal', 'ATTENTION\nTrop de tentatives votre machine va exploser!')

def mess_e_mail():
    messagebox.showinfo('info_e_mail', 'User_name: k4cK3rM4n04\n Password: k4cK3rM4n04')

def mess_agora_pc_mika_mathieu():
    messagebox.showinfo('info_agora', 'User_name: k4cK3rM4n04\n Password: k4cK3rM4n04')

def mess_pix():
    messagebox.showinfo('info_pix', 'User_name: k4cK3rM4n04\n Password: k4cK3rM4n04')

def acces():
    x, y = user_entry.get(), pass_entry.get()
    if x == "04" and y == "04":
        text_error.config(text='Choose your password', fg = 'lightgreen')
        button_validate.config(text='Agora_pass', command = mess_agora_pc_mika_mathieu)
        texte_vide.destroy()

        button_email.config(text='E-mail_pass')
        button_email.grid(row=3, column=0, sticky=W)

        button_pix.config(text='    Pix_pass    ', command = mess_pix)
        button_pix.grid(row=3, column=2, sticky=W)
    else:
        text_error.config(text='ERROR ACCES DENIED')
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        button_validate.config(command = info_erreur)



window = Tk()

window.title("Password Store")
window.geometry("552x300")
window.minsize(500, 300)
window.config(background='darkblue')


texte_vide = Label(window, text="You only have one attemp!", bg = 'darkblue',
                   font = ('Arial', 15), fg = 'white')
texte_vide.grid(row=6, column=1, sticky=W)

user_name = Label(window, text='User_name:  ', font=('Helvetica', 24),bg='darkblue',fg='white')
password = Label(window, text='Password:    ',font=('Helvetica', 24), bg='darkblue',fg='white')

user_entry = Entry(window, font=('Helvetica'))
pass_entry = Entry(window, show='♥', font=('Arial'))

button_validate = Button(window, text='Validate', font=('Arial', 15), bg='darkgrey', command = acces)

text_error = Label(window, font=('Arial', 15), text="", bg='darkblue', fg='red')

button_email = Button(window, font = ('Arial', 15), bg = 'darkgrey', command = mess_e_mail)

button_pix = Button(window, font = ('Arial', 15), bg = 'darkgrey')


user_name.grid(row=0, column=0, sticky=W)
password.grid(row=1, column=0,sticky=W)

user_entry.grid(row=0, column=1, sticky=W)
pass_entry.grid(row=1, column=1,sticky=W)

button_validate.grid(row=3, column=1, sticky=W, pady=20)

text_error.grid(row=2, column=1, sticky=W)


window.mainloop()