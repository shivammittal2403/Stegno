from PIL import Image

class ImageSteg:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path)

    def embed_message(self, message):
        # Convert message to binary
        binary_message = ''.join(format(ord(i), '08b') for i in message)
        data_index = 0

        # Modify the least significant bit of the image pixels
        pixels = self.image.load()
        for y in range(self.image.size[1]):
            for x in range(self.image.size[0]):
                pixel = list(pixels[x, y])
                for i in range(3):  # Modify RGB
                    if data_index < len(binary_message):
                        pixel[i] = pixel[i] & ~1 | int(binary_message[data_index])
                        data_index += 1
                pixels[x, y] = tuple(pixel)

        self.image.save('output_' + self.image_path)

    def extract_message(self):
        binary_message = ''
        pixels = self.image.load()
        for y in range(self.image.size[1]):
            for x in range(self.image.size[0]):
                pixel = pixels[x, y]
                binary_message += str(pixel[0] & 1)  # Get LSB of the red channel

        # Convert binary to string
        message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
        return message.split('\x00', 1)[0]  # Return message until null character
