import RPi.GPIO as GPIO
import pygame
import random

# Configurer le bouton et le GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configurer pygame pour la lecture de sons
pygame.mixer.init()

# Liste de fichiers audio
audio_files = ['son1.mp3', 'son2.mp3', 'son3.mp3']

# Boucle principale
while True:
    # Attendre l'appui sur le bouton
    GPIO.wait_for_edge(11, GPIO.FALLING)

    # Sélectionner un fichier audio aléatoire
    audio_file = random.choice(audio_files)

    # Jouer le fichier audio
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
