letter_Value = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
                "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
                "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
                "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
                "x": 8, "z": 10}

player_1_score = 0
player_2_score = 0

for letter in input("Enter a word for Player 1: ").casefold():
    if letter in letter_Value:
        player_1_score += letter_Value[letter]
        
for letter in input("Enter a word for Player 2: ").casefold():
    if letter in letter_Value:
        player_2_score += letter_Value[letter]

print(f"Player 1: {player_1_score} \nPlayer 2: {player_2_score}")

if player_1_score > player_2_score:
    print("Player 1 wins!")
elif player_2_score > player_1_score:
    print("Player 2 wins!")
else:
    print("It's a tie!")
