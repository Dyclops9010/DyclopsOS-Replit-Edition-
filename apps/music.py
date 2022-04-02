import os
from replit import audio

print("Please make sure you have already imported your music to the user/music folder")

while True:
  print("""
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
Type "pause" to pause
Type "exit" to exit (music will still be playing)
        """)
  song = input("Put Song Full Name (including .mp3): ")
  if song == "exit":
    os.system('python home.py')
  elif song == "pause":
    source.paused = not source.paused
  else:
    source = audio.play_file("user/music/" + song)