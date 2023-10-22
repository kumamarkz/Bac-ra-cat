from tkinter import *
import pygame

root = Tk()
root.title('icon game')
root.geometry("500x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("C:/project pscp/Bac-ra-cat/titanium.mp3")
    pygame.mixer.music.play(loops=1)
my_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=20)

root.mainloop()