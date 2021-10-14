#!/usr/bin/python
# -*- coding:UTF-8 -*-

dashes = '\n' + '-' * 50
exec_dict = {

    'f': """
for %s in %s:
    print(%s)
    """,
    's': """
%s = 0
%s = %s
while %s < len (%s):
    print(%s[%s])
    %s = %s + 1
""",
    'n': """#counting while loop
%s = %d
while %s < %d:
    print(%s)
    %s = %s + %d
"""
}


def main():
    ltype = input('Loop type? (For/While) ')
    dtype = input('Data type? (Number/Seq) ')

    if dtype == 'n':
        start = input('Starting value? ')
        stop = input('Ending value (non-inclusive)? ')
        step = input('Stepping value? ')
        seq = str(range(int(start), int(stop), int(step)))
        # var = input('Iterative variable name? ')
    else:
        seq = input('Enter sequence: ')
    var = input('Iterative variable name? ')

    if ltype == 'f':
        exec_str = exec_dict['f'] % (var, seq, var)
    elif ltype == 'w':
        if dtype == 's':
            svar = input('Enter sequence name? ')
            exec_str = exec_dict['s'] % (var, svar, seq, var, svar, svar, var, var, var)
        elif dtype == 'n':
            exec_str = exec_dict['n'] % (var, int(start), var, int(stop), var, var, var, int(step))

    print(dashes)
    print('Your custom-generated code:' + dashes)
    print(exec_str + dashes)
    print('Test execution of the code:' + dashes)
    exec(exec_str)
    print(dashes)


if __name__ == '__main__':
    main()
