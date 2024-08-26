import random
import sys
word_list = [
    "happy",
    "sunny",
    "rainbow",
    "friend",
    "music",
    "mountain",
    "ocean",
    "explore",
    "dream",
    "imagine",
    "create",
    "laugh",
    "dance",
    "discover",
    "learn",
    "challenge",
    "inspire",
    "believe",
    "hope",
    "courage",
    "wisdom",
    "justice",
    "peace",
    "harmony",
    "nature",
    "wonder",
    "beauty",
    "kindness",
    "respect",
    "gratitude",
    "adventure",
    "mystery",
    "celebrate",
    "together",
    "journey",
    "destiny",
    "courageous",
    "determined",
    "resilient",
    "compassionate",
    "enthusiastic",
    "optimistic",
    "inventive",
    "resourceful",
    "adaptable",
    "persistent",
    "integrity",
    "curiosity",
    "growth",
    "potential",
    "achievement",
]
compGuess= random.choice(word_list)
word=[]
for i in compGuess:
    word.append(i)
guesses =[]
for j in word:
        guesses.append("_")
aag =""
for n in guesses:
    aag+=n
print(aag)
po=""
j=0
oogs=""
nice =[]
for n in word:
    po+=n
while "_" in guesses:
    oogs =""
    if j == 6:
        print(f"You guessed the wrong letter 6 times. YOU LOSE. The correct word was {po}.")
        sys.exit()
    slab = input(f"Incorrect characters guessed: {nice}\nWhat is your guess? (single letter only): ")
    found = False
    for i, letter in enumerate(guesses):
        if letter == "_" and slab.lower() == word[i].lower():
            guesses[i] = slab.lower()
            found = True
        if slab.lower()==letter:
            print("You've already guessed that")
            found= True
    for r in guesses:
        oogs+=r
    print(oogs)
    if found==False:
        j+=1
        print(f"Your letter is wrong, try again. Incorrect letters guessed: {j}")
        nice+=slab.lower()
print(f"You got it right! Total incorrect characters guessed:{j}")
