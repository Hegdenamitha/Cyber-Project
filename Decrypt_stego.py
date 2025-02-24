import cv2

def decrypt_image(img_path, entered_password):
    img = cv2.imread(img_path)

    if img is None:
        print("Error: Unable to load image. Check the file path.")
        return

    n, m, z = 0, 0, 0

    # Extract stored password length
    pas_length = img[n, m, z]
    
    # Extract stored message length
    msg_length = img[n+1, m+1, (z+1) % 3]

    n += 2
    m += 2
    z = (z + 2) % 3

    extracted_password = ""

    # Extract the stored password
    for _ in range(pas_length):
        extracted_password += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3

    print(f"Extracted Password: {extracted_password}")

    # Check if the password matches
    if entered_password != extracted_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    print("Password Matched! Decrypting message...")

    decrypted_message = ""

    # Extract the stored message
    for _ in range(msg_length):
        decrypted_message += chr(img[n, m, z])
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    img_path = "encrypted_Image.png"  # Path to the encrypted image
    entered_password = input("Enter the original passcode used during encryption: ")
    decrypt_image(img_path, entered_password)
