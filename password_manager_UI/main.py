from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip

##constants
my_image = "logo.png"


def password_button(): #password button function
    random_password = password_generator() #password generator
    password_entry.delete(0, END)
    password_entry.insert(0,random_password)
    pyperclip.copy(random_password) #copy the password so that the user can use it instant


def append_to_file():#saves username,password and email to file - popup message
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    if password != "" and email != "" and website != "":
        popup_box = messagebox.askokcancel(title="Add info?",message=f"Your details:\nWebsite:{website} \nEmail:{email}"
                                           f"\nPassword:{password} \n Adding info to password file, Continue?")
        if popup_box: #if true
            #opens the password file and writes on it
            password_file = open("password.txt", "a")
            password_file.write(f"{website} - {email} - {password}\n")
            password_file.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Error!",message="All field are mandatory")



##UI
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

##image
canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_image = PhotoImage(file=my_image) #change
canvas.create_image(100, 100, image=logo_image) #change
canvas.grid(column=1, row=0)

##labels
website_label = Label(text="Website:", font=("Times new roman", 18))
website_label.grid(column=0, row=1)
website_label.config()

email_label = Label(text="Email/Username:", font=("Times new roman", 18))
email_label.grid(column=0, row=2)
email_label.config()

password_label = Label(text="Password:", font=("Times new roman", 18))
password_label.grid(column=0, row=3)
password_label.config()

##Entries

website_entry = Entry(width=35)
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1,columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, string="alex@gmail.com")
email_entry.grid(column=1, row=2,columnspan=2)

password_entry = Entry(width=21)
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

##buttons
generate_password_button = Button(text="Generate Password", command=password_button)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", command=append_to_file, width=36)
add_password_button.grid(column=1, row=4,columnspan=2)


window.mainloop()