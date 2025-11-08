number=int(input("Enter the number :"))
factorial=1
if number<0:
    print("factorial does not exist for negative number ")
elif number==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,number+1):
      factorial*=i
print(f"the factorial of {number} is {factorial} ")

