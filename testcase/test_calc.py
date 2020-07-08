import pytest

from test_demo10.test_demo2 import Calc


class TestCal:

    @pytest.mark.parametrize("a,b,sum", [(1, 2, 3), (-1, -1, -2), (1, -2, -1), (1.1, 1.2, 2.3)])
    def test_add(self, a, b, sum):
        self.calc = Calc()
        result = self.calc.add(a, b, sum)
        print(result)
        assert result == sum

    @pytest.mark.parametrize("a,b,div", [(4, 2, 2.0), (-4, 2, -2), (0.6, 0.3, 2.0), (0, 0, "被除数不能为0")])
    def test_div(self, a, b, div):
        self.calc = Calc()
        result_div = self.calc.div(a, b, div)
        print(result_div)
        assert result_div == div
