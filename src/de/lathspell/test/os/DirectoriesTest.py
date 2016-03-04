import time
import stat
import glob
import os.path
import unittest
import os

class  DirectoriesTest(unittest.TestCase):

    def testDirectories(self):
        # @type cwd str
        cwd = os.getcwd();
        self.assertTrue(cwd.endswith('python_test'))

        path1 = os.path.realpath('/home/james')
        path2 = os.path.expanduser("~james")
        self.assertEqual(path1, path2)

        (dir, path) = os.path.split("/usr/bin/bash")
        self.assertEqual('/usr/bin', dir)
        self.assertEqual('bash', path)

        entries = glob.glob('Make*')
        self.assertTrue('Makefile' in entries)

        stat = os.stat('Makefile')
        self.assertTrue(stat.st_mtime < time.time())
