#coding=GBK
print('10-30之间的素数是： ')
for num in range(10,31):
    for i in range(2,num):
        if num%i == 0:
            break
        else:
            print(num)
