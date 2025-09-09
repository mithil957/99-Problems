---
tags:
    - Tree
    - Intermediate
---

# Tree from inorder and preorder sequence

From a preorder and inorder tree traversal sequence, generate a tree $T$.


=== "Test"
    ```python
    def test_(solution):
        tree = string_to_tree_v1('a(b(d,e),c(,f(g,)))')
        assert solution('abdecfg', 'dbeacgf') == tree
    ```

=== "Recursive"
    ```python
    def tree_from_sequence_v1(preorder: str, inorder: str) -> Tree:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        
        root_node = preorder[0]
        split_point = inorder.index(root_node)
        
        left_inorder = inorder[:split_point]
        right_inorder = inorder[split_point + 1:]

        left_preorder = preorder[1: 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder): ]

        left_tree = tree_from_sequence_v1(left_preorder, left_inorder)
        right_tree = tree_from_sequence_v1(right_preorder, right_inorder)
        
        return Node(root_node, left_tree, right_tree)
    ```