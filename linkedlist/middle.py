from linkedlist import List

class Solution(object):

    def middle_node(self, head):

        if not head:
            return None
        if not head.next:
            return head
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

l = List()

s = [1,2,3,4,5,6]

for i in s:
    l.append(i)

s = Solution()
m = s.middle_node(l.head)

while m:
     print(m.value)
     m = m.next