# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        if l1 == None:
            return l2
        if l2 == None:
            return l1

        head = None
        iterNode = None

        if l1.val <= l2.val:
            iterNode = l1
            l1 = l1.next
            head = iterNode
        else:
            iterNode = l2
            l2 = l2.next
            head = iterNode
        while not (l1 == None and l2 == None):
            if l2 == None or (l1 != None and l1.val <= l2.val):
                iterNode.next = l1
                l1 = l1.next
                iterNode = iterNode.next
            elif l1 == None or (l2 != None and l1.val > l2.val):
                iterNode.next = l2
                l2 = l2.next
                iterNode = iterNode.next

        return head
