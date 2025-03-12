def count_vowels (x):
    vowels = "AEIOUaeiou"
    count = 0 #counter to return the number of char
    for char in x :
        if char in vowels :
            count += 1
    return count 
word = input("please enter the required word")
print (count_vowels(word))
