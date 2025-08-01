from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# --------------------------- SEARCH EMAIL AND PASSWORD -------------------------#
def search():
     website= website_input.get()
     try:
        with open("passwords.json","r") as passwords:
            data = json.load(passwords)
     except FileNotFoundError:
        messagebox.showinfo(title="Error",message=f"No Password File Found")
     else:
            if website in data:
                em= data[website]["email"]
                ps = data[website]["password"]
                messagebox.showinfo(title=f"{website}",message=f"Email: {em}\nPassword: {ps}")
                
            else:     
                messagebox.showinfo(title="X Error X",message=f"No passwords were stored for {website}")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_output.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for x in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for x in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for x in range(random.randint(2,4))]
    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password_generated ="".join(x for x in password_list)
    password_output.insert(0,password_generated)
    pyperclip.copy(password_generated)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website= website_input.get()
    email = email_input.get()
    password = password_output.get()
    new_password_dict = {
       website: {
          "email": email,
          "password":password
       }
    }
    if len(website) ==0  or len(password) == 0:
        messagebox.showinfo(title=f"Oops!",message="Make sure you haven't left anything as empty")
    
    # elif "@" not in email:
    #     messagebox.showwarning(title=f"Invalid Email",message="You have entered an Invalid Mail")
    else:
        try:
            with open("passwords.json","r") as passwords:
                 # Reading Old data
                data = json.load(passwords)
        except FileNotFoundError:
            with open("passwords.json","w") as passwords:
                 # Reading Old data
                data = json.dump(new_password_dict,passwords,indent=4)
        else:
            # just a normal python dictionary
            # Update old data with new data
            data.update(new_password_dict)
        # Write into json file - w
        #json.dump(new_password_dict,passwords,indent=4)
        # Read json file - r
            with open("passwords.json","w") as passwords:
        # save the updated data
                json.dump(data,passwords,indent=4)
        
        finally:   
            messagebox.showinfo("Info", "Password added successfully!") 
            website_input.delete(0,END)
            password_output.delete(0,END)   

# added_text = Label(text="Added")
# added_text.grid(row=5,column=1)
# The above lines are used to display the user that passwords are added
# We can do this using popups in tkinters using tkmessagebox
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_input = Entry(width=32)
website_input.grid(row=1,column=1)
website_input.focus()

search_button = Button(text="Search",width=16,command=search)
search_button.grid(row=1,column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_input = Entry(width=52)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"neelscr007@gmail.com")
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_output = Entry(width=33)
password_output.grid(row=3,column=1)

generate_button = Button(text= "Generate Password",command=generate_password)
generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()