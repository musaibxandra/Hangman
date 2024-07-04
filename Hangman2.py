import random

words = ['dog', 'lion', 'cat', 'tiger', 'giraffe', 'antelope',
         'panther', 'deer','reindeer', 'crocodile', 'elephant',
         'sparrow', 'catepillar', 'shark', 'parrot', 'bear']


HANGMAN = ['+______+',
           '|      |',
           '|      O',
           '|     /|\ ',
           '|      | ',
           '|     / \ ']


class Hangman:
    def __init__(self):
        self.words = words
        self.attempts = 0
        self.word_to_guess = random.choice(self.words)
        self.guess_word = '_'*len(self.word_to_guess)
        self.guess_letters = set()

    def get_index(self, user_input):
        indices = [i for i, char in enumerate(self.word_to_guess) if char == user_input]
        return indices

    def display_guess(self):
        print()
        for line in HANGMAN[:self.attempts]:
            print(line)
        print()
        print()
        print(' '.join(self.guess_word))
        print()

    def play(self):
        max_attempts = len(HANGMAN)

        while True:

            self.display_guess()
            user_input = input('Enter a letter to guess the animal: ')

            if not user_input.isalpha():
                print('\nEnter a single alphabet.')
                continue

            indices = self.get_index(user_input)

            if user_input in self.guess_letters:
                print('You guessed that already.')
                continue
            self.guess_letters.add(user_input)

            if user_input in self.word_to_guess:
                for index in indices:
                    self.guess_word = self.guess_word[:index] + user_input + self.guess_word[index+1:]
            else:
                print('Incorrent!')
                self.attempts += 1

            if self.guess_word == self.word_to_guess:
                self.display_guess()
                print('\nYour guess is correct.')
                print(f'The Word is: {self.word_to_guess}')
                break

            if self.attempts == max_attempts:
                self.display_guess()
                print(f'\n--- GAME OVER ---\nYou ran out of attempts.\nThe word is: {self.word_to_guess}.')
                break

hman = Hangman()
hman.play()
