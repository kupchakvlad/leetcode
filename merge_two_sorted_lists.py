# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    class ListNode:
        def __init__(self, value, next=None, previous=None):
            self.value = value
            self.next = next
            self.previous = previous

    class LinkedList:
        def __init__(self, head=None):
            self.head = head
            self.sorted_list = []
        def init(self, node):
            current = None
            if self.head is None:
                self.head = node
                return
            if current.value > node.value:
                node.next = self.head
                self.head = node
                return
            current = self.head
            while current.next and current.next.value <= node.value:
                current = current.next
                node.next = current.next
                current.next = node

        def append(self, node_list):
            for node in node_list:
                self.init(node)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

linked_list = LinkedList()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)

l5 = ListNode(5)
l6 = ListNode(6)

node_list1 = [l1, l2, l3, l4]
node_list2 = [l5, l6]