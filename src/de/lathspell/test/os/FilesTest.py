import sys
import os.path
import io
import unittest
import os
import gzip

class FilesTestTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists('tmp.txt'):
            os.unlink("tmp.txt")
        self.assertFalse(os.path.exists("tmp.txt"))

    def testFiles(self):
        # writing
        with open("tmp.txt", mode='w', encoding='utf-8') as f:
            f.write("täst")
        self.assertTrue(os.path.isfile("tmp.txt"))

        # reading
        f = open('tmp.txt')
        s = f.read()
        f.close()
        self.assertTrue(f.closed)
        self.assertEqual('täst', s)
        
        # reading2 (Vorsicht bei seek und (UTF-8 Multibyte Zeichen)
        f = open('tmp.txt', encoding='utf-8')
        f.seek(1)
        c = f.read(1)
        f.close()
        self.assertEqual('ä', c)

        # reading3
        with open('tmp.txt') as f:
            s = f.readline()
        self.assertEqual('täst', s)

        # reading4 (files implementieren Iterator)
        with open('tmp.txt', encoding='utf-8') as f:
            i=0
            for line in f:
                # Python erkennt Zeilenende üblicherweise automatisch
                self.assertEqual('täst', line)
                i+=1
        self.assertEqual(1, i)

    def testStringsAsFiles(self):
        source = "Hello World"
        f = io.StringIO(source)
        s = f.readline()
        self.assertEqual(source, s)

    def testGzip(self):
        with gzip.open('tmp.txt.gz', mode='wb') as zf:
            zf.write("zipped täst".encode('utf-8'))

        self.assertTrue(os.path.isfile('tmp.txt.gz'))
        os.unlink('tmp.txt.gz')

    def testStdErr(self):
        sys.stderr.write('stderr1')
        print('stderr2', file=sys.stderr, end=' ')