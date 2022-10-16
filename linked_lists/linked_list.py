class MyLinkedList:
    class Node:
        def __init__(self, val, next_=None):
            self.val = val
            self.next = next_

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 0 if not node else 1

    def get(self, index: int) -> int:
        last_i = self.length - 1

        if last_i < index:
            return -1
        if last_i == index:
            return self.tail.val

        cur = self.head
        for i in range(index):
            cur = cur.next

        return cur.val

    def addAtHead(self, val: int) -> None:
        node = MyLinkedList.Node(val)
        node.next = self.head
        self.head = node
        self.length += 1
        if self.length == 1:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = MyLinkedList.Node(val)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length - 1:
            return

        node = MyLinkedList.Node(val)

        if index == 0:
            self.addAtHead(val)

        elif index == self.length - 1:
            self.addAtTail(val)

        else:
            cur = self.head
            for i in range(1, index):
                cur = cur.next
            cur.next = node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length - 1:
            return
        if index == 0:
            self.head = self.head.next

        cur = self.head
        for i in range(1, index-1):
            cur = cur.next

        prev = cur.next
        next_ = prev.next.next
        prev.next = next_




# TODO: write tests

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


