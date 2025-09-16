
from PIL import Image, ImageOps
import glob
import numpy as np

class ImagePreprocessor():
    """Preprocesses images for training and testing use
    
    Author: Matthew Cartwright

    """


    def __init__(self):
        """Initialises the object and creates image list"""
        self.imagesList = []
        pass

    def preprocessImages(self, imagesLocation, imgCols, imgRows):
        """Runs the required functions to preprocess a folder of images in order for convenience"""
        self.loadImages(imagesLocation)
        self.resizeImages(imgCols, imgRows)
        self.greyscaleImages()
        self.normaliseImages()

    def loadImages(self, imagesLocation):
        """Loads the image files into python using glob"""
        for filename in glob.glob(imagesLocation):
            image = Image.open(filename)
            self.imagesList.append(image)

    def resizeImages(self, imgCols, imgRows):
        """Sets the images to a standard preselected size"""
        newList = []
        for image in self.imagesList:
            newList.append(image.resize((imgCols, imgRows)))
        self.imagesList = newList

    def greyscaleImages(self):
        """Makes images greyscale for easier learning - Ideally to be replaced with full colour training for better performance"""
        newList = []
        for image in self.imagesList:
            newList.append(ImageOps.grayscale(image))
        self.imagesList = newList

    def normaliseImages(self):
        """Normalise colour values between images for better learning"""
        newList = []
        for image in self.imagesList:
            newList.append(np.asarray(image))
        
        numpyNewList = np.array(newList)
        numpyNewList = numpyNewList.astype('float32')
        numpyNewList /= 255

        self.imagesList = numpyNewList
        
    def preprocessSingleImage(self, image, imgCols, imgRows):
        """Preprocess a single image with the same steps for detection use"""
        image = image.resize((imgCols, imgRows))
        image = ImageOps.grayscale(image)
        image = np.asarray(image)

        singleImageList = [image]
        numpySingleImageList = np.array(singleImageList)
        numpySingleImageList = numpySingleImageList.astype('float32')
        numpySingleImageList /= 255

        return numpySingleImageList

    def reset(self):
        """Reset object after to use for future use"""
        self.imagesList = []


#test = ImagePreprocessor()
#test.loadImages('data/*.*')
#for item in test.imagesList:
#    print(item)
#test.resizeImages(150,100)
#for item in test.imagesList:
#    print(item)