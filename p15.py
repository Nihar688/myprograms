#Anagram

def alpha_sorting(text):
    abc = "abcdefghijklmnopqrstuvqxyz"
    result = ""
    i = 0
    while i < len(abc)
        current_letter = abc[1]
        text_lowered = text.lower()
        if current_letter in text_lowered:
            letter_count = text_lowered.count(current_letter)
            result = result + (current letter * letter_count)
        #if abc[i] in text.lower():
            #result += abc[i]*text.lower*().count(abc[1])
    return result

     
