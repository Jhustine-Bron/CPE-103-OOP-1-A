bad_words = ["butt", "ugly", "stupid", "dumb", "bullcrap", "frick"]

sentence = input("Enter a sentence: ")

for word in bad_words:
    sentence = sentence.replace(word, "*" * len(word))
    sentence = sentence.replace(word.capitalize(), "*F" * len(word))
    
print (sentence)