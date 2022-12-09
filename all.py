# #!/usr/bin/env python
# # _*_ coding:utf-8 _*_

import pytest
import os, time

if __name__ == '__main__':
    pytest.main()
    time.sleep(1)
    os.system('allure generate ./temp -o ./report --clean')