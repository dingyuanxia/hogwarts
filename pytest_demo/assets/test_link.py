import allure

# class TestLink:
#     #添加连接
#     @allure.link("https://baidu.com", name="百度连接")
#     def test_link(self):
#         print("link")
#     #添加case连接
#     test_case_link = "https://www.baidu.com"
#     @allure.testcase(test_case_link, "登录用例")
#     def test_link2(self):
#         print("这是一条测试用例连接，连接到测试用例里面")
#
#     #连接到bug库中对应的bug
#     #--allure-link-pattern=issue:https://www.baidu.com
#     @allure.issue("140", "这是一个issue")
#     def test_link3(self):
#         pass
#     @allure.severity(allure.severity_level.NORMAL)
#     def test_severity(self):
#         print("标注用例级别")


class TestAttach:
    def test_attach(self):
        allure.attach.file("/Users/heweimao/丁元霞/hogwarts/pytest_demo/assets/assets/IMG_20170604_091540.jpg",attachment_type=allure.attachment_type.JPG)