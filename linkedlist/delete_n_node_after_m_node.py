from linkedlist import List
class Solution:
    def deleteNodes(self, head, m, n):
        # return None
        if not head:
            return []

        mth_node = head
        nth_node = head
        i = m - 1

        while nth_node:
            while mth_node and i > 0:
                mth_node = mth_node.next
                i -= 1

            if not mth_node:
                return head

            nth_node = mth_node.next
            j = n - 1

            while nth_node and j > 0:
                nth_node = nth_node.next
                j -= 1

            mth_node.next = nth_node.next if nth_node else None
            i = m

        return head

s=[1,2,3,4,5,6,7,8,9,10,11]
m = 1
n = 3
l = List()
for i in s:
    l.append(i)

s = Solution()
k = s.deleteNodes(l.head, m, n)

l.display()