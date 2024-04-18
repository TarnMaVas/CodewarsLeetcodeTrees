'''
Module containing a function that allows
the user to traverse a binary tree by levels.
'''

from collections import deque

def tree_by_levels(node: 'Node')-> list:
    '''
    Traverse a given binary tree "by levels"
    (left to right).
    '''

    if node is None:
        return []

    result = []

    queue = deque()
    queue.append(node)

    while bool(queue):

        cur_node = queue.popleft()

        result.append(cur_node.value)
        queue.extend(n for n in (cur_node.left, cur_node.right) if n is not None)

    return result
