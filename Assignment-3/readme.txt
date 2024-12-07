Assignment 3: Creating a Collage from 4 Images

Overview:
This Python script allows you to create a 2x2 image collage by combining four images. You can choose to either resize or crop the images to fit the collage grid. The output collage can be saved in formats such as JPG, PNG, or BMP.

Libraries to Install:
pip install pillow

Extra Feature Added:
An additional feature I have implemented to allow users to choose how the images should be adjusted to fit the grid:
- Resize the images (which may cause stretching) to fit the smallest size. 
    OR
- Crop the images to maintain the aspect ratio, cutting parts of the image as needed to fit the dimensions of the grid.

How It Works:
1. The script takes four image paths as input and checks if they exist and are valid images.
2. Based on the user's choice, the images are either resized or cropped to fit the smallest dimensions of the provided images.
3. A blank canvas of appropriate size is created to accommodate the images in a 2x2 grid layout.
4. The images are pasted into the collage.
5. The collage is then saved in the user-specified format (JPG, PNG, or BMP).

Input:
The script requires four image paths, which should be provided when prompted. Additionally, the user must specify:
1. Whether to resize or crop the images.
2. The desired output format for the collage (JPG, PNG, BMP).

Output:
The script will output a collage in the specified format (JPG, PNG, or BMP). The collage will be saved with the name "collage" in the current working directory, unless a different name is provided.

Example:
Please enter the path for Image 1: /path/to/image1.jpg
Please enter the path for Image 2: /path/to/image2.jpg
Please enter the path for Image 3: /path/to/image3.jpg
Please enter the path for Image 4: /path/to/image4.jpg
Do you want to resize (may stretch) or crop the images? (resize/crop): resize
Please specify the output file format (jpg, png, bmp): png

The collage will be saved as "collage.png" in the current directory.