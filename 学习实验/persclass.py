# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 15:43
# @FileName: persclass.py
# @Author  : CNTian
# @GitHub  ：https://github.com/CNPolaris
# @Email   : 1875091912@qq.com
class Person :
    weight = 0.0
    height = 0.0
    def __init__(self):
        self.weight=0.0
        self.height=0.0
        #self._weight=0.0
        #self._height=0.0
    def __init__(self,weight,height):
        self.height=height/100
        self.weight=weight
        #self._height=height/100
        #self._weight=weight
    def calculateBmi1(self):
        bmi=self.weight/pow(self.height,2)
        return bmi
    def judge(self,bmi):
        if bmi>=18.5 and bmi<=25:
            print("这个人的体重正常")
        else:
            print("体重不正常")
    @staticmethod
    def static_calculateBmi():
        return
    @staticmethod
    def static_judge():
        return 
    @classmethod
    def cls_calculateBmi(cls):
        return cls.weight/pow(cls.height,2)
    @classmethod
    def cls_judge(cls,bmi):
        if bmi >= 18.5 and bmi <= 25:
            print("这个人的体重正常")
        else:
            print("体重不正常")



if __name__=='__main__':
    test=Person(100,180)
    bmi=test.calculateBmi1()
    print("这个人的BMI指数是 {:.2f}".format(bmi))
    test.judge(bmi)



