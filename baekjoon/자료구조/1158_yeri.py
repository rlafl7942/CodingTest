import sys

cnt=0

n, k = input().split()
n = int(n)
k = int(k)
array=[]
for i in range(n):
  array.append(i+1)

order=[]
j=k-1

while len(array)!=0:
  order.append(array[j])
  del array[j]
  j+=k-1
  if j>=len(array):
    while j-len(array)>=0 and len(array)>0:
      j-=len(array)
  


a="<"
cnt=0
for i in order:
  a=a+str(i)
  cnt+=1
  if cnt!=n:
    a=a+", "
a=a+">"
print(a)
