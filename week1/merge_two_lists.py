class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(list1, list2):
        dummy = ListNode(0)
        current = dummy  #поінтер

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        


        return dummy.next



# class Solution(object):
#     def mergeTwoLists( list1, list2):
#         merged_list = list1 + list2
#         merged_list.sort()
#         return merged_list

#  print(Solution.mergeTwoLists(list1= [12,6,2],list2=[0,16,9]))
