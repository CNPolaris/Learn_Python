# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 13:58
# @FileName: 爬虫测试.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com

from requests import *


# url=get("https://nj.lianjia.com/")
# print(url.status_code)
# print(url.encoding)
# print(url.text)
# 京东商品爬取，以及商品图
def spider_Jingdong():
    url = "https://item.jd.com/13490648144.html"
    src = "https://img14.360buyimg.com/n1/jfs/t1/54731/21/15301/89379/5dc4de4dE030916ad/7dda58f0b3158f75.jpg"
    path = "E://GitHub//Learn_Python//ws72.jpg"
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        spider = get(url, headers=kv)
        print(spider.status_code)
        print(spider.text)

        spider = get(src, headers=kv)
        f = open(path, 'wb')
        f.write(spider.content)
        f.close()
    except:
        print("爬取错误")

# 爬取亚马逊
def spider_Amazon():
    url = "https://www.amazon.cn/dp/B0754FT1M8/ref=sr_1_2?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&keywords=%E6%98%8E%E6%9C%9D%E9%82%A3%E4%BA%9B%E4%BA%8B&qid=1590136122&sr=8-2"
    kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    cookie = {'session-id': '459-4568418-5692641', 'ubid-acbcn': '459-5049899-3055220',
              'x-wl-uid': '1AK7YMFc9IzusayDn2fT6Topjz3iAOpR3EeA2UQSqco8fo5PbK2aCpyBA/fdPMfKFqZRHc4IeyuU=',
              'session-token': 'OH1wPvfOj6Tylq2nnJcdn5wyxycR/lqyGsGU3+lUtU4mbC0ZD9s8/4Oihd1BlskUQG8zRbLVs9vfWXuiJmnRlDT4x35ircp2uLxOLNYQ4j5pzdFJIqqoZUnhHSJUq2yK80P3LqH8An7faXRCPW9BIqX1wu0WmHlSS9vYAPKA/2SGdV9b//EljYjIVCBjOuR/dKRiYEeGK3li0RJOVz7+vMWg7Rnzbx89QxlbCp0WyquZyVxG6f2mNw=="',
              'session-id-time': '2082787201l'}
    try:
        # kv = {'User-Agent': 'Mozilla/5.0'}
        spider = get(url, headers=kv,timeout=30,cookies=cookie)
        spider.encoding='utf-8'
        print(spider.status_code)
        print(spider.headers)
        print(spider.apparent_encoding)
        print(spider.text)
    except:
        print("爬取失败")

# 爬取百度图片
def spider_Baidu():
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1590143728828&di=166a4111c2ceef61bf83e6249890e928&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farticle%2F16762011b86d324193e4876294b36d8a76aaa8a0.jpg"
    path = "E://GitHub//Learn_Python//qianxun.jpg"
    try:
        spider = get(url)
        f = open(path, 'wb')
        f.write(spider.content)
        f.close()
    except:
        print("爬取失败")

# ip地址查询
def spider_Ip():
    ip = "218.2.135.1"
    url = "http://www.882667.com/ip_{}.html".format(ip)
    print(url)
    try:
        kv = {'User-Agent': 'Mozilla/5.0'}
        spider = get(url, headers=kv)
        print(spider.status_code)
        spider.encoding = spider.apparent_encoding
        print(spider.text)
    except:
        print("爬取失败")

# 搜索引擎
def spider_Baidu_360():
    keyword="南京中医药大学"
    keyword2={'q':'南京中医药大学'}
    urlBaidu="http://www.baidu.com/s?wd="+keyword
    url360="http://www.so.com/s"
    try:
        kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        # print(spiderBaidu.url)
        spiderBaidu = get(urlBaidu,headers=kv)
        spiderBaidu.raise_for_status()
        spiderBaidu.encoding = 'utf-8'
        print(spiderBaidu.text)

        # spider360=get(url360,params=keyword2)
        # print(spider360.text)
    except:
        print("爬取失败")
if __name__ == '__main__':
    # spider_Jingdong()
    # spider_Amazon()
    # spider_Baidu()
    # spider_Ip()
     spider_Baidu_360()
