from tkinter import *
from tkVideoPlayer import TkinterVideo
import math
bgMain = "#3c3c3c"
bgSecondary = "#222324"
fgWhite = "snow"
"""
Install this libraries:
pip install tkvideoplayer
"""
video = "igquiroga.mp4"
def run():
    """
    Create a window with a video
    """
    window = Tk()
    window.title("Video Player")
    window.geometry("400x400")
    frameButtons = Frame(window, bg=bgMain)
    frameButtons.pack(fill=X)

    def setIniVideo(evt):
        playButton['text'] = "Play"

    def playVideo():
        if(videoplayer.is_paused()):
            videoplayer.play()
            playButton['text'] = "Pause"
            timeVideo()
        else:
            videoplayer.pause()
        playButton['text'] = "Play"

    def stopVideo():
        videoplayer.stop()
    playButton = Button(frameButtons, text="Pause",
                            bg=bgSecondary, fg=fgWhite, command=playVideo)
    playButton.pack(side=LEFT, fill=X, expand=1)

    stopButton = Button(frameButtons, text="Stop",
                            bg=bgSecondary, fg=fgWhite, command=stopVideo)
    stopButton.pack(side=LEFT, fill=X, expand=1)
    frameVideo = Frame(window, bg=bgMain)
    frameVideo.pack(fill=BOTH, expand=1)
    videoplayer = TkinterVideo(frameVideo, scaled=True)
    videoplayer.load(video)
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    videoplayer.bind('<<Ended>>', setIniVideo)
    labelTime = Label(frameVideo, text="Time: ", bg=bgMain, fg=fgWhite)
    labelTime.pack()

    def timeVideo():
        labelTime["text"] = "Time: " + \
            str(math.floor(videoplayer.current_duration()))+"s"
        if(not videoplayer.is_paused()):
            labelTime.after(500, timeVideo)
    labelTime.after(0, timeVideo)
    window.mainloop()

if __name__ == "__main__":
    run()