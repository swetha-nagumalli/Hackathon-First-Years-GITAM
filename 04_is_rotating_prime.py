import unittest

question_04 = """
Rotating primes

Given an integer n, return whether every rotation of n is prime.
Example 1:
Input:
n = 199
Output:
True
Explanation:
199 is prime, 919 is prime, and 991 is prime.

Example 2:
Input:
n = 19
Output:
False
Explanation:
Although 19 is prime, 91 is not.
"""


# Implement the below function and run the program

def is_rotating_prime(num):
 num1 = str(num)
 if(len(num1)==2):
    return False
 def is_prime(num): 
  if num<=1:
     return False
  else:
    return not any(num%2==0 or num%i==0 for i in range(3,int(num**0.5)+1,2)) 
  num = str(num)
  for_in range(len(num)):
    if not is_prime(int(num)):
        return False
    num = num[1:] + num[0]
    return True
    
    


class TestIsRotatingPrime(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_rotating_prime(2), True)

    def test_2(self):
        self.assertEqual(is_rotating_prime(199), True)

    def test_3(self):
        self.assertEqual(is_rotating_prime(19), False)

    def test_4(self):
        self.assertEqual(is_rotating_prime(791), False)

    def test_5(self):
        self.assertEqual(is_rotating_prime(919), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
