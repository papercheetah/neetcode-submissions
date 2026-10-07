# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head
            
        elif not head.next:
            return head
        else:
            # Head node, addNode,tail
            addNode = head.next
            tail = addNode.next

            # Unlink the head.
            head.next = None
            addNode.next = head
            head = addNode
            addNode = tail

            while (addNode):
                tail = tail.next
                addNode.next = head
                head = addNode
                addNode = tail
            return head

