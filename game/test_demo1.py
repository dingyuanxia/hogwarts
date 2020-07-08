import unittest


class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test case01")
        self.assertEqual(1, 1, "判断相等")
    @unittest.skip
    def test_case02(self):
        print("test case02")
        self.assertEqual(1, 1, "判断相等")

if __name__ == '__main__':
    unittest.main()