from ehpar import eh_par

import unittest
class TestPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(2))

    def test_impar(self):
        self.assertFalse(eh_par(5))

if __name__ == '__main__':
    unittest.main()