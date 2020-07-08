import allure
import pytest
@allure.feature("测试样例")
class TestAllure():
    @allure.story("测试成功")
    def test_success(self):
        """this test succeeds"""
        assert True

    @allure.story("测试失败")
    def test_failure(self):
        """this test fails"""
        assert False

    @allure.story("跳过测试")
    def test_skip(self):
        """this test is skipped"""
        with allure.step("测试步骤"):
            print("打印测试步骤")
            pytest.skip('for a reason!')

    @allure.story("测试中断")
    def test_broken(self):
        raise Exception('oops')
