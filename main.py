from msvcrt import getch
import winsound

# freq = 1000
# dur = 500
# # winsound.Beep(freq, dur)
#
# for i in range(0, 50):
#     winsound.Beep(freq, dur)
#     freq += 100
#     dur += 50

# winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME)

# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
from time import sleep


flag = True
while flag:
    key = getch()
    print(key)
    print(ord(key))
    if ord(key) == 113:
        print('Quit')
        sleep(1)
        flag = False

    key.lower()
    key.strip()

    if ord(key) == 97:
        # press a
        winsound.Beep(440, 500)
    elif ord(key) == 98:
        # press b
        winsound.Beep(494, 500)
    elif ord(key) == 99:
        # press c
        winsound.Beep(262, 500)
    elif ord(key) == 100:
        # press d
        winsound.Beep(294, 500)
    elif ord(key) == 101:
        # press e
        winsound.Beep(330, 500)
    elif ord(key) == 102:
        # press f
        winsound.Beep(349, 500)
    elif ord(key) == 103:
        # press g
        winsound.Beep(392, 500)
