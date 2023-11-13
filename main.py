from tkinter import *
import tkinter.messagebox
import tkinter as tk
from PIL import ImageTk, Image, ImageOps
from pygame import mixer
from tkinter import font



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


#font
font1 = font.Font(family="Helvetica",size=20)


#ใส่รูป
img = Image.open("main.png")
resize_img = img.resize((1600, 900))
photo = ImageTk.PhotoImage(resize_img)
labelcat = tk.Label(start_page, image=photo)
labelcat2 = tk.Label(name_page, image=photo)
labelcat.pack()
labelcat2.pack()


#ใส่ข้อความในจอ
mylabel2 = tk.Label(name_page,text="PG 2",fg="Green",font=60,bg="orange")
mylabel2.place(relx=0.5, rely=0.5, anchor="center")
mylabel2 = tk.Label(name_page,text="PG 2",fg="Green",font=60,bg="orange")
mylabel2.place(relx=0.5, rely=0.5, anchor="center")




#ใส่ปุ่ม
btn_start = tk.Button(start_page,text="Start",font=font1,command= lambda: name_page.tkraise())
btn_start.place(relx=0.5, rely=0.55, anchor="center")
btn_exit = tk.Button(start_page,text="Exit",font=font1,command=exitProgram)
btn_exit.place(relx=0.5, rely=0.65, anchor="center")


start_page.tkraise()
root.geometry("1600x900")
root.resizable(False, False)

#เพลง bg
mixer.init()
mixer.music.load("song_bg_1.mp3")
mixer.music.play(loops=1000)


#icon game
root.iconbitmap("cat_icon.ico")


root.mainloop()
