import unittest
from random import choice, randint

from app import Figure # назва файлу з нашим класом повинна бути app.py

class TestFigure(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            """Виконається лише раз на початку тестів
            """
            pass
        
        def setUp(self) -> None:
            """Виконується кожного разу коли запускається тест
            """
            self.figure = choice(Figure.FIGURES)
            self.length = randint(1, 10)
            self.obj = Figure(self.figure, self.length)
            return super().setUp()

        def tearDown(self) -> None:
            del self.obj
            return super().tearDown()

        def test_figure_type(self):
            print(f"Тестуємо вивід, має бути: {self.figure} == {self.obj.get_figure_type}")
            self.assertEqual(self.figure, self.obj.get_figure_type, "Властивість get_figure_type повертає неправильну фігуру!")

        def test_figure_lengh(self):
            self.assertEqual(self.length, self.obj.get_figure_length, "Властивість get_figure_length повертає неправильну довжину!")
        
        def test_obj(self):
            with self.assertRaises(AssertionError):
                Figure("коло", 5) # Спробуємо створити об'єкт з недозволеними параметрими, в нас має бути помилка AssertionError

        def test_if_object_created(self):
            self.assertEqual(self.obj.type, self.type)
            self.assertEqual(self.obj.length, self.length)
            self.assertIsInstance(self.obj, Figure)
            self.assertNotIsInstance(self.obj, str)


#if __name__ == '__main__':
#        unittest.main(verbosity=2) # unittest.main(verbosity=2) щоб був більш детальний вивід