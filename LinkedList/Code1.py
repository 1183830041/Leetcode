#合并连个升序的链表
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        先吧链表元素存入列表排序再生成链表
        '''
        l = []
        while l1:
            l.append(l1.val)
            l1 = l1.next
        while l2:
            l.append(l2.val)
            l2 = l2.next
        l.sort()
        
        dummy = ListNode(0)
        curr = dummy
        for i in l:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        return dummy.next