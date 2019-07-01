#coding=GBK
import random
secret=random.randint(1,100)#生成随机数
#print(secret)
time=6#猜数字的次数
guess=0#输入的数字
minnum=0#最小随机数
maxnum=100#最大随机数
print("----------------------欢迎来到猜数字的地方，请开始-------------------")
while guess!=secret and time>=0:
    guess=int(input("*数字区间0~100，请输入你的数字："))
    print("你输入的数字是： ",guess)
    if guess==secret:
        print("猜对了，你真厉害！")
    elif guess<secret:
        minnum=guess
        print("你的猜数小于正确答案")
        print("现在的数字区间是：",minnum,"-",maxnum)
        print("太遗憾了，你猜错了。你还有",time,"次机会")
    else:
        maxnum=guess
        print("你的猜数大于正确答案")
        print("数字区间是：",minnum,"-",maxnum)
        print("太遗憾了，你猜错了。你还有",time,"次机会")
    time-=1
print("游戏结束")
