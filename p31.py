#anagram w dict

def anagram(word1, word2):
    #assuming word1 and word2 are cleaned
    #all uppercase, no special characters, no numbers
    #Frequency table
    freq_table = ()#empty dict
    for c in word1:
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1
    
    for c in word2:
        if c not in freq_table:
            return False
        else:
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False

    for key, value in freq_table.items():
        if value != 0:
            return False 
    
    return True 
    
    # words = ["word1", "word2"]
    # for i in words:
    #     if len(word1) == len(word2):
    #         return True
    #     else:
    #         return False
    # for i in wordds:
    #     if word1 = word2:
    #         return True
    #     else:
    #         return False



    


