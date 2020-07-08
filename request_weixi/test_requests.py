import pytest
import requests

@pytest.fixture(scope="session")
def test_token():
    corpid = 'ww74c686921713d570'
    corpsecret = 'bBVMDlHST0nr7C-qIuLha0EWKwAa_fp0o1cMFKmxI0k'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    return res.json()['access_token']


def test_readmember(userid, test_token):
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}')
    print(res.text)
    return res.json()

def test_creatrember(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1]

    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}", json=data)
    print(res.json())
    return res.json()


def test_updatemember():
    data = {
        "userid": "zhangsan",
        "name": "李四",
        "mobile": "13811111111"
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}', json=data)
    print(res.json())

def test_deletemember():
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid=zhangsan')
    print(res.json())


@pytest.mark.parametrize("userid, name, mobile", [("2", "小白4", "19967879800")])
def test_all(userid, name, mobile, test_token):
    assert "created" == test_creatrember(userid, name, mobile, test_token)['errmsg']
    assert name == test_readmember(userid, test_token)['name']
    print(test_readmember(userid, test_token)['name'])


