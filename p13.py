#String stuff
#tacocat is a plaindrome 

def is_palindrome(word):
    #checks is argument word is a palindrome 
    return word == word[::-1]

text = input("Please enter a word: ")
if is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is BORING~")
