#!/usr/bin/python
# coding=utf-8
'''
Degree: Medium
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself
example:
    list1:  2->4>3    list2: 5->6->4
    return 7->0->8
    explanation: 342 + 465 = 807 
'''
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        #c用来存放 进位值
        c = val // 10
        #当前节点剩下加和后的个位数
        ret = ListNode(val % 10 )
        #递归处理余下的节点
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret

def main():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next = None
    l2 = ListNode(5)
    l2.next=ListNode(6)
    l2.next.next=ListNode(4)
    l2.next.next.next = None
    solution = Solution()
    l3 = ListNode()
    l3 = solution.addTwoNumbers(l1,l2)
    while l3 != None:
        print(l3.val)
        l3=l3.next
if __name__ == "__main__":
    main()
