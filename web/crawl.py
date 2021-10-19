#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
# from string import replace,find.lower # 已经出厂内置
# from HTMLParser import HTMLParser
from html.parser import HTMLParser
from urllib.request import urlretrieve
from urllib.parse import urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from io import StringIO as stringIO


class Retriever(object):  # download web pages
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile='index.htm'):
        parsedurl = urlparse(url, 'http:', 0)  ## parse path
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '':  # no file, use default
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path)  # local directory
        if sep != '/':  # os-indep. path separator
            ldir = ldir.replace('/', sep)
        if not isdir(ldir):  # create archive dir if nec.
            if exists(ldir): unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):  # download web page
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = ('*** ERROR: invalid URL "%s"' % self.url,)
            return retval

    def parseAndGetLinks(self):  # parse HTML, save links
        self.parser = HTMLParser(AbstractFormatter(DumbWriter(stringIO())))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


class Crawler(object):  # manage entire crawling process
    count = 0  # static downloaded page counter

    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        print('retval=', retval)
        if retval[0] == '*':  # error situation,do not parse
            print(retval)
            return
        Crawler.count += 1
        print('\n(', Crawler.count, ')')
        print('URL:', url)
        print('FILE:', retval[0])
        self.seen.append(url)

        links = r.parseAndGetLinks()
        for eachLink in links:
            if eachLink[:4] != 'http' and eachLink.find('://') == -1:
                eachLink = urljoin(url, eachLink)
            print('* ', eachLink, )

            if eachLink.lower().find('mailto: ') != -1:
                print('... discarded,mailto link')
                continue

            if eachLink not in self.seen:
                if eachLink.find(self.dom) == -1:
                    print('...discarded,not in domain')
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print('...new,added to Q')
                    else:
                        print('...discarded,already processed')
            else:
                print('...discarded,already processed')

    def go(self):
        while self.q:
            url = self.q.pop()
            self.getPage(url)


def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = input('Enter staring URL: ')
        except (KeyboardInterrupt, EOFError) as e:
            url = ''
        if not url: return
        robot = Crawler(url)
        robot.go()


if __name__ == '__main__':
    main()
