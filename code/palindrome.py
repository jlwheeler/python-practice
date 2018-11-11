w = input('Enter a word: ').lower()


if w == w[::-1]:
    print("You pick an awesome palindrome. You rock. Play again!")
else:
    print("You didn't pick a palindrome.")
    
