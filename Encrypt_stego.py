import cv2
import os
import numpy as np

def encrypt_image(img_path, secret_message, password):
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Image not found!")
        return

    n, m, z = 0, 0, 0

    # Store password length in the first pixel
    img[n, m, z] = len(password)
    
    # Store message length in the second pixel
    img[n+1, m+1, (z+1) % 3] = len(secret_message)

    n += 2
    m += 2
    z = (z + 2) % 3

    # Encode the password into the image
    for char in password:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Encode the secret message into the image
    for char in secret_message:
        img[n, m, z] = ord(char)
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save the encrypted image
    cv2.imwrite("encrypted_Image.png", img)
    print("Message encrypted successfully!")

if __name__ == "__main__":
    img_path = "image.png"  # Replace with the correct image path
    secret_message = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt_image(img_path, secret_message, password)
