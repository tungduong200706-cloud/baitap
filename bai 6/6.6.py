
print('ho ten: Dang Phan Tung Duong; MAV:245752021610119')
class StringModifier:
    def __init__(self):
        self.input_string = ""

    def get_String(self):
        self.input_string = input("Nhập chuỗi: ")

    def print_String(self):
        print("Chuỗi in hoa:", self.input_string.upper())

# Sử dụng
modifier = StringModifier()
modifier.get_String()
modifier.print_String()

