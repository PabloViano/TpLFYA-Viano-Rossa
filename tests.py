import unittest
from Solucion import _Solucion

class TestSolucion(unittest.TestCase):

    #Con gramatica LL(1)
    def test_sin_recursion_derecha(self):
        print("---------------test_sin_recursion_derecha---------------")
        test = _Solucion()
        gramatica = "S:A a\nA:c\nA:d"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("da"))
    
    def test_con_recursion_derecha(self):
        print("---------------test_con_recursion_derecha---------------")
        test = _Solucion()
        gramatica = "S:Q a\nS:P\nP:b P\nQ:b"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("ba"))
    
    def test_con_lambda_en_derivaciones(self):
        print("---------------test_con_lambda_en_derivaciones---------------")
        test = _Solucion()
        gramatica = "S:A b\nA:c\nA:#"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("cb"))

    def test_sin_lambda_en_derivaciones(self):
        print("---------------test_sin_lambda_en_derivaciones---------------")
        test = _Solucion()
        gramatica = "S:A b\nA:c A\nA:d"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("db"))

    def test_produccion_innecesarias(self):
        print("---------------test_produccion_innecesarias---------------")
        test = _Solucion()
        gramatica = "S:A P\nA:c h\nA:d\nP:h\nU:U"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("dh"))
    
    def test_con_simbolos_innacesibles_desde_axioma(self):
        print("---------------test_con_simbolos_innacesibles_desde_axioma---------------")
        test = _Solucion()
        gramatica = "S:A P\nA:c h\nA:d\nP:h\nU:U"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("chh"))
    
    def test_con_no_terminales_no_generativos(self):
        print("---------------test_con_no_terminales_no_generativos---------------")
        test = _Solucion()
        gramatica = "S:A \nA:d A \nA:b B \nA:a \nB:b B"
        test.setear(gramatica)
        self.assertTrue(test.evaluar_cadena("da"))

    #Sin gramatica LL(1)

    def test_sin_recursion_derecha_no_ll1(self):
        print("---------------test_sin_recursion_derecha_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:Q a\nQ:P\nQ:b\nP:b"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_con_recursion_derecha_no_ll1(self):
        print("---------------test_con_recursion_derecha_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:a A\nQ:Q b\nP:b\nA:b A\nA:b"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_con_lambda_en_derivaciones_no_ll1(self):
        print("---------------test_con_lambda_en_derivaciones_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:Q a\nS:P\nP:b\nQ:b\nQ:#"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_sin_lambda_en_derivaciones_no_ll1(self):
        print("---------------test_sin_lambda_en_derivaciones_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:a Q\nQ:b R\nQ:b\nR:b"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_produccion_innecesarias_no_ll1(self):
        print("---------------test_produccion_innecesarias_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:P a\nS:Q\nQ:b\nP:P\nP:b"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_con_simbolos_innacesibles_desde_axioma_no_ll1(self):
        print("---------------test_con_simbolos_innacesibles_desde_axioma_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:a Q\nS:a R\nQ:b\nR:b\nP:d"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    def test_con_no_terminales_no_generativos_no_ll1(self):
        print("---------------test_con_no_terminales_no_generativos_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:Q a\nS:P\nS:R\nQ:c\nP:c\nR:R a"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

    #Deberia romper por demasiadas iteraciones, ya que no aplicamos la factorizacion por izquierda
    def test_con_recursion_izquierda_no_ll1(self):
        print("---------------test_con_recursion_izquierda_no_ll1---------------")
        test = _Solucion()
        gramatica = "S:Q a\nQ:Q b\nQ:B\nB:b"
        test.setear(gramatica)
        self.assertFalse(test.EsLL1)

if __name__ == '__main__':
    unittest.main()