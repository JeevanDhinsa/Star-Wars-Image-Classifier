# Star-Wars-Image-Classifier

 Image classifier for Star Wars characters in python using the residual neural network ResNet-50.

 The classifier currently has an accuracy of 77% in predicting characters based on testing data.

## Performance

### Model accuracy over training
![modacc](https://github.com/JeevanDhinsa/Star-Wars-Image-Classifier/blob/main/Outputs/modacc.png)

### Model loss over training
![modloss](https://github.com/JeevanDhinsa/Star-Wars-Image-Classifier/blob/main/Outputs/modloss.png))

## Example

![r2d2](https://github.com/JeevanDhinsa/Star-Wars-Image-Classifier/blob/main/Outputs/r2d2test.png)

```
image=cv2.imread("r2d2test.png")
image_resized= cv2.resize(image, (img_height,img_width))
image=np.expand_dims(image_resized,axis=0)
print(image.shape)

pred=resnet_model.predict(image)
output_class=class_names[np.argmax(pred)]
print("The predicted class is", output_class)
```
The predicted class is R2D2

## Data Preparation

For instructions on splitting data into Training, Testing and Validation catergories see [Data Preprocessing](https://github.com/JeevanDhinsa/Star-Wars-Image-Classifier/blob/main/star_wars_classifier.ipynb)

## Data Availability

Uses 4727 star wars images from a publically available dataset linked here: [Star Wars Images](https://www.kaggle.com/datasets/mathurinache/star-wars-images?resource=download)

## Dependencies

* Tensorflow
* Keras
* Matplotlib
* numpy
* cv2
