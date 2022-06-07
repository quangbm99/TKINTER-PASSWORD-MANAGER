from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
import pyperclip
# ******************************************* SINH MÃ **************************************************************************


def tao_password():
    # chu_cai = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    #            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    #            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # so = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # ki_hieu = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # so_chu_cai = int(input("Số lượng chữ cái: "))
    # so_so = int(input("Số lượng số hạng: "))
    # so_ki_hieu = int(input("Số lượng kí hiệu: "))
    # so_ki_tu = int(input('Nhập số lượng kí tự của mật khẩu:'))
    # password = []
    # password = [random.choice(ki_tu) for i in range(so_ki_tu)]
    #
    # random.shuffle(password)
    # f_password = "".join(password)
    # password_input.insert(0, f_password)
    # print(f"Your password is {f_password}")
    # pyperclip.copy(f_password)

    # Clear entryBox
    password_input.delete(0, END)

    # get password length and convert to integer
    pw_length = int(spinbox.get())

    # create a variable to hold our password
    my_password = ''

    # loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33, 126))
    # output password to screen
    password_input.insert(0, my_password)
    pyperclip.copy(my_password)
# ********************************************** LƯU MÃ **************************************************************************
def luu():
    website = website_input.get()
    email = email_input.get()
    my_password = password_input.get()
    khong_trong_website = len(website)
    khong_trong_password = len(my_password)
    if khong_trong_website == 0 or khong_trong_password == 0:
        messagebox.showwarning(title="Lỗi!", message="Có vẻ như bạn để trống URL hoặc password.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Đã nhập \nEmail: {email}"
                                                              f"\nPassword: {my_password}"
                                                              f"\nGhi chú: {notes_input.get('1.0', END)}\n "
                                                              f"Bạn có muốn lưu lại không?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {my_password} | {notes_input.get('1.0', END)} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)

# ********************************************* CODE CHÍNH **************************************************************************

window = Tk()
window.title("Quản lý mật khẩu")
window.config(padx = 50, pady = 50)
window.geometry("670x600")
canvas = Canvas(width=200, height=200)
sym_img = PhotoImage(file="10819.png")
canvas.create_image(100, 100, image=sym_img)
canvas.grid(column=1,row=0, pady=(0,20))

#labels
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
#entries
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

#button
password_button = Button(text="Tạo mật khẩu", command=tao_password)
password_button.grid(column=1, row=5)
add_button = Button(text="Thêm", width=38, command=luu)
add_button.grid(column=1, row=7)


mainloop()
