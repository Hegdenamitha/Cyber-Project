# Secure Data Hiding in Images Using Steganography
## Steganography
Steganography is the practice of concealing any information within a file, image, audio or video to ensure undetectable and secure communication. This method hides the existence of the data, enabling effective covert communication between users.
## Project Overview
This project is a LSB Image Steganography built using Python, enabling secure and user-friendly way to encrypt and decrypt information within an image using password protection. 
## Technologies used
 * **Python** – Programming Language
 * **OpenCV** – Image Processing
 * **Numpy** – Array modification
 * **Os** – File handling
 * **Least Significant Bit (LSB) Steganography**
## Features
  * **Password Protected Authentication** - Enhance security and prevent unauthorized retrieval
  * **Lossless embedding** – The quality of the image remains unchanged visually
  * **User friendly** – Simple  and easy to use without deep technical knowledge
  * **No additional storage requirement** – The message is embedded inside the image
## How it works
1.	**Encryption**
  * Select an image
  * Enter secret message and password
  * Encrypted image generated.
2. **Decryption**
  * Select encrypted image
  * Enter password used for encryption
  * If the decryption password matches the encrypted password, the embedded message is retrieved.
## Installation
### Prerequisities
1.	Ensure Python installed in the system
2.	Install dependencies
   ```Pip install opencv-python numpy```


