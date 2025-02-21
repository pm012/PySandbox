import os


def switch_to_english():
    os.system("setxkbmap us")

def switch_to_ukrainian():
    os.system("setxkbmap ua")

# Test: Switch to English
switch_to_english()
print("Switched to English")

# Test: Switch to Ukrainian
switch_to_ukrainian()
print("Switched to Ukrainian")
