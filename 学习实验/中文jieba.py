# -*- coding: utf-8 -*-
# @Time    : 2020/4/3 15:43
# @FileName: 中文jieba.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
import jieba as j
import collections
txt=open('中文测试文本.txt','r',encoding = 'utf-8').read()
words=j.lcut(txt)
print(words)

res=collections.Counter(words)
#text=words.split
print(res.items())
counts={}#出现词语和次数作为键值对的字典，初始化为空
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
ls=list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(5):
    print(ls[i])
counts={}
for w in words:
    if len(w)==0:
        continue
    else:
        counts[w]=counts.get(w,0)+1
