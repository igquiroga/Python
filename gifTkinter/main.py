import cv2
from tkinter import *
from PIL import ImageTk, Image
"""
Install these libraries:
pip install pillow
pip install opencv-python
"""
bgPrincipal = "gray22"
cap = None


def run():
    window = Tk()
    window.configure(bg=bgPrincipal)
    window.title("Gif")
    window.geometry('400x400')
    frameGif = Frame(window, bg=bgPrincipal)
    frameGif.pack(fill=BOTH, pady=10, padx=20)
    labelGif = Label(frameGif, relief=FLAT, bd=0, bg=bgPrincipal)
    labelGif.pack(fill=BOTH, expand=1)
    gif = 'up.gif'

    def displayGif():
        global cap
        if (not cap):
            cap = cv2.VideoCapture(gif)
        ret, frame = cap.read()
        if (ret):
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # size of gif
            width = 300
            height = 300
            img = Image.fromarray(cv2image).resize((width, height))
            imgtk = ImageTk.PhotoImage(image=img)
            labelGif.imgtk = imgtk
            labelGif.configure(image=imgtk)
        else:
            cap = cv2.VideoCapture(gif)
        # changing 80 change the speed of gif
        labelGif.after(80, displayGif)
    displayGif()
    window.mainloop()


if __name__ == '__main__':
    run()
