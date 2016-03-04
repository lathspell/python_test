import unittest

class  BytesTest(unittest.TestCase):

    def testBytes(self):
        # Byte Objekte sind immutable
        b = b'\x41\x42'
        b += b'\x43'
        self.assertEqual(b'ABC', b)

        # Bytearrays sind nicht immutable
        barr = bytearray(b)
        barr[1] = 0x44
        self.assertEqual(b'ADC', barr)

        # String Umwandlung (UTF-8 wenn nicht anders angegeben!)
        self.assertEqual(b, 'ABC'.encode())
        self.assertEqual('ADC', barr.decode())
        