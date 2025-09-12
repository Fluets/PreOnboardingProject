''' 
Normalises and preprocesses images for training and testing use
'''
from PIL import Image
import glob

class preprocessImages():


    def __init__(self, imagesLocation):
        self.imagesLocation = imagesLocation
        self.imagesList = []
        pass

    def loadImages(self, imagesLocation):
        for filename in glob.glob('data/*.*'):
            image = Image.open(filename)
            self.imagesList.append(image)

    def resizeImages(self, imgCols, imgRows):
        newList = []
        for image in self.imagesList:
            newList.append(image.resize((imgCols, imgRows)))
        self.imagesList = newList

    def greyscaleImage(self):
        # Not implemented unless colour convolution causes issues
        pass

test = preprocessImages("test")
test.loadImages("test")
for item in test.imagesList:
    print(item)
test.resizeImages(150,100)
for item in test.imagesList:
    print(item)