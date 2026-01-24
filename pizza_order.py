print("Welcome to Python Pizza Deliverie!")
size = input('What size pizza you want ? s,m,l : ')
peopperoni = input('do you want peopperoni in your pizza ? y, n : ')
extra_chease = input('do you want peopperoni in your pizza ? y, n : ')
s = 25
m= 30
l= 40
bill = 0
if size=="s":
    bill +=25
    print(f'your final bill is : {bill}')
if size == "m":
    bill+=30
    print(f'your final bill is : {bill}')
if size == "l":
    bill+=40
    print(f'your final bill is : {bill}')
# else:
#     print('you enter a wrong input')
if peopperoni == "y" or peopperoni=="n":
    bill==25
    print(f'your final bill is : {bill}')
# else:
#     bill+=3
if extra_chease=="y":
    bill+=1
    print(f'your final bill is : {bill}')
else:
    print('thanku')
