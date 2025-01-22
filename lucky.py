i=int(input("enter number"))
l=0
p=0
while i>0:
    k=i%10
    if (k == 4 or k ==7):
      l +=1
    i=int(i/10)
    p=p+1
if(l==p):
   print("lucky")
else:
   print("not")


if (l ==4 or l == 7):
   print("nearly lucky")


