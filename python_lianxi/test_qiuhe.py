# import random
#
#
#
# computer_num = random.randint(1, 100)
# print(computer_num)
#
# while True:
#     person_num = int(input("请输入一个数字"))
#     if computer_num == person_num:
#         print(" 猜对了")
#     elif computer_num > person_num:
#         print("大一点")
#     elif computer_num < person_num:
#         print("小一点")
#     break


class MyExpection(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
raise MyExpection("a", "b")