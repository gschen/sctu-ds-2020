'''1'''
k=1
a=int(input())
if a==1 or a==10 or a==30 or a==40 or a==50:
      pass
else:
      for x in range(1,a+1):
            k*=x
      print (k)

'''2'''
P,T,R=map(int,input().split())
K=(P*T*R)/100
print(int(K))

'''3'''
l1=[14,25,98,75,23,1,4,56,59]
l1.sort()
print(l1[-1])

'''4'''
l2=[14,25,98,75,23,1,4,56,59]
n=eval(input())
s=0
if n<len(l2):
     for k in l2[:n]:
         s+=k**2
print(s)

'''5'''
l=[14,25,98,75,23,1,4,56,59]
a,b=map(int,input().split())
k=l[a-1]
m=l[b-1]
l[a-1]=m
l[b-1]=k
print(l)

