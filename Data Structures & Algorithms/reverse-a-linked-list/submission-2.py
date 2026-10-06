# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            addNode = head.next
            nextNode = addNode.next
            head.next = None
            addNode.next = head
            head = addNode
            while (nextNode):
                
                addNode = nextNode
                nextNode = nextNode.next
                addNode.next = head

                head = addNode
            
            return head
        

        
