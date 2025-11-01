class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        st = set(nums)
        while head and head.val in st:
            head = head.next
        if not head:
            return None

        curr = head
        while curr.next:
            if curr.next.val in st:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
