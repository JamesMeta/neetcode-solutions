# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = l1
        head2 = l2
        remainder = 0

        l3 = ListNode()
        head3 = l3

        while True:
            head1_val = 0
            head2_val = 0

            if head1 != None:
                head1_val = head1.val 
            if head2 != None:
                head2_val = head2.val 
            
            head_sum = head1_val + head2_val + remainder

            if head_sum > 9:
                remainder = 1
                head_sum -= 10
            else:
                remainder = 0 
            
            head3.val = head_sum

            if (head1 == None or head1.next == None) and (head2 == None or head2.next == None):

                if remainder == 1:
                    head3.next = ListNode(1)

                break
            else:
                head1 = head1.next if head1 != None and head1.next != None else None
                head2 = head2.next if head2 != None and head2.next != None else None
                head3.next = ListNode()
                head3 = head3.next
        
        return l3
        

       

        
            

        