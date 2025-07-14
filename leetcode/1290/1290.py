class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        b = ""
        while head != None:
            b += str(head.val)
            head = head.next
        return int(b, 2)
