import time
def rand_val(x,y):
   sub=y-x
   random=int(time.time()*1000)
   random %=sub
   random+=x
   return random

x=int(input("Start Range: "))
y=int(input("End Range: "))

print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
print(rand_val(x,y))
