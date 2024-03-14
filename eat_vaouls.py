user_word = input("write word ")
user_word = user_word.upper()
vowel = ("A", "E", "I", "O", "U")

novowel = ""


for letter in user_word:
    if letter in vowel:
        continue
    novowel += letter


print("word no vowel", novowel)