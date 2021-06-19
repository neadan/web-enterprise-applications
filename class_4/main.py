import wikipedia

results = wikipedia.search("Barack")
print(results)

obama_page = wikipedia.page("Barack Obama")
print(obama_page.title)
print(obama_page.content)
