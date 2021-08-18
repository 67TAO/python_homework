'''
寻找水仙花数
'''
for x in range(100,1000):
    low=x%10
    mid=x//10%10
    high=x//100
    if x==low**3+mid**3+high**3:
        print(x)
'''
正整数的反转
'''
num=int(input('请输入正整数：'))
reversed_num=0
while num>0:
    reversed_num=reversed_num*10+num%10
    num//=10
    print(reversed_num)
'''
百鸡百钱
'''
for a in range(20):
    for b in range(33):
        z=100-a-b
        if 100==5*a+3*b+z/3:
            print('公鸡%d,母鸡%d,小鸡%d'%(a,b,z))
'''
赌博游戏
'''
from random import randint
money=1000
while money>0:
    print('余额：%d'%money)
    needs_go_on=False
    debt=int(input('请下注：'))
    while True:
        0<debt<money
        break
    first=randint(1,6)+randint(1,6)
    print(first)
    if first==7 or first==11:
        print('玩家胜')
        money+=debt
    elif first==2 or first==5 or first==11:
        print('庄家胜')
        money-=debt
    else:
        needs_go_on=True
    while needs_go_on:
        needs_go_on=False
        second=randint(1,6)+randint(1,6)
        print(second)
        if second==7:
          print('庄家胜')
          money-=debt
        elif second==first:
            print('玩家胜')
            money+=debt
        else:
            needs_go_on=True
print('你已经破产')
'''
斐波那契数
'''
a=1
b=1
count=2
while True:
    c=a+b
    a=b
    b=c
    count+=1
    if count==20:
        print(c)
'''
完美数
'''
for num in range(1,10000):
    sum=0
    for x in range(1,10000):
        if num%x==0 and num!=x:
            sum+=x
    if sum==num:
        print(num)

'''
100内素数
'''
from math import sqrt
for num in range(100):
    end=int(sqrt(num))
    for x in range(2,end+1):
        if num%end==0:
            break
    if num%x!=0 and num!=1:
        print(num)