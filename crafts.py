from tkinter import *
from random import randint

root = Tk()
root.title('Quản lý mật khẩu')
# root.iconbitmap('10819.png')
root.geometry('670x600')
# my_password = chr(randint(33, 126))
# def new_rand():
#     #Clear entryBox
#     pw_entry.delete(0, END)
#
#     #get password length and convert to integer
#     pw_length = int(my_entry.get())
#
#     #create a variable to hold our password
#     my_password = ''
#
#     #loop through password length
#     for x in range(pw_length):
#         my_password += chr(randint(33, 126))
#     #output password to screen
#     pw_entry.insert(0, my_password)
#
# def copy_password():
#     root.clipboard_clear()
#     root.clipboard_append(pw_entry.get())
# # LabelFrame
# lf = LabelFrame(root, text="How many characters? ")
# lf.pack(pady=20)
#
#
# #Entry Box
# my_entry = Entry(lf, font=("Helvetica", 24))
# my_entry.pack(padx=20, pady=20)
#
# pw_entry = Entry(root, text='', font=("Helvetica", 24))
# pw_entry.pack(pady=20)
#
# #Frame for buttons
# my_frame = Frame(root)
# my_frame.pack(pady=20)
#
# #Buttons created
# my_button = Button(my_frame, text="Generate strong password", command=new_rand)
# my_button.grid(row=0, column=0, padx=10)
#
# clip_button = Button(my_frame, text="Copy to Clipboard", command=copy_password)
# clip_button.grid(row=0, column=1, padx=10)
#Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

website = Label(text="Website: ")
website.grid(column=0,row=1)
email = Label(text="Email/Account ")
email.grid(column=0, row=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)
do_manh = Label(text="Độ mạnh")
do_manh.grid(column=0, row=4)
ghi_chu = Label(text="Ghi chú")
ghi_chu.grid(column=0, row=6)

website_input = Entry(width=38)
website_input.grid(column=1, row=1)
website_input.insert(0, "https://")

email_input = Entry(width=38)
email_input.grid(column=1, row=2)
email_input.insert(0, "em@il.com")  #0 hoặc END: Hằng số của Tkinter: con trỏ sẽ xuất hiện ở kí tự đầu hoặc cuối

password_input = Entry(width=38)
password_input.grid(column=1, row=3)

#The rest
spinbox = Spinbox(from_=0, to=999, width=5)
spinbox.grid(column=1, row=4)

notes_input = Text(height=5,width=38)
notes_input.insert(END, "Ghi chú, cách khôi phục password, câu hỏi bảo mật, v.v...")
notes_input.grid(column=1, row=6)

mainloop()