
print('ho ten: Dang Phan Tung Duong; MAV:245752021610119')
transactions = input("Nhập nhật ký giao dịch, cách nhau bởi dấu phẩy: ").split(',')
account_balance = sum(map(float, transactions))
print(f"số tiền thực trong tài khoản: {account_balance}")

