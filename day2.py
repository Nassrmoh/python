
# num = []
# for x in range (5):
#     y = input(f"enter a number {x}")
#     int(y)
#     num.append(y)
# num_1 = sorted (num)
# num_2 = sorted(num, reverse = True)
# print("Ascending order",num_1)
# print ("descending order",num_2)
# print("-----------------------------------")

# input_number = int(input("write a number from 1 to 10 "))
# list_1 = []
# for i in range (1, input_number+1):
#     list_2 = []
#     for j in range (1, i+1):
#         list_2.append(i*j)
#     list_1.append(list_2)
# print(list_1)
#_----------------------------
# email = input("enter your email ")
# if "@" not in email :
#     print("enter valid email")
# if "." not in email :
#         print("enter valid email")
# at_index = email.index ("@")
# dot_index = email.index (".")
# if at_index > 0 and dot_index > at_index+1:
#     if dot_index == -1 :
#         print ("the email is invalid")
#     else:
#         print("the email is valid")
# else:
#     print("the email is invalid")
Name = input("write your name ")
if Name.isalpha():
    print (f"welcome {Name}")
else : 
    print("enter valid name") 
while True :
    email = input ("enter your email")
    if "@" in email and "." in email :
        username , domain = email.split("@")
        if username and domain:
            x,y = domain.split(".")
            if x and y :
                break
    else :
        print ("invalid email, please enter a valid email")
print(f"\nyour name is {Name}")
print(f"your email is {email}")


