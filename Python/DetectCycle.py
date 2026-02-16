def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        fast=head
        for _ in range(10**6):
            if not fast or not fast.next:
                return False
            sl=sl.next
            fast=fast.next.next
            if sl==fast:
                return True