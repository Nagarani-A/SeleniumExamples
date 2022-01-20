import unittest
from DemoExample1 import Sample1


class MyTestCase(unittest.TestCase):
    def test_add(self):
        Sample1.add(self,4,7)
       # self.assertEqual(4,7)  2,2 is crt

    def test_sub(self):
        Sample1.sub(self, 7, 4)


