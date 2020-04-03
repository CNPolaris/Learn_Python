# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 15:24
# @FileName: 英文ieba.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import collections
def getText():
    fo=open('Hamlet.txt','r')
    txt=fo.read()
    txt=txt.lower()
    for ch in ',.?':
        txt=txt.replace(ch,' ')
    print(txt)
    return txt
hamletTxt=getText()
words=hamletTxt.split()
count={}#单词和出现次数为键值对的字典
for word in words:
    count[word]=count.get(word,0)
    count[word]=count[word]+1
# for word in excludes:
#     del(count[word])
print(collections.Counter(words))
items=list(count.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items)
