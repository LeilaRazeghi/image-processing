import cv2
import numpy as np

def add_snowflakes(image, num_snowflakes):
    height, width, _ = image.shape
    snowflakes = []

    for _ in range(num_snowflakes):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        speed = np.random.randint(1, 5)
        snowflakes.append([x, y, speed])

    return snowflakes

def animate_snowfall(image, snowflakes):
    for flake in snowflakes:
        x, y, speed = flake
        cv2.circle(image, (x, y), 1, (255, 255, 255), -1)
        flake[1] += speed

        # If snowflake reaches the bottom, reset its position to the top
        if flake[1] > image.shape[0]:
            flake[1] = 0
            flake[0] = np.random.randint(0, image.shape[1])

    return image


landscape = cv2.imread('snow.jpg')


num_snowflakes = 500

# Add snowflakes to the image
snowflakes = add_snowflakes(landscape.copy(), num_snowflakes)


while True:
    image_with_snowfall = animate_snowfall(landscape.copy(), snowflakes)
    cv2.imshow('Image with Snowfall', image_with_snowfall)

    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
