import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Import đúng class Ui_MainWindow từ file ui/ecc.py vừa biên dịch của bạn
from ui.ecc import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Khởi tạo giao diện chuẩn của phân hệ ECC
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Kết nối các nút bấm logic dựa trên tên biến thực tế trong file ui/ecc.py
        self.ui.btn_general_key.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)
        
    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/ecc/sign"
        # Đọc dữ liệu từ ô thông tin txt_information
        payload = {
            "message": self.ui.txt_information.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị chữ ký số nhận được vào ô txt_signature
                self.ui.txt_signature.setText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/ecc/verify"
        # Lấy đồng thời dữ liệu từ cả 2 ô txt_information và txt_signature để xác thực
        payload = {
            "message": self.ui.txt_information.toPlainText(),
            "signature": self.ui.txt_signature.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                
                # Kiểm tra kết quả logic trả về từ API Flask
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verified Fail")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())