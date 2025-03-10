import random
print("Welcome to Hangman!")
word_list = [
    "apple",
    "elephant",
    "banana",
    "absence",
    "orange",
    "eager",
    "python",
    "novel",
    "water",
    "robot",
    "account",
    "basin",
    "between",
    "house",
    "equator",
    "chair",
    "rectangle",
    "table",
    "night",
    "flower",
    "rubic",
    "cloud",
    "disaster",
    "block",
    "berry",
    "blood",
    "bridge",
    "bicycle",
    "award",
    "dolphin",
    "posture",
    "monitor",
    "laptop",
    "pumpkin",
    "computer",
    "regulation",
    "abbey",
    "chemical",
    "circle",
    "clock",
    "jungle",
    "diamond",
    "island",
    "volcano",
    "guitar",
    "guide",
    "report",
    "barrier",
    "tissue",
    "score",
    "bush",
    "cotton",
    "copper",
    "damage",
    "algorithm",
    "hemisphere",
    "philosophy",
    "labyrinth",
    "camouflage",
    "encryption",
    "asteroid",
    "masquerade",
    "dirty",
    "engine",
    "female",
    "kaleidoscope",
    "equilibrium",
    "cinema",
    "install",
    "update",
    "makeup",
    "notebook",
    "bottle",
    "crime",
    "rabbit",
    "garden",
    "gloves",
    "insect",
]
rand_word = list(random.choice(word_list))
lives = 6
answer = ["-"] * len(rand_word)
while answer != rand_word and lives >= 0:
    letter = str(input("enter a letter: ").lower())
    check = 0
    for i in range(len(rand_word)):
        if str(rand_word[i]) == letter:
            answer[i] = letter
            check = 1
    if not check:
        lives -= 1
        print(f"Wrong. Lives remaining - {lives}")
    res = "".join(answer)
    print(res)
if answer == rand_word:
    print("You won!")
else:
    rw = "".join(rand_word)
    print(f"The word is {rw}")
    print("Zero lives remaining. You Lost.")
