# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #converting the Srings to lowercase
    word.lower()
    anagram.lower()

    # Checking the strings if they are anagram equal
    if sorted(word) == sorted(anagram):
        return True
    elif sorted(word)!= sorted(anagram):
        return False
        
# Getting the two strings and printing out the result.
print(find_anagram(input("please enter second string here \n"),input("please enter word here \n")))