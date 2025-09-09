---
tags:
    - List
    - Intermediate
---

# Sort Lists based on Frequency

Sort a list of lists based on their length frequency. Lists with rare lengths are placed first. Lists with more frequent lengths come later.


=== "Test"
    ```python
    def test_sort_by_frequency_of_length(solution):
        assert [len(t) for t in solution([
                ["a", "b", "c"], ["d", "e"], ["f", "g", "h"], ["d", "e"],
                ["i", "j", "k", "l"], ["m", "n"], ["o"]])
            ] ==\
                [len(t) for t in [
                    ["i", "j", "k", "l"], ["o"], ["a", "b", "c"], ["f", "g", "h"], ["d", "e"], ["d", "e"], ["m", "n"]]
                ]
    ```

=== "Direct"
    ```python
    from collections import Counter
    
    def sort_by_frequency_of_length_v1[T](lst: list[list[T]]) -> list[list[T]]:
        length_counts = Counter((len(sub_lst) for sub_lst in lst))
        return sorted(lst, key=lambda sub_lst: length_counts[len(sub_lst)])
    ```