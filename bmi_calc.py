print("Welcome to BMI Calculator")
a= float(input("Enter your weight in Kgs:"))
b= float(input("Enter your height in meters:"))
c= a/(b*b)
if c <= 18.5:
    print("You are Underweight")
elif c <= 25:
    print("You have normal BMI")
elif c <=30:
    print("You are Overweight class I")
elif c <=35:
    print("You are Overweight class II")
else:
    print("You are Obese")
print( "Your BMI is", f'{c:.2f}')