#validate user input excercise
#1.username is more than 12 characters
#2. username must not contain space
#3, username must not contain digits
 
#ask the user his name
name = input("enter your name : ")

if len(name) < 12 :
    print("you need 12 characters to continue")
elif not name.find(" ") == -1:
    print("you name must dont have any space")
elif not name.isalpha() == True :
    print("your name must not contain digits ")
else :
    print(name)
    





