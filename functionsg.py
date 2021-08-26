import calendar
def display_calender(year,month):
    print(calendar.month(year,month))
a = display_calender(1992,11)



# ax^2+bx+c=0
a =2       #int(input("Enter num_1: "))
b = 4       #int(input("Enter num_2: "))
c =  5       #int(input("Enter num_3: "))

print("Quadratic Equation is: {}x^2+{}x+{}=0".format(a,b,c))

if a==0:
    print("a should not be equal to Zero")
else:
    r = b**2 - 4*a*c
    x1 = (((-b) + r**0.5)/(2*a))
    x2 = (((-b) - r**0.5)/(2*a))
    print("Two possible values of our quadratic equation are {} and {}".format(x1,x2))

def check_num(num):
    if type(num)==int or type(num)==float :
        if num > 0:
            print("{} is a postive integer".format(num))
        elif num < 0:
            print("{} is a negative integer".format(num))
        else:
            print("It is zero")
    else:
        print("not a number")
check_num(0)

def oddeven(nuu):
    if nuu==0:
        print("enter non zero")
    elif nuu % 2==0:
        print("Even no")
    else:
        print("odd")
oddeven(90)

def leap(year):
    if year%400==0:
        print("leap year")
    elif year%4==0 and year%100 !=0:
        print("leap year")
    else:
        print("not leap year")

leap(1992)
leap(2400)
leap(1700)
leap(1993)

def prime_no(num2):
    if num2 ==1:
        print("enter otr no")
    elif num2==2:
        print("prime no")
    else:
        for i in range(1,num2):
            if num2 % i ==0:
                print("not prime")
                break
        else:
              print("prime no")

prime_no(67)

for i in range(1,10):
    for num in range(2,i):
        if  i% num==0:
            break
    else:
        print(i)
def facto(a):
    factorial=1
    if a<0:
        print("Enter positive integer.")
    elif a==0:
        print("Factorial=1")
    else:
        for i in range(1,a+1):
            factorial=factorial*i
        print("Factorial of {} is {}".format(a,factorial))

facto(9)

def table(b):
    for i in range(1,11):
        product=b*i
        print("{} X {} = {}".format(b,i,product))

table(6)

#n = int(input("Enter the length :"))
n=4
a=0
b=1
sum=0
count=1
print("Fibbonacci series:",end=" ")
while (count<=n):
    print(sum,end=" ")
    count +=1
    a = b
    b = sum
    sum = a + b

print("\n")
#a=input("Enter the number :")
a='1634'
b=len(a)
d=int(a)
c=int(a)
sum1=0
while c > 0:
    e= c%10
    c= c//10
    sum1 = sum1 + e**b
if d == sum1:
    print(f'{d} is a Armstrong no')
else:
    print(f'{d} is not a Armstrong no'


          