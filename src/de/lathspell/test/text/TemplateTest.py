import unittest
from string import Template

class TemplateTest(unittest.TestCase):

    def testTemplate(self):
        # Missing substitution variables raise "KeyError"
        t = Template('${village}folk send $$10 to $cause.')
        result = t.substitute(village='Nottingham', cause='the ditch fund', foo='bar')
        self.assertEqual('Nottinghamfolk send $10 to the ditch fund.', result)

if __name__ == '__main__':
    unittest.main()

