# Validation-Set-Creator
Creates validation set from a training dataset(image datasets)

Often in ML challenges and many online datasets contains only training sets. This python script creates a validation set out of the training set by selecting random images from the training set and moving them to a new folder which is named "validation" by default.
Inside the valdiation folder will be the validation.csv file containing the tags for the validation dataset.

After successful execution, a completion message will be printed and a new folder named "validation" will be created in the same directory as the one containing the training images.

Note- This script currently only copies the needful data from the train.csv file. The tags data of the images transferred to validation dataset might still present in the train.csv file.
