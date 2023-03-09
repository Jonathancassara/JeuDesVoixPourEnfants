import random
import pygame.mixer
import RPi.GPIO as GPIO
import time

# Configurer les broches pour les boutons
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # bouton 1
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # bouton 2
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # bouton 3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # bouton 4

# Configurer les chemins d'accès aux fichiers audio
button1_sounds = ['sound1_1.wav', 'sound1_2.wav', 'sound1_3.wav', 'sound1_4.wav']
button2_sounds = ['sound2_1.wav', 'sound2_2.wav', 'sound2_3.wav', 'sound2_4.wav']
button3_sounds = ['sound3_1.wav', 'sound3_2.wav', 'sound3_3.wav', 'sound3_4.wav']
button4_sounds = ['sound4_1.wav', 'sound4_2.wav', 'sound4_3.wav', 'sound4_4.wav']

# Initialiser Pygame Mixer
pygame.mixer.init()

# Fonction pour jouer un son aléatoire pour le bouton donné
def play_random_sound(button_sounds):
    sound_file = random.choice(button_sounds)
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

# Boucle principale
while True:
    # Vérifier si l'un des boutons est pressé
    if not GPIO.input(17):
        play_random_sound(button1_sounds)
        time.sleep(0.2) # attendre un peu pour éviter les rebonds
    if not GPIO.input(18):
        play_random_sound(button2_sounds)
        time.sleep(0.2)
    if not GPIO.input(27):
        play_random_sound(button3_sounds)
        time.sleep(0.2)
    if not GPIO.input(22):
        play_random_sound(button4_sounds)
        time.sleep(0.2)

