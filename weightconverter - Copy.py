weight = float(input("weight : "))
unit = str(input("(L)bs or (k)g :"))
if unit =="k" :
    print(f"you are {weight*0.45}kg")
else:
    print(f"you are{weight/0.45} kg")
    