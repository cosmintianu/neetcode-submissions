class ListNode:
    def __init__(self, value = 0, next_node = None):
        self.val = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i+=1
        return -1 

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val)
        new_head.next = self.head.next
        self.head.next = new_head

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr and curr.next:
            curr = curr.next

        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        
        while i < index and curr:
            i+=1
            curr = curr.next

        if curr and curr.next:
            curr.next = curr.next.next
            return True

        return False
        

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head.next
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr
        
