import random
def hangman():
    word_list = ["python", "datheon", "internship", "developer", "github", "hangman"]
    word = random.choice(word_list)
    guessed = ["_"] * len(word)
    attempted = set()
    lives = 6
    print("=== HANGMAN ===")
    while lives > 0 and "_" in guessed:
        print("\nWord: ", " ".join(guessed))
        print(f"Lives: {lives} | Tried: {', '.join(attempted)}")
        guess = input("Guess a letter: ").lower().strip()
        if len(guess)!=1 or not guess.isalpha(): continue
        if guess in attempted: continue
        attempted.add(guess)
        if guess in word:
            for i,ch in enumerate(word):
                if ch==guess: guessed[i]=guess
        else: lives-=1
    print(f"You Won! {word}" if "_" not in guessed else f"Game Over! {word}")
hangman()
