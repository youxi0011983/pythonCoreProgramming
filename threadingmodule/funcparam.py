# def check(func):
#     print("正在检测权限")
#     func()
#
#
# def get_name():
#     print("get_name_func")
#
#
# def main():
#     check(get_name)
#
#
# if __name__ == '__main__':
#     main()

# class CLanguage:
#     # 定义__call__方法
#     def __call__(self, name, add):
#         print("调用__call__()方法", name, add)
#
#
# clangs = CLanguage()
# clangs("C语言中文网", "http://c.biancheng.net")
# from past.builtins import apply


# def function(a, b):
#     print(a, b)
#
#
# apply(function, ('good', 'better'))
# apply(function, (2, 3 + 6))
# apply(function, ('cai', 'quan'))
# apply(function, ('cai',), {'b': 'caiquan'})
# apply(function, (), {'a': 'caiquan', 'b': 'Tom'})

# from socket import *
# import sys
# from threading import Thread, Lock
#
#
# class mythread(Thread):
#     def __init__(self, func, args):
#         Thread.__init__(self)
#         self.func = func
#         self.args = args
#
#     def run(self):
#         self.func(*self.args)
#
#     def test(self, args):
#         print('right', args)
#
#
# p = mythread(test, "my")
# p.run()


import threading

from time import ctime, sleep


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        # apply(self.func, self.args)  # 用不了...
        self.func(*self.args)
        pass


def super_play(file, time):
    for i in range(2):
        print('开始运行： %s! %s' % (file, ctime()))
        sleep(time)


list = {'爱情买卖.mp3': 2, '雷神.mp4': 5}

threads = []

files = range(len(list))

for k, v in list.items():
    t = MyThread(super_play, (k, v), super_play.__name__)
    threads.append(t)

if __name__ == '__main__':

    for i in files:
        threads[i].start()

    for i in files:
        threads[i].join()

    print('结束 %s' % ctime())
