import unittest
from practice.fizzbuzz import FizzBuzz


class MyTestCase(unittest.TestCase):
    def test_fizz(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(3), "Fizz")

    def test_fizz_mul(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(9), "Fizz")

    def test_buzz(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(5), "Buzz")

    def test_fizz_buzz(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(15), "FizzBuzz")

    def test_fizz_contains(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(13), "Fizz")

    def test_buzz_contains(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(55), "Buzz")

    def test_fizz_buzz_2(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(54), "FizzBuzz")

    def test_fizz_buzz_3(self):
        fb = FizzBuzz(3, 5)
        self.assertEqual(fb.say(53), "FizzBuzz")

    def test_x(self):
        fb = FizzBuzz(3, 5)
        x = 107
        self.assertEqual(fb.say(x), str(x))

if __name__ == '__main__':
    unittest.main()



"""

Test Cases:
input: m，n，x
m=3,n=5
8、x=353535353,FizzBuzz

"""