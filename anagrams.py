# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

a = str(input("enter a word: "))
b = str(input("enter another word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here
    sortedWord = sorted(word)
    sortedanagram = sorted(anagram)
    if sortedWord == sortedanagram:
        return True
    else: 
        return False

print(find_anagram(a, b))