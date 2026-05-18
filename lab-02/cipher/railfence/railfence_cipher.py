class RailFenceCipher:

    def __init__(self):
        pass

    def encrypt(self, plain_text, num_rails):

        rails = [[] for _ in range(num_rails)]

        rail_index = 0
        direction = 1

        for char in plain_text:

            rails[rail_index].append(char)

            if rail_index == 0:
                direction = 1

            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        cipher_text = ''.join( ''.join(rail) for rail in rails)

        return cipher_text

    def decrypt(self, cipher_text, num_rails):

        rail_lengths = [0] * num_rails

        rail_index = 0
        direction = 1

        # Đếm số ký tự mỗi rail
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Chia cipher_text vào từng rail
        rails = []
        start = 0

        for length in rail_lengths:

            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Khôi phục plain text
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):

            plain_text += rails[rail_index].pop(0)

            if rail_index == 0:
                direction = 1

            elif rail_index == num_rails - 1:
                direction = -1

            rail_index += direction

        return plain_text