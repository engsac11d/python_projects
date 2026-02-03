#PYTHON CALCULATER 
operator = input("enter the opreator (+ , -, * , /)? ")
if operator == "+" or operator =="-" or operator =="*" or operator =="/" :
 num1= float(input("enter a number1 : "))
 num2 = float(input("enter a number2 : "))
 if operator == "+" :
    result = num1 + num2
    print(round(result))
 elif operator == "-":
    result = num1 -num2
    print(round(result))
 elif operator == "*":
    result = num1 * num2
    print(round(result))
 elif operator == "/" :
    result =num1 / num2
    print(round(result))
else :
    print(f"{operator} is not avalid operator")
    

