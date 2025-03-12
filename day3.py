def count_vowels (x):
    vowels = "AEIOUaeiou"
    count = 0 #counter to return the number of char
    for char in x :
        if char in vowels :
            count += 1
    return count 
word = input("please enter the required word")
print (count_vowels(word))

######################################
users = [
    {"name":"omar","password":"123"},
    {"name":"Omar","password":"143"},
    {"name":"ahmed","password":"456"}
    ]
user_name = input("enter username : ")
password = input ("enter password : ")

def checker (name , password) :
    for user in users :
        if user ["name"] == name and user ["password"] == password:
            return True 
    return False 

if checker (user_name ,password ) :
    print ("Valid Login")
else:
    print ("invalid username or password")