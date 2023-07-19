class Solution:
    def FindFibonacci(self,num):
        if num==0:
            return 0
        if num ==1:
            return 1
        return self.FindFibonacci(num-1)+self.FindFibonacci(num-2)
if __name__ == '__main__':
    num=int(input())
    print(Solution().FindFibonacci(num))
"""
The Fibonacci numbers are the numbers in the following integer sequence.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:

Fn = Fn-1 + Fn-2

Given a number A, find and return the Ath Fibonacci Number using recursion.

Given that F0 = 0 and F1 = 1.
"""