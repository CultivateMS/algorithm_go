#!/usr/bin/python
# coding = utf-8
 def getSum(self, a: int, b: int) -> int:
        arr_a = []
        arr_b = []
        while a != 0:
            arr_a.append(a%10)
            a= a/10
        while b != 0:
            arr_b.append(b % 10)
            b = b/10
        c=0

