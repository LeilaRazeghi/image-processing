# Supplementary Topics
##  1- PNG (Portable Network Graphics)
Transparent Microsoft logo and remove it's background.
![](output\ms_logo_transparent.png)
## 2- Color Recognition
Writting a program with webcam to recognize these colors
![](output\blue.png)  ![](output\green.png)

## 3- MediaPipe
Using mediapipe to detect body landmarks on webcam stream.
![](output\mediapipe.png)

## 4- PIL (Python Imaging Library) without using OpenCV
### input: ![](input\photo_2024-03-22_00-33-08.jpg)
### output:
#### calculate and display 3 histogram ![](output\original_image_histogram.png)
#### Image with Persian text
![](output\ashkan_image.png)
#### Equalized image and its hisogram plot
![](output\equalized_image.jpg) ![](output\Equalied_image_histogram.png)
#### Gray image and its hisogram plot
![](output\gray_image.jpg)
![](output\gray_image_histogram.png)
#### Equalized gray image and its hisogram plot
![](output\equalized_gray_image.jpg)
![](output\equalized_gray_image_histogram.png)
## 5- Image Encryption and Decryption
Writting encryptor.py to get an image, then generating a random secret key and encrypt the image using secret key. Finally saving the encrypted image as a .bmp file and save the secret key as a .npy file.

Writting decryptor.py to get a cipher image and a secret key, then converting the cipher image into the original image. Finally saving the decrypted image as a .jpg file.

Writting main.py using PySide6 (Qt for Python) to show input and output in GUI.
![](encrytor_decrytor\encrypted_decrypted.png)