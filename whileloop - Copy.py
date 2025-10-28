#Conditional Statements
i=0
print("Conditional Statement")
x=10
if x>0:
    print("x is positive")
elif x==0:
    print("x is zero")
else:
    print("x is negative")

    i=0
    #loop-for
    print("\nFor Loop:")
    for i in range(5):
        print(f"Iteration {i}")

    #Loop-while
    print("\n While loop:")
    count=0
    while count<5:
        print(f"Count is {count}")
        count+=1
    i=1
    #Using berak in a loop
    print("\n Using berak in a loop:")
    for i in  range(10):
      if i==3:
       break
    print(f"Looping until break:{i}")



    #Using continue in a loop
print("\n Using continue in a loop:")
for i in range(5):
   if i==2:
      continue
   print(f"Looping with continue:{i}")
