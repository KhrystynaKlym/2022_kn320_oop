import unittest

from lab5 import Animal

class TestMyApp(unittest.TestCase):
    def test_if_object_created(self):
        name = "Monkey"
        mass = 40.5
        obj = Animal(name, mass)
        self.assertEqual(obj.name, name)
        self.assertEqual(obj.mass, mass)
        self.assertIsInstance(obj, Animal)
        self.assertNotIsInstance(obj, str)

    def test_mock(self):
        self.assertTrue(False)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)