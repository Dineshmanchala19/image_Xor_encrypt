# Image XOR Encryption

This project provides Python scripts for encrypting and decrypting images using the XOR cipher.

## Introduction

Image XOR Encryption is a simple encryption technique that uses the XOR (exclusive OR) operation to encrypt and decrypt image files. The XOR operation combines the pixel values of the image with a randomly generated key, making it difficult for unauthorized users to view the content of the image without the key.

## Features

- Encrypt images using a randomly generated key.
- Decrypt encrypted images using the same key.
- Maintains the same image quality after encryption and decryption.

## How to Use

### Encryption

1. Clone the repository to your local machine.
2. Navigate to the repository directory.
3. Place the image file you want to encrypt in the same directory.
4. Run the `encryption.py` script:
5. Follow the on-screen instructions to specify the image file for encryption and the output directory.
6. The encrypted image will be saved in the specified output directory, and the encryption key will be saved in a file with the same name as the encrypted image but with the extension `.key.npy`.

### Decryption

1. Clone the repository to your local machine if you haven't already.
2. Navigate to the repository directory.
3. Place the encrypted image file and the encryption key file in the same directory.
4. Run the `decryption.py` script:
5. Follow the on-screen instructions to specify the encrypted image file, the encryption key file, and the output directory.
6. The decrypted image will be saved in the specified output directory.

## Explanation

- **Encryption Process**: During encryption, the image pixel values are combined with a randomly generated key using the XOR operation. This results in an encrypted image where the original pixel values are obscured.
- **Decryption Process**: To decrypt the encrypted image, the same key used for encryption is applied using the XOR operation. This reverses the encryption process and restores the original pixel values, resulting in a decrypted image identical to the original.

## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

