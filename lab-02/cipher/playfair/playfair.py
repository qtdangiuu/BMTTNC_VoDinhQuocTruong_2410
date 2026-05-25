class PlayFairCipher:
    def __init__(self):
        pass
    
    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        
        # Chỉ giữ lại các ký tự duy nhất trong key theo thứ tự xuất hiện
        seen = set()
        matrix = []
        for char in key:
            if char.isalpha() and char not in seen:
                seen.add(char)
                matrix.append(char)
                
        # Điền các ký tự còn lại của bảng chữ cái vào ma trận
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in seen:
                seen.add(letter)
                matrix.append(letter)
                if len(matrix) == 25:
                    break
                    
        # Chuyển mảng phẳng thành ma trận 5x5
        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix
        
    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None # Tránh lỗi nếu không tìm thấy ký tự
                
    def playfair_encrypt(self, plain_text, matrix):
        plain_text = plain_text.upper().replace("J", "I")
        
        # Lọc chỉ lấy chữ cái
        clean_text = "".join([c for c in plain_text if c.isalpha()])
        
        # Xử lý chèn 'X' vào giữa các cặp ký tự trùng nhau
        prepared_text = ""
        i = 0
        while i < len(clean_text):
            prepared_text += clean_text[i]
            if i + 1 < len(clean_text):
                if clean_text[i] == clean_text[i+1]:
                    prepared_text += "X"  # Chèn X nếu 2 ký tự liên tiếp trùng nhau
                    i += 1
                else:
                    prepared_text += clean_text[i+1]
                    i += 2
            else:
                i += 1
                
        # Nếu tổng số ký tự lẻ, chèn thêm 'X' ở cuối
        if len(prepared_text) % 2 != 0:
            prepared_text += "X"
            
        encrypted_text = ""
        for i in range(0, len(prepared_text), 2):
            pair = prepared_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:  # Cùng hàng -> Dịch phải
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột -> Dịch xuống
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:  # Khác hàng khác cột -> Tạo hình chữ nhật
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        return encrypted_text
    
    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace("J", "I")
        clean_text = "".join([c for c in cipher_text if c.isalpha()])
        
        decrypted_text = ""
        for i in range(0, len(clean_text), 2):
            pair = clean_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            
            if row1 == row2:  # Cùng hàng -> Dịch trái
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột -> Dịch lên
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:  # Khác hàng khác cột -> Lấy góc đối diện
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]
                
        # Khử các ký tự 'X' đã chèn thêm (Khôi phục bản rõ nguyên bản)
        banro = ""
        j = 0
        while j < len(decrypted_text):
            if j + 2 < len(decrypted_text) and decrypted_text[j+1] == 'X' and decrypted_text[j] == decrypted_text[j+2]:
                banro += decrypted_text[j] + decrypted_text[j+2]
                j += 3  # Bỏ qua ký tự 'X' ở giữa
            else:
                banro += decrypted_text[j]
                j += 1
                
        # Khử ký tự 'X' ở cuối cùng nếu nó là ký tự đệm lẻ ban đầu
        if banro.endswith('X'):
            banro = banro[:-1]
            
        return banro