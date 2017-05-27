# coding=utf8
import itchat
from itchat.content import *


@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    rooms = itchat.get_chatrooms()
    for room in rooms:
        if (room['NickName'] == 'Family.DuoGe'):
            groupDuoge = room['UserName']

        if (room['NickName'] == '微信群机器人测试'):
            groupTest = room['UserName']


    if msg['FromUserName'] == groupDuoge:
        if msg['isAt']:
            itchat.send("喂喂喂 为所欲为 @%s" % msg['ActualNickName'] , groupDuoge)

    if msg['FromUserName'] == groupTest:
        if msg['isAt']:
            itchat.send("@%s %s" % (msg['ActualNickName'],msg['ActualNickName'][:3]), groupTest)


itchat.auto_login(True)
itchat.run()
