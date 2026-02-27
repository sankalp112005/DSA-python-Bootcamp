#1. PRINTING N TIME THE SENTENCE
n=int(input('Enter the time you want to print the sentence'))
for i in range(n):
    print("hii sankalp!!")

#2. PRINT NTURAL NUMBERS UPTO N
a=int(input('tell your number upto you want'))
for i in range(1,a+1):
    print (i)

#3.REVERSE FOR LOOP.print n to 1
n=int(input("enter the number"))
for i in range(n,0,-1):        #we need to give steps also(-1)
    print(i)

#4.PRINTING TABLE
n=int(input('enter the no.you want to print table: '))
for i in range(1,11):
    print (f"{n} * {i} = {n*i}")         #FORMATED STRING-WE CAN USE VARIABLE IN BETWEEN TEXT

#5.SUM UPTO N TERMS
n=int(input('enter the no. upto you want  to add: '))
sum = 0
for i in range(1,n+1):
    sum=sum+i
print(f"the sum of number is {sum}")

#6.FACTORIAL OF N NUMBER
n=int(input('enter the no: '))
fac = 1                          #factorial strart with 1*2*3*4.....
for i in range(1,n+1):
    fac *= i
print(f"factorial of {n} is {fac}")

#7.PRINT THE SUM OF ALL EVEN & ODD NUMBER USING RANGE SEPARATELY
n=int(input('enter the no: '))
even=0
odd=0
for i in range(1,n+1):
    if n%2==0:
        even += i
    else:
        odd += i
print(f"{even},{odd}") 

#8.PRINT ALL THE FACTORS OF THE NUMBER
n=int(input('enter the no.: '))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#9.CHECK IF IT IS PERFECT NO. OR NOT
#no whose sum of factors is equal to number itself.
n=int(input('checking the number is perfect or not:  '))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print('the nummber is perfect')
else:
    print('it is not perfect')

#10.CHECK PRIME OR NOT
n=int(input('enter the no.: '))
count=0
for i in range(1,n+1):
    if n%i==0:
        count =count+1
if count==2:
    print('no is prime')
else:
    print('no is not prime')
      
#11.REVERSE THE STRING
str=input('give the string: ')
newstr=""
for i in range(len(str)-1,-1,-1):
    newstr=newstr+str[i]
print(newstr)

#12.PALINDROME STRING CHECK
str=input('give the string: ')
newstr=""
for i in range(len(str)-1,-1,-1):
    newstr=newstr+str[i]
if str==newstr:
    print('string is palindrome')
else:
    print('string is not palindrome')

#13.COUNTING ALL DIGIT,CHAR,SPECIAL SYMBOL IN A GIVEN sring
a="Ajdjnwy^@#*dhkj51545"
digit=0
alpha=0
schar=0
for i in a:
    if i.isdigit():        #method to check digit in string
        digit+=1
    elif i.isalpha():      #method to check alphabet in string
        alpha+=1
    else:
        schar+=1
print(f" your digits are{digit}\n character are {alpha}\n special character are{schar}\n") 
    

