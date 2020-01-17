"""
xxx= 'bluue'
bluue = 'movie'
movie = xxx

print(xxx)
print(bluue)
print(movie)



var = '8.342  python is eassy'
print(var)


var = True
print (var)


lang = input(' fav prog languange ?: ')
print(lang, ' is ', 'fun', sep = '*', end = '!\n')



num = int(input("Enter you rnum: "))
print("You entered")
print(num, 's', 'a ' ,' cool number', sep=' *', end = '!\n') 


num = 3
print(num *( 8+ 4))

num =3
print(num * 8+4)



#a=10
b=5
c=4
d=3
e=2
f=6

a = b*c - d % e / f
a = (b*c) - ( ( d% e) / f)
print(a)



b=5
c=4
d=3
e=2
f=6
a = (d % f ) / ( (e ) - ( b*c))
print(a)


a =8
b=2
print('Addition : \t', a, '+', b, '=' , a+b )



print('Multiplication : \t', a, '*', b, '=' , a*b)
print('Multiplication : \t', a, '*' , b, '*', c, '=' , a*b*c)


a =8
b=2
c=1000

print('division : \t', c , '/', a, '/', b,  '=' , c/a/b)

a =8
b=2
c=1000

print('Modulo : \t', a, '% ',c , '=', a%c)
print('Modulo: \t', c, '%' ,a , '=', c%a)
print('Modulo : \t' , b, '%', a, '=', b%a)
print('Modulo \t', c, '%', a, '%', b, '=', c%a%b)


x = [1,2,3,4,5,6,7,8,9]
for i in x:
    if i % 2 !=0:
        print(i)
    else:
        print(i%2==0)
        



mylist = [ 10,29,39, 98,54,33,23,57,99 ]
total =0
for nums in mylist:
    total = total + nums
    print(total)
    for nums in mylist:
         total = total - nums
         print(total)
        
print(total)
 
string = 'john '
greeting = 'hello '
greeting += string
print(greeting)


var1 = 'marlon'
var2='briscoe'
var2 += var1
var1 +=var2
print(var2)
print (var1)


a=9
b=5



a/=b
print('Assign values: \t\t ' ,' a= ' , a, '\tb =' , b)
print('divide and assign: \t\t ' , 'a=', a , '(9/5)')
a+=b
print('Add & Assign : \t\t' , ' a=' , a, '(9 + 5)')
a*=b
print('multiply & Assign : \t\t', 'a= ' , a , '(9*5)' )
c=a-b
print('Subtract & assign : \t\t', 'a=', a,  'b=',b, 'c=(9-5)',c)
c=a%b
print('Modulo and assign :\t\t', 'a =', a, 'b=' , b, 'c=(a%b) =: ',c)


#comparing values

nil=0
num=0
max=1
cap='A'
low='a'

print("Equality: \t\t", nil, '==' , num, nil==num)
print("Equality : \t\t", cap, ' ==' , low, cap == low)

print("Inequality : \t\t", nil, ' !=', max, max!=num)
print("Greater: \t", nil, ' > ', max, nil > max )
print("Lesser: \t\t", nil, '<' , max, nil < max)

print("More or Equal : \t\t", nil, '>=', num, nil>=num)
print("Less or Equal : \t\t" , nil, '<=' , num, nil <=num) 


a=True
b=False

print('And logic')
print('a and a', '\t=', a and a )
print('a and b', '\t=', a and b)
print('b and b', '\t=', b and b)
print('b and a', '\t=', b and a)

a=True
b=False
print('\n Or logic: ')
print(' a or a' , a or a)
print('a or b' , a or b)
print(' b or b', b or b)
print(' b or a', b or a)



a=True
b=False

print('\n Not logic: ')
print(' a = ' , a , '\tnot  a = ', not a)
print(' b = ', b, '\tnot b = ', not b)

print('And logic')
print('a and a','\t=' , a and a )
print('a and b', '\t=', a and b)
print('b and b', '\t=', b and b)
print('b and a', '\t=', b and a)



a=1
b=2
c= b+a+b
print("\nVariable a Is :\t ", 'one' if(a==1)else 'not one')
print("\nVariable b Is :\t" , 'Even' if(b%2==0) else ' odd')
print("\nVariable c Is :\t" , 'Even' if(b%2==0) else ' odd')

max = a if(a>b) else b
print('Greater value is :\t', max)



a=2
b=4
c=8

print('\nDefault :\t ', a , '*' , c, '+', b, '=' , a*c + b)
print('\Forced out :\t' , a, '* (', c, ' + ' , b, ') = ' , a*(c+b))

print('\ndefault : \t', c, '//', b, '-',a, '=', c//b-a)
print('\nForced out : \t', c, '// (' ,b, '-' , a,')', '=' , c//(b-a)) 


print('\nDefault :\t', c, '%', b, '+',a, '=', c%b+a)
print('\Forced out :\t', c, ' % (', a , '+' , b, ')' , '=' , c% (b+a))

print('\nDefault :\t', c,'**', b, '+', b, '=', c**a+b)
print('\nForced out :\t', c, '**(',a,  '+',b,')', '=', c**(a+b))


#casting datatypes

a = input("Enter a number: ")
b=input("Now enter another num: ")

sum= a+b
print("\nData type sum:\t", sum, type(sum))

sum =int(a) + int(b)
print("\nData type sum:\t ", sum, type(sum))



a = input("Enter a number: ")
b=input("Now enter another num: ")

sum =a+b
sum = float(a) + float(b)
print("\nData type sum:\t", sum, type(sum))



a = input("Enter a number: ")
b=input("Now enter another num: ")
sum =a+b

sum = chr(int(sum))
print("\n data type sum:/t", sum, type(sum))
"""

# manipulating bits
"""
a=10
b=5

print("a =",a,'\tb = ',b)
a = a^ b
b = a^b
a = a^b
b= a^b
a= a ^ b
print("a = ",a, '\tb = ',b)





print('customer: Good morning.\n Owner: good morning sir')

#print('print("print")')




input("Enter something: ")
print("this is what \n the user enters!")




f='Spam'
s='eggs'
a='Spam' + 'eggs'
print('first string' ,'+','+', 'second string',a)


print("2" + "2")
print("Spam" *'3')



print("2" + "3" )
print(int("2") + int("3"))
print(int('3' + '4' ))

print(float(input("Enter a num: ") )+ float(input("Enter another num: ")))
print(float(input("Enter num:  ")) + int(input("Enter more num: ")))

print(float("210" * int(input("Enter a number:" )))

x=4
x*=3
print(x)

x='spam'
x+="Eggs"

print(x)


spam='7'
spam = spam +'0'
eggs = int(spam) +3
print(float(eggs))


x=5
y=x+3
y = int(str(y) +"2")
print(y)


mybool =3
notmyboo=4

if mybool==notmyboo:
    print(True)
else:
    print(False)

print(3==5)


num =12
if num >5:
    print("Bigger than 5")
    if num <=47:
        print("between 5 and 47")


num=7
if num >6:
    print("3")
    if num <5:
        print("5")
        if num==7:
            print("7")


spam=7
if spam >5:
    print("five")
    if spam >8:
        print("eight")


x=4
if x==5:
    print("Yes")
else:
    print("No")


if 1+1==2:
    if 2*2==8:
        print("if")
    else:
        print("Else")


num = int(input("Enter a num:  "))
if num==5:
    print("Number is 5")
else:
    if num==11:
        print("Num is 11")
    else:
        if num==7:
            print("num is 7")
        else:
            print("Num isn\'t 5,11 or 7")




num= 7
int(input(" Enter a num "))
if num ==5:
    print("Num is 5")
elif num ==11:
    print("Num is 11")
elif num ==7:
    print("num is 7")
else:
     print("Num isn\'t 5,11 or 7")


print(1!=1)
print(1!=2)



print(2<1 and 3 > 6)



if (1!=1) or (2+2<3) :
    print("True")
else:
    print("False")


print(not 1==1)
print(not 1>7)


if  True:
    print('1')
elif not (1+1 ==3):
    print('2')
else:
    print('3')

apple = 'red'
mango = 'green'

if not True:
    print(apple)
elif not(apple==mango):
    print(mango)
else:
    print('both')


a =(False==False or True)
print(a)

print((False==False)or True)


if (1+1)*3 ==6:
    print("yes")
else:
    print("No")


x=4
y =2

if not 1+1==y or x==4 and 7==8:
    print("Yes")
else:
    print("No")



i=1
while i<6:
    print(i)
    i=i+1
print("End")


i=3
while i>=0:
    print(i)
    i=i-1
 

x=0
while x<=20:
    print(x)
    x+=2 *2


x=10
while x<=100:
    if x%2==0:
        print(x)
    x=x+2
    


i=5
while True:
    print(i)
    i=i-1
    if i<=2:
        break
 

i=0
while True:
    i=i+1
    if i==2:
        print("Skipping")
        continue
    if i==5:
        print('Breaking')
        break
    print(i)
print("Finished")

nums=3
things =['strings',0,[1,2,nums],4.56]

print(things[3])

words= ['spam', 'egg', ' spam', 'sausage']
print('Spam' in words)
print('egg' in words)
print('tomato' in words)


nums =[10,9,8,7,6,4]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])


words = [3,4,5,6,0]
words[0] = words[3] *6

if 36 in words:
    print(True)
else:
    print(False)

nums=[1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

nums=[1,2,3]
nums.append(4)
print(nums)

words =['hello']
words.append('world')
print(words[1])



nums=[1,3,5,2,4]
print(len(nums))


letters =['a','b','c']
letters.append('d')
print(len(letters))


words=['python ', 'is','fun']
index=2
words.insert(index,'not')
print(words)


sums = [33,44,55,66,88]
index=4
sums.insert(index,77)
print(sums)


nums =[9,8,7,6,5]
nums.append(4)
nums.insert(2,11)
print(len(nums))


letters = ['p','q','r','p','s','t','u','r','s']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('s'))
print(letters.count('p'))


num = list(range(3,10))
print(num)

print(range(20) ==range(0,20))




nums=list(range(2,50,3))
print(nums)
print( list(range(20)))


words=['hello', 'world','spam','eggs']
for word in words:
    print(word +'!')



words=['hello', 'world','spam','eggs']
counter =0
max_index=len(words)-1

while counter<= max_index:
    word=words[counter]
    print(word + '!')
    counter = counter +1


fam= ['liz','ryan','marlon','baby']
counter =0
index= len(fam)-1

while counter <= index:
    family=fam[counter]
    print(family + '!')
    counter +=1

for word in fam:
    print(word)




i = 7
while i >=0:
    print( i )
    print(i%2==0)
    i-=1

print(i %2 ==1)


x=100
sum = 0
while x >=10:
    print(x)
    x=x-2
    sum +=x
print(sum)


for i in range(5):
    print('hello')

print(list(range(0,46,5)))



for i in range(5):
    print('marlon')


while True:
    print("Options")
    print("\n Enter 'addition - to add two nums : \t")
    print("\n Enter 'subtract - to minus two nums :\t")
    print("\n Enter 'divide- to divide two nums : \t ")
    print("\n Enter ' multiply- to mult two nums :\t ")
    print("\n Enter 'q to end the program")
    user_input = input(": ")

    if user_input == 'q':
          break
    elif user_input == 'addition':
          num1=float(input("Enter a num:\t "))
          num2=float(input("Enter another num:\t "))
          sum=num1+num2
          print("The answer is " , sum)
          
    elif user_input == "subtract":
          num1=float(input("Enter a num:\t "))
          num2=float(input("Enter another num:\t "))
          sum=num1- num2
          print("The answer is " , sum)           
      
    elif user_input == "multiply":
          num1=float(input("Enter a num:\t "))
          num2=float(input("Enter another num:\t "))
          sum=num1* num2
          print("The answer is " , sum)            
      
    elif user_input == "divide":
          num1=float(input("Enter a num:\t "))
          num2=float(input("Enter another num:\t "))
          sum=num1/ num2
          print("The answer is " , sum)           
      
    else:
      print("Unknown input") 
    



list =[1,1,2,3,5,8,13]
print(list[list[4]])



for i in range(10):
    if not i%2==0:
        print(i+1)


while  False==True:
    print("LOOPING")


list =[1,2,3,4]
if len(list) %2 ==0:
    print(list[0])


letters =['x','y','z']
letters.insert(1,'w')
print(letters[2])



list =[1,2,3]
for var in list:
    print(var)






















    







