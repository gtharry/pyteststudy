# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_
import allure

@allure.feature("自定义allure报告")
class Testdo:
    @allure.title("用例1")
    def test_01(self):
        print("你好：")

    @allure.title("用例2")
    def test_02(self):
        print("你好呀：")