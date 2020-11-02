from linkedlist import Node, List


class Solution(object):

    def get_decimal_value_using_string(self, head):
        binary_num = ''
        curr = head
        while curr:
            binary_num += str(curr.value)
            curr = curr.next


        length = len(binary_num) - 1
        decimal = 0
        print(binary_num)

        for i in binary_num:
            decimal += int(i) * pow(2, length)
            length -= 1

        print(decimal)

    def get_decimal(self, head):
        sum = 0

        curr = head
        while curr:
            sum = sum * 2
            sum = sum + curr.value
            curr = curr.next
        print(sum)

    def get_decimal_with_shift(self, head):
        sum = 0
        curr = head

        while curr:
            sum += curr.value << 2
            curr = curr.next

        print(sum)

l = List()
s=[1,0,0,1]
for i in s:
    l.append(i)
s = Solution()
s.get_decimal_with_shift(l.head)




