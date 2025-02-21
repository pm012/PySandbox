import subprocess

def get_keyboard_layout():
    result = subprocess.run(["setxkbmap", "-query"], capture_output=True, text=True)
    for line in result.stdout.split("\n"):
        if "layout" in line:
            return line.split(":")[-1].strip()

print("Current layout:", get_keyboard_layout())
