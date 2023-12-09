## Program to generate an abbreviation of given phrase
## following given guidelines:
## - abbreviation is a word formed by taking first 2 letters
##      of the words in the phrase and making a word from them
## - the short form will have 1sr, 3rd, 5th,... letters uppercase,
##      while 2nd, 4th, 6th,... letters lowercase irrespective
##      of the casing of the letters from the input phrase.
## - any of the words from the COMMON_WORDS list are excluded

# Useful global constants
COMMON_WORDS = ["the", "of", "from", "for", "by"]

def generateShortForm(phrase):
    new_list = []     # form empty array from collect new parts
    for item in COMMON_WORDS:                                 
        phrase = phrase.replace(item,"")   # check phrase on COMMON WORDS , if they have over there , just replace to empty 
    phrase = phrase.title()   # convert first letter any words to uper letter
    phrase = phrase.split() # convert string to list of words
    for word in phrase:      # cliding words  
        new_word = word [0:2]   
        new_list.append(new_word)   # collect new words 

    
    new_word1 = "".join(new_list)   # just convert list to string and combinate all words to new_word

    return new_word1  
    



def main():
    print("Welcome to generateShortForm program")
    ans = 'y'
    while (ans == 'y'):
        phrase = input("\nEnter the phrase: ")
        abbr = generateShortForm (phrase)
        print("The abbreviation is :", abbr)

        #prompt to check if want to continue
        ans = input("\nContinue?(y/n)").lower()
        
    print("Good Bye!")

    
if __name__ == "__main__":
    main()
    
