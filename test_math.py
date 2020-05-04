import mathPrac
import unittest

class TestFunc(unittest.TestCase):
        def test_add(self):
            a = 12
            b = 12
            res = 24
            result = mathPrac.test_add(a,b,res)
            self.assertEqual(result,res)

        def test_sub(self):
            a = 15
            b = 1
            res = 14
            result = mathPrac.test_sub(a,b, res)
            self.assertEqual(result,res)

        def test_sol(self):
            a = 12
            b = 12
            cnt = 1
            result = mathPrac.menu_option(a,b)
            self.assertEqual(result,cnt)


if __name__ == '__main__':
    unittest.main()
