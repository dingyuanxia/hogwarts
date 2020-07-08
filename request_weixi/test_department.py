import requests

#1.获取token
def test_token():
    corpid = 'ww74c686921713d570'
    corpsecret = 'bBVMDlHST0nr7C-qIuLha0EWKwAa_fp0o1cMFKmxI0k'
    res = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    return res.json()['access_token']

#2.创建部门
def test_createdepartment():
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 1,
        "order": 1,
        "id": 2
    }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}', json=data)
    print(r.json())

#3.更新部门
def test_updatedepartment():
    data = {

            "id": 2,
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
    r = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}', json=data)
    print(r.json())

#4.删除部门
def test_deletedepartment():
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id=2')
    print(r.json())

#5.获取部门列表
def test_getdepartment():
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={test_token()}')
    print(r.json())
