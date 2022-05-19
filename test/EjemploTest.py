import unittest
from model.EvalEstudiante import EvaluacionEstudiante
from model.Calificacion import Calificacion


class ExampleTest(unittest.TestCase):

    def test_establecer_nota(self):
        probar = EvaluacionEstudiante()
        nota_final = probar.establecer_nota( 5, 0.2, 0 )
        self.assertEqual(1, nota_final)  # add assertion here

    def test_establecer_nota_incorrecto(self):
        probar = EvaluacionEstudiante()
        nota_final = probar.establecer_nota(5, 0.2, 0)
        self.assertFalse(nota_final == 0.75)  # add assertion here

    def test_editar_nota(self):
        prueba = EvaluacionEstudiante()
        nota = prueba.editar_nota( 1, 3, 0.1 )
        self.assertEqual( 1.3, nota )

    def test_editar_nota_incorrecto(self):
        prueba = EvaluacionEstudiante()
        nota = prueba.editar_nota( 2, 4, 0.3 )
        self.assertFalse( 2 == nota )

    def test_editar_nota_final(self):
        prueba = Calificacion()
        nota = prueba.editar_nota_final( 5,3,2 )
        self.assertEqual( 4, nota )

    def test_editar_nota_final_incorrecto(self):
        prueba = Calificacion()
        nota = prueba.editar_nota_final( 1,3,2 )
        self.assertFalse( 3 == nota )

    def test_editar_nota_final1(self):
        prueba = Calificacion()
        nota = prueba.editar_nota_final(5,5,2)
        self.assertEqual(5,nota)

    def test_editar_nota_final1_incorrecto(self):
        prueba = Calificacion()
        nota = prueba.editar_nota_final(4, 5, 2)
        self.assertFalse(1 == nota)





if __name__ == '__main__':
    unittest.main()
