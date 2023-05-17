# Thanks To : • - [ Dvanmeploph ( Ferly Afriliyan ) ] - •
# Script Ini Gw Coding Sendiri
# Coded By : • - [ Dvanmeploph ( Ferly Afriliyan ) ] - • 
import time
import random
import pyautogui as pg

time.sleep(5)
pesan_random = ["Ngentot", "Woi Bangsat", "Anjing", "Tolol", "Woy Kontol"]
for i in range(100):
    pg.typewrite(random.choice(pesan_random))
    pg.press("enetr")
    time.sleep(0.5)
