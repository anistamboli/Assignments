start=int(input("Enter Starting Number : "))
end=int(input("Enter Ending Number : "))
for i in range(start,end+1):
    sum=0
    for j in range(1,(i//2)+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
