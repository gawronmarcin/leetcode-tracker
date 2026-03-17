from typing import List, Optional
from solution import ListNode, Solution

def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_mergeKLists():
    sol = Solution()

    input_lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    result = sol.mergeKLists(input_lists)
    assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]

    input_empty = []
    result_empty = sol.mergeKLists(input_empty)
    assert linked_list_to_list(result_empty) == []

    input_one_empty = [build_linked_list([])]
    result_one_empty = sol.mergeKLists(input_one_empty)
    assert linked_list_to_list(result_one_empty) == []