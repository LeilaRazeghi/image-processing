import numpy as np
import cv2

def encrypt_image(image_path):
    original_image = cv2.imread("input\photo_2024-03-22_00-32-53.jpg", cv2.IMREAD_GRAYSCALE)
    secret_key = np.random.randint(0, 256, size=original_image.shape, dtype=np.uint8)
    encrypted_image = cv2.bitwise_xor(original_image, secret_key)

    cv2.imwrite('encrypted_image.bmp', encrypted_image)
    np.save('secret_key.npy', secret_key)


if __name__== "__main__":
    input_image_path = "input\photo_2024-03-22_00-32-53.jpg"
    encrypt_image(input_image_path)