string = input("Please enter your own string : ")
string2 = ""
for i in string:
    string2 = i + string2
print("\nThe Original String = " , string)
print("\nThe reversed String = " , string2)
if string == string2:
    print("The word is a palindrome! Suprise there!")
else:
    print("The word is not a palindrome! It made a randomn gibberish word!")
