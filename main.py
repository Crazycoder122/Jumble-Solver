from scraper import find
from itertools import  permutations


if __name__=='__main__':
    word=input("Enter the Word:")

    perms=permutations(word)

    isFound=False

    # Traversing all the permutations of the word
    for words in perms:
        
        # If the word is found then we break out of loop and print the word
        if(find(words)):
            isFound=True

            real_word=''
            for item in words:
                real_word+=item
            print(f'The Real Word is:{real_word}')

            break
    
    # If the word has already been found, then we do nothing
    if(isFound):
        pass
    
    # Else we print that we could not find the word
    else:
        print("No Valid Permutation Found!!!!!")
