#!/usr/bin/python
# coding=utf-8
'''
Level:Medium
Given two integers a and b, return the sum of the two integers without using the operators + and -
example:
    Input: a = 1, b = 2
    Output: 3
'''
def getSum(a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        两数 位相加的结果可以用异或得到， 进位可以用与得到，重复此操作直至进位遗留变为0
        example： 11 + 5    11:1011, 5:0101
        step1: 1011^0101 = 1110, 1011&0101=0001
        重复step1知道 进位数为全为0， 即1110^0001=1111, 进位1110&0001=0
        得到的结果为1111 即为16
        """
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

def main():
    a = input("please input int a: ")
    b = input("please input int b: ")
    print("the sum of a and b is: ", getSum(int(a),int(b)))

if __name__ == "__main__":
    main()
