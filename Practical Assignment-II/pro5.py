# 5. Function Inside Another Function

def cal(a, b):
    
    def add():
        return a + b
    
    def mul():
        return a * b
    
    print("Addition:", add())
    print("Multiplication:", mul())

cal(5, 3)
