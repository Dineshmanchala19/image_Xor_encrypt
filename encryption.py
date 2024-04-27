from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, output_path):
    # Load the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypt the image
    key = np.random.randint(0, 256, size=image_array.shape, dtype=np.uint8)
    encrypted_image_array = np.bitwise_xor(image_array, key)

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_image_array)
    encrypted_image.save(output_path)
    
    # Save the encryption key in a separate file
    key_path = output_path + ".key.npy"
    np.save(key_path, key)

    print("Image encrypted successfully!")

if __name__ == "__main__":
    # Get the path to the image file from the user for encryption
    image_path = input("Enter the path to the image file for encryption: ")
    output_directory = input("Enter the directory path to save the encrypted image: ")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_filename = input("Enter the filename for the encrypted image (including extension): ")
    output_path = os.path.join(output_directory, output_filename)
    
    # Encrypt the :image
    encrypt_image(image_path, output_path)
