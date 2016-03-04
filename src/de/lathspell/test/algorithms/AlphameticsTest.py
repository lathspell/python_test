# encoding: utf-8
'''
Diving into Python - Chapter 8 - Advanced Iterators

Cryptarithm- or Alphametic-Puzzle
http://diveintopython3.org/advanced-iterators.html

'''
from symbol import continue_stmt
import string
import itertools
import re
import unittest

class AlphameticsTest(unittest.TestCase):

    def myFirstTry(self, puzzle):
        '''
        Mein erster nicht so pythy Versuch.

        Schritt 1:
            Es werden alle vorkommenden Buchstaben ermittelt
        Schritt 2:
            Es wird eine Liste aller verschiedenen Buchstaben<->Zahl
            Mappings ermittelt.
        Schritt 3:
            Es werden für alle Mapping-Varianten die Buchstaben durch Zahlen
            ersetzt und geschaut ob das Ergebnis mathematisch korrekt ist.

        '''
        # Schritt 1 - find unique chars
        alle_chars = re.findall('[A-Z]', puzzle.upper())
        unique_chars = set(alle_chars)
        # unique_chars = {'A', 'B', 'C'}
        # numbers = (4, 2, 1)
        #print('unique_chars: ', unique_chars)
        #print('numbers: ', numbers)

        # Schritt 2 - Permutieren
        number_maps = itertools.permutations(list(range(0,10)), len(unique_chars))

        # Schritt 3 - translate & check für alle erzeugten Permutationen
        for numbers in number_maps:
            unique_chars_values = [ ord(i) for i in unique_chars ]
            numbers_values = [ ord("{0}".format(i)) for i in numbers ]
            zipped_obj = list(zip(unique_chars_values, numbers_values))
            zipped_dict = dict(zipped_obj)
            # zipped_dict = {68: 49, ...}
            #print("zipped_dict: ", zipped_dict)
            translated_s = puzzle.translate(zipped_dict)
            # translated_s = "5041 + 2360 = 23407"
            #print(translated_s)

            # Kein Wort darf mit '0' starten
            if re.match('.*\D0', translated_s):
                # print("0-TREFFER: ", translated_s)
                continue

            # Mathematisch korrekt?
            left1, left2, right = re.split(r'\D+', translated_s)

            if int(left1) + int(left2) == int(right):
                print(("TREFFER: ", translated_s))
                # return translated_s

    def mySecondTry(self, puzzle):
        alle_chars = re.findall('[A-Z]', puzzle.upper())
        unique_chars = set(alle_chars)
        digits = [ord(i) for i in '0123456789']
        number_maps = itertools.permutations(digits, len(unique_chars))

        unique_chars_values = [ ord(i) for i in unique_chars ]
        for numbers in number_maps:
            zipped_obj = list(zip(unique_chars_values, numbers))
            zipped_dict = dict(zipped_obj)
            translated_s = puzzle.translate(zipped_dict)

            if translated_s[0] == '0' or translated_s[7] == '0' or translated_s[15] == '0':
                continue

            if eval(translated_s):
                print(("TREFFER: ", translated_s))

    def his(self, puzzle):
        words = re.findall('[A-Z]+', puzzle.upper())
        unique_characters = set(''.join(words))
        assert len(unique_characters) <= 10, 'Too many letters'
        first_letters = {word[0] for word in words}
        n = len(first_letters)
        sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
        characters = tuple(ord(c) for c in sorted_characters)
        digits = tuple(ord(c) for c in '0123456789')
        zero = digits[0]
        for guess in itertools.permutations(digits, len(characters)):
            # Es werden genau die ersten drei Buchstaben auf ein Mapping zu 0
            # geprüft weil oben die Anfangsbuchstaben der drei Wörter an den
            # Anfang von sorted_characters und damit characters gesetzt wurden
            if zero not in guess[:n]:
                equation = puzzle.translate(dict(list(zip(characters, guess))))
                if eval(equation):
                    # return equation
                    print(("TREFFER: ", equation))

    def testMyFirstTry(self):
        # solved = self.myFirstTry('SEND + MORE == MONEY') # 41s
        # solved = self.mySecondTry('SEND + MORE == MONEY') # 28s
        # solved = self.his('SEND + MORE == MONEY') # 26s
        # self.assertEqual('9567 + 1085 == 10652', solved)
        self.skipTest('Dauert zu lange!')

if __name__ == '__main__':
    unittest.main()