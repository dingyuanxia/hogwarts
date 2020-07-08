import os
import time
import urllib.request
import requests
#查看当前的绝对路径
#print(os.getcwd())

#判断当前路径下是否存在b文件
#print(os.path.exists("b"))

#新建文件
# if not os.path.exists("b"):
#     os.mkdir("b")
# if not os.path.exists("./b/b.txt"):
#     with open("./b/b.txt", "w") as f:
#         f.write("hello")

#显示所有的py文件
# print(os.listdir("./"))
#
# os.removedirs("/b")
#print(time.time())

#print(time.strftime("%Y%m%d %H:%M:%S",time.localtime()))
# print(time.ctime())
#
# respone = urllib.request.urlopen("https://www.baidu.com")
# print(respone.status)
r = requests.get("https://www.baidu.com")
r.encoding = "utf8"
print(r.text)