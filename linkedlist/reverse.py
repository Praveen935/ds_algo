from linkedlist import List
class Solution(object):


    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverse_recursive(self, head):
        if head == None or head.next == None:
            return head;
        p = self.reverse_recursive(head.next);
        head.next.next = head
        head.next = None
        return p
            

l = List()

s = [1,2,3,4]

for i in s:
    l.append(i)
s = Solution()

k = s.reverse_recursive(l.head)
l.head = k
l.display()