#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json
import nntplib
import re
import socket

HOST = 'news.newsfan.net'
GRNM = 'alt.language.English'
# GRNM = '\udcc1\udcc4\udccc\udcec\udcb9\udce0ˮ.\udcc7\udce9\udcb8\udcd0'
# GRNM = GRNM.encode('utf-8', 'replace').decode('utf-8')
USER = 'wesley'
PASS = "you'll NeverGuess"


def main():
    try:
        n = nntplib.NNTP(HOST)
        # print(n.getwelcome())
        # groupLists = n.list()
        # for groupList in groupLists[1]:
        #     print(str(groupList))
        # user = USER,password=PASS
    except socket.gaierror as e:
        print('ERROR: cannot reach host "%s"' % HOST)
        print('  ("%s")' % eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR: access denied on "%s"' % HOST)
        print('  ("%s")' % str(e))
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: cannot load group "%s"' % GRNM)
        print('  ("%s")' % str(e))
        print('  Server may require authentication')
        print('  Uncomment/edit login line above')
        n.quit()
        return
    print('*** Found newgroup "%s"' % GRNM)

    rng = '%s-%s' % (lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print('''*** Found last article (#%s):
    
    From: %s
    Subject: %s
    Date: %s
''' % (lst, frm[0][1], sub[0][1], dat[0][1]))

    rsp, (anum, mid, data) = n.body(lst)
    # rsp, data = n.body(lst)
    # for line in data:
    #     print("\n",line)
    displayFirst20(data)
    n.quit()


def displayFirst20(data):
    print('*** First (<=20) meaningful lines:\n')
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True

    for line in lines:
        if line:
            lower = line.lower()
            if ((lower.startswith(b'>') and not lower.startswith(b'>>>')) or lower.startswith(
                    b'|') or lower.startswith(
                b'in article') or lower.endswith(b'writes: ') or lower.endswith(b'wrote: ')):
                continue
        if not lastBlank or (lastBlank and line):
            print('  %s' % line)
            if line:
                count += 1
                lastBlank = False
            else:
                lastBlank = True
        if count == 20:
            break


if __name__ == '__main__':
    main()
