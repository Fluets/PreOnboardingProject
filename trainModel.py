from keras import layers, losses, utils
from keras.models import Sequential
from preprocessImages import ImagePreprocessor
import numpy as np
import random
import sklearn.model_selection

class modelTrainer():
    """Trains models using provided preprocessed images by building a Convolutional Neural Network
    
    Author: Matthew Cartwright
    
    """

    def __init__(self, dataLocation):
        """Initialises the object with data in the form of a 2D list containing positive images and negative images"""
        self.data = []

        # Positive images
        imagePreprocessor = ImagePreprocessor()
        imagePreprocessor.preprocessImages(dataLocation + '/m/*.*', 150, 100) #! SHOULDN'T HARD CODE THESE VALUES
        self.data.append(imagePreprocessor.imagesList)
        imagePreprocessor.reset()

        # Negative images        
        imagePreprocessor.preprocessImages(dataLocation + '/n/*.*', 150, 100) #! SHOULDN'T HARD CODE THESE VALUES
        self.data.append(imagePreprocessor.imagesList)
        imagePreprocessor.reset()
        


    def trainModel(self):
        """Train the model using provided training data"""

        # Create X and Y arrays
        xData = []
        yData = []

        for item in self.data[0]:
            xData.append(item)
            yData.append(1)
        for item in self.data[1]:
            xData.append(item)
            yData.append(0)
        print(yData)

        # Mix and split the data NEW
        xData, yData = self.mixData(xData, yData)
        xTrain, xTest, yTrain, yTest = self.splitData(xData, yData, 0.1)

        # Convert python arrays to numpy arrays NEW
        xTrain = np.array(xTrain)
        yTrain = np.array(yTrain)
        xTest = np.array(xTest)
        yTest = np.array(yTest)

        # Assign numpy classes to y values (2 classes as pos/neg options) NEW
        yTrain = utils.to_categorical(yTrain, 2)
        yTest = utils.to_categorical(yTest, 2)
        

        # Convert python arrays to numpy arrays OLD
        #self.xNumpyData = np.array(xData)
        #self.yNumpyData = np.array(yData)

        # Assign numpy classes to y values (2 classes as pos/neg options) OLD
        #self.yNumpyData = utils.to_categorical(self.yNumpyData, 2)

        # Mix and split the data OLD
        #self.xNumpyData, self.yNumpyData = self.mixData(self.xNumpyData, self.yNumpyData)
        #xTrain, xTest, yTrain, yTest = self.splitData(self.xNumpyData, self.yNumpyData, 0.1)

        # Create the model
        self.model = self.createCNN()
        
        # Train the model
        self.model.fit(xTrain, yTrain, batch_size=32, epochs=12, verbose = 0, validation_data=(xTest, yTest))
        score = self.model.evaluate(xTest, yTest, verbose=2)
        print(score)
        return self.model


    def testModel(self, model):
        pass


    def mixData(self, xData, yData):
        """Randomises the order of the items in the data matrix"""
        combinedList = list(zip(xData, yData))
        random.shuffle(combinedList)
        newXData, newYData = zip(*combinedList)
        return newXData, newYData
    
    def splitData(self, xData, yData, testingRatio):
        """Splits the data into training and testing sets"""
        xTrain, xTest, yTrain, yTest = sklearn.model_selection.train_test_split(xData, yData, test_size=testingRatio)
        # Might need reshaping
        return xTrain, xTest, yTrain, yTest



    def createCNN(self):
        """Creates a Convolutional Neural Network to specification. Seperated for convenience."""
        model = Sequential()
        model.add(layers.Input((150,100,1)))
        model.add(layers.Conv2D(32, kernel_size=(4,4), activation='relu'))
        model.add(layers.Conv2D(64, (4,4)))
        model.add(layers.LeakyReLU(negative_slope=0.01))
        model.add(layers.MaxPooling2D(pool_size=(2,2)))
        model.add(layers.Dropout(0.2))
        model.add(layers.Flatten())
        model.add(layers.LeakyReLU(negative_slope=0.01))
        model.add(layers.Dense(2, activation='softmax'))
        model.compile(optimizer='adam', metrics=['accuracy'], loss=losses.binary_crossentropy)
        model.summary()

        return model
    
    def saveCNN(self, modelName):
        """Saves the CNN model"""
        self.model.save(modelName+".keras")



test = modelTrainer("data")
test.trainModel()
test.saveCNN("minionDetector")
#for list in test.data:
#    print("========================")
#    for item in list:
#        print(item)
# 'data/*.*'

        #print()
        #print()
        #print()
        #print()
        #for i in range(0,5):
        #    print(xTrain[i])
        #print()
        #print()
        #print()
        #print()
        #for i in range(0,5):
        #    print(yTrain[i])