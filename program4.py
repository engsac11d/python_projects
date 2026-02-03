#Temprature conventer 
print("-----welcome to spido temptatuer conventer----")
#ask the user for the unit and  temprature to know what we will calculate
unit = input("is this temprature in Celsius or Fahrenheit (t,c): ").lower()
#check if the answer is unit 
if unit == "t" or unit == "c":
    temp = float(input("enter your temprature : "))
    #now calculate
    if unit == "t":
        temp = round((9 * temp) / 5 +32,1)
        print(f"the temprature in fahrenheit is : {temp} oF")
    elif unit == "c":
        temp = round((temp -32) *5 / 9, 1)
        print(f"the temprature in celsius is : {temp}oC")
else:
    print(f"{unit} unit is an invailed unit for mesurement")
     
 
