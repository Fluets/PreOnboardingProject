from tkinter import *
from tkinter.ttk import *
import numpy
from keras import saving

class minionDetector():
    """Builds UI and applies model trained by trainModel.py to selected image file
    
    Author: Matthew Cartwright

    """

    def __init__(self):
        """initialises the object: creating the window, building the UI and loading the CNN model"""
        self.window = Tk()
        self.window.title("Minion Meme Detector Bot!")
        self.window.configure(bg="#8a8880", width="480px", height="450px")
        self.model = saving.load_model("minionDetector.keras")
        self.buildUI()

    def buildUI(self):
        """Creates and places the widgets that make the UI into the window"""

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
        """Uploads the image then detects if it a minion meme or not"""
        self.uploadImage()
        self.detectImage()

    def uploadImage(self):
        """Prompts the user to upload the image for detection"""
        pass

    def detectImage(self):
        """Applies the CNN model to determine if the image is a minion meme or not, returning true if so and false otherwise"""
        pass



    def main():
        detectorWindow = minionDetector()

    if __name__ == "__main__":
        main()