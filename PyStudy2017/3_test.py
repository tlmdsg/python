#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author:tlm
from __future__ import print_function
import os.path

try:
    import json
except ImportError:
    import simplejson as json


def demo():
    # 导入模块
    print(os.path.isdir(r'C:\Windows'))
    print(os.path.isfile(r'C:\Windows\notepad.exe'))

    print(json.dumps({'python': 2.7}))


if __name__ == '__main__':
    demo()
