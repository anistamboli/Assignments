l=[0,0,0,0,0,0,0,0,0,0]
n=int(input("Enter Number : "))
while(n>0):
    a=n%10
    l[a]+=1
    n//=10
for i in range(len(l)):
    if(l[i]!=0):
        print(i," : ",l[i])
