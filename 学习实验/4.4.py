# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 20:05
# @FileName: 4.4.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
from collections import *
from jieba import *


def getTxt():
    txt = open('4.4的测试文档.txt', 'r', encoding='utf-8').read()
    #res = ['\n', ',', ':', ';', '!', '‘', '’', '；', ': ', '。', '\t', '.']
    res="\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\，。=？、：“”‘’￥……（）《》【】]"
    for ch in res:
        txt = txt.replace(ch, ' ')
    words = lcut(txt, cut_all=False)
    lastWords = []
    for word in words:
        if word != ' ':
            lastWords.append(word)
    return lastWords


ans = Counter(getTxt())

print(ans.most_common(10))
# print(ans)
