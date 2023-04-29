import os
import random
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.5)

music_dir = r'C:\Users\Administrator\Desktop\New folder'
music_files = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]

random.shuffle(music_files)


for file in sorted(music_files):
    print("Now playing:", file)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()