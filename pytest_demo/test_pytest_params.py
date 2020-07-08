import pytest
import yaml


@pytest.mark.parametrize("a,b",yaml.safe_load(open('./data.yaml')))
def test_sum(a, b):
    print(f"{a}+{b}=", a+b)

#print(yaml.safe_load(open("./data.yaml")))