class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:

    head = ListNode(0)

    now = None

    carry = 0

    while l1 or l2:

        if l1 is not None:
            x = l1.val
            l1 = l1.next
        else:
            x = 0


        if l2 is not None:
            y = l2.val
            l2 = l2.next
        else:
            y =0
        
        sum = x + y + carry
        node = ListNode(sum % 10)

        carry = sum // 10

        if now is None:
            now = head = node
        else:
            now.next = node
            now = now.next
        
    if carry > 0:
        now.next = ListNode(carry)
        
    return head
