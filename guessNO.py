#coding=GBK
import random
secret=random.randint(1,100)#���������
#print(secret)
time=6#�����ֵĴ���
guess=0#���������
minnum=0#��С�����
maxnum=100#��������
print("----------------------��ӭ���������ֵĵط����뿪ʼ-------------------")
while guess!=secret and time>=0:
    guess=int(input("*��������0~100��������������֣�"))
    print("������������ǣ� ",guess)
    if guess==secret:
        print("�¶��ˣ�����������")
    elif guess<secret:
        minnum=guess
        print("��Ĳ���С����ȷ��")
        print("���ڵ����������ǣ�",minnum,"-",maxnum)
        print("̫�ź��ˣ���´��ˡ��㻹��",time,"�λ���")
    else:
        maxnum=guess
        print("��Ĳ���������ȷ��")
        print("���������ǣ�",minnum,"-",maxnum)
        print("̫�ź��ˣ���´��ˡ��㻹��",time,"�λ���")
    time-=1
print("��Ϸ����")
