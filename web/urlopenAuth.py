#!/usr/bin/python
# -*- coding:UTF-8 -*-

import urllib.request, urllib.error

LOGIN = 'wesc'
PASSWD = "you'll NeverGuess"
# URL = 'http://localhost'
URL = 'http://www.baidu.com'


def handler_version(url):
    from urllib.parse import urlparse as up
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password('Archives', up(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)
    return url


def request_version(url):
    from base64 import b64encode
    req = urllib.request.Request(url)
    req.add_header("Authorization", "Basic %s" % req)
    return req


for funcType in ('request', 'handler'):
    print('*** using %s:' % funcType.upper())
    url = eval('%s_version' % funcType)(URL)
    f = urllib.request.urlopen(url)
    print(f.readline())
    f.close()
