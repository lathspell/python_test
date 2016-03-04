import unittest
import locale

class LocaleTestCase(unittest.TestCase):

    def testLocale(self):
        locale.setlocale(locale.LC_ALL, 'de_DE')
        
        x = 1234567.8
        self.assertEqual("1.234.567,80", locale.format("%.2f", x, grouping=True))
        
        conv = locale.localeconv()
        self.assertEqual('EUR', conv['currency_symbol'])
        self.assertEqual(2, conv['frac_digits'])

if __name__ == '__main__':
    unittest.main()

