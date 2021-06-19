import wikipedia

page = input("What page would you like to view?")
word_to_count = input("Which word would you like to count?")

desired_page = wikipedia.page(page)
# url
print(desired_page.url)

# number of words
content = desired_page.content
split = content.split(" ")
print(f"The number of words in the document is: {len(split)}")

# count of specific word
count = 0
for word in split:
    if word == word_to_count:
        count = count + 1

print(f"The word '{word_to_count}' shows up {count} times")
