#arithmatic operators

#addition 
a = 5
b = 2
sum= a+b
print(sum)

#subration
subraction =a-b 
print(subraction)

#multiplication
multiply =a*b
print(multiply)

#division
divide =a/b
print(divide)

#remainder
remainder =a%b 
print(remainder)

#exponential (a^b)
power =a**b
print(power)

#realtional/comparison operator
a =50
b =20
print(a==b)#false
print(a !=b)#true
print(a>=b)#true
print(a>b)#true
print(a<=b)#false
print(a<b)#false

#assignment operators
num = 10
num =num +10
print("num :",num)

a = 10
a += 20
print("a :",a) #a(10)+a(20)=30
a /=20
print("a :", a)

#logical operator
#not operator
a = 50
b = 20
print( not False)
print(not (a < b))
print( (a >  b))
 #and operator
val1 = True
val2 = False
print("and operator :",val1 and val2)
#or operator
print("or operator :", val1 or val2)
print("or operator in expression form :",(a==b) or (a < b))
#example
has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

# type conversion 
a = 2
b = 4.25
sum = a+b
print(sum) 
print(type)
