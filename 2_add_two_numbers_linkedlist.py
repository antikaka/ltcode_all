
"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pernesti = False
        atsakymas = ListNode()
        current = atsakymas
        while (l1 or l2) != None:
            if l1 == None:
                skaicius = l2.val + 0
                l2 = l2.next
                print(skaicius, "l1")
            elif l2 == None:
                skaicius = l1.val + 0
                l1 = l1.next
                print(skaicius, "l2")
            else:
                skaicius = l1.val + l2.val
                l1, l2 = l1.next, l2.next
                print(skaicius, "else")
            if pernesti:
                skaicius += 1
            pernesti = False
            if skaicius >= 10:
                skaicius -= 10
                pernesti = True
                print(skaicius, "pernesti")
            current.next = ListNode(skaicius)
            current = current.next
            print(atsakymas)

        if pernesti:
            current.next = ListNode(1)

        return atsakymas.next


