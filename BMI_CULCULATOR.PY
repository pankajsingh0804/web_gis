#The body mass index (BMI) is a measure used in\n
#  medicine to see if someone is underweight\n or overweight.\n
#  This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared
# BMI = WEIGHT/(HEIGHT**2)
a = float(input('ENTER YOUR HEIGHT : '))
b = float(input('ENTER YOUR wEIGHT : '))
bmi = b/(a**2)
print(round(bmi))