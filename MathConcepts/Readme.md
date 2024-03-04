# Convolution Basic Concepts
## 1. Calculate Histogram
Getting an image as input and calculate its **Histogram** then visualize the results with plt.plot(), plt.hist() and plt.bar() 
### input: ![](input/photo_2024-02-22_09-38-32.jpg)

### output: plt.hist() ![](output/histogram.png)
### output: plt.bar()  ![](output/bar.png)
### output: plt.plot()  ![](output/plot.png)

## 2. Forground focus and Blurred background
### input: ![Flower](input/flower_input.jpg)
### output: ![Blurred backround](output/blur_background.png)
## 3. Edge Detection
Laplacian Operator is used to detect edges of image
### input: ![lion](input/lion.png) ![spide](input/spider.webp)

### output: ![edged lion](output/lion_edge.png)  ![edged spider](output/spider_edge.png)

## 4. Building Horiontal & Vertical Edge Eetection
### input: ![building](input/building.png)
### output:  ![Hor Biulding](output/Building_h.png)  ![Ver Building](output/Building_v.png)

## 5. Image Noise Reduction
### input: ![xray noise](input/xray_noisy.png) ![board noise](input/board_noisy.png) ![circle noise](input/image_noisy.png)
### output: ![reduced noise board](output/board_noise_reduction.png) ![reduced noise circle](output/circle_noise_reduction.png) ![reduced noise xray](output/xray_noise_reduction.png)
