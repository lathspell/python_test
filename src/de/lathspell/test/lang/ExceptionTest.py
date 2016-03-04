import unittest



class ExceptionTest(unittest.TestCase):

    def testException(self):
        catchedException = None
        try:
            1/0
        except Exception as e:
            catchedException = e

        self.assertTrue(isinstance(catchedException, ZeroDivisionError))

    def testMyOwnException(self):
        # private Class
        class MyOwnException(Exception): pass

        foo = None
        try:
            raise MyOwnException("foo")
        except MyOwnException as e:
            # Es gibt leider kein getMessage()
            msg = e.args[0]
        self.assertEqual('foo', msg)

