# Neural Network project with TensorFlow 
As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

This project uses TensorFlow to build a neural network to classify road signs based on an image of those signs. It uses labelled dataset of a collection of images that have already been categorised by the road sign represented in them.

The German Traffic Sign Recognition Benchmark (GTSRB) dataset is used, which contains thousands of images of 43 different kinds of road signs.

## To run program
### Install requirements 
pip3 install -r requirements.txt

### Download datasets
Actual - https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip
Small (for quick testing) - https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb-small.zip 

#### Run command
python traffic.py data_directory (The latest version of Python you should use is Python 3.11 due to interactions with TensorFlow)

## Experiment with tensor flow parameter
### Convolutional and pooling layers
I tried it out with different numbers of convolutional and pooling layers starting with 1 first. It had an accuracy of around 20%. 

When 2 layers were used, it could rise up to over 90% depending on the values of other parameters used, such as the number of neurons in the Dense layer. However, the higher Dense input value might bring about overfitting. I settled at 4 convolutional and pooling layers in order to ensure good mix of computational complexity and accuracy results. 

## Different numbers and sizes of filters for convolutional layers
When there is only one layer of convolutional layer, the accuracy didn't improve much as the number of filters increased. This means that the dataset's complexity is not so complex such that it doesn't increase the model's capacity to learn complex patterns. 

Increasing the filter/kernel size generally improved the accuracy. The larger kernel size allows the convolutional layer to capture more spatial information from the input data This allows the network to learn more complex features but it also increases the computational cost and the risk of overfitting. 

Best result 32, (7,7)

## Different pool sizes for pooling layers
Noticed that smaller pool size is better with the dataset.  

## Different numbers and sizes of hidden layers
Generally better with more hidden layers but increases complexity.

## Dropout
Lower the better, but increases chances of over-fitting the result. 


