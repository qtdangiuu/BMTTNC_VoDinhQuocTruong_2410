import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size

    # Chuyển thông điệp sang nhị phân
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Ký tự kết thúc
    binary_message += '00000000'

    data_index = 0

    for row in range(height):
        for col in range(width):
            pixel = list(img.getpixel((col, row)))

            for channel in range(3):
                if data_index < len(binary_message):
                    pixel[channel] = (pixel[channel] & ~1) | int(binary_message[data_index])
                    data_index += 1

            img.putpixel((col, row), tuple(pixel))

            if data_index >= len(binary_message):
                encoded_image_path = "encoded_image.png"
                img.save(encoded_image_path)
                print(f"Steganography complete.")
                print(f"Encoded image saved as {encoded_image_path}")
                return

    print("Error: Message is too large for this image.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> <message>")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]

    encode_image(image_path, message)

if __name__ == "__main__":
    main()