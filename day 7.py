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