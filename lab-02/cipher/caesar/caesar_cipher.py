from cipher.caesar import Alphabet

class CaesarCipher:
    def __init__(self):
        self.alphabet = Alphabet

    def encrypt_text(self, text : str, key : int) -> str:
        text = text.upper() # Chuyển đổi văn bản thành chữ hoa "HUTECH"
        alphabet_len = len (self.alphabet) # Độ dài của bảng chữ cái (26)
        encrypted_text = []
        for i in text: #Lặp qua từng ký tự trong văn bản
            letter_index = self.alphabet.index(i) # Tìm vị trí của ký tự trong bảng chữ cái VD: H = 7 
            output_index = (letter_index + key) % alphabet_len # Tính vị trí mới sau khi dịch chuyển VD: (7 + 5) % 26 = 12
            output_letter = self.alphabet[output_index] # Lấy ký tự mới từ bảng chữ cái VD: M
            encrypted_text.append(output_letter) # Thêm ký tự đã mã hóa vào
        return "".join(encrypted_text)

    def decrypt_text(self, text : str, key : int) -> str:
        text = text.upper() # Chuyển đổi văn bản thành chữ hoa "M"
        alphabet_len = len (self.alphabet) # Độ dài của bảng chữ cái (26)
        decrypted_text = []
        for i in text: #Lặp qua từng ký tự trong văn bản
            letter_index = self.alphabet.index(i) # Tìm vị trí của ký tự trong bảng chữ cái VD: M = 12 
            output_index = (letter_index - key) % alphabet_len # Tính vị trí mới sau khi dịch chuyển VD: (12 - 5) % 26 = 7
            output_letter = self.alphabet[output_index] # Lấy ký tự mới từ bảng chữ cái VD: H
            decrypted_text.append(output_letter) # Thêm ký tự đã giải mã vào
        return "".join(decrypted_text)