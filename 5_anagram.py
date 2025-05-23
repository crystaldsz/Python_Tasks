# Anagram Checker
# Write a function to check if two strings are anagrams of each other.
# Anagrams have the same characters, just in a different order (e.g., "listen" and "silent").
def are_anagrams_sort(str1, str2):
    # We remove spaces and convert to lowercase 
    s1 = "".join(sorted(str1.replace(" ", "").lower()))
    s2 = "".join(sorted(str2.replace(" ", "").lower()))
    # If the sorted strings are identical, they're anagrams!
    return s1 == s2

word1 = input("Enter the first word or phrase: ")
word2 = input("Enter the second word or phrase: ")

if are_anagrams_sort(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams!")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")