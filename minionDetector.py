import tkinter # Imported explicitly to allow editing of button attributes, see: https://stackoverflow.com/questions/60928474/tkinter-tclerror-unknown-option-on-widget-attributes
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog # Apparently needs to be explicitly imported
from keras import saving
from PIL import Image
from preprocessImages import ImagePreprocessor

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
        self.titleLabel = Label(self.window, text="Minion Meme Detector Bot!", background="#8a8880", font=("Arial", 40))
        self.instructionsLabel = Label(self.window, text="Upload the image to verify!", font=("New Amsterdam", 15), width="140", wraplength="500", justify="left", background="#8a8880")
        self.resultLabel = tkinter.Label(self.window, text="Answer...", background="#8a8880", font=("Arial", 50), justify="right")

        # Buttons
        self.uploadAndDetectButton = tkinter.Button(self.window, text="Upload and Detect", command=self.uploadAndDetect)
        self.uploadAndDetectButton.config(height="10", width="50")
        self.exitButton = Button(self.window, text="Exit", command=self.quit)

        # Place widgets
        self.titleLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
        self.instructionsLabel.place(relx=0.1, rely=0.2)
        self.uploadAndDetectButton.place(relx=0.1, rely=0.4)
        self.resultLabel.place(relx=0.1, rely=0.7)
        self.exitButton.place(relx=0.85, rely=0.9)

        # Run the window
        self.window.mainloop()

    def uploadAndDetect(self):
        """Uploads the image, preprocesses it, then detects if it a minion meme or not"""
        self.uploadImage()
        self.preprocessImage()
        self.classifyImage()

    def uploadImage(self):
        """Prompts the user to upload the image for detection (-requires user to have saved image)"""
        fileTypes = [("Image files", "*.png;*.jpg;*.jpeg;*.webp;*.avif")]
        path = filedialog.askopenfilename(filetypes=fileTypes)
        self.image = Image.open(path)

    def preprocessImage(self):
        """Uses the preprocessor to preprocess the provided image"""
        imagePreprocessor = ImagePreprocessor()
        self.processedImage = imagePreprocessor.preprocessSingleImage(self.image, 150, 100)


    def classifyImage(self):
        """Applies the CNN model to determine if the image is a minion meme or not, returning true if so and false otherwise"""
        prediction = self.model.predict((self.processedImage), verbose=0)[0][1]
        #print(prediction)
        
        if prediction > 0.5:
            self.minionDetected()
        else:
            self.clearOfMinions()

    def minionDetected(self):
        
        self.resultLabel.config(text="Minion meme detected!", fg="red", font=("Arial", 40))

    def clearOfMinions(self):
        """Sets the label to display the result"""
        self.resultLabel.config(text="No minions detected!", fg="green", font=("Arial", 40))

    def quit(self):
        """Explicitly quitting to avoid having to press the button twice"""
        quit()
        
        



def main():
    detectorWindow = minionDetector()
    detectorWindow.buildUI()

if __name__ == "__main__":
    main()