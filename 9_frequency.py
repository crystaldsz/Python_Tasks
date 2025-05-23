# Frequency Counter
# Count the frequency of each word in a given paragraph.

paragraph = "This is a simple paragraph. This paragraph is for testing word frequency counter."
 
paragraph = paragraph.lower()
 
paragraph = paragraph.replace(".", "").replace(",", "")
 
words = paragraph.split()
 
word_count = {}
 
for word in words:
    if word in word_count:
        word_count[word] += 1 
    else:
        word_count[word] = 1  

for word, count in word_count.items():
    print(f"{word}: {count}")