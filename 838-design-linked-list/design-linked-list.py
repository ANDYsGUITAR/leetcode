# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#
# Implement these functions in your linked list class:
#
#
# 	get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# 	addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# 	addAtTail(val) : Append a node of value val to the last element of the linked list.
# 	addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# 	deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
#
#
# Example:
#
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
#
#
# Note:
#
#
# 	All values will be in the range of [1, 1000].
# 	The number of operations will be in the range of [1, 1000].
# 	Please do not use the built-in LinkedList library.
#
#


class listNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = listNode(None)
        self.length = 0
        self.tail = listNode(None)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index not in range(self.length):
            return -1
        else:
            i = 0
            cur = self.head
            while i != index:
                cur = cur.next
                i += 1
            return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newHead = listNode(val)
        newHead.next = self.head
        self.head = newHead
        self.length += 1
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newTail = listNode(val)
        i = 0
        cur = self.head
        while i != self.length-1:
            cur = cur.next
            i += 1
        cur.next = newTail
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """

        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            newNode = listNode(val)
            i = 0
            prev = self.head
            while i != index - 1:
                prev = prev.next
                i += 1
            newNode.next = prev.next
            prev.next = newNode
            self.length += 1
                
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index not in range(self.length):
            return
        if index == 0:
            self.head = head.next
            self.length -= 1
        else:
            i = 0
            prev = self.head
            while i != index - 1:
                prev = prev.next
                i += 1
            prev.next = prev.next.next
            self.length -= 1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
