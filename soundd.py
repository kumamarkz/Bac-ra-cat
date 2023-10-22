from pygame import mixer

mixer.init()
mixer.music.load("C:/project pscp/Bac-ra-cat/titanium.mp3")
mixer.music.play(loops=1)

root.mainloop()