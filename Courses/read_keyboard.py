import keyboard

rc = keyboard.record('Esc')
print([x.name for x in rc])