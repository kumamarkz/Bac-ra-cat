from tkinter import *
import tkinter.messagebox
import tkinter as tk
from pygame import mixer
from tkinter import font
import random
from PIL import Image, ImageTk
from tkinter import messagebox
import time



root = tk.Tk()
root.title("BA-RA-CAT")

#หน้าจอ
start_page = tk.Frame(root)
play_page = tk.Frame(root)
start_page.grid(row=0,column=0,sticky="nsew")
play_page.grid(row=0,column=0,sticky="nsew")

game_img = Image.open("game.jpg")
resize_game_img = game_img.resize((1600, 900))
game_photo = ImageTk.PhotoImage(resize_game_img)
labelcat = tk.Label(play_page, image=game_photo)
labelcat.place(relwidth=1, relheight=1)

#ออกจากโปรแกรม
def exitProgram():
    confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการออกโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()


#ใส่รูป
img = Image.open("main.png")
resize_img = img.resize((1600, 900))
photo = ImageTk.PhotoImage(resize_img)
labelcat = tk.Label(start_page, image=photo)
labelcat.pack()


#ใส่ปุ่ม
btn_start = tk.Button(start_page,text="Start",font=("Helvetica", 20),command= lambda: play_page.tkraise())
btn_start.place(relx=0.5, rely=0.55, anchor="center")
btn_exit = tk.Button(start_page,text="Exit",font=("Helvetica", 20),command=exitProgram)
btn_exit.place(relx=0.5, rely=0.65, anchor="center")

count = 1000

def player():
	global stat
	stat = "player"
	stand_button.config(state="normal")
	tie_button.config(state="disable")
	dealer_button.config(state="disable")

def dealer():
	global stat
	stat = "dealer"
	stand_button.config(state="normal")
	play_button.config(state="disable")
	tie_button.config(state="disable")

def tie():
	global stat
	stat = "tie"
	stand_button.config(state="normal")
	dealer_button.config(state="disable")
	play_button.config(state="disable")
	

#play function
"""Play_Function"""
def play():
	"""ใช้ตอนกดplay จะนับเเต้มไพ่เเละดูว่าฝั่งไหนชนะ"""
	global player_total, dealer_total, player_score, stat, count
	player_total = 0
	dealer_total = 0

	#เพิ่มสกอร์ฝั่งเจ้ามือ
	for score in dealer_score:
		dealer_total += score

	#เพิ่มสกอรืฝั่งผู้เล่น
	for score in player_score:
		player_total += score

	# Freeze the buttons
	stand_button.config(state="disabled")

	#ถ้าเกินสิบนับเเต้มหลักหน่วย
	if player_total >= 10:
			player_total = player_total % 10
	if dealer_total >= 10:
			dealer_total = dealer_total % 10

	if player_total >= 6:
		if dealer_total >= 8:
			if dealer_total == player_total:
				messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				if stat == "tie":
					count += 500
				else:
					count -= 100
			elif dealer_total > player_total:
				messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				if stat == "dealer":
					count += 100
				else:
					count -= 100
			else:
				messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				if stat == "player":
					count += 100
				else:
					count -= 100
		elif dealer_total < 8:
			if dealer_total >= player_total:
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
					if stat == "tie":
						count += 500
					else:
						count -= 100
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "dealer":
						count += 100
					else:
						count -= 100
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "player":
						count += 100
					else:
						count -= 100
			else:
				dealer_hit()
				dealer_total += dealer_score[-1]
				if dealer_total >= 10:
					dealer_total = dealer_total % 10
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
					if stat == "tie":
						count += 500
					else:
						count -= 100
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "dealer":
						count += 100
					else:
						count -= 100
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "player":
						count += 100
					else:
						count -= 100
	else:
		player_hit()
		player_total += player_score[-1]
		if player_total >= 10:
			player_total = player_total % 10
		if dealer_total >= 8:
			if dealer_total == player_total:
				messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				if stat == "tie":
						count += 500
				else:
					count -= 100
			elif dealer_total > player_total:
				messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				if stat == "dealer":
					count += 100
				else:
					count -= 100
			else:
				messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				if stat == "player":
					count += 100
				else:
					count -= 100
		elif dealer_total < 8:
			if dealer_total >= player_total:
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
					if stat == "tie":
						count += 500
					else:
						count -= 100
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "dealer":
						count += 100
					else:
						count -= 100
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "player":
						count += 100
					else:
						count -= 100
			else:
				dealer_hit()
				dealer_total += dealer_score[-1]
				if dealer_total >= 10:
					dealer_total = dealer_total % 10
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
					if stat == "tie":
						count += 500
					else:
						count -= 100
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "dealer":
						count += 100
					else:
						count -= 100
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
					if stat == "player":
						count += 100
					else:
						count -= 100
"""size_cards"""
def size_cards(card):
	"""ปรับขนาดไพ่"""
	card_image = Image.open(card)
	card_resize_size = card_image.resize((150, 218))
	
	global card_image_open
	card_image_open = ImageTk.PhotoImage(card_resize_size)
	return card_image_open

def standby():
	backcard_image = Image.open("backcard.png")
	resize = backcard_image.resize((150, 218))
	global backcard_resize
	backcard_resize = ImageTk.PhotoImage(resize)
	dealer_label_1.config(image=backcard_resize)
	dealer_label_2.config(image=backcard_resize)
	dealer_label_3.config(image=backcard_resize)

	player_label_1.config(image=backcard_resize)
	player_label_2.config(image=backcard_resize)
	player_label_3.config(image=backcard_resize)
	nextbet_button.config(state="disable")
	stand_button.config(state="disable")
	tie_button.config(state="normal")
	play_button.config(state="normal")
	dealer_button.config(state="normal")
	stand_button.config(state="disable")
	



# สับไพ่
"""shuffle"""
def shuffle():
	"""ฟังก์ชันสำหรับ สับไพ่"""
	global player_total, dealer_total
	
	print(count)
	player_total = 0
	dealer_total = 0
	# Enable buttons
	stand_button.config(state="normal")

	#เคลียร์การ์ดเก่า
	dealer_label_1.config(image='')
	dealer_label_2.config(image='')
	dealer_label_3.config(image='')

	player_label_1.config(image='')
	player_label_2.config(image='')
	player_label_3.config(image='')
	
	# สร้างสำรับไพ่
	suits = ["clubs"]
	values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')

	global dealer, player, dealer_area, player_area, dealer_score, player_score
	dealer = []
	player = []
	dealer_score = []
	player_score = []
	dealer_area = 0
	player_area = 0


	# Shuffle Two Cards for player and dealer
	dealer_hit()
	dealer_hit()

	player_hit()
	player_hit()


"""dealer_hit function"""
def dealer_hit():
	"""ใช้สำหรับจั่วไพ่ฝั่งเจ้ามือ"""
	global dealer_area, dealer_total
	if dealer_area < 3:
		dealer_card = random.choice(deck)
		dealer.append(dealer_card)
		score_card_dealer = int(dealer_card.split("_", 1)[0])
		if score_card_dealer == 14:
			dealer_score.append(1)
		elif score_card_dealer == 11 or score_card_dealer == 12 or score_card_dealer == 13 or score_card_dealer == 10:
			dealer_score.append(0)
		else:
			dealer_score.append(score_card_dealer)

		global dealer_image1, dealer_image2, dealer_image3

		if dealer_area == 0:
				dealer_image1 = size_cards(f'image0/card2/{dealer_card}.png')
				dealer_label_1.config(image=dealer_image1)
				dealer_area += 1
		elif dealer_area == 1:
			dealer_image2 = size_cards(f'image0/card2/{dealer_card}.png')
			dealer_label_2.config(image=dealer_image2)
			dealer_area += 1
		elif dealer_area == 2:
			dealer_image3 = size_cards(f'image0/card2/{dealer_card}.png')
			dealer_label_3.config(image=dealer_image3)
			dealer_area += 1

"""player_hit function"""
def player_hit():
	"""ใช้สำหรับจั่วไพ่ฝั่งผู้เล่นมือ"""
	global player_area, player_total, dealer_score

	if player_area < 3:
		player_card = random.choice(deck)
		player.append(player_card)
		score_cards_player = int(player_card.split("_", 1)[0])
		if score_cards_player == 14:
			player_score.append(11)
		elif score_cards_player == 11 or score_cards_player == 12 or score_cards_player == 13 or score_cards_player == 10:
			player_score.append(0)
		else:
			player_score.append(score_cards_player)

			global player_image1, player_image2, player_image3
			
		if player_area == 0:
			player_image1 = size_cards(f'image0/card2/{player_card}.png')
			player_label_1.config(image=player_image1)
			player_area += 1
		elif player_area == 1:
			player_image2 = size_cards(f'image0/card2/{player_card}.png')
			player_label_2.config(image=player_image2)
			player_area += 1
		elif player_area == 2:
			player_image3 = size_cards(f'image0/card2/{player_card}.png')
			player_label_3.config(image=player_image3)
			player_area += 1






# Create Frames For Cards
dealer_frame = LabelFrame(play_page, text="Dealer", bd=0)
dealer_frame.place(relx=0.7, rely=0.4, anchor="center")

player_frame = LabelFrame(play_page, text="Player", bd=0)
player_frame.place(relx=0.3, rely=0.4, anchor="center")

# Put Dealer cards in frames
dealer_label_1 = Label(dealer_frame, text='')
dealer_label_1.grid(row=0, column=0, pady=20, padx=20)

dealer_label_2 = Label(dealer_frame, text='')
dealer_label_2.grid(row=0, column=1, pady=20, padx=20)

dealer_label_3 = Label(dealer_frame, text='')
dealer_label_3.grid(row=0, column=2, pady=20, padx=20)


# Put Player cards in frames
player_label_1 = Label(player_frame, text='')
player_label_1.grid(row=1, column=0, pady=20, padx=20)

player_label_2 = Label(player_frame, text='')
player_label_2.grid(row=1, column=1, pady=20, padx=20)

player_label_3 = Label(player_frame, text='')
player_label_3.grid(row=1, column=2, pady=20, padx=20)


name_label_1 = Label(play_page, text="Money : "+str(count), font=("Helvetica", 20),width=12,height=2)
name_label_1.place(relx=0.8, rely=0.8, anchor="center")

rule_label = Label(play_page, text="เลือกฝั่งที่คุณจะลง ลงครั้งละ 100 \nถ้าคุณเลือกถูกจะได้เพิ่ม100เเต่ถ้าผิดจะลบ100\nเเต่ถ้าคุณเลือก Tie คุณมีโอกาสได้รับถึง500\nง่ายใช่ไหมล่ะ ลองเล่นได้เลย", font=("Helvetica", 20))
rule_label.place(relx=0.18, rely=0.8, anchor="center")



def shuffleandplay():
	shuffle()
	play()
	stand_button.config(state="disable")
	tie_button.config(state="disable")
	play_button.config(state="disable")
	dealer_button.config(state="disable")
	nextbet_button.config(state="normal")
	name_label_1 = Label(play_page, text="Money : "+str(count), font=("Helvetica", 20),width=12,height=2)
	name_label_1.place(relx=0.8, rely=0.8, anchor="center")
	if count <= 0:
		confirm = tkinter.messagebox.askquestion("คุณหมดตัวเเล้ว","คุณต้องการออกโปรแกรมหรือไม่ ?")
		if confirm == "yes":
			root.destroy()
		elif confirm == "no":
			confirm2 = tkinter.messagebox.askquestion("ขอโทษทีคุณเเพ้เเล้ว","ถึงตอบไม่ก็ต้องออก")
			if confirm2 == "yes":
				root.destroy()
			else:
				root.destroy()

# Create a couple buttons
nextbet_button = Button(play_page, text="Next Bet", font=("Helvetica", 20), command=standby)
nextbet_button.place(relx=0.45, rely=0.7, anchor="center")

stand_button = Button(play_page, text="  Play  ", font=("Helvetica", 20), command=shuffleandplay)
stand_button.place(relx=0.55, rely=0.7, anchor="center")

play_button = Button(play_page, text="Player", font=("Helvetica",20), command=player)
play_button.place(relx=0.4, rely=0.8, anchor="center")

tie_button = Button(play_page, text="  Tie  ", font=("Helvetica", 20), command=tie)
tie_button.place(relx=0.5, rely=0.8, anchor="center")

dealer_button = Button(play_page, text="Dealer", font=("Helvetica", 20), command=dealer)
dealer_button.place(relx=0.6, rely=0.8, anchor="center")



# Standby Deck On Start
standby()

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
