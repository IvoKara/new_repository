import unittest
import totest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestMakeTodict(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(totest.make_to_dict([["one",1],["two",2]]),\
                         {"one": 1, "two": 2})
        self.assertEqual(totest.make_to_dict([["three",3]]),\
                         {"three": 3})
    def test_not_dict(self):
        expected = None
        actual = totest.make_to_dict(["four",4])
        self.assertEqual(expected,actual)
if __name__ == '__main__':
    unittest.main()
