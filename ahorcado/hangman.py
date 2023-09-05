class Hangman:
    guesses = []
    errors = 0
    def __init__(self, solution: str):
        self.solution: list = [i for i in solution]
        self.word: list = ["_" for i in range(len(solution))]

    def guess(self, word: str):
        self.add_guess(word)
        if (len(word) == 1):
            if word in self.solution:
                self.word[self.solution.index(word)] = word
                return True
            return False
        elif word == "".join(self.solution):
            self.word = [i for i in word]
        
    def add_guess(self, guess: str):
        self.guesses.append(guess)

    def correct(self):
        return self.word == self.solution

    def __repr__(self):
        return "".join(self.word)

    def __add__(self, other: int):
        self.errors += other

