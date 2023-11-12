from tkinter import *
import random
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Codemy.com - Card Deck')
root.geometry("1200x800")
root.configure(background="green")

# Stand
def stand():
	global player_total, dealer_total, player_score
	# Keep track of score totals
	player_total = 0
	dealer_total = 0

	# Get the dealers score total
	for score in dealer_score:
		# Add up score
		dealer_total += score
	

	# Loop thru player score list and add up cards
	for score in player_score:
		# Add up score
		player_total += score

		

	# Freeze the buttons
	card_button.config(state="disabled")
	stand_button.config(state="disabled")

	if player_total >= 10:
			player_total = player_total % 10
	if dealer_total >= 10:
			dealer_total = dealer_total % 10

	if player_total >= 6:
		if dealer_total >= 8:
			if dealer_total == player_total:
				messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
			elif dealer_total > player_total:
				messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
			else:
				messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
		elif dealer_total < 8:
			if dealer_total >= player_total:
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
			else:
				dealer_hit()
				dealer_total += dealer_score[-1]
				if dealer_total >= 10:
					dealer_total = dealer_total % 10
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
	else:
		player_hit()
		player_total += player_score[-1]
		if player_total >= 10:
			player_total = player_total % 10
		if dealer_total >= 8:
			if dealer_total == player_total:
				messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
			elif dealer_total > player_total:
				messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
			else:
				messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
		elif dealer_total < 8:
			if dealer_total >= player_total:
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))
			else:
				dealer_hit()
				dealer_total += dealer_score[-1]
				if dealer_total >= 10:
					dealer_total = dealer_total % 10
				if dealer_total == player_total:
					messagebox.showinfo("Tie OwO", "It's a Tie!!  %d : %d"%(dealer_total, player_total))
				elif dealer_total > player_total:
					messagebox.showinfo("Dealer Wins OwO", "Dealer Wins!  Dealer: %d : %d"%(dealer_total, player_total))
				else:
					messagebox.showinfo("Player Wins OwO", "Player Wins!  Dealer: %d : %d"%(dealer_total, player_total))

# Resize Cards
def resize_cards(card):

	our_card_img = Image.open(card)
	our_card_resize_image = our_card_img.resize((150, 218))
	
	global our_card_image
	our_card_image = ImageTk.PhotoImage(our_card_resize_image)

	return our_card_image

# Shuffle The Cards
def shuffle():
	# Keep track of winning
	global blackjack_status, player_total, dealer_total
	
	# Keep track of score totals
	player_total = 0
	dealer_total = 0

	blackjack_status = {"dealer":"no", "player":"no"}

	# Enable buttons
	card_button.config(state="normal")
	stand_button.config(state="normal")
	# Clear all the old cards from previous games
	dealer_label_1.config(image='')
	dealer_label_2.config(image='')
	dealer_label_3.config(image='')


	player_label_1.config(image='')
	player_label_2.config(image='')
	player_label_3.config(image='')
	


	# Define Our Deck
	suits = ["clubs"]
	values = range(2, 15)
	# 11 = Jack, 12=Queen, 13=King, 14 = Ace

	global deck
	deck =[]

	for suit in suits:
		for value in values:
			deck.append(f'{value}_of_{suit}')
			
	# Create our players
	global dealer, player, dealer_spot, player_spot, dealer_score, player_score
	dealer = []
	player = []
	dealer_score = []
	player_score = []
	dealer_spot = 0
	player_spot = 0



	# Shuffle Two Cards for player and dealer
	dealer_hit()
	dealer_hit()

	player_hit()
	player_hit()

	# Put number of remaining cards in title bar
	root.title(f'Codemy.com - {len(deck)} Cards Left')

def dealer_hit():
	global dealer_spot, dealer_total
	if dealer_spot < 3:
		try:
			# Get the player Card
			dealer_card = random.choice(deck)
			# Remove Card From Deck
			deck.remove(dealer_card)
			# Append Card To Dealer List
			dealer.append(dealer_card)
			# Append to dealer score list and convert facecards to 10 or 11
			dcard = int(dealer_card.split("_", 1)[0])
			if dcard == 14:
				dealer_score.append(1)
			elif dcard == 11 or dcard == 12 or dcard == 13 or dcard == 10:
				dealer_score.append(10)
			else:
				dealer_score.append(dcard)
			
	

			global dealer_image1, dealer_image2, dealer_image3
			
			
			if dealer_spot == 0:
				# Resize Card
				dealer_image1 = resize_cards(f'image0/card2/{dealer_card}.png')
				# Output Card To Screen
				dealer_label_1.config(image=dealer_image1)
				# Increment our player spot counter
				dealer_spot += 1
			elif dealer_spot == 1:
				# Resize Card
				dealer_image2 = resize_cards(f'image0/card2/{dealer_card}.png')
				# Output Card To Screen
				dealer_label_2.config(image=dealer_image2)
				# Increment our player spot counter
				dealer_spot += 1
			elif dealer_spot == 2:
				# Resize Card
				dealer_image3 = resize_cards(f'image0/card2/{dealer_card}.png')
				# Output Card To Screen
				dealer_label_3.config(image=dealer_image3)
				# Increment our player spot counter
				dealer_spot += 1

			# Put number of remaining cards in title bar
			root.title(f'Codemy.com - {len(deck)} Cards Left')

		except:
			root.title(f'Codemy.com - No Cards In Deck')



def player_hit():
	global player_spot, player_total, dealer_score

	if player_spot < 3:

			# Get the player Card
			player_card = random.choice(deck)
			# Remove Card From Deck
			# Append Card To Dealer List
			player.append(player_card)

			# Append to dealer score list and convert facecards to 10 or 11
			pcard = int(player_card.split("_", 1)[0])
			if pcard == 14:
				player_score.append(11)
			elif pcard == 11 or pcard == 12 or pcard == 13 or pcard == 10:
				player_score.append(0)
			else:
				player_score.append(pcard)

				 
			global player_image1, player_image2, player_image3, player_image4, player_image5
			
			
			if player_spot == 0:
				# Resize Card
				player_image1 = resize_cards(f'image0/card2/{player_card}.png')
				# Output Card To Screen
				player_label_1.config(image=player_image1)
				# Increment our player spot counter
				player_spot += 1
			elif player_spot == 1:
				# Resize Card
				player_image2 = resize_cards(f'image0/card2/{player_card}.png')
				# Output Card To Screen
				player_label_2.config(image=player_image2)
				# Increment our player spot counter
				player_spot += 1
			elif player_spot == 2:
				# Resize Card
				player_image3 = resize_cards(f'image0/card2/{player_card}.png')
				# Output Card To Screen
				player_label_3.config(image=player_image3)
				# Increment our player spot counter
				player_spot += 1



my_frame = Frame(root, bg="green")
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
button_frame = Frame(root, bg="green")
button_frame.pack(pady=20)

# Create a couple buttons
shuffle_button = Button(button_frame, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.grid(row=0, column=0)

card_button = Button(button_frame, text="Hit Me!", font=("Helvetica", 14), command=player_hit)
card_button.grid(row=0, column=1, padx=10)

stand_button = Button(button_frame, text="Stand!", font=("Helvetica", 14), command=stand)
stand_button.grid(row=0, column=2)



# Shuffle Deck On Start
shuffle()


root.mainloop()
