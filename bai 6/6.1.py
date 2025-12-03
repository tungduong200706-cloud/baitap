
print('ho ten: Dang Phan Tung Duong; MAV:245752021610119')

# Sử dụng def methodName(self) để định nghĩa method.
class Circle(object):
    def __init__(self, r):
        self.radius = r

############################
    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())

