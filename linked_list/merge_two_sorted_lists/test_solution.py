import pytest
from solution import Solution, ListNode


def to_linked_list(elements: list[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for val in elements:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def to_python_list(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result



def test_mergeTwoLists_standard_case():
    sol = Solution()
    list1 = to_linked_list([1, 2, 4])
    list2 = to_linked_list([1, 3, 4])

    result_head = sol.mergeTwoLists(list1, list2)

    assert to_python_list(result_head) == [1, 1, 2, 3, 4, 4]


def test_mergeTwoLists_both_empty():
    sol = Solution()
    list1 = to_linked_list([])
    list2 = to_linked_list([])

    result_head = sol.mergeTwoLists(list1, list2)

    assert to_python_list(result_head) == []


def test_mergeTwoLists_one_empty():
    sol = Solution()
    list1 = to_linked_list([])
    list2 = to_linked_list([0])

    result_head = sol.mergeTwoLists(list1, list2)

    assert to_python_list(result_head) == [0]