''' Dive into Python - Chapter 7

    * Es gibt nur public, nicht private/protected/default.

'''

import unittest

class IAmEmpty:
    pass # leere Klasse

class Fib:
    '''iterator that yieldds numbers in the Fibonacci sequence'''

    def __init__(self, max):
        '''Constructor'''
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

class ClassesTest(unittest.TestCase):

    def testClasses(self):
        # Instanziierung ohne new!
        fib = Fib(3)
        # Aufruf des Objekts über einen Iterator
        all_fibs = [i for i in fib]
        self.assertEqual([0,1,1,2,3], all_fibs)
        

