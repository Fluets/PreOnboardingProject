
from PIL import Image, ImageOps
import glob
import numpy as np

class ImagePreprocessor():
    """Preprocesses images for training and testing use
    
    Author: Matthew Cartwright

    """


    def __init__(self):
        self.imagesList = []
        pass

    def preprocessImages(self, imagesLocation, imgCols, imgRows):
        self.loadImages(imagesLocation)
        self.resizeImages(imgCols, imgRows)
        self.greyscaleImages()
        self.normaliseImages()

    def loadImages(self, imagesLocation):
        for filename in glob.glob(imagesLocation):
            image = Image.open(filename)
            self.imagesList.append(image)

    def resizeImages(self, imgCols, imgRows):
        newList = []
        for image in self.imagesList:
            newList.append(image.resize((imgCols, imgRows)))
        self.imagesList = newList

    def greyscaleImages(self):
        # Ideally to be replaced with full colour training
        newList = []
        for image in self.imagesList:
            newList.append(ImageOps.grayscale(image))
        self.imagesList = newList

    def normaliseImages(self):
        newList = []
        for image in self.imagesList:
            newList.append(np.asarray(image))
        
        numpyNewList = np.array(newList)
        numpyNewList = numpyNewList.astype('float32')
        numpyNewList /= 255

        self.imagesList = numpyNewList
        
    def preprocessSingleImage(self, image, imgCols, imgRows):
        image = image.resize((imgCols, imgRows))
        image = ImageOps.grayscale(image)
        image = np.asarray(image)

        singleImageList = [image]
        numpySingleImageList = np.array(singleImageList)
        numpySingleImageList = numpySingleImageList.astype('float32')
        numpySingleImageList /= 255

        return numpySingleImageList

    def reset(self):
        self.imagesList = []


#test = ImagePreprocessor()
#test.loadImages('data/*.*')
#for item in test.imagesList:
#    print(item)
#test.resizeImages(150,100)
#for item in test.imagesList:
#    print(item)