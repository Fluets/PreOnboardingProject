# Minion Meme Detector

## Summary
The Minion Meme Detector scans an image provided to it and tells you if it suspects that image is a dastardly minion meme or simply an innocent image, using a Convolutional Neural Network trained on hundreds of images!
This repository also includes the code used to make the CNN so you can make your own model using your own dataset.

## How to use
Run the `minionDetector.py` file in a folder with `preprocessImages.py` and `minionDetector.keras`.
Hit the large button and select your image.
Done! It should give you its answer right away.

To create your own model run `trainModel.py` in a folder with `preprocessImages.py` and two other folders: `m` and `n` - where `m` contains images of minion memes and `n` contains other images.
Please use the following formats for images: png, jpg, webp, jpeg, avif

## Evaluation
The CNN model provided reports an 80% testing accuracy. It has a high success rate with few false negatives, but is prone to inexplicable false negatives at times.

The model can be improved with more images. It was trained on 100 minion memes and 100 other images. Both could be expanded manually or through the use of data augmentation.
The model also learns in greyscale and could be improved by adding full colour recognition.

The model's practicality is hampered by its nature as a run file. Ideally it would in future be implemented as a browser extension in order to automatically flag and censor minion memes before the user is subjected to them in the first place.
Training new models could also be more user-friendly through implementing the feature into the UI.

The above features were deemed beyond the scope of the project due to the assigned time and (slow!) rate at which the creator got underway with the project.
