from tkinter import*
root=Tk()
root.title("Inheritance project")
root.geometry("600x600")

user_name = Entry(root)
user_name.pack()

email_id = Entry(root)
email_id.pack()

lbl = Label(root)

dictionary = {}

class Users: 
    
    def addUser(key, value): 
        global dictionary
        dictionary[key] = value
        lbl["text"] = dictionary

class GetUsers(Users): 
        
    def getUser(self):
        un = user_name.get()
        ei = email_id.get()
        Users.addUser(un, ei)

user = GetUsers()

btn = Button(root, text="Add User Details", command = user.getUser)
btn.place(relx = 0.5, rely = 0.4, anchor = CENTER)

lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()