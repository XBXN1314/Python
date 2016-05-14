# -*- coding = utf-8 -*-

# 定义节点结构
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        ret = ListNode(0)
        cur = ret
        add = 0

        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = val // 10        # 整除取整数部分
            cur.next = ListNode(val % 10)  # 整除取余数部分
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ret.next


if __name__ == '__main__':
    l1 = ListNode(2)
    cur = l1
    cur.next = ListNode(4)
    cur = cur.next
    cur.next = ListNode(3)

    l2 = ListNode(5)
    cur = l2
    cur.next = ListNode(6)
    cur = cur.next
    cur.next = ListNode(4)
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
