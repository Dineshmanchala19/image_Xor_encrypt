from PIL import Image
import numpy as np
import os

def decrypt_image(image_path, key_path, output_path):
    # Load the encrypted image
    encrypted_image = Image.open(image_path)
    encrypted_image_array = np.array(encrypted_image)
    
    # Load the encryption key
    key = np.load(key_path)

    # Decrypt the image
    decrypted_image_array = np.bitwise_xor(encrypted_image_array, key)

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_image_array)
    decrypted_image.save(output_path)

    print("Image decrypted successfully!")

if __name__ == "__main__":
    # Get the paths from the user
    encrypted_image_path = input("Enter the path to the encrypted image file: ")
    key_path = input("Enter the path to the encryption key file: ")
    output_directory = input("Enter the directory path to save the decrypted image: ")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_filename = input("Enter the filename for the decrypted image (including extension): ")
    output_path = os.path.join(output_directory, output_filename)
    
    # Decrypt the image
    decrypt_image(encrypted_image_path, key_path, output_path)
