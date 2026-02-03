#python weight conventor
weight = float(input("enter your weight: "))
unit =input("choose kilograms or pounds write (k or l)")
if unit == "k" or unit == "l" :
    if unit =="k":
        weight *= 2.205
        unit = "lbs"
        print(f"your weight is {round(weight,1)},{unit}")
    elif unit =="l":
         weight /= 2.205
         unit = "kgs"
         print(f"your weight is {round(weight,1)},{unit}")
else :
    print (f"this{unit} unit was not valid")


 