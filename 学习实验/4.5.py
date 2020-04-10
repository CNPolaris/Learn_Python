# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 14:19
# @FileName: 4.5.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import random, string


def creatCard():
    cardNum = []
    head = '6102009'
    cardCount = input("请确认有多少张银行卡：")

    for i in range(1, eval(cardCount) + 1):
        tail = ("%03d" % i)
        cardNum.append(''.join([head, tail]))

    return cardNum


def gen_Key():
    passwds = []  # 保存符合要求的密码
    count = input('请确认要生成几条密码： ')
    i = 0  # 记录符合要求的密码个数
    while i < int(count):
        passwd = set(random.sample(string.ascii_letters + string.digits, 8))  # 从字母和数字中随机抽取8位生成密码
        if passwd.intersection(string.ascii_uppercase) and passwd.intersection(
                string.ascii_lowercase) and passwd.intersection(string.digits):  # 判断密码中是否包含大小写字母和数字
            passwds.append(''.join(passwd))  # 将集合转化为字符串
            i += 1  # 每生成1个符合要求的密码，i加1
    return passwds


def bankInfo(card, password):
    bankCard = {}
    cardCount = len(card)
    passwordCount=len(password)
    for i in range(cardCount):
        bankCard[card[i]] = password[random.randint(0,passwordCount-1)]
    lastBankCard=tuple(bankCard.items())
    for i in range(cardCount):
        print("银行卡号：{0} 密码：{1}".format(lastBankCard[i][0],lastBankCard[i][1]))

if __name__ == '__main__':
    bankInfo(creatCard(), gen_Key())
