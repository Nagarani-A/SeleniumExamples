'''import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("ths is start")

    def tearDown(self):
        print("this is end")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")
'''


import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("ths is start")

    @classmethod
    def tearDownClass(cls):
        print("this is end")

    def test_add(self):
        print("test1")

    def test_sub(self):
        print("test2")
