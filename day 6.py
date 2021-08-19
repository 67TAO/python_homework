m=int(input('请输入m'))
n=int(input('请输入n'))
fm=1
for m in range(1,m+1):
    fm*=m
fn=1
for n in range(1,n+1):
    fn*=n
fmn=1
for mn in range(1,m-n+1):
    fmn*=mn
print(fm//fn//fmn)
'''
将重复封装在一个模块中，函数 def （自变量）return（因变量）
'''
def fac(num):
    result=1
    for num in range(1,num+1):
        result*=num
    return result
m=int(input('请输入m:'))
n=int(input('请输入n:'))
print(fac(m)//fac(n)//fac(m-n))
'''
重复！！！！省略重复
'''
'''
摇色子
'''
from random import randint
def roll_dice(n=2):
    total=0
    for n in range(n+1):
        total+=randint(1,6)
    return total
print(roll_dice())
print(roll_dice(3))
'''
a+b+c
'''
def add(a=0,b=0,c=0):
    return a+b+c
print(add())
print(add(1))
print(add(1,2))
'''
参数前的*代表可变c参数
'''
def add(*args):
    total=0
    for val in args:
        total+=val
    return total
print(add())
print(add(1,2))
'''
函数命名
'''
def foo():
    print('hello world')
def foo():
    print('goodbye world')
foo()
'''
调用模块
'''
'''
module 1.py
def foo():
    print('hello world')
module 2.py
def foo():
    print('goodbye world')
test.py
from module 1 import foo
foo()
from moudle 2.import foo
foo()
import moudle 1 as m1
import moudle 2 as m2
m1.foo()
m2.foo()
from moudle 1 import foo
from moudle 2 import foo
foo() 会被覆盖
若有代码执行，写条件if_name_=='_main_'
def foo():
pass
def foo():
pass
if _name_=='_main_'才会执行
print('call foo()')
foo()
只有直接执行才是main
'''
'''
作业1：最大公约数，最小公倍数
'''
def almost(x,y):
    (x,y)=(y,x) if x>y else(x,y)
    for factor in range(x,0,-1):
        x%factor==0 and y%factor==0
        return factor
def mult(x,y):
    return x*y//almost(x,y)
'''
作业2 回文数
'''
def is_palindrom(num):
    total=0
    while num>0:
        total=total*10+num%10
        num//=10
    return total==num
'''
作业3 素数
'''
def is_prime(num):
    for factor in range(2,int(num**0.5)+1):
        if num%factor==0:
            return False
    return True if num!=1 else False
'''
回文素数
'''
if __name__ =='__main__':
    num=int(input('请输入整数：'))
    if is_palindrom(num) and is_prime(num):
        print('%d是回文素数'%num)
'''
局部作用，嵌套作用，全局作用
'''
def foo():
    b='hello world'
    def bar():
        c=True
        print(a)
        print(b)
        print(c)
if __name__=='__main__':
    a=100
    foo()
'''
global关键词全局作用域，若全局没有a,则下一行代码定义变量a 并置于全局
局域作用域修改嵌套作用域的变量可以用nonlocal
'''
def main():
    #...闭包，局域作用域运行完还可以调用
    pass
if __name__=='__main__':
    main()