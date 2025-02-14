import cv2
import numpy as np

class Steganography:
    def __init__(self, image_path):
        """Initialize with the image path."""
        self.image_path = image_path

    def embed(self, secret_message):
        """Embed a secret message into the image."""
        image = cv2.imread(self.image_path)
        data = secret_message.encode('utf-8')
        data_len = len(data)

        # Check if the image is large enough to hold the message
        if data_len * 8 > image.size:
            raise ValueError("Image is too small to hold the secret message.")

        # Embed the message into the image's least significant bits
        data_index = 0
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                pixel = list(image[i, j])
                for k in range(3):  # RGB channels
                    if data_index < data_len:
                        pixel[k] = pixel[k] & ~1 | ((data[data_index] >> (7 - (k % 8))) & 1)
                        if k % 8 == 7:
                            data_index += 1
                image[i, j] = tuple(pixel)

        result_image_path = 'output_image.png'  # Save the modified image
        cv2.imwrite(result_image_path, image)
        return result_image_path

    def extract(self):
        """Extract the secret message from the image."""
        image = cv2.imread(self.image_path)
        data = []

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                pixel = image[i, j]
                for k in range(3):  # RGB channels
                    data.append(pixel[k] & 1)

        # Convert bits to bytes
        message = bytearray()
        for i in range(0, len(data), 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | data[i + j]
            message.append(byte)

        return message.decode('utf-8', errors='ignore')
