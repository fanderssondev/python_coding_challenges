def check_result[T](func: T, expected_result: T) -> None:
    """
    Compares a the return value of the tested function (func) against an
    expected result and prints the outcome.

    Args:
        func (T): The return value of the function being checked.
        expected_result (T): The expected output of the function (func).

    Returns:
        None: This function prints the result and does not return anything.
    """
    print(f"{"✅" if func == expected_result else "❌"}\t {func}\t {expected_result}")


# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
# You are given a node that is the beginning of a linked list. This list contains a dangling
# piece and a loop. Your objective is to determine the length of the loop.
#
# For example in the following picture the size of the dangling piece is 3 and the loop size is 12:
#
#
# Use the `next' attribute to get the following node
# node.next
#
# Notes:
# do NOT mutate the nodes!
# in some cases there may be only a loop, with no dangling piece


def loop_size(node):
    # Step 1: Detect cycle using Floyd's algorithm
    slow = node
    fast = node

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # Step 2: Find loop size
    count = 1
    current = slow.next
    while current != slow:
        count += 1
        current = current.next

    return count


# node1 = Node()
# node2 = Node()
# node3 = Node()
# node4 = Node()
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2
# check_result(loop_size(node1), 3)  # Loop size of 3 expected
# # Make a longer chain with a loop of 29
# nodes = [Node() for _ in xrange(50)]
# for node, next_node in zip(nodes, nodes[1:]):
#     node.next = next_node
# nodes[49].next = nodes[21]
# check_result(loop_size(nodes[0]), 9)  # Loop size of 29 expected
# # Make a very long chain with a loop of 1087
# chain = create_chain(3904, 1087)
# check_result(loop_size(chain), 1087)  # Loop size of 1087 expected
