from linkedlist import Node, List

class Solution(object):
    def find_cycle_with_map(self, head):
        '''
        TODO: time complexity - n - for scanning list
        TODO: space complexity - n - hash table
        '''
        map = {}
        curr = head
        pre = None
        cycle = False

        while curr:
            if not curr.next:
                break
            if map.get(curr):
                cycle = True
                break
            else:
                map[curr] = 1
            pre = curr
            curr = curr.next
        if cycle:
            return pre, curr
        else:
            return None, None

    def find_cycle_with_two_pointers(self, head):
        # floyd's cycle-finding algorithm
        if not head or not head.next:
            return None
        fast = head.next.next
        slow = head.next

        while fast and fast.next:
            if slow == fast:
                break
            fast = fast.next.next
            slow = slow.next

        if fast is None or fast.next is None:
            return

        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast

    def detectAndRemoveLoop(self, head):
        if not head or not head.next:
            return None
        # Move slow and fast 1 and 2 steps respectively
        slow = head.next
        fast = head.next.next

        # Search for loop using slow and fast pointers
        while fast and fast.next:
            if slow == fast:
                print("slow: %s fast:%s " % (slow.value, fast.value))
                break
            print("slow: %s" % slow.value)
            print("fast: %s" % fast.value)
            slow = slow.next
            fast = fast.next.next

        # if loop exists
        print("================")
        if slow == fast:
            slow = head
            while slow.next != fast.next:
                print("slow: %s" % slow.value)
                print("fast: %s" % fast.value)
                slow = slow.next
                fast = fast.next
            fast.next = None


l = List()

for i in range(5):
    l.append(i)
node4 = l.search(4)
node2 = l.search(2)
node4.next = node2

s = Solution()
# from_node, to_node = s.find_cycle_with_map(l.head)
#
# if not from_node and not to_node:
#     print("not found")
# else:
#     print("from: %s to: %s" %(from_node.value, to_node.value))

t = s.detectAndRemoveLoop(l.head)

print(t.value)
