num=int(input("enter the number :"))
a,b=0,1
count=0
print("fibonacci series")
while count<num:
    print(a)
    next_term=a+b
    a=b
    b=next_term
    count+=1


   
