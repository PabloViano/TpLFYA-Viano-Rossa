import unittest
from Solucion import _Solucion

class Test(unittest.TestCase):
    def primer_test(self):
        test = _Solucion()
        test.setear(self,"S: A B\nA: a A a\nB: b B | b")
        self.assertTrue(test.evaluar_cadena("a a a b b"))