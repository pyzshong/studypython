#coding=GBK
print('10-30֮��������ǣ� ')
for num in range(10,31):
    for i in range(2,num):
        if num%i == 0:
            break
        else:
            print(num)
