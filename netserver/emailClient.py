#!/usr/bin/python
# -*- coding:UTF-8 -*-

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTRSVR = 'smtp.python.is.cool'
POP3SVR = 'pop.python.is.cool'

origHdrs = ['From:wesley @python.is.cool', 'to:wesley@python.is.cool', 'Subject:test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join((['\r\n'.join(origHdrs), '\r\n'.join(origBody)]))

sendSvr = SMTP(SMTRSVR)
errs = sendSvr.sendmail('wesley@pyhon.is.cool', ('wesley@python.is.cool',), origMsg)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('wesley')
recvSvr.pass_('youllNeveGuess')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep + 1:]
assert origBody == recvBody
