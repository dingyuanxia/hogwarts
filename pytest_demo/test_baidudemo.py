import time

from selenium import webdriver
import pytest
import allure


@allure.feature("百度测试demo")
class TestBaidu:

    @pytest.mark.parametrize("data1", ["pytet", "allure"])
    def test_baidudemo(self, data1):
        with allure.step("打开浏览器"):
            driver = webdriver.Chrome()
            driver.get("https://www.baidu.com")
        driver.maximize_window()
        driver.find_element_by_id("kw").send_keys(data1)
        time.sleep(2)
        with allure.step("保存图片"):
            driver.save_screenshot("./assets/11.png")
            allure.attach.file("./assets/11.png", attachment_type=allure.attachment_type.PNG)
        driver.quit()


