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