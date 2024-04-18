'''
Module containing a function that
deletes a given value from a
binary search tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Class representing the solution.
    '''

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        Method that deletes a given value from the tree.
        '''

        if root is None:
            return None

        if root.val == key:

            if root.right is None:
                root = root.left

            else:
                cur_node = root.right
                prev = None

                while cur_node.left is not None:

                    prev = cur_node
                    cur_node = cur_node.left

                if prev is None:
                    root, root.left, root.right = cur_node, root.left, root.right.right

                else:
                    prev.left = cur_node.right
                    root, root.left, root.right = cur_node, root.left, root.right

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            root.right = self.deleteNode(root.right, key)

        return root
