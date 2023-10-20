from tkinter import *
import tkinter.messagebox
import tkinter as tk
from PIL import ImageTk, Image, ImageOps

root = tk.Tk()
root.title("BA-RA-CAT")

#หน้าจอ
start_page = tk.Frame(root)
name_page = tk.Frame(root)
start_page.grid(row=0,column=0,sticky="nsew")
name_page.grid(row=0,column=0,sticky="nsew")

#ออกจากโปรแกรม
def exitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการออกโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()


#ใส่รูป
img = Image.open("cat.png")
resize_img = img.resize((1280, 720))
photo = ImageTk.PhotoImage(resize_img)
labelcat = tk.Label(start_page, image=photo)
labelcat2 = tk.Label(name_page, image=photo)
labelcat.pack()
labelcat2.pack()



img2 = Image.open("cat2.png")
resize_img2 = img2.resize((400, 200))
photo2 = ImageTk.PhotoImage(resize_img2)
newcat = tk.Label(start_page, image=photo2)
newcat.place(relx=0.5, rely=0.3, anchor="center")



#ใส่ข้อความในจอ
mylabel1 = tk.Label(start_page,text="Welcome",fg="Green",bg="orange")
mylabel1.place(relx=0.5, rely=0.5, anchor="center")
mylabel2 = tk.Label(name_page,text="PG 2",fg="Green",font=60,bg="orange")
mylabel2.place(relx=0.5, rely=0.5, anchor="center")




#ใส่ปุ่ม
btn_start = tk.Button(start_page,text="Start",font=50,command= lambda: name_page.tkraise())
btn_start.place(relx=0.5, rely=0.6, anchor="center")
btn_exit = tk.Button(start_page,text="Exit",font=40,command=exitProgram)
btn_exit.place(relx=0.5, rely=0.65, anchor="center")


start_page.tkraise()
root.geometry("1280x720")
root.resizable(False, False)
root.mainloop()

