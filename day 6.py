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