import pytest


# 单次循环
@pytest.mark.parametrize("name", ["李白", "鲁迅"])
def test_parametrize_01(name):
    print("我是" + name)


# 多次循环
@pytest.mark.parametrize("name,word", [("李白", "大河之水天上来"), ("鲁迅", "不在沉默中爆发，就在沉默中灭亡")])
def test_parametrize_02(name, word):
    print(f'{name}的名言是{word}')
