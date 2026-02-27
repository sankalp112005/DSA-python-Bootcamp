#WHILE LOOP QUESTIONS
#1.SEPAERATE EACH DIGIT OF NUMBER AND PRINT IT ON SEPARATE LINE
'''a=int(input('Enter the number'))
while a>0:
    print (a%10)
    a=a//10 

#2.ACCEPT A NUM AND PRUINT ITS REVERSE
a=int(input('Enter the number'))
rev=0
while a>0:
    rev=rev*10 + a%10
    a=a//10
print(rev)

#3.CHECK PALINDROME BY WHILE LOOP
a=int(input('Enter the number'))
copy=a       #we create copy of a bcoz we are destroying a in coming lines
rev=0
while a>0:
    rev=rev*10 + a%10
    a=a//10
if copy==rev:
    print('it is palindrome')
else:
    print('not palindrome')'''

#4.RANDOM NUMBER GUESSING GAME BY PYHTON