import unittest
print(dir(unittest))

class Sample(unittest.TestCase):

    def test_demo(self):
	    self.assertEqual("foo".upper(),"FOO")

unittest.main()