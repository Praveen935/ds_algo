from linkedlist import List


class Solution(object):
    def merge_point(self, list1, list2):
        if not list1 or not list2:
            return None

        l1 = l2 = 0
        head1= list1
        head2 = list2
        while head1:
            l1 += 1
            head1 = head1.next
        while head2:
            l2 += 1
            head2 = head2.next

        diff = abs(l1-l2)
        if l1 > l2:
            head1 = list1
            head2 = list2
        else:
            head1 = list2
            head2 = list1

        while diff > 0:
            head1 = head1.next
            diff -= 1

        while head1 and head2:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next

l1 = List()
l2 = List()

for i in range(7):
    l1.append(i)

for i in range(3, 5):
    l2.append(i)

merge_p = l1.search(5)
l2_last_node = l2.search(4)

l2_last_node.next = merge_p

print("============== l1")
l1.display()

print("=======l2")
l2.display()

print('------------')
s = Solution()
k = s.merge_point(l1.head, l2.head)

if not k:
    print("============= not fouund")
else:
    print(k.value)