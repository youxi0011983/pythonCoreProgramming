#!/usr/bin/python
# -*- coding:UTF-8 -*-

import string
import keyword

alphas = string.ascii_letters + '_'
nums = string.digits
key = keyword.kwlist

# print(type(nums))
# print(type(key))


if __name__ == '__main__':
    print("Welcome to the Identifier checker v1.0")
    print("Testes must be at least 2 chars long.")

    myInput = input("Identifier to test?")

    if len(myInput) > 1:
        if myInput[0] not in alphas:
            print('''invalid: first symbol must be alphabetic''')
        else:
            for otherChar in myInput[1:]:
                if otherChar not in alphas + nums:
                    print('''invalid: remaining symbols must be alphament''')
                    break
            # else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行
            else:
                print('okay as an identifier')