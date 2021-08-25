s1='hello world!'
s2="hello wprld!"
s3="""hello 
world!"""
s4='''hello     
my world'''
#三个单引号或双引号可以折行
print(s1,s2,s3,s4,end='')
s1='\'hello world\''
s2='\n\\hello world\\\n'#\n换行\输出这两个斜杠之间的数值\
print(s1,s2,end='')
s1='\141\142\143\x61\x62\x63'
s2='\u9a86\u660a'
print(s1,s2,end='')
s1=r'\'hello word\''
s2=r'\n\\hello world\\\n'
print(s1,s2,end='')#加r不让其转义
#+字符串的拼接，*字符串的重复，in notin字符串包含关系[]提取字符[:]切片计算
s1='hello'*3
print(s1)
s2='world'
print(s1+s2)

str2='abc123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])

str1='hello, world!'
print(len(str1))
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.find('or'))
print(str1.find('shit'))
print(str1.index('or'))
print(str1.startswith('He'))
print(str1.startswith('hel'))
print(str1.endswith('!'))
print(str1.endswith('world'))
print(str1.center(50,'*'))
print(str1.center(80,'*'))
print(str1.rjust(50,' '))
print(str1.ljust(50,'8'))
str2='abc123456'
print(str2.isdigit())
print(str2.isalpha())
print(str2.isalnum())
str3='    liuqitao@nimte.ac.cn  '
print(str3)
print(str3.strip())

a,b=5,10
print('%d*%d=%d'%(a,b,a*b))
print('{0}*{1}={2}'.format(a,b,a*b))
print(f'{a}*{b}={a*b}')
'''
列表
'''
list1=[1,3,5,7,100]
print(list1)
list2=['hello']*3
print(list2)
print(list1[2])
print(len(list1))
print(list1[0])
print(list1[4])
list1[2]=1000
print(list1)
for index in range(len(list1)):#遍历列表
    print(list1[index])
for enlem in list1:
    print(enlem)
for index,enlem in enumerate(list1):
    print(index,enlem)
#添加与移除
list1=[1,3,5,7,100]
list1.append(200)#后边添加一位
list1.insert(1,400)#插入
list1+=[1000,2000]
print(list1)
print(len(list1))
if 3 in list1:
    list1.remove(3)
    print(list1)
#移除
list1.pop(0)#从index=0处移除
print(list1)
list1.pop(len(list1)-1)#从index最后移除
print(list1)
list1.clear()#清除
print(list1)
'''
列表的切片
'''
fruits=['grape','apple','strawberry','waxberry']
fruits+=['pitaya','pear','mango']
print(fruits)
print(fruits[1:4])
print(fruits[3])
print(fruits[-3:-1])
print(fruits[::-1])
'''
分类
'''
list1=['origin','apple','zoo','internationalization','blueberry']
list2=sorted(list1)
list3=sorted(list1,reverse=True)
list4=sorted(list1,key=len)
print(list1)
print(list2)
print(list3)
print(list4)
list1.sort(reverse=True)
print(list1)
'''
生成式和生成器
'''
f=[x for x in range(100)]
print(f)
f=[x+y for x in 'ABCD' for y in '123456']
print(f)
f=[x**2 for x in range(1,1000)]
print(f)
for val in f:
    print(f)
'''
斐波拉切数列
'''
def fib(n):
    a=0
    b=1#a,b=0,1
    for _ in range(n):
        a,b=b,a+b
        yield a
def main():
    for val in fib(20):
        print(val)
if __name__=='__main__':
    main()
'''
元组
'''
#元组的元素不能更改
t=('骆昊',38,True,'四川成都')
print(t)
print(t[0])
print(t[3])
for number in t:#in t 表示等于其中代表的元素
    print(number)
for val in t:
    print(val)
t=('王大锤',20,True,'云南昆明')
print(t)
person=list(t)#元组转换成列表，列表可进行编辑
print(person)
person[0]='李小龙'
person[3]='中国'
print(person)
#列表转元组
fruits_list=['apple','orange','banana']
fruits_tuple=tuple(fruits_list)#类似元组转列表list(tuple),列表转元组为tuple(list)
print(fruits_tuple)
print(fruits_tuple[0])
print(fruits_tuple[2])
f=[1,2,3,4,5]
f_tuple=tuple(f)
print(f_tuple[2])
print(f_tuple)
b=(1,2,3,4,5)
b_list=list(b)
print(b_list[0])
print(b_list)

'''
集合
'''
set1={1,2,3,4,5,6,7}
print(set1)
print('length=',len(set1))
set2=set(range(1,10))
set3=set((1,2,3,2,2,1))#两个括号
print(set2,set3)
set4={num for num in range(1,100) if num%3==0 and num%5==0}
print(set4)
set1.add(4)
print(set1)
set1.add(5)
print(set1)
set1.add(10)
print(set1)
set1.update((11,12))#
print(set1)
set1.add((11,12,13))
set1.update((11,12,13))
print(set1)
set1.discard(5)
print(set1)
if 4 in set1:
    set1.remove(4)
    print(set1)
print(set1.pop())
print(set1)
set1={1,2,3,4,5}
set2={3,4,5,6,7}
set3={4,5}
print(set1&set2)#交集
print(set1|set2)#并集
print(set1-set2)#差集
print(set1^set2)#子集和超集
print(set2<=set1)
print(set1<=set2)
print(set3<=set1)
print(set2>=set3)
'''
字典
'''
#键值对
scores={'骆昊':95,'百元房':78,'狄仁杰':82}
print(scores)
item1=dict(one=1,two=2,three=3,four=4)
item2=dict(zip(['a','b','c'],'123')) #将两个序列压成字典
item3={num:num**2 for num in range(1,10)}
print(item1,item2,item3)
print(scores['骆昊'])
print(scores['狄仁杰'])
for key in scores:
    print(f'{key}:{scores[key]}')
scores['百元房']=92
scores['诸葛王明']=72
scores.update(冷面=67,放弃和=85)
print(scores)
if '武则天' in scores:
    print(scores['武则天'])
print(scores.get('武则天'))
print(scores.get('武则天',60))
print(scores.popitem())#popitem,从后往前减，与字符串和序列不同
print(scores.popitem())
print(scores)
print(scores.pop('骆昊',95))
print(scores)
scores.clear()
print(scores)
'''
练习
'''
'''
跑马灯
'''
import os
import time
def main():
    content='北京欢迎你为你开天辟地....'
    while True:
        print(content)
        time.sleep(1)
        content=content[1:]+content[0]
if __name__=='__main__':
    print(main())
'''
验证码
'''
import random
def generate_code(len_code=4):
    str='0123456789abcdefghigklmnopqistuvwxyzABCDEFGHIGKLMNOPQISTUVWXYZ'
    code=''
    for _ in range(len_code):
        index=random.randiant(len(str)-1)
        code+=str[index]
    return code
'''
函数后缀
'''
def get_suffix(filename,haadot=False):
    pose=filename.rfind('.')
    if 0<pose<len(filename):
        index=pose if hasdot else pose+1
        return filename[index:]
    else:
        return ''
'''
返回最大值和第二大值
'''
def max(2)(m1,m2):
    m1,m2=(x[0],x[1]) if x[0]>x[1] else(x[1],x[0])
    for index in range(len(x)-1):
        if x[index]>m1:
            m2=m1
            m1=x[index]
        elif x[index]>m2:
            m2=x[index]
    return m1,m2
'''
年月日
'''
def is leapyear(year):
    return year%4==0 and year%100!=0 or year%400==0
def which_day(year,month,day):
        days_of_month=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31][is leapyear(year)]]
        total=0
        for index in range(month-1):
            total+=days_of_month[index]
        return total
def main()
    print(which_day(1997,8,24))
    print(which_day(1765,12,12))
if __name__=='__main__':
   print(main())
