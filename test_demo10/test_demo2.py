class Calc:

    def add(self, a, b, sum):
        print(sum == a + b)
        return a+b

    def div(self, a, b, div):
        if b == 0:
            return "被除数不能为0"
        else:
            return a / b
        test


