search_words = ["Python", "PHP", "Java", "C", "C++", "OOP", "Hello"]

file = open('words.txt', 'r')

content = file.read()

words_in_file = content.split()

word_count = {
    word : 0 for word in search_words
}

for word in words_in_file:
    if word in search_words:
        word_count[word] += 1

for word, count in word_count.items():
    print(f"{word}: {count}")