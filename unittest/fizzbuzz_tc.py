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


if __name__ == '__main__':
    unittest.main()



"""
此时有100名学生在上课，游戏的规则如下：


1. 老师先说出两个不同的特殊数(都是个位数)，比如3, 5；
2. 让所有学生拍成一队，然后按顺序报数；
3. 学生报数时
4. 如果所报数字是「第一个特殊数(3)」的倍数，或者包含「第一个特殊数(3)」，那么不能说该数字，而要说Fizz；
5. 如果所报数字是「第二个特殊数(5)」的倍数，或者包含「第二个特殊数(5)」，那么不能说该数字，而要说Buzz；
6. 如果所报数字同时是「两个特殊数」的倍数，那么也不能说该数字，而是要说FizzBuzz。
7. 如果所报数字中包含某个「特殊数」，那么也不能说该数字，而是要说对应的英文单词（见规则1和规则2）。例如，要报13的同学应该说Fizz；要报52的同学应该说Buzz。
8. 如果在一次报数中，匹配上述多个规则，Fizz和Buzz都只能出现一次，Fizz在前。
9. 否则，直接说出要报的数字。


## 要求

使用程序模拟执行上述要求，打印出 从1~100所报的内容。每行打印一个报数内容。
"""

"""
思路：
1)输入
2)

Test Cases:
input: m，n，x
m=3,n=5
4、x=15,FizzBuzz
5、x=34,Fizz
6、x=53,FizzBuzz
7、x=102, 102
8、x=353535353,FizzBuzz

"""