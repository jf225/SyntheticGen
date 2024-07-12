# SyntheticGen v0.1.1

This is a Python package available on PyPi that creates synthetic datasets for various dataset types.

**SyntheticGen currently supports:**
 - Linear Synthetic Datasets
 - Linear Augmentations

# Installation
    pip install syntheticgen

# Usage
In v0.1.0 there is only a linear augmentor available however, image and experimental augmentation techniques will be available soon.
```
#Import a dataset as a numpy array (in this example it is named dataset)
#Create an augmentor object and initialize it with the dataset
aug = linearAugmentor(dataset)


#addMatrix() and setPowerRange() will configure the augmentor with custom specifications.
aug.addMatrix(.25)
aug.setPowerRange(2,2)

#performOperations() will run the augmentation operations with the set configuration.
aug.performOperation()

#Returns the augmented dataset
dataset = aug.getCombinedSet()
```

# Object and Method Details
**linearAugmentor(dataset):**\
This is the augmentor object for psuedo-linear datasets.
>Dataset Specifications For Proper Function:
 - Must be a numpy array with sub-lists holding inputs and outputs in the same order every line.
 - Each sub-list in the dataset must be of equal length to one another


**linearAugmentor.addMatrix(percentAdded):**\
This method will randomly add a custom percentage of the inputed dataset into a matrix to then be augmented.
>Parameters:
 - percentAdded
    - This is a float value that determines the percentage of the inputted dataset that will be augmented.
    - Minimum to function: whatever float equates to 2 lines of the dataset.
    - Maximum is 1.0, the entire dataset.

**linearAugmentor.setIntRange(lowerBound, upperBound):**\
This method will set an integer range for the number of operations to be performed on the matrix.
>Parameters:
 - lowerBound
   - This is the fewest possible operations to be performed on the inputted dataset's matrix.
   - Minimum: 0
   - No Maximum
 - upperBound
   - This is the maximum number of possible operations to be performed on the inputted dataset's matrix.
   - Minimum: 0
   - No Maximum

**linearAugmentor.setPowerRange(lowerBound, upperBound):**\
This method will set a range for the number of operations to be performed on the matrix based on the length of the matrix raised to a power (the bounds).
>Parameters:
 - lowerBound
   - This is the value the length of the matrix will be raised by creating the fewest possible operations to be performed.
   - Minimum: 0
   - No Maximum
 - upperBound
   - This is the value the length of the matrix will be raised by creating the maximum number of possible operations to be performed.
   - Minimum: 0
   - No Maximum
     
**linearAugmentor.performOperations():**\
This is the method that will perform the operations on the matrix given the inputted specifications. 
   
**linearAugmentor.getCombinedSet():**\
This method returns the original dataset randomly combined with the newly created augmented data.

**linearAugmentor.getSyntheticData()**\
This method returns only the augmented data creating a fully synthetic dataset.

**linearAugmentor.getInitialDataset()**\
This method returns the originally inputted, unchanged dataset. 

# Roadmap
>Linear Augmentor
 - Add additional customization options pertaining to the type of operations performed
 - Add more advanced augmentation techniques utilizing eingenvectors.
>Image Augmentor
 - Add an image augmentor that performs multiple augmentation techniques. 
>Differential Augmentor
 - Experimental augmentor that's currently in production utilizing differential calculus.

# Recent Changes
v0.1.1
  - README changes.

v0.1.0
  - Created package and added the linear augmentor.
