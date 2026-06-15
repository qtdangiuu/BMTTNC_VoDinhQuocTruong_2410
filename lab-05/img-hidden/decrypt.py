import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)

    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size

    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for channel in range(3):
                binary_message += str(pixel[channel] & 1)

    message = ""

    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]

        if len(byte) < 8:
            break

        # Gặp ký tự kết thúc
        if byte == "00000000":
            break

        message += chr(int(byte, 2))

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]

    decoded_message = decode_image(encoded_image_path)

    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()