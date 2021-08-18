'''
1+100
'''
sum = 0
for x in range(101):
    sum += x
    print(sum)
    '''
    range(101)
    range(1, 101)
    range(1, 101, 2)
    range(100, 0, -2)
    '''
'''
100—1之间偶数和
'''
sum = 0
for x in range(100, 0, -2):
    sum += x
    print(sum)
#另一种方法，把语句加进去
sum=0
for x in range(100,0):
    if x%2==0:
       sum+=x
    print(sum)
'''
猜随机数
'''
import random
answer=random.randint(1,100)
count=0
while True:
    count+=1
    x=int(input('请输入1-100内的整数：'))
    if x<answer:
        print('大一点')
    elif x>answer:
        print('小一点')
    else:
        print ('恭喜你！你答对啦')
        break
print('你猜对共用了%d次'%count)
if count<=7:
    print('聪明')
else:
    print('大笨蛋')
'''
9*9乘法口诀
'''
for y in range(1,10):
   for x in range (1,y+1):
      print('%.2f*%.2f=%.2f'%(x,y,x*y),end='\t')#不换行
   print()#下行print换行
'''
判断是不是素数
'''
from math import sqrt
num=int(input('请输入一个整数'))
end=int(sqrt(num))
is_prime=True
for x in range(2,end+1):
    if num%x==0:
        is_prime=False
        break
if is_prime and num!=1:
    print('%d是素数'%num)
else:
    print('%d不是素数'%num)
#另一种写法
from math import sqrt
num=int(input('请输入一个整数：'))
end=int(sqrt(num))
for x in range(2,end+1):
    if num%x==0:
        print('%d不是素数'%num)
        break
if num%x!=0 and num!=1:
    print('%d是素数'%num)



'''
最大公约数和最小公倍数
'''
x=int(input('请输入第一个整数:'))
y=int(input('请输入第二个整数:'))
if x>y:
  x,y=y,x
for factor in range(x,1,-1):
   if x%factor==0 and y%factor==0:
    print('%d和%d最大公约数为%d'%(x,y,factor))
    print('%d和%d最小公倍数%d'%(x,y,x*y//factor))
    break
'''
输出三角形
'''
row=int(input('请输入行数：'))
for i in range(0,row):
    for j in range(0,i+1):
        print('*',end='')
    print()
#右下角50
row=int(input('请输入行数：'))
for i in range(row):
    for j in range(row):
        if j<row-i-1:
          print(' ',end='')
        else:
          print('*',end='')
    print()
#三角
row=int(input('请输入行数：'))
for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()



