# Cartoonify an Image with OpenCV in Python 😎
### What is OpenCV?
Python is the pool of libraries. It has numerous libraries for real-world applications. One such library is OpenCV. OpenCV is a cross-platform library used for Computer Vision. It includes applications like video and image capturing and processing. It is majorly used in image transformation, object detection, face recognition, and many other stunning applications.

### What are we going to build?
At the end of this article, we aim to transform images into its cartoon. Yes, we will CARTOONIFY the images. Thus, we will build a python application that will transform an image into its cartoon using OpenCV.

## Steps to develop Image Cartoonifier
### Step 1: Importing the required modules
We will import the following modules:

CV2: Imported to use OpenCV for image processing
easygui: Imported to open a file box. It allows us to select any file from our system.
Numpy: Images are stored and processed as numbers. These are taken as arrays. We use NumPy to deal with arrays.
Imageio: Used to read the file which is chosen by file box using a path.
Matplotlib: This library is used for visualization and plotting. Thus, it is imported to form the plot of images.
OS: For OS interaction. Here, to read the path and save images to that path.

### Step 2: How is an image stored?
Now, just think, how will a program read an image? For a computer, everything is just numbers. Thus, in the below code, we will convert our image into a numpy array.
Imread is a method in cv2 which is used to store images in the form of numbers. This helps us to perform operations according to our needs. The image is read as a numpy array, in which cell values depict R, G, and B values of a pixel.


### NOTE: We resize the image after each transformation to display all the images on a similar scale at last.

Beginning with image transformations:
To convert an image to a cartoon, multiple transformations are done. Firstly, an image is converted to a Grayscale image. Yes, similar to the old day’s pictures.! Then, the Grayscale image is smoothened, and we try to extract the edges in the image. Finally, we form a color image and mask it with edges. This creates a beautiful cartoon image with edges and lightened color of the original image.

Let’s start with these transformations to convert an image to its cartoon image.

### Step 3: Transforming an image to grayscale
cvtColor(image, flag) is a method in cv2 which is used to transform an image into the colour-space mentioned as ‘flag’. Here, our first step is to convert the image into grayscale. Thus, we use the BGR2GRAY flag. This returns the image in grayscale. A grayscale image is stored as grayScaleImage.

After each transformation, we resize the resultant image using the resize() method in cv2 and display it using imshow() method. This is done to get more clear insights into every single transformation step.

### Step 5: Smoothening a grayscale image
To smoothen an image, we simply apply a blur effect. This is done using medianBlur() function. Here, the center pixel is assigned a mean value of all the pixels which fall under the kernel. In turn, creating a blur effect.

### Step 6: Retrieving the edges of an image
Cartoon effect has two specialties:

-> Highlighted Edges
-> Smooth colors
In this step, we will work on the first specialty. Here, we will try to retrieve the edges and highlight them. This is attained by the adaptive thresholding technique. The threshold value is the mean of the neighborhood pixel values area minus the constant C. C is a constant that is subtracted from the mean or weighted sum of the neighborhood pixels. Thresh_binary is the type of threshold applied, and the remaining parameters determine the block size.

### Step 7: Preparing a Mask Image
In the above code, we finally work on the second specialty. We prepare a lightened color image that we mask with edges at the end to produce a cartoon image. We use bilateralFilter which removes the noise. It can be taken as smoothening of an image to an extent.

The third parameter is the diameter of the pixel neighborhood, i.e, the number of pixels around a certain pixel which will determine its value. The fourth and Fifth parameter defines signmaColor and sigmaSpace. These parameters are used to give a sigma effect, i.e make an image look vicious and like water paint, removing the roughness in colors.

Yes, it’s similar to BEAUTIFY or AI effect in cameras of modern mobile phones.

### Step 8: Giving a Cartoon Effect
So, let’s combine the two specialties. This will be done using MASKING. We perform bitwise and on two images to mask them. Remember, images are just numbers?

Yes, so that’s how we mask edged image on our “BEAUTIFY” image.

This finally CARTOONIFY our image!
