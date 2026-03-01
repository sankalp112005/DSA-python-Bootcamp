'''Funtions are reusable code in block that can be rused by calling its name.
it rreducese redundancy and avoid repitiaion.
*built in functions are print(), len(),input()
*we can create your own function by using 'def' keyword and functiin name
*we can call that user defined function by using name nd parathesis()'''

def hello():
    print('hi sankalp')
hello()       #calling function

#PARAMETER AND ARGUMENT
'''Parameter are variables listed inside the function deifntion//The thing you accept is parameter.  (FORMAL PARAMETER)
ARGUMENT :the thing you provide to parameter. / its given at the time of calling the fucction.       (ACTUAL PARAMETERS)'''

def sum(a,b=6):             #a,b are parameter     #b=6 default argument.
    print(f'the sum of a & b is {a+b}')

sum(5,5)            # 5,5 are positional argument
sum(20)             #if one argument is no passed defualt value is selcted .

#Default argument--if you dont pass any value function will run
#Keyword argument--values are passed in any otrder by using the key value

def school(name , age):
    print (f'the name is {name },the age is {age}')
school(age=21,name ='sankalp')         #KEYWORD ARGUMENT

#using fucntion to check the srting is pallindrome or not
def pallindrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev =rev+st[i]
    if rev== st:
        print(f'string {st} is pallindrome')
    else:
        print(f'{st} is not pallindrome')
pallindrome ("NAMAN")
pallindrome("SANKALP")