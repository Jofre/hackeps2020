i,a,b=10**5,0,0
while i>0:
 v,n=0,i
 while n>1:
  n=(3*n+1)//6**((n+1)%2);v+=1
 if v>a:a,b=v,i
 i-=1
print(b)
