import pytest


class TestDemo():
    @pytest.fixture(autouse=True)
    def login(self):
        print("首先需要登录")
        #yield
        print("退出登录")
    def test_one(self):
        print("test one")
        a = "hello"
        b = "hello everyone"
        assert a in b
        # pytest.assume(1==4)

    def test_two(self):
        print("test two")
        a = "hello"
        b = "hello everyone"
        assert a in b



if __name__ == '__main__':
    # 运行的第一个方式
    # pytest.main("-v,-s,TestDemo")
    # 运行的第二个方式
    pytest.main(['-v', '-s', 'TestDemo'])
