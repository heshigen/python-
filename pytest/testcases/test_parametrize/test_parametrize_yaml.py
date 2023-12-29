

import pytest
import requests

from pytest.testcases.utils.read_data import get_data


@pytest.mark.parametrize("shouji,appkey", get_data()["mobile_parametrize"])
def test_mobile_post(shouji,appkey):
    print(shouji,appkey)

    print("获取手机归属地post请求")
    params = {"shouji": shouji,"appkey": appkey}
    """获取手机号归属号信息"""
    r = requests.post("https://api.binstd.com/shouji/query",params=params)
    print(r.status_code)
    assert r.status_code == 200
    result = r.json()
    assert result["status"] == 0
    assert result["msg"] == "ok"
    assert result["result"]["shouji"] == "13456755448"
    assert result["result"]["province"] == "浙江"
    assert result["result"]["city"] == "杭州"
    assert result["result"]["cardtype"] is None
    assert result["result"]["areacode"] == "0571"