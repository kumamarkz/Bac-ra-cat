from tkinter import *
import random
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('BA-RA-CAT')
root.geometry("1600x900")
game_img = Image.open("game.jpg")
resize_game_img = game_img.resize((1600, 900))
game_photo = ImageTk.PhotoImage(resize_game_img)
labelcat = tk.Label(root, image=game_photo)
labelcat.place(relwidth=1, relheight=1)

count = 100
if count < 100:
	messagebox.showinfo("Game over")

def player():
	global stat
	stat = "player"
	
def dealer():
	global stat
	stat = "dealer"
	
def tie():
	global stat
	stat = "tie"
	

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
	card_button.config(state="disabled")
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
					count += 100
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
						count += 100
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
						count += 100
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
						count += 100
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
						count += 100
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
						count += 100
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

	player_label_1.config(image=backcard_resize)
	player_label_2.config(image=backcard_resize)




# สับไพ่
"""shuffle"""
def shuffle():
	"""ฟังก์ชันสำหรับ สับไพ่"""
	global player_total, dealer_total, stat
	
	print(count)
	player_total = 0
	dealer_total = 0
	stat = 0
	# Enable buttons
	card_button.config(state="normal")
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

			global player_image1, player_image2, player_image3, player_image4, player_image5
			
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



my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Frames For Cards
dealer_frame = LabelFrame(my_frame, text="Dealer", bd=0)
dealer_frame.pack(padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text="Player", bd=0)
player_frame.pack(ipadx=20, pady=10)

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



# Create Button Frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Create a couple buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command=play)
stand_button.grid(row=0, column=2)

play_button = Button(button_frame, text="player", font=("Helvetica", 14), command=player)
play_button.grid(row=1, column=0)

dealer_button = Button(button_frame, text="Dealer!", font=("Helvetica", 14), command=dealer)
dealer_button.grid(row=1, column=1, padx=10)

tie_button = Button(button_frame, text="Tie", font=("Helvetica", 14), command=tie)
tie_button.grid(row=1, column=2)



# Shuffle Deck On Start
standby()


root.mainloop()
