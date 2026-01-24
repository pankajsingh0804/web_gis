# write a program to calculate a restrurent bill
print ('WELCOME TO TIP CALCULATOR !')
a = float(input('what is the total bill ?'))
b = float(input('how much tip would you like to give ?'))
c  = float(input('how many people to splite this bill ?'))
d = (a+b)/c
print('your total per person bill is : ',round(d,2))