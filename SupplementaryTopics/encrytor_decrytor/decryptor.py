import numpy as np
import cv2

def decrypt_image(encrypted_image_path, secret_key_path):
    encrypted_image = cv2.imread(encrypted_image_path, cv2.IMREAD_GRAYSCALE)

    secret_key = np.load(secret_key_path)

    decrypted_image = cv2.bitwise_xor(encrypted_image, secret_key)

    cv2.imwrite("decrypted_image.jpg", decrypted_image)

if __name__ =="__main__":
    encrypted_image_path = "encrytor_decrytor\encrypted_image.bmp"
    secret_key_path = "encrytor_decrytor\secret_key.npy"
    decrypt_image(encrypted_image_path, secret_key_path)