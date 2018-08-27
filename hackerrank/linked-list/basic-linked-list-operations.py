class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __str__(self):
        return str(self.data)

def insertNodeAtHead(llist, data):
    llist_head = SinglyLinkedListNode(data)
    llist_head.next = llist
    return llist_head

def reverse(head):
    pre = None
    cur = head
    next = None
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def reversePrint(head):
    if not head:
        return
    reversePrint(head.next)
    print(head.data)


def insertNodeAtPosition(head, data, position):
    node = head
    count = 1
    while count < position and node:
        count += 1
        node = node.next
    newNode = SinglyLinkedListNode(data)
    newNode.next = node.next
    node.next = newNode
    return head

def deleteNode(head, position):
    if not head:
        return
    count = 0
    pre = None
    cur = head
    while( cur and count < position):
        count += 1
        pre = cur
        cur = cur.next
    if count != position:
        print("Not enough nodes in the list")
    else:
        if pre is None:
            head = cur.next
        else:
            pre.next = pre.next.next
    return head
