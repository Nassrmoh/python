x = input("write a word : ")
def I_finder (x) :
    char = 'i'
    for char in range(len(x)) :
        if x[char] == x:
            return x[char]
        else :
            return 2
position = I_finder(x)
if position!=2 :
    print (f"char position at {position +1}")
else :
    print ("char I isn't found")