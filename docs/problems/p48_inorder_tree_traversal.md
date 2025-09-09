---
tags:
    - Tree
---

# Inorder Traversal

Given a tree $T$, output a string of its values via [inorder traversal](https://en.wikipedia.org/wiki/Tree_traversal#Depth-first_search).

=== "Test"
    ```python
    def test_inorder_tree_traversal(solution):
        tree = string_to_tree_v1('a(b(d,e),c(,f(g,)))')
        assert solution(tree) == 'dbeacgf'
    ```

=== "Recursive"
    ```python
    def inorder_tree_traversal_v1(tree: Tree) -> str:
        match tree:
            case None: 
                return ''
            case Node(val, left, right): 
                return inorder_tree_traversal_v1(left) + val + inorder_tree_traversal_v1(right)

    ```