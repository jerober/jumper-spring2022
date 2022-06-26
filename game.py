import random

class Game:
    #all game functionality and inter-class communicating
    def __init__(self):
        #initializes and randomly chooses a word in the list
        self.word_list = ['food', 'celebrate', 'geek', 'magic']
        self.ran_word = Word(random.choice(self.word_list))
        self.hold_word = ""
        for letter in self.ran_word.word:
            self.hold_word += "_"
        self.build_word = Word(self.hold_word)

    def get_input(self):
        #asks user for a letter guess
        self.player_guess = input('Guess a letter [a-z]: ')

    def evaluate_guess(self):
        #takes users guess and compares it to the letter in the random word
        i = 0
        guess = False
        while i < self.ran_word.get_length():
            for letter in self.ran_word.word:
                if self.ran_word.word[i] == self.player_guess:
                    self.build_word.set_char(i, self.player_guess)
                    guess = True
            i+=1
        return guess

    def word_incomplete(self):
        #checks if the word has been completed
        for letter in self.build_word.word:
            if letter == "_":
                return True
        return False

class Word:
#all things word related
    def __init__(self, w):
        self.word = w
        self.length = len(self.word)

    def get_char(self, index):
        return self.word[index]

    def set_char(self, index, char):
        l = list(self.word)
        l[index] = char
        self.word = "".join(l)

    def get_length(self):
        return self.length

class Parachuter:
#all things related to the parachuter
    def __init__(self):
        #creates and adds to the arrays all the characters in the symbol
        self.parachute = Picture()
        self.parachute.add_line(" ___")
        self.parachute.add_line("/___\ ")
        self.parachute.add_line("\   / ")
        self.parachute.add_line(" \ / ")
        self.person = Picture()
        self.person.add_line("  O ")
        self.person.add_line(" /|\ ")
        self.person.add_line(" / \ ")

    def cut_line(self):
        #deletes a row in the parachute picture
        self.parachute.delete_line()

    def alive(self):
        #checks to see if there are any lines remaining in parachute
        if len(self.parachute.picture) == 0:
            return False
        else:
            return True

    def draw(self):
        #draws the parachute and person
        self.parachute.draw()
        self.person.draw()
        print('\n')

class Picture:
    # Sets the initial picture
    def __init__(self):
        #empty array for picture and future interactions
        self.picture = []

    def add_line(self,line):
        #adds line to the picture
        self.picture.append(line)

    def delete_line(self):
        #deletes a line in parachute when called
        self.picture.pop(0)

    def draw(self):
        #prints the drawn picture
        for line in self.picture:
            print(line)

def main():
#called at beginning of program to start and move through the game
    parachuter = Parachuter()
    game = Game()
    while parachuter.alive() == True and game.word_incomplete() == True:
        print(game.build_word.word)
        print('')
        parachuter.draw()
        game.get_input()
        game.evaluate_guess()
        if game.evaluate_guess() == False:
            parachuter.cut_line()
    print(game.build_word.word)
    print('')
    if parachuter.alive() == False:
        parachuter.person.picture[0] = '  X'
    print(parachuter.draw())
    print('Game Over')

main()