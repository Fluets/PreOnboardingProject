from tkinter import *
from tkinter.ttk import *
import numpy

class minionDetector():
    """Builds UI and applies model trained by trainModel.py to selected image file
    
    Author: Matthew Cartwright

    """

    def __init__(self):
        self.window = Tk()
        self.window.title("Minion Meme Detector Bot!")
        self.window.configure(bg="#8a8880", width="480px", height="450px")

    def buildUI(self):
        """Creates and places the widgets that make the UI"""

        # Labels
        self.titleLabel = Label(self.window, text="Minion Meme Detector Bot!", background="#8a8880", font=("Arial", 50))
        self.instructionsLabel = Label(self.window, text="Upload the image and hit \"detect\" to verify!", font=("New Amsterdam", 15), width="70", wraplength="250", justify="left", background="#8a8880")
        self.resultLabel = Label(self.window, text="Answer...", background="#8a8880", font=("Arial", 50), justify="right")

        # Buttons
        self.uploadAndDetectButton = Button(self.window, text="Rate", command=self.uploadAndDetect)
        self.exitButton = Button(self.window, text="Exit", command=self.window.quit)

        # Place widgets
        self.titleLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.instructionsLabel.place(relx=0.1, rely=0.2)
        self.resultLabel.place(relx=0.1, rely=0.4)
        self.uploadAndDetectButton.place(relx=0.2, rely=0.8)
        self.exitButton.place(relx=0.85, rely=0.9)

        # Run the window
        self.window.mainloop()

    def uploadAndDetect(self):
        self.uploadImage()
        self.detectImage()

    def uploadImage(self):
        pass

    def detectImage(self):
        pass



    def main():
        detectorWindow = minionDetector()
        detectorWindow.buildUI()

    if __name__ == "__main__":
        main()