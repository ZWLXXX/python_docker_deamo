#!/usr/bin/env python
import urllib

print('Hello World!!!')

paramMap = {
    'paramMap.uname': '15361858980',
    'paramMap.pwd': 'ZWL119998',
    'paramMap.pageId': 'login',
    'paramMap.stat': '1',
    'paramMap.isCode': 'none',
    'paramMap.RandCode': ''
}

print(urllib.urlencode(paramMap))
