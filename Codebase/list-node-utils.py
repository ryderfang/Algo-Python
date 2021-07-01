from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def node_linked_list(cls, data: List):
        if len(data) == 0:
            return None
        head = cls()
        p = cls()
        p.next = head
        for _, x in enumerate(data):
            p = p.next
            p.val = x
            p.next = cls()
        p.next = None
        return head
    
    @classmethod
    def list(cls, head):
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        return ans